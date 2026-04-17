---
title: "Y2Pal PDF Splitter 2026.04 Update — Bookmark Mode Released"
labels: update
---

# Y2Pal PDF Splitter 2026.04 Update

The April 2026 update ships automatic bookmark detection, an expanded language list, and a faster upload pipeline. This is a server-side update — no user action required; the next time you load the page, you're on the new build.

## What's New in 2026.04

### 1. Bookmark-Based Split Mode

Split at each top-level bookmark of the source PDF in one pass. The tool now auto-detects structural bookmarks and presents them as a checkbox list. Each selected bookmark becomes one output PDF named after its bookmark title.

Perfect for:

- Academic textbooks with chapter bookmarks.
- Legal bundles with per-exhibit bookmarks.
- Consolidated invoice statements with per-invoice bookmarks.
- Multi-section annual reports.

### 2. Five Interface Languages

The UI is now available in English, German, French, Japanese, and Simplified Chinese. Automatic language detection from `Accept-Language`, with manual override in the header dropdown.

### 3. Download-All ZIP Bundle

When splitting produces ≥ 2 output files, a **Download All** button appears. Files bundle into a single zip archive — handy when splitting produces 50+ pieces that would otherwise require 50+ clicks to download.

### 4. TLS 1.3 Upload Transport

All uploads now negotiate TLS 1.3 by default, with automatic fallback for legacy clients. Improves both security and upload latency.

## Improvements

- Upload pipeline rewritten for streaming — PDFs over 100 MB start processing sooner.
- Output PDFs preserve form fields, annotations, and embedded media correctly when splitting by range.
- File size caps increased for the free tier (see page header for current value).
- Safari 14 drag-drop regression fixed; valid PDFs are now accepted correctly.
- Mobile layout refresh: larger tap targets, better drop zone on iPad.

## Bug Fixes

- Fixed page-range parsing for overlapping ranges like `1-5, 4-8` (output count was previously off-by-one in edge cases).
- Fixed zip archive losing filenames containing non-ASCII characters (CJK, accented Latin, Arabic).
- Fixed Firefox strict tracking protection blocking the download action in some configurations.
- Fixed occasional mobile Safari tab suspension mid-upload producing a misleading "upload failed" error.

## What's Coming Next

- Programmatic API access (tentative for Q3 2026).
- Additional UI languages based on user request volume.
- Advanced bookmark depth controls (split by nested sub-bookmarks, not just top-level).

## Access

| Channel | Link                                  |
|---------|---------------------------------------|
| Web     | [y2pal.com/split-pdf](https://y2pal.com/split-pdf) |

No download required — the new build is already live on the service URL.

## Feedback

Found a bug or have a feature idea from this release?

- [Open a bug report →](https://github.com/AndrewYao93/y2pal-pdf-splitter/issues/new?template=bug_report.md)
- [Request a feature →](https://github.com/AndrewYao93/y2pal-pdf-splitter/issues/new?template=feature_request.md)

---

**[Back to README →](https://github.com/AndrewYao93/y2pal-pdf-splitter)**
