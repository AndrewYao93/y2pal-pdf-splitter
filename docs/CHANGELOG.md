# Changelog

All notable changes to Y2Pal PDF Splitter.

[← Back to README](../README.md)

---

## [2026.04.01] — 2026-04-01

### What's New
- Bookmark-detection split mode — reads the source PDF's table-of-contents tree and splits at each top-level bookmark automatically.
- Localized UI in 5 languages: English, German, French, Japanese, Simplified Chinese.
- "Download All" bundles output PDFs into a single zip archive.

### Improvements
- Upload transfer switched to TLS 1.3 with automatic fallback for legacy clients.
- Output PDFs now preserve form field state, annotations, and embedded media correctly when splitting by range.
- File size cap increased for the free tier.

### Bug Fixes
- Fixed page-range parsing for overlapping ranges such as `1-5, 4-8`.
- Fixed zip generation losing filenames containing non-ASCII characters.
- Fixed Safari 14 drag-drop regression where the drop zone rejected valid PDFs.

### Access

| Channel | Link |
|---------|------|
| Web     | [y2pal.com/split-pdf](https://y2pal.com/split-pdf) |

---

## [2026.02.15] — 2026-02-15

### What's New
- Encrypted PDF support — accepts PDFs with open-passwords (PDF 1.4 RC4, PDF 2.0 AES-256, all versions in between).
- "Every N pages" split mode for evenly chunking large documents.

### Improvements
- Mobile layout refresh: larger tap targets, better drop zone behavior on iPad.
- Processing latency reduced for PDFs over 100 MB (streaming rewrite of the splitter core).

### Bug Fixes
- Fixed an issue where PDFs with embedded subset fonts rendered with substituted fonts after splitting.
- Fixed zip archive download not triggering on Firefox with strict tracking protection enabled.

---

## [2025.12.01] — 2025-12-01

### What's New
- Initial public release of Y2Pal PDF Splitter.
- Split by page range (comma-separated, inclusive ranges).
- PDF 1.4 through PDF 2.0 input support.
- Output as PDF 1.7 for broadest reader compatibility.

### Improvements
- First-party drop zone with visual state transitions (idle, dragging, uploading, processing, ready).
- Clean session teardown — source PDFs removed from processing bucket once the browser session closes.

### Bug Fixes
- N/A (initial release).

---

[← Back to README](../README.md)
