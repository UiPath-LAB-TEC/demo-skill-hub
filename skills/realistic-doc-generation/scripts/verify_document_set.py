#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import sys
import zipfile
from pathlib import Path


DEFAULT_FORBIDDEN = [
    "synthetic",
    "mock",
    "training sample",
    "watermark",
    "fictional",
    "placeholder",
    "lorem",
    "tbd",
    "not valid",
]


def extract_pdf_text(path: Path) -> tuple[int, str]:
    try:
        from pypdf import PdfReader
    except Exception as exc:
        raise RuntimeError("pypdf is required for PDF verification") from exc

    reader = PdfReader(str(path))
    text = "\n".join((page.extract_text() or "") for page in reader.pages)
    return len(reader.pages), text


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify a generated synthetic document set.")
    parser.add_argument("folder", type=Path, help="Folder containing generated documents")
    parser.add_argument("--zip", dest="zip_path", type=Path, help="Optional zip package to inspect")
    parser.add_argument("--allow-term", action="append", default=[], help="Forbidden term to allow")
    parser.add_argument("--no-term-scan", action="store_true", help="Skip forbidden-term scan")
    args = parser.parse_args()

    folder = args.folder
    if not folder.exists() or not folder.is_dir():
        print(f"ERROR: folder not found: {folder}", file=sys.stderr)
        return 2

    pdfs = sorted(folder.glob("*.pdf"))
    if not pdfs:
        print("ERROR: no PDFs found", file=sys.stderr)
        return 2

    forbidden = [t for t in DEFAULT_FORBIDDEN if t not in set(args.allow_term)]
    rows = []
    hits = []
    total_pages = 0
    empty_text = []

    for pdf in pdfs:
        pages, text = extract_pdf_text(pdf)
        total_pages += pages
        rows.append({"file": pdf.name, "pages": pages, "chars": len(text.strip())})
        if not text.strip():
            empty_text.append(pdf.name)
        if not args.no_term_scan:
            lower = text.lower()
            for term in forbidden:
                if term.lower() in lower:
                    hits.append((pdf.name, term))

    manifest = folder / "manifest.csv"
    if manifest.exists():
        with manifest.open(newline="", encoding="utf-8") as f:
            manifest_rows = list(csv.DictReader(f))
        manifest_files = {r.get("file") for r in manifest_rows}
        missing = [p.name for p in pdfs if p.name not in manifest_files]
        if missing:
            print(f"ERROR: PDFs missing from manifest: {missing}", file=sys.stderr)
            return 1

    if args.zip_path:
        if not args.zip_path.exists():
            print(f"ERROR: zip not found: {args.zip_path}", file=sys.stderr)
            return 2
        with zipfile.ZipFile(args.zip_path) as zf:
            names = set(zf.namelist())
        missing_in_zip = [p.name for p in pdfs if not any(n.endswith('/' + p.name) or n == p.name for n in names)]
        if missing_in_zip:
            print(f"ERROR: PDFs missing from zip: {missing_in_zip}", file=sys.stderr)
            return 1

    print(f"Verified {len(pdfs)} PDFs, {total_pages} total pages")
    for row in rows:
        print(f"{row['file']}: pages={row['pages']} text_chars={row['chars']}")

    if empty_text:
        print(f"WARNING: PDFs with no extractable text: {empty_text}", file=sys.stderr)
    if hits:
        print(f"ERROR: forbidden terms found: {hits}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
