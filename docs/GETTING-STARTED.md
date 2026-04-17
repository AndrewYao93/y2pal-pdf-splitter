# Y2Pal PDF Splitter Getting Started Guide

> Browser-based PDF splitter. No installer, no sign-up for the free tier. This guide covers first use, advanced split modes, encrypted PDFs, mobile workflow, and cloud-drive integration.

[← Back to README](../README.md)

---

## Browser Requirements

### Desktop

| Component  | Minimum                           | Recommended                 |
|------------|-----------------------------------|-----------------------------|
| Browser    | Chrome 90 / Firefox 88 / Safari 14 / Edge 90 | Latest stable build |
| OS         | Windows 10 / macOS 11 / any Linux | Latest version              |
| RAM        | 2 GB available                    | 4 GB+ for files over 100 MB |
| Storage    | 200 MB free (for temporary write) | 1 GB+                       |
| Network    | Stable HTTPS, 2 Mbps upload       | 10 Mbps+ upload             |

### Mobile

| Component  | Minimum                 | Recommended         |
|------------|-------------------------|---------------------|
| Browser    | Safari 14 / Chrome 90   | Latest stable build |
| OS         | iOS 14 / Android 10     | Latest version      |
| Network    | Stable cellular or Wi-Fi| Wi-Fi preferred     |

## First Use

### Step 1: Open the Page

Visit [y2pal.com/split-pdf](https://y2pal.com/split-pdf). There is no landing screen to dismiss and no pop-up — the drop zone is the first thing visible.

### Step 2: Upload a PDF

Drag a `.pdf` file onto the drop zone, or click **Upload File** to pick from disk. A single upload per session is supported in the free tier.

### Step 3: Choose a Split Mode

Three modes are available:

- **By page range** — enter comma-separated ranges such as `1-5, 8, 12-20`. Each range produces one output PDF.
- **Every N pages** — enter a number; the source is divided into fixed-size chunks. A 100-page PDF with N=25 yields 4 output files.
- **By bookmark** — the splitter reads the source's table-of-contents tree and splits at each top-level bookmark.

### Step 4: Download

When processing completes, each output PDF appears with its own download button. Use **Download All** for a zipped bundle.

## Advanced: Encrypted PDF

If the PDF is protected with an open password:

1. Upload the file normally.
2. A password prompt appears before processing.
3. Enter the open password. Y2Pal does not store or cache it.
4. Processing proceeds as usual after verification.

Owner-password PDFs (permissions-only locks) are not bypassed. Remove the permission lock locally before uploading — the splitter will refuse to process locked permissions by design.

## Advanced: Bookmark-Based Split

For PDFs with a table of contents:

1. Upload the source PDF.
2. Select **Split by bookmark**.
3. The tool lists detected top-level bookmarks with their page numbers.
4. Each bookmark becomes one output file named after its title.

If the source has no bookmarks, the option is disabled and the tool suggests page-range or every-N-pages mode.

## Advanced: Split-and-Re-Combine Workflow

A common workflow: split a bundled PDF, edit one of the pieces in another tool, then re-combine. Y2Pal PDF Splitter focuses on the split step. For the combine step, use [Y2Pal PDF Merger](https://y2pal.com/split-pdf) (separate tool in the Y2Pal suite).

## Mobile Workflow (iOS & Android)

On phones and tablets, drag-drop is limited; use the file picker instead:

1. Open [y2pal.com/split-pdf](https://y2pal.com/split-pdf) in mobile Safari or Chrome.
2. Tap **Upload File**.
3. Pick the PDF from the OS file browser — iCloud Drive, Files, Google Drive, Dropbox, etc. are all accessible through the native picker.
4. Choose a split mode and confirm.
5. Output files are saved to the device's Downloads folder (or prompted with a share sheet on iOS).

Mobile browsers enforce OS-level memory caps; source PDFs over 200 MB may fail on older devices. Move to a desktop browser for files that large.

## Integrating with Cloud Drives

Y2Pal PDF Splitter does not connect directly to cloud storage. The supported workflow:

1. Download the source PDF from iCloud / Google Drive / OneDrive / Dropbox to the local device (desktop or mobile).
2. Upload it to the splitter.
3. Save the split output to disk.
4. Re-upload the output files to the cloud drive.

This keeps Y2Pal out of the file's cloud-storage audit trail and avoids OAuth scope creep — a common ask from privacy-sensitive users.

## Keyboard Shortcuts (Desktop)

| Shortcut          | Action                                           |
|-------------------|--------------------------------------------------|
| Drag file         | Enter drop zone                                  |
| `Esc`             | Cancel active upload/processing                  |
| `Tab` / `Enter`   | Navigate and activate buttons (accessibility)    |

## Updating

There is no local install, so there is no update step. Y2Pal's cloud service is updated server-side; users always get the latest build on page reload.

## Clearing Local State

The splitter does not write cookies beyond the session identifier. To clear state:

- Close the tab.
- Or clear site data in the browser: Settings → Privacy → Cookies and Site Data → y2pal.com.

## Uninstalling / Removing Data

Because the tool is browser-delivered, there is nothing to uninstall. Source PDFs are removed from the cloud service after the session ends. Output files live only on the user's device.

---

[← Back to README](../README.md)
