---
title: "How to Split a Scanned PDF into Chapters — Books & Textbooks"
labels: guide
---

# How to Split a Scanned PDF into Chapters

Scanned PDFs — photocopied textbooks, archived manuscripts, image-only digitizations — rarely have structural bookmarks. That means bookmark-based splitting doesn't work, but page-range mode does. Here's the workflow for turning one scanned book into one file per chapter.

## The Problem with Scanned PDFs

- No structural TOC, even when the scanned book has a printed table of contents.
- Pages are images, not text — so automatic chapter detection via OCR is unreliable.
- File sizes are large (0.8–2.5 MB per page at 300–600 DPI).

Y2Pal PDF Splitter solves this with manual page-range splitting plus sensible defaults.

## Step-by-Step Guide

### Step 1: Identify Chapter Start Pages

Open the scanned PDF in any reader. Note the **absolute page position** where each chapter starts — not the printed "Chapter 1 p. 1" number, but the PDF page position (which counts cover, front matter, and blank pages).

Example for a 320-page scan:

| Chapter    | Starts at PDF Page | Ends at PDF Page |
|------------|--------------------|------------------|
| Front matter | 1                | 12               |
| Chapter 1  | 13                 | 45               |
| Chapter 2  | 46                 | 82               |
| Chapter 3  | 83                 | 124              |
| Chapter 4  | 125                | 178              |
| Chapter 5  | 179                | 230              |
| Chapter 6  | 231                | 285              |
| Appendix   | 286                | 320              |

### Step 2: Upload

Visit [y2pal.com/split-pdf](https://y2pal.com/split-pdf). A scanned 300-page PDF can easily be several hundred MB — see the free-tier cap before uploading.

### Step 3: Enter the Ranges

Select **Split by page range** and type all chapter ranges at once:

```
1-12, 13-45, 46-82, 83-124, 125-178, 179-230, 231-285, 286-320
```

The tool produces 8 output files in one operation.

### Step 4: Rename Output Files

Output files are named by page range (`source_pages_13-45.pdf`). For a scanned book, rename them to chapter titles after download for library management.

## Speeding Up Repeated Splits

If you regularly split similar-format scanned books, keep a spreadsheet of chapter ranges per book — paste the full range string into the tool rather than typing it each time.

## Handling Very Large Scans

A full-color 600 DPI scan of a 500-page book can exceed 1 GB. Approaches:

1. Re-scan or re-process at a lower DPI (300 DPI is usually sufficient for text) using desktop OCR tools.
2. First split locally with a desktop tool into halves, then upload each half to Y2Pal for chapter-level splitting.

## Tips

1. Count pages including front matter — the cover, copyright page, and TOC all occupy PDF page positions even if they're not numbered in the book.
2. If the scan has blank pages between chapters, include them in the preceding chapter's range to avoid orphan files.
3. For academic citation, keep a master file that maps chapter titles to PDF page ranges — the output files are easier to cite with a reference table.

## Requirements

- A scanned PDF (image-only or OCR'd).
- Absolute PDF page positions for each chapter start and end.
- Sufficient free-tier cap to upload the full file (or first split locally).

---

**[Open Y2Pal PDF Splitter →](https://y2pal.com/split-pdf)** | **[Back to README →](https://github.com/AndrewYao93/y2pal-pdf-splitter)**
