#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

import fitz


def add_annotation(page: fitz.Page, anchor: str, note: str) -> bool:
    hits = page.search_for(anchor)
    if not hits:
        return False
    rect = hits[0]
    highlight = page.add_highlight_annot(rect)
    highlight.set_info(title="Codex", subject=anchor, content=note)
    highlight.update()
    point = fitz.Point(min(rect.x1 + 8, page.rect.width - 32), rect.y0)
    sticky = page.add_text_annot(point, note)
    sticky.set_info(title="Codex", subject=anchor)
    sticky.update()
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description="Add text-linked PDF annotations from JSON.")
    parser.add_argument("input_pdf", type=Path)
    parser.add_argument("annotations_json", type=Path)
    parser.add_argument("output_pdf", type=Path)
    args = parser.parse_args()

    entries = json.loads(args.annotations_json.read_text(encoding="utf-8"))
    doc = fitz.open(args.input_pdf)
    missing: list[tuple[int, str]] = []
    try:
        for entry in entries:
            page_num = int(entry["page"])
            anchor = str(entry["anchor"])
            note = str(entry["note"])
            if not add_annotation(doc[page_num - 1], anchor, note):
                missing.append((page_num, anchor))
        args.output_pdf.parent.mkdir(parents=True, exist_ok=True)
        doc.save(args.output_pdf, garbage=4, deflate=True)
    finally:
        doc.close()

    if missing:
        print("Missing anchors:")
        for page_num, anchor in missing:
            print(f"page {page_num}: {anchor}")
        raise SystemExit(2)


if __name__ == "__main__":
    main()
