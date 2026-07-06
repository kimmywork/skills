#!/usr/bin/env python3
"""Requirement-discovery track CLI — thin wrapper around shared parser."""
import sys
from pathlib import Path

# Import shared parser from solution-delivery-loop
_SDL_SCRIPTS = Path(__file__).resolve().parents[2] / "solution-delivery-loop" / "scripts"
sys.path.insert(0, str(_SDL_SCRIPTS))

from track_parser import extract, validate, index, children, kanban, main

if __name__ == "__main__":
    main()
