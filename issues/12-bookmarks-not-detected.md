---
title: "Y2Pal PDF Splitter Not Detecting Bookmarks — Solutions"
labels: troubleshooting
---

# Y2Pal PDF Splitter Not Detecting Bookmarks — Solutions

When bookmark-mode splitting is disabled or shows "no bookmarks found" for a PDF that you're sure has a table of contents, the cause is almost always that the PDF's TOC is visual (text on a page), not structural (in the bookmark tree).

## Common Causes & Solutions

### 1. The PDF Has a Visual TOC, Not Structural Bookmarks

A table of contents printed as text on page 3 is just text — Y2Pal cannot extract it. Structural bookmarks live in a separate tree that appears in Adobe Reader's left sidebar.

**Fix**: Open the PDF in Adobe Reader. If the Bookmarks pane is empty, there are no structural bookmarks. Add them in a desktop editor or use page-range mode as a fallback.

### 2. Source Exporter Strips Bookmarks

Some PDF exporters (old versions of Word, rasterizing print drivers) drop bookmarks during export.

**Fix**: Re-export from the source application with "Create bookmarks from headings" enabled, or manually add bookmarks in a desktop editor.

### 3. PDF Is Image-Only (Scanned)

Scanned PDFs are image-only and have no bookmark tree by design.

**Fix**: Use page-range mode with manually noted chapter start pages. Or OCR the PDF first (which still doesn't add bookmarks — those need to be added explicitly afterward).

### 4. Bookmarks Exist but at a Deeper Level

Y2Pal's default is top-level bookmarks only. A deeply nested TOC may appear empty if top-level entries are missing.

**Fix**: Check Adobe Reader's bookmark pane — if entries only appear when expanded, they're nested. Use the depth selector in Y2Pal if available, or flatten bookmarks locally.

### 5. Update Y2Pal PDF Splitter

Bookmark parsing is updated periodically. The latest server build is always live at the URL — just reload the page. Release notes: [GitHub Releases](https://github.com/AndrewYao93/y2pal-pdf-splitter/releases).

### 6. Bookmarks Reference Pages via Named Destinations

Some PDFs use named destinations instead of direct page references in bookmarks — an edge case that occasionally trips parsers.

**Fix**: Convert to direct page references using a desktop tool, then re-upload.

### 7. Encrypted PDF With Restricted Permissions

Even with the correct open password, some encrypted PDFs restrict bookmark extraction via owner-password flags.

**Fix**: Remove the owner-password permission lock locally (using `qpdf --decrypt` or similar), then re-upload.

### 8. File Corruption Affecting the TOC

A partially corrupted PDF may have a valid page stream but a broken bookmark tree.

**Fix**: Open in a desktop reader — if bookmarks render strangely there too, the source is damaged. Re-export from the original if possible.

## Still Not Working?

- Try uploading a known-good PDF with structural bookmarks (any modern ebook export) to confirm bookmark detection works on your account.
- Fall back to page-range mode — it's the universal option.
- [Open a bug report →](https://github.com/AndrewYao93/y2pal-pdf-splitter/issues/new?template=bug_report.md)

---

**[Open Y2Pal PDF Splitter →](https://y2pal.com/split-pdf)** | **[Back to README →](https://github.com/AndrewYao93/y2pal-pdf-splitter)**
