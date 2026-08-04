---
name: realistic-doc-generation
description: Generate ultra-realistic but fully synthetic documents and document sets with realistic filled-in data, varied visual styles, scans/photos, forms, receipts, letters, tables, handwriting, and QA. Use when the user asks to create mock/synthetic documents, realistic sample artifacts, document-understanding test sets, training data documents, one document per category/type, or industry-specific document packs such as insurance, banking, healthcare, legal, government, invoices, IDs, claims, or onboarding artifacts.
---

# Realistic Document Generation

Use this skill to create believable synthetic documents for workflow demos, OCR/layout testing, extraction testing, and document-understanding prototypes.

## Core Principles

- Generate net-new fictional data. Do not copy real customer records, real IDs, real medical/legal claims, or live financial artifacts.
- Make the visible document look operational, not like a demo template. Avoid big watermarks, repeated styling, generic dashboards, and identical headers.
- Use synthetic names, addresses, IDs, providers, agencies, claim numbers, policy numbers, invoices, dates, line items, totals, signatures, and notes that are internally consistent.
- Keep safety caveats in README/manifest metadata or a low-visibility footer when needed. Do not put obvious "SYNTHETIC TRAINING SAMPLE" overlays on the documents unless the user explicitly requests watermarks.
- Vary source realism: phone photos, scanned forms, faxed packets, carrier PDFs, state records, thermal receipts, EHR printouts, law firm letters, shop estimates, handwritten annotations, stamps, barcodes, and imperfect alignment.
- Match structure to document type: receipts are usually one page, demand packets and medical records are multi-page, IDs are often photo captures, reports may be packets.
- Verify output by rendering representative pages and checking text extraction, page counts, zip contents, and obvious leftover placeholder/sample language.

## Workflow

1. Identify document types from the user input or attached files.
   - For PDFs or documents, extract the list first.
   - If categories are ambiguous, infer conservatively and mention assumptions.

2. Do targeted research when domain shapes matter.
   - Use official or public reference pages for field structure and layout conventions.
   - Do not copy source samples verbatim; use them only to understand field patterns.

3. Build a per-document style plan before generating.
   - Assign each document a distinct visual profile, source system, page count, and realism treatment.
   - Read `references/document-profiles.md` for reusable visual patterns.

4. Generate realistic synthetic data.
   - Use complete data, not placeholders.
   - Keep values cross-document consistent when documents belong to the same scenario.
   - Include realistic imperfections: abbreviated addresses, attachment references, adjuster notes, provider codes, processing logs, timestamps, signatures, checkboxes, and receipt artifacts.

5. Produce documents in the most natural format.
   - Prefer PDFs for form packets, letters, estimates, reports, and statements.
   - Use images embedded in PDFs for phone captures, scanned IDs, receipts, and photo uploads.
   - Use DOCX only when editability is the user’s main need.

6. Package deliverables.
   - Create one file per document type unless the user asks otherwise.
   - Include `manifest.csv` with type, file, page count, format, and style profile.
   - Include a short README explaining that all records are synthetic and listing research references.
   - Create a zip package when there are multiple documents.

7. QA before final response.
   - Run the verifier script if PDFs are produced:
     `python scripts/verify_document_set.py <output-folder> --zip <zip-file>`
   - Render representative first pages or thumbnails and inspect visually.
   - Check for repeated styling, obvious placeholders, giant watermarks, table overflow, black/transparent backgrounds, unreadable text, and leftover sample-language inside PDFs.

## Implementation Notes

- Use existing project/runtime libraries when available: ReportLab/Pillow/pypdf for PDF/image generation, python-docx for Word documents, openpyxl for manifests when needed.
- For high-realism image captures, create raster assets with Pillow, then embed them into PDFs.
- For handwriting, use italic/script-like fonts or image-layer annotations in blue/black ink. Do not rely on a single perfect font everywhere.
- Use muted visual diversity: different margins, typography, line weights, paper colors, form grids, receipt widths, letterheads, and scan noise. Avoid making everything colorful.
- Keep generation code in the working folder so the set is reproducible.

## References

- Use `references/document-profiles.md` for visual style profiles and document-type heuristics.
- Use `references/quality-checklist.md` before delivery.
