"""Minimal SingleTask base — what all 138 AndroidLab task judges inherit from.

Upstream mixes a heavyweight replay-eval driver (tqdm / jsonlines / PIL /
openai / zhipuai) with ``SingleTask`` in the same module. This slimmed-down
version keeps only the base class; downstream users who need the replay
driver can reconstruct it from git history.

``check_answer`` is preserved for the Q&A tasks (information retrieval) that
compare ``finish(message=...)`` against a stored ground truth via LLM judge.
It returns ``False`` when ``OPENAI_API_KEY`` is unset so offline eval
doesn't crash — Q&A tasks score 0 instead of raising.
"""
from __future__ import annotations

import logging
import os

logger = logging.getLogger(__name__)


class SingleTask:
    """Base for all AndroidLab task judges.

    Subclasses override ``judge_page(xml_tree)`` and ``judge(xml_tree, line)``.
    ``judge()`` returns ``{"judge_page": bool, "1": bool, ..., "complete": bool}``.
    The live-eval driver caches the most recent ``judge_page=True`` result and
    treats ``complete=True`` as reward 1.0.
    """

    def __init__(self, args=None):
        self.metric_type = ""
        self.final_ground_truth = None
        self.args = args

    def check_answer(self, line) -> bool:
        parsed = line.get("parsed_action", {}) or {}
        if parsed.get("action") != "finish" and parsed.get("type") != "finish":
            return False
        if self.final_ground_truth is None:
            return False
        try:
            question = line.get("target", "")
            if "kwargs" in parsed:
                model_answer = parsed["kwargs"].get("message", "")
            else:
                model_answer = parsed.get("input", "")
            return self._llm_judge(question, model_answer, self.final_ground_truth)
        except Exception as e:
            logger.warning("check_answer failed: %s", e)
            return False

    def _llm_judge(self, question: str, model_answer: str, ground_truth: str) -> bool:
        if not os.environ.get("OPENAI_API_KEY"):
            logger.warning(
                "OPENAI_API_KEY not set — Q&A judge returns False (reward=0). "
                "Set OPENAI_API_KEY to enable LLM-graded Q&A tasks."
            )
            return False
        prompt = (
            "You need to judge the model answer is True or False based on "
            "Standard Answer we provided. Answer [True] or [False].\n\n"
            f"Question: {question}\n\nModel Answer: {model_answer}\n\n"
            f"Standard Answer: {ground_truth}"
        )
        try:
            from openai import OpenAI
            client = OpenAI()
            model = (getattr(self.args, "judge_model", None) if self.args else None) or "gpt-4o-mini"
            r = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=16, temperature=0.0,
            )
            out = r.choices[0].message.content or ""
            return "True" in out and "False" not in out
        except Exception as e:
            logger.warning("LLM judge call failed: %s", e)
            return False

    def judge_page(self, xml_compressed_tree) -> bool:
        return True

    def judge(self, xml_compressed_tree, line):
        raise NotImplementedError

    def save_answer(self, answer) -> None:
        self.final_ground_truth = answer
