#!/usr/bin/env python3
"""Track document parser for drafting-loop tracks."""

from __future__ import annotations
import argparse, json, re, sys
from pathlib import Path
from typing import Any

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
VALID_STATUS = {"pending", "in_progress", "blocked", "done"}
VALID_KIND = {"crafting", "composing", "evaluating", "investigating", "creating", "mixed"}
VALID_PHASE = {"Sense", "Clarify", "Shape", "Design", "Build", "Verify", "Record", "ContinueStop"}
VALID_SCOPE = {"parent", "stage", "standalone"}


def parse_frontmatter(text: str) -> dict[str, Any] | None:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return None
    data: dict[str, Any] = {}
    for raw in match.group(1).splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, val = line.split(":", 1)
        key = key.strip()
        val = val.strip().strip('"').strip("'")
        if key == "version":
            try:
                data[key] = int(val)
            except ValueError:
                data[key] = val
        else:
            data[key] = val
    return data


def read_frontmatter(path: str | Path) -> dict[str, Any] | None:
    return parse_frontmatter(Path(path).read_text(encoding="utf-8"))


def extract(path: str | Path, fields: list[str] | None = None) -> dict[str, Any]:
    fm = read_frontmatter(path)
    if fm is None:
        return {"error": "missing frontmatter"}
    if fields:
        return {k: fm.get(k) for k in fields}
    return fm


def _candidate_track_docs(folder: Path) -> list[Path]:
    return [p for p in [folder / "requirements-v1.md", folder / "track.md"] if p.exists()]


def validate(path: str | Path) -> list[str]:
    p = Path(path)
    fm = read_frontmatter(p)
    errors: list[str] = []
    if fm is None:
        return ["missing frontmatter"]

    required = ["status", "kind", "phase", "scope_type", "created", "version"]
    if fm.get("scope_type") == "stage":
        required.append("parent_id")
    for key in required:
        if key not in fm:
            errors.append(f"missing field: {key}")

    if "status" in fm and fm["status"] not in VALID_STATUS:
        errors.append(f"invalid status: {fm['status']}")
    if "kind" in fm and fm["kind"] not in VALID_KIND:
        errors.append(f"invalid kind: {fm['kind']}")
    if "phase" in fm and fm["phase"] not in VALID_PHASE:
        errors.append(f"invalid phase: {fm['phase']}")
    if "scope_type" in fm and fm["scope_type"] not in VALID_SCOPE:
        errors.append(f"invalid scope_type: {fm['scope_type']}")
    if "created" in fm and not re.match(r"^\d{4}-\d{2}-\d{2}$", str(fm["created"])):
        errors.append("created must be YYYY-MM-DD")
    if "version" in fm and not isinstance(fm["version"], int):
        errors.append("version must be an integer")

    scope = fm.get("scope_type")
    if scope == "stage":
        parent_id = fm.get("parent_id")
        if parent_id:
            parent_dir = p.parent.parent / parent_id
            if not parent_dir.exists():
                errors.append(f"parent_id points to missing folder: {parent_id}")
    if scope == "parent":
        child_dirs = [d for d in p.parent.iterdir() if d.is_dir()]
        matching = []
        for child in child_dirs:
            for doc in _candidate_track_docs(child):
                cfm = read_frontmatter(doc)
                if cfm and cfm.get("scope_type") == "stage" and cfm.get("parent_id") == p.parent.name:
                    matching.append(cfm)
        if not matching:
            errors.append("parent has no matching stage children")
        elif fm.get("status") == "done" and any(c.get("status") != "done" for c in matching):
            errors.append("parent marked done but at least one child is not done")
    return errors


def index(root: str | Path) -> list[dict[str, Any]]:
    base = Path(root)
    rows = []
    for md in sorted(base.rglob("*.md")):
        fm = read_frontmatter(md)
        if fm:
            rows.append({"path": str(md.relative_to(base)), **fm})
    return rows


def children(parent_file: str | Path) -> list[dict[str, Any]]:
    p = Path(parent_file)
    parent_dir = p.parent
    parent_id = parent_dir.name
    rows = []
    for child in sorted([d for d in parent_dir.iterdir() if d.is_dir()]):
        for doc in _candidate_track_docs(child):
            fm = read_frontmatter(doc)
            if fm and fm.get("scope_type") == "stage" and fm.get("parent_id") == parent_id:
                rows.append({"path": str(doc), **fm})
    return rows


def kanban(root: str | Path) -> dict[str, list[dict[str, Any]]]:
    board = {s: [] for s in sorted(VALID_STATUS)}
    for row in index(root):
        status = row.get("status", "pending")
        if status in board:
            board[status].append(row)
    return board


def main() -> None:
    ap = argparse.ArgumentParser(description="Drafting-loop track parser")
    sub = ap.add_subparsers(dest="cmd")
    p = sub.add_parser("extract"); p.add_argument("file"); p.add_argument("fields", nargs="*")
    p = sub.add_parser("validate"); p.add_argument("file")
    p = sub.add_parser("index"); p.add_argument("root")
    p = sub.add_parser("children"); p.add_argument("parent_file")
    p = sub.add_parser("kanban"); p.add_argument("root")
    args = ap.parse_args()

    if args.cmd == "extract":
        print(json.dumps(extract(args.file, args.fields or None), indent=2, ensure_ascii=False))
    elif args.cmd == "validate":
        errs = validate(args.file)
        if errs:
            print("INVALID")
            for err in errs:
                print(f"- {err}")
            sys.exit(1)
        print("VALID")
    elif args.cmd == "index":
        print(json.dumps(index(args.root), indent=2, ensure_ascii=False))
    elif args.cmd == "children":
        print(json.dumps(children(args.parent_file), indent=2, ensure_ascii=False))
    elif args.cmd == "kanban":
        print(json.dumps(kanban(args.root), indent=2, ensure_ascii=False))
    else:
        ap.print_help(); sys.exit(1)


if __name__ == "__main__":
    main()
