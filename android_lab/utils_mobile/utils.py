"""Minimal ``get_compressed_xml`` — the only function the judge path needs.

Upstream's ``utils_mobile/utils.py`` bundled ~15 helpers for the CLI driver
(screenshot annotation, jsonlines IO, LLM calls, color printing, Chinese
detection, image similarity, etc.) alongside ``get_compressed_xml``. Live
eval only needs the last one, so this version strips the heavy deps
(``cv2`` / ``pyshine`` / ``openai`` / ``zhipuai`` / ``backoff``).

``UIXMLTree`` (in ``xml_tool.py``) parses UI Automator dumps into the
compact nested-dict form every ``judge()`` expects.
"""
from __future__ import annotations

from android_lab.utils_mobile.xml_tool import UIXMLTree


def get_compressed_xml(xml_path, type="json"):
    """Compress a UI Automator XML file for judge consumption.

    Returns a nested-dict when ``type="json"`` (the format judges expect) or
    a plain string otherwise. Returns ``None`` on parse failure.
    """
    xml_parser = UIXMLTree()
    with open(xml_path, "r", encoding="utf-8") as f:
        xml_str = f.read()
    try:
        return xml_parser.process(xml_str, level=1, str_type=type).strip()
    except Exception:
        return None


def get_compressed_xml_from_str(xml_str: str, type: str = "json"):
    """Same as ``get_compressed_xml`` but for an already-in-memory XML string.

    Added for live evaluation where the adb-dumped XML is kept in-memory
    rather than written to a temp file.
    """
    xml_parser = UIXMLTree()
    try:
        return xml_parser.process(xml_str, level=1, str_type=type).strip()
    except Exception:
        return None
