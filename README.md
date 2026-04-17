# Y2Pal PDF Splitter

> Online PDF splitter that separates one PDF into multiple files by page range, bookmark, or fixed interval — no install, no sign-up, runs in the browser.

Y2Pal PDF Splitter is a browser-based tool for splitting a single PDF document into smaller PDFs. Upload the source file, choose how to split it (by page range, bookmark, or every N pages), and download the resulting files. Processing happens on Y2Pal's cloud service; local files are removed after the session ends.

- Split by custom page ranges (e.g. `1-5`, `8`, `12-20`)
- Split by bookmarks / table-of-contents entries
- Split every N pages into equal parts
- Extract single pages as standalone PDFs
- Preserves original formatting, fonts, and embedded media
- Works on Windows, macOS, Linux, iOS, Android — anywhere a browser runs

## Links

- :rocket: Open the tool: [Y2Pal PDF Splitter](https://y2pal.com/split-pdf)
- :new: Version notes: [GitHub Releases](https://github.com/AndrewYao93/y2pal-pdf-splitter/releases/latest)
- :question: Comparison & help: [Y2Pal vs Y2mate — differences explained](https://y2pal.com/articles/y2pal-vs-y2mate-difference)
- :beetle: Report bugs: [GitHub Issues](https://github.com/AndrewYao93/y2pal-pdf-splitter/issues)

## Table of Contents

- [Why Y2Pal PDF Splitter](#why-y2pal-pdf-splitter)
- [Features](#features)
- [How It Works](#how-it-works)
- [Step-by-Step Tutorial](#step-by-step-tutorial-how-to-split-a-pdf-online)
- [Supported Input & Output](#supported-input--output)
- [Who It's For](#who-its-for)
- [Common Use Cases](#common-use-cases)
- [Troubleshooting](#troubleshooting)
- [Browser Requirements](#browser-requirements)
- [Getting Started](#getting-started)
- [Free Trial & Access](#free-trial--access)
- [FAQ](#faq)
- [Notes](#notes)
- [License](#license)

## Why Y2Pal PDF Splitter

Large PDFs are common: scanned books, multi-chapter reports, bundled invoices, exported presentations. But email attachment caps, page-specific review workflows, and chapter-by-chapter sharing all require breaking one PDF into several — and most desktop PDF editors are paid, heavyweight, or locked to a single OS.

Y2Pal PDF Splitter solves this at the URL level: one page, any device, no install step.

- **No software to install** — opens directly in Chrome, Firefox, Safari, Edge; nothing downloaded to disk until you export.
- **Three split modes** — by page range, by bookmark, or every N pages, so the same tool handles textbooks, reports, and invoices.
- **Cross-platform by default** — same workflow on Windows laptop, MacBook, Chromebook, iPad, Android tablet.
- **Preserves document fidelity** — fonts, form fields, annotations, and embedded images come through unchanged.
- **No account required for the free tier** — drag, split, download; the session leaves nothing behind after the tab closes.

## Features

- Split a single PDF into multiple PDFs by custom page ranges.
- Split by detected bookmarks (table-of-contents entries).
- Split every N pages into equal-sized chunks (common for print-layout exports).
- Extract individual pages as standalone 1-page PDFs.
- Preserves original fonts, embedded images, form fields, and annotations.
- Handles PDF 1.4 through PDF 2.0, including encrypted files if the open password is provided.
- Works with scanned PDFs (image-only) and born-digital PDFs alike.
- Bulk-download all resulting pieces as a single `.zip` archive.
- No watermark on output files.
- Files are processed over HTTPS and removed from the cloud after the session.
- Interface available in English, German, French, Japanese, and Simplified Chinese.
- Runs in any modern browser — no Flash, no Java, no plugin.

## How It Works

A PDF is dropped into the browser, streamed to Y2Pal's processing service over HTTPS, parsed into its page-level object tree, then split according to the chosen rule. Each output PDF is rebuilt as a valid standalone document with its own trailer, xref table, and metadata. Files are returned individually or bundled into a zip, and the source PDF is purged from the server once the session ends.

```
┌──────────────────┐     ┌──────────────────┐     ┌──────────────────┐
│  Browser Upload  │     │  Y2Pal Cloud     │     │  Download (local) │
│  Source PDF      │ ──► │  Split Engine    │ ──► │  Multiple PDFs /  │
│  (HTTPS, TLS 1.3)│     │  (range / bm / N)│     │  zip archive      │
└──────────────────┘     └──────────────────┘     └──────────────────┘
```

## Step-by-Step Tutorial: How to Split a PDF Online

### Step 1: Open the Splitter Page

Visit the Y2Pal PDF Splitter page (link at the top of this README) in any modern browser. No sign-up, no extension, no desktop installer required.

### Step 2: Upload the Source PDF

Drag a PDF onto the drop zone, or click **Upload File** to pick it from disk. The file is transferred over HTTPS. Max file size in the free tier is noted on the page header.

### Step 3: Choose a Split Rule

Pick one of the three modes: custom page ranges (enter values like `1-5, 8, 12-20`), split every N pages, or split at each bookmark. A live preview shows how many output PDFs will be produced before you confirm.

### Step 4: Download the Result

Once processing finishes, each resulting PDF appears as a separate download. Use **Download All** to get a single `.zip`. Files open in any PDF reader — Adobe Acrobat, Preview, Foxit, or a browser's built-in viewer.

## Supported Input & Output

| Direction | Format  | Version    | Notes                                                    |
|-----------|---------|------------|----------------------------------------------------------|
| Input     | PDF     | 1.4 – 2.0  | Text, scanned images, and hybrid PDFs all accepted       |
| Input     | PDF     | Encrypted  | Open password required; owner-password files unsupported |
| Output    | PDF     | 1.7        | Standard compatibility; opens in any modern PDF reader   |
| Output    | ZIP     | —          | Bundle of all resulting PDFs when splitting ≥ 2 files    |

## Who It's For

- **Students and academics** splitting a thesis, dissertation, or scanned textbook into per-chapter PDFs for annotation.
- **Legal and finance professionals** extracting specific exhibits or invoices from long bundled filings.
- **Content creators** cutting an export deck into per-slide handouts without reopening PowerPoint.
- **Anyone hitting email/attachment size limits** who needs to break a large PDF into mailable chunks.
- **Mobile and tablet users** who don't have access to a desktop PDF editor.

## Common Use Cases

| Use Case                          | How Y2Pal PDF Splitter Helps                                                    |
|-----------------------------------|---------------------------------------------------------------------------------|
| Share one chapter of a book       | Split by bookmark, download only the chapter PDF                                |
| Email a 50 MB PDF over a 25 MB cap| Split every N pages until each chunk fits the attachment limit                  |
| Extract a signed page from a bundle| Use single-page extraction to isolate the signature page                       |
| Print only pages 10–20 of a report| Split by range `10-20` and print the resulting PDF                              |
| Archive a multi-invoice statement | Split by bookmark so each invoice becomes its own file for per-client filing    |
| Prepare e-signing documents       | Extract specific pages, then re-combine with a signing tool after signature     |

## Troubleshooting

### Upload fails or stalls on very large PDFs

1. Check the free-tier file-size cap on the page header.
2. Verify the network upload speed (`≥ 2 Mbps` recommended for files over 100 MB).
3. Try a wired or hotel-wifi-free connection; some captive portals silently cap POST payload size.
4. If the PDF is over 500 MB, split it locally first with a desktop tool, then upload the pieces.
5. See the [full troubleshooting guide](docs/TROUBLESHOOTING.md).

### Output PDFs appear corrupted in certain readers

1. Confirm the reader supports PDF 1.7 (all readers since 2008 do).
2. Try opening the file in Chrome's built-in viewer as a baseline.
3. If pages with form fields render incorrectly, flatten the form in the source before splitting.
4. Report the specific reader version and source PDF type on [GitHub Issues](https://github.com/AndrewYao93/y2pal-pdf-splitter/issues).
5. See the [full troubleshooting guide](docs/TROUBLESHOOTING.md).

### Encrypted PDF rejected on upload

1. Supply the open password when prompted. Y2Pal does not cache passwords.
2. If the file has an owner password (permissions-only), remove it locally before uploading — Y2Pal does not bypass permission locks.
3. Verify that the PDF is not expired (some DRM-protected PDFs self-lock after a date).
4. See the [full troubleshooting guide](docs/TROUBLESHOOTING.md).

## Browser Requirements

| Component | Minimum                | Recommended              |
|-----------|------------------------|--------------------------|
| Browser   | Chrome 90 / Firefox 88 | Latest Chrome / Firefox  |
| Browser   | Safari 14 / Edge 90    | Latest Safari / Edge     |
| JavaScript| Enabled                | Enabled                  |
| Cookies   | Enabled (session only) | Enabled                  |
| Network   | Stable HTTPS           | 2 Mbps+ upload bandwidth |

Works on Windows 10/11, macOS 11+, any current Linux distro, iOS 14+, Android 10+, and ChromeOS.

## Getting Started

1. Open [y2pal.com/split-pdf](https://y2pal.com/split-pdf).
2. Upload the source PDF via drag-drop or file picker.
3. Choose a split mode (range / bookmark / every N pages).
4. Click **Split PDF**, then download the resulting files.

No installer, no registration, no email confirmation for the free tier. See the [getting-started guide](docs/INSTALLATION.md) for advanced workflows (bookmark detection, encrypted files, bulk splitting).

## Free Trial & Access

- Free tier: limited file size and daily operation count — exact limits listed on the page header.
- No credit card required for the free tier.
- Full feature access during the trial; output is unwatermarked.
- Lifetime license unlocks larger files, unlimited operations, and priority processing — see [product page](https://y2pal.com/split-pdf) for details.

## FAQ

### Is Y2Pal PDF Splitter free?

Yes, the free tier covers everyday splitting tasks with a capped file size and daily operation count. A lifetime license is available for higher limits.

### Does Y2Pal store my uploaded PDF?

Files are held only for the duration of processing and are deleted from Y2Pal's cloud service after the session ends. Transfers use HTTPS.

### Can I split a password-protected PDF?

Yes, if you supply the open password. Y2Pal does not bypass or remove owner-password permission locks.

### How do I split a PDF into exactly two halves?

Use the "split by page range" mode — if the source has 100 pages, enter ranges `1-50` and `51-100`. Or use "split every N pages" with `N = 50`.

### Does the tool work on iPad or iPhone?

Yes. Safari 14+ and Chrome on iOS 14+ are fully supported — the drag-drop area also accepts file-picker uploads from the Files app or iCloud Drive.

### Will the split PDFs lose form fields or signatures?

Form fields and annotations are preserved in each output file. Digital signatures remain valid only in the PDF containing the originally signed page(s); splitting the document invalidates signatures on the other pieces by design.

### Can I use Y2Pal PDF Splitter offline?

No — it's a browser-delivered service and requires an internet connection. For offline use, export the service via your OS's built-in PDF tools or a desktop editor.

### Is there a bulk or batch mode?

The single-session interface processes one source PDF at a time. To split many PDFs back-to-back, reload the page between operations, or use the Y2Pal All-in-One plan for chained workflows.

### Y2Pal PDF Splitter vs online competitors — what's different?

Y2Pal emphasizes clean server-side cleanup (files removed after the session), no watermark on output, and five UI languages including Japanese and Chinese — see the help link at the top for a detailed comparison.

### What happens if the upload disconnects midway?

The session is discarded and no partial file is retained. Retry the upload — Y2Pal does not reconstruct partial transfers.

## Notes

- You are responsible for confirming you have the right to split and redistribute the uploaded PDF content.
- Use of Y2Pal PDF Splitter must comply with the copyright, privacy, and export regulations applicable to your jurisdiction.
- The tool is intended for personal and internal business document workflows, not for stripping DRM or circumventing access controls.

## License

This project is released under the [MIT License](LICENSE).

Y2Pal PDF Splitter is a proprietary service developed by [Fabsoft Technology Limited](https://y2pal.com/).
