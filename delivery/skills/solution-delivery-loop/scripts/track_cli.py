#!/usr/bin/env python3
"""Solution-delivery-loop track CLI — entry point for shared parser."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from track_parser import extract, validate, index, children, kanban, main

if __name__ == "__main__":
    main()
