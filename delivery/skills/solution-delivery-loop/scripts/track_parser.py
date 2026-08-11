#!/usr/bin/env python3
"""Track document parser — extract, validate, index, and query frontmatter."""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
FIELD_TYPES = {
    "status": str,
    "scope_type": str,
    "created": str,
    "parent_id": str,
    "version": int,
}
VALID_STATUS = {"pending", "in_progress", "done", "blocked"}
VALID_SCOPE_TYPE = {"parent", "stage", "standalone"}


def parse_frontmatter(text: str) -> dict[str, Any] | None:
    """Extract YAML frontmatter from markdown text (simple key: value parsing)."""
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None
    raw = m.group(1)
    result: dict[str, Any] = {}
    for line in raw.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            continue
        key, _, val = line.partition(":")
        key = key.strip()
        val = val.strip().strip('"').strip("'")
        if key in FIELD_TYPES:
            expected = FIELD_TYPES[key]
            try:
                result[key] = expected(val)
            except (ValueError, TypeError):
                result[key] = val
    return result


def read_frontmatter(path: str | Path) -> dict[str, Any] | None:
    """Read and parse frontmatter from a file."""
    text = Path(path).read_text(encoding="utf-8")
    return parse_frontmatter(text)


def validate(path: str | Path) -> list[str]:
    """Validate frontmatter against schema. Returns list of errors (empty = valid)."""
    errors = []
    text = Path(path).read_text(encoding="utf-8")
    fm = parse_frontmatter(text)

    if fm is None:
        errors.append("missing or unparseable frontmatter")
        return errors

    for field, expected_type in FIELD_TYPES.items():
        required = field != "parent_id" or fm.get("scope_type") == "stage"
        if required and field not in fm:
            errors.append(f"missing field: {field}")
        elif field in fm and not isinstance(fm[field], expected_type):
            errors.append(f"field '{field}': expected {expected_type.__name__}, got {type(fm[field]).__name__}")

    if "status" in fm and fm["status"] not in VALID_STATUS:
        errors.append(f"status: invalid value '{fm['status']}', expected one of {sorted(VALID_STATUS)}")

    if "scope_type" in fm and fm["scope_type"] not in VALID_SCOPE_TYPE:
        errors.append(f"scope_type: invalid value '{fm['scope_type']}', expected one of {sorted(VALID_SCOPE_TYPE)}")

    if "created" in fm and not re.match(r"^\d{4}-\d{2}-\d{2}$", str(fm["created"])):
        errors.append(f"created: expected YYYY-MM-DD format, got '{fm['created']}'")

    if "version" in fm and isinstance(fm["version"], int) and fm["version"] < 1:
        errors.append(f"version: must be >= 1, got {fm['version']}")

    # Parent/child consistency
    scope = fm.get("scope_type")
    path_obj = Path(path)

    if scope == "parent":
        parent_dir = path_obj.parent
        child_stages = []
        for sub in sorted(parent_dir.iterdir()):
            if not sub.is_dir():
                continue
            child_req = sub / "requirements-v1.md"
            if not child_req.exists():
                continue
            child_fm = read_frontmatter(child_req)
            if child_fm and child_fm.get("parent_id") == parent_dir.name:
                child_stages.append(child_fm)

        if not child_stages:
            errors.append("scope_type parent has no child stages (no sub-folders with matching parent_id)")
        elif fm.get("status") == "done":
            not_done = [c for c in child_stages if c.get("status") != "done"]
            if not_done:
                names = [c.get("parent_id", "?") for c in not_done]
                errors.append(f"scope_type parent marked done but {len(not_done)} child stage(s) not done: {names}")

    elif scope == "stage":
        parent_id = fm.get("parent_id")
        if parent_id:
            parent_req = path_obj.parent.parent / parent_id / "requirements-v1.md"
            if not parent_req.exists():
                errors.append(f"parent_id '{parent_id}' points to non-existent folder: {parent_req}")

    return errors


def extract(path: str | Path, fields: list[str] | None = None) -> dict[str, Any]:
    """Extract frontmatter fields. If fields specified, return only those."""
    fm = read_frontmatter(path)
    if fm is None:
        return {"error": "no frontmatter found"}
    if fields:
        return {k: fm.get(k) for k in fields if k in fm}
    return fm


def index(track_root: str | Path) -> list[dict[str, Any]]:
    """Scan track root for all docs with frontmatter, return JSON index."""
    root = Path(track_root)
    entries = []
    for md in sorted(root.rglob("*.md")):
        fm = read_frontmatter(md)
        if fm is None:
            continue
        rel = md.relative_to(root)
        entries.append({
            "path": str(rel),
            **fm,
        })
    return entries


