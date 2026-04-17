---
title: "How to Split a Password-Protected PDF — Encrypted File Guide"
labels: guide
---

# How to Split a Password-Protected PDF

Encrypted PDFs come in two flavors: open-password (you need the password to read it) and owner-password (you can read it but certain actions like printing or copying are restricted). Y2Pal PDF Splitter handles the first; the second needs to be removed locally first.

## Open Password vs Owner Password

| Type             | Behavior                                                    | Y2Pal Behavior             |
|------------------|-------------------------------------------------------------|----------------------------|
| Open password    | Password required to open/read the PDF                      | Supported — supply password|
| Owner password   | File opens freely; restricts print/copy/edit/extract        | Not bypassed — remove first|

Y2Pal never bypasses owner-password permission locks by design — that protects the original author's intent.

## Step-by-Step Guide (Open Password)

### Step 1: Upload the Encrypted PDF

Visit [y2pal.com/split-pdf](https://y2pal.com/split-pdf) and upload the file normally. The server detects encryption and prompts for a password.

### Step 2: Enter the Open Password

Type the password into the prompt. The password is used in-memory for decryption and is never written to disk, never logged, and never transmitted outside the processing worker.

### Step 3: Choose a Split Mode

Once decrypted, the split UI behaves identically to an unencrypted file — page range, bookmark, or every-N-pages.

### Step 4: Output Options

Choose whether to:

- Produce unencrypted output PDFs (default).
- Produce output PDFs re-encrypted with the same password (advanced — select the "Preserve encryption" checkbox if visible).

## Supported Encryption Schemes

| PDF Version | Algorithm     | Support                       |
|-------------|---------------|-------------------------------|
| PDF 1.4     | RC4 40-bit    | With open-password            |
| PDF 1.5     | RC4 128-bit   | With open-password            |
| PDF 1.6     | AES-128       | With open-password            |
| PDF 1.7     | AES-128       | With open-password            |
| PDF 2.0     | AES-256       | With open-password            |

## Handling Owner-Password PDFs

If your PDF is owner-password-only (no prompt appears when opening, but operations are blocked):

1. Open the file in a desktop reader that supports permission removal (Adobe Acrobat Pro or free tools like `qpdf`).
2. Save an unlocked copy.
3. Upload the unlocked copy to Y2Pal.

## Tips

1. Do not paste the password into any chat, comment, or Issue — Y2Pal's interface is the only place it should appear.
2. For recurring encrypted-PDF workflows, upgrade to a lifetime license for faster processing of large encrypted files.
3. If splitting fails after password entry, confirm the password is the **open** password (not the owner password).

## Requirements

- The source PDF's open password, if encrypted.
- A supported browser version.
- Private network — enter passwords only from trusted machines.

---

**[Open Y2Pal PDF Splitter →](https://y2pal.com/split-pdf)** | **[Back to README →](https://github.com/AndrewYao93/y2pal-pdf-splitter)**
