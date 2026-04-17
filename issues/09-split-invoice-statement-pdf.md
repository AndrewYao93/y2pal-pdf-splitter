---
title: "How to Split an Invoice Statement PDF by Client or Month"
labels: guide
---

# How to Split an Invoice Statement PDF

Accounting systems and billing platforms often produce one consolidated PDF containing dozens of invoices — one per client, one per month, one per project. Archiving or forwarding individual invoices means first splitting the consolidated file.

## Two Common Invoice-Split Scenarios

- **One page per invoice** (common for subscription billing): use every-N=1 to extract every page, or use bookmarks if the source has them.
- **Multi-page invoices with per-invoice bookmarks**: use bookmark mode — each bookmark = one invoice.

Mixed-length invoices without bookmarks need manual page-range splitting.

## Step-by-Step Guide (Bookmark-Based)

### Step 1: Check for Bookmarks

Many accounting platforms (QuickBooks, Xero, SAP, NetSuite) embed a bookmark per invoice in the consolidated PDF. Verify by opening the source in Adobe Reader and checking the Bookmarks pane.

### Step 2: Upload

Visit [y2pal.com/split-pdf](https://y2pal.com/split-pdf) and upload the consolidated statement.

### Step 3: Select Bookmark Mode

If bookmarks are detected, Y2Pal lists them with invoice numbers/names (assuming the source named them well).

### Step 4: Split

Click **Split PDF**. Each output PDF is one invoice, named after its bookmark.

## Step-by-Step Guide (Every-N-Pages)

For uniform 1-page invoices without bookmarks:

### Step 1: Confirm Page Count = Invoice Count

Open the source and verify that each page is exactly one invoice.

### Step 2: Upload to Y2Pal

Same upload workflow as above.

### Step 3: Split Every 1 Page

Choose **Split every N pages** with `N = 1`. A 120-invoice statement yields 120 output files.

### Step 4: Bulk Download

Use **Download All** to zip all 120 files — saving them one by one is impractical.

## Handling Multi-Page Invoices Without Bookmarks

For a mixed-length statement (invoice A is 3 pages, invoice B is 5 pages, invoice C is 2 pages), use page-range mode:

### Step 1: Note Invoice Boundaries

Skim the source and note where each invoice starts/ends:

```
Invoice A: pages 1-3
Invoice B: pages 4-8
Invoice C: pages 9-10
```

### Step 2: Enter Ranges

```
1-3, 4-8, 9-10
```

### Step 3: Rename After Download

Files are named by page range; rename each to the invoice number after download.

## Workflow Tips

1. Ask your accounting software's admin to enable bookmark export for consolidated statements — it's usually a one-click setting that makes future splits trivial.
2. For per-client archiving, pair Y2Pal's split output with a cloud-drive naming convention like `Invoices/{CLIENT}/{YYYY-MM}_{INVOICE_ID}.pdf`.
3. If privacy is a concern (client financial data), close the browser tab after downloads to trigger server-side cleanup of the uploaded source.

## Tips

1. When renaming, use leading-zero numbering (`01-invoice`, `02-invoice`) so file explorers sort correctly.
2. For monthly recurring workflows, keep a template ranges file — the boundaries often repeat month to month.
3. Encrypted invoice statements should have the open password ready before starting the split.

## Requirements

- The consolidated invoice PDF.
- Accounting software that either embeds bookmarks or produces a predictable per-page layout.
- Any modern browser.

---

**[Open Y2Pal PDF Splitter →](https://y2pal.com/split-pdf)** | **[Back to README →](https://github.com/AndrewYao93/y2pal-pdf-splitter)**