def children(parent_path: str | Path) -> list[dict[str, Any]]:
    """List all stage children of a parent track doc."""
    parent_fm = read_frontmatter(parent_path)
    if parent_fm is None:
        return []
    parent_dir = Path(parent_path).parent
    parent_name = parent_dir.name
    results = []
    for sub in sorted(parent_dir.iterdir()):
        if not sub.is_dir():
            continue
        req = sub / "requirements-v1.md"
        if not req.exists():
            continue
        fm = read_frontmatter(req)
        if fm and fm.get("parent_id") == parent_name:
            results.append({
                "stage": sub.name,
                "path": str(req.relative_to(parent_dir.parent)),
                **fm,
            })
    return results


def _derive_parent_status(parent_entry: dict, children_entries: list[dict]) -> str:
    """Derive parent status from children. Done only if all children done."""
    if not children_entries:
        return parent_entry.get("status", "pending")
    statuses = [c.get("status", "pending") for c in children_entries]
    if all(s == "done" for s in statuses):
        return "done"
    if any(s == "blocked" for s in statuses):
        return "blocked"
    if any(s == "in_progress" for s in statuses):
        return "in_progress"
    return "pending"


def kanban(track_root: str | Path) -> dict[str, dict[str, list[dict[str, Any]]]]:
    """Build kanban: status columns, rows grouped by parent scope or standalone.

    Parent status is derived from children: done only when all children done.
    """
    entries = index(track_root)

    # Separate parents, stages, standalone
    parents = {e.get("path"): e for e in entries if e.get("scope_type") == "parent"}
    stages_by_parent: dict[str, list[dict]] = {}
    standalone = []

    for e in entries:
        scope = e.get("scope_type", "standalone")
        if scope == "stage":
            pid = e.get("parent_id", "")
            stages_by_parent.setdefault(pid, []).append(e)
        elif scope == "parent":
            pass  # handled separately
        else:
            standalone.append(e)

    # Build entries with derived parent status
    all_entries = []
    for p in parents.values():
        pid = p.get("path", "").split("/")[0]
        children = stages_by_parent.get(pid, [])
        derived = _derive_parent_status(p, children)
        all_entries.append({**p, "_derived_status": derived})
    for s in standalone:
        all_entries.append({**s, "_derived_status": s.get("status", "pending")})
    for child_list in stages_by_parent.values():
        for c in child_list:
            all_entries.append({**c, "_derived_status": c.get("status", "pending")})

    # Group by derived status
    result: dict[str, dict[str, list[dict[str, Any]]]] = {s: {} for s in sorted(VALID_STATUS)}
    for e in all_entries:
        status = e.pop("_derived_status", "pending")
        parent_id = e.get("parent_id")
        scope_type = e.get("scope_type", "standalone")
        if status not in result:
            continue
        if scope_type == "stage" and parent_id:
            group = parent_id
        elif scope_type == "parent":
            group = e.get("path", "").split("/")[0] if e.get("path") else "_unparented"
        else:
            group = "_standalone"
        result[status].setdefault(group, []).append(e)
    return result


# ── CLI ──────────────────────────────────────────────────────────────────────

def _cli_extract(args):
    result = extract(args.file, args.fields or None)
    print(json.dumps(result, indent=2, ensure_ascii=False))


def _cli_index(args):
    result = index(args.track_root)
    print(json.dumps(result, indent=2, ensure_ascii=False))


def _cli_validate(args):
    errors = validate(args.file)
    if errors:
        print(f"INVALID: {args.file}")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print(f"VALID: {args.file}")


def _cli_children(args):
    result = children(args.parent_file)
    print(json.dumps(result, indent=2, ensure_ascii=False))


def _cli_kanban(args):
    result = kanban(args.track_root)
    for status, groups in result.items():
        total = sum(len(v) for v in groups.values())
        print(f"\n=== {status.upper()} ({total}) ===")
        for group, items in sorted(groups.items()):
            label = group if group != "_standalone" else "(standalone)"
            print(f"  {label}:")
            for item in items:
                scope = item.get("scope_type", "?")
                path = item.get("path", "?")
                print(f"    [{scope}] {path}")


def main():
    parser = argparse.ArgumentParser(description="Track document parser")
    sub = parser.add_subparsers(dest="command")

    p_ext = sub.add_parser("extract", help="Extract frontmatter fields")
    p_ext.add_argument("file", help="Path to track doc")
    p_ext.add_argument("fields", nargs="*", help="Fields to extract (default: all)")

    p_idx = sub.add_parser("index", help="Index all track docs under root")
    p_idx.add_argument("track_root", help="Track root directory")

    p_val = sub.add_parser("validate", help="Validate frontmatter schema")
    p_val.add_argument("file", help="Path to track doc")

    p_ch = sub.add_parser("children", help="List child stages of a parent")
    p_ch.add_argument("parent_file", help="Path to parent requirements doc")

    p_kb = sub.add_parser("kanban", help="Show kanban board by status")
    p_kb.add_argument("track_root", help="Track root directory")

    args = parser.parse_args()
    if args.command == "extract":
        _cli_extract(args)
    elif args.command == "index":
        _cli_index(args)
    elif args.command == "validate":
        _cli_validate(args)
    elif args.command == "children":
        _cli_children(args)
    elif args.command == "kanban":
        _cli_kanban(args)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
