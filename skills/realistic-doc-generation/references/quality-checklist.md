# Quality Checklist

Run this before delivery.

## Content

- One document exists per requested document type.
- No placeholders remain: no `TBD`, `Lorem`, `Sample Name`, blank critical fields, or generic IDs.
- Cross-document scenario data is consistent: names, claim/policy numbers, VINs, dates, providers, totals.
- Page counts fit the document type.
- README/manifest identify the set as synthetic; visible documents do not rely on giant watermarks.

## Visual Realism

- Documents do not all share the same header, colors, margins, or table style.
- At least some artifacts include realistic capture/source variation: scan noise, phone image, fax marks, handwriting, receipt paper, system printout, letterhead, or form grids.
- Tables fit within page bounds and text remains readable.
- Raster captures render with white/nontransparent backgrounds.
- No overly polished design-system look unless the document type is a modern portal PDF.

## Verification

- Generated PDFs open and have expected page counts.
- PDF text extraction works where expected. Image-only captures may have less text, but the set should still be inspectable.
- Zip contains only intended deliverables.
- Search extracted text for giveaway phrases if the user requested realism without visible sample labeling:
  `synthetic`, `mock`, `training sample`, `watermark`, `fictional`, `placeholder`, `not valid`.
- Render representative pages and inspect visually.
