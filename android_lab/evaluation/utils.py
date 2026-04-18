"""Minimal judge helpers — only what ``evaluation/tasks/*.py`` call.

Upstream's ``evaluation/utils.py`` also bundled AVD/Docker subprocess helpers
(``clone_avd``, ``find_free_ports``, ``start_avd``, …). Those are driver-level
concerns; downstream projects like cua-lite own emulator lifecycle separately
(file-locked pool, KVM passthrough), so this module ships only the two
tree-search functions every AndroidLab judge actually imports.
"""
from __future__ import annotations


def find_matching_subtrees(tree, search_str):
    """Return every subtree whose key or leaf value contains ``search_str``."""
    matched = []

    def _search(node):
        if not isinstance(node, dict):
            return
        for key, value in node.items():
            if search_str in key:
                matched.append({key: value})
            elif isinstance(value, dict):
                _search(value)
            elif isinstance(value, str) and search_str in value:
                matched.append({key: value})

    _search(tree)
    return matched


def find_subtrees_of_parents_with_key(tree, search_key):
    """Return every parent subtree whose child key contains ``search_key``.

    Judges use this to confirm the agent reached a target page — the
    presence of ``search_key`` implies the parent's subtree is the relevant
    judgment context.
    """
    parent_subtrees = []

    def _search(current, parent=None):
        if not isinstance(current, dict):
            return False
        for key, value in current.items():
            if search_key in key:
                if parent is not None:
                    parent_subtrees.append({parent: current})
                return True
            if isinstance(value, dict):
                _search(value, key)
        return False

    _search(tree)
    return parent_subtrees
