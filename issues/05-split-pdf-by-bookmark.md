---
title: "How to Split a PDF by Bookmark or Chapter — Auto TOC Detection"
labels: guide
---

# How to Split a PDF by Bookmark (Table of Contents)

When a PDF has real bookmarks — the structured tree Adobe Acrobat shows in its left panel — splitting at each bookmark is the fastest way to get one file per chapter, one file per invoice, or one file per exhibit. Y2Pal PDF Splitter auto-detects bookmarks and presents them as checkboxes.

## Bookmark-Based vs Page-Range Splitting

| Aspect                     | Bookmark mode             | Page-range mode          |
|----------------------------|---------------------------|--------------------------|
| Input required             | Just click chapters       | Type range numbers       |
| Accuracy                   | Matches source structure  | Depends on user typing   |
| Works on scanned PDFs      | Only if bookmarks exist   | Always                   |
| Naming                     | Uses bookmark titles      | Uses range (e.g. 1-5)    |

Bookmark mode is the right choice when the document already has structural TOC — textbooks, legal bundles with exhibit bookmarks, multi-invoice statements, etc.

## Step-by-Step Guide

### Step 1: Confirm the PDF Has Bookmarks

Open the source PDF in Adobe Reader, Preview, or Chrome's built-in viewer. Look for a sidebar labeled **Bookmarks** or a tree icon. If the sidebar is empty, there are no structural bookmarks — a visual TOC on a page does not count.

### Step 2: Upload to Y2Pal

Visit [y2pal.com/split-pdf](https://y2pal.com/split-pdf) and upload the PDF.

### Step 3: Select Bookmark Mode

Y2Pal auto-detects bookmarks. If found, the "Split by bookmark" option is available with a tree view of detected entries and their page numbers.

### Step 4: Choose Bookmark Depth

- **Top-level only** (default): each top-level bookmark becomes one file.
- **Deeper levels** (advanced): if the PDF has nested sub-chapters, choose how deep to split.

### Step 5: Review Output Names

Each output file is named after its bookmark title. Review and edit names before confirming — bookmark titles sometimes contain characters that are illegal in file names.

### Step 6: Split and Download

Click **Split PDF**. Output PDFs appear with their bookmark titles.

## What Counts as a Bookmark?

| Source                          | Has Structural Bookmarks? |
|---------------------------------|---------------------------|
| Exported from InDesign/Word with TOC | Yes                  |
| Exported from LaTeX with hyperref     | Yes                  |
| Scanned book, text-OCR only           | No (add manually)    |
| Bundled PDF with click-to-page nav    | Yes                  |
| Printed visual TOC (text on page 3)   | No                   |

## Adding Bookmarks to a PDF That Lacks Them

If your PDF has no bookmarks, add them first in a desktop editor:

1. Open in Adobe Acrobat Pro or a free alternative (PDFescape, Foxit).
2. Add one bookmark per chapter at the correct page.
3. Save and re-upload to Y2Pal.

Alternatively, use page-range mode with manually noted chapter start pages.

## Tips

1. Clean up bookmark titles before splitting if they contain slashes or special characters — the tool sanitizes, but manual review avoids awkward file names.
2. For deeply nested bookmark trees, start with top-level only; nested splits can multiply files unexpectedly.
3. Bookmark mode is unavailable if no bookmarks are detected — use page-range mode as a fallback.

## Requirements

- Source PDF with structural bookmarks.
- A browser that supports modern JavaScript (Chrome 90+, Firefox 88+).

---

**[Open Y2Pal PDF Splitter →](https://y2pal.com/split-pdf)** | **[Back to README →](https://github.com/AndrewYao93/y2pal-pdf-splitter)**
