# Y2Pal PDF Splitter Supported Formats & Document Types — Complete List

> Y2Pal PDF Splitter accepts PDF 1.4 through PDF 2.0 as input and produces standards-compliant PDF 1.7 output. Below is the complete compatibility matrix organized by PDF version, document type, browser, language, and integration pattern.

[← Back to README](../README.md)

---

## PDF Specification Versions (Input)

| #  | Version  | Year  | Acrobat Equivalent | Support                          |
|----|----------|-------|--------------------|----------------------------------|
| 1  | PDF 1.4  | 2001  | Acrobat 5          | Full                             |
| 2  | PDF 1.5  | 2003  | Acrobat 6          | Full                             |
| 3  | PDF 1.6  | 2004  | Acrobat 7          | Full                             |
| 4  | PDF 1.7  | 2006  | Acrobat 8          | Full (ISO 32000-1)               |
| 5  | PDF 2.0  | 2017  | Acrobat DC         | Full (ISO 32000-2)               |
| 6  | PDF/A-1a | 2005  | Archival           | Preserved on output              |
| 7  | PDF/A-1b | 2005  | Archival           | Preserved on output              |
| 8  | PDF/A-2a | 2011  | Archival           | Preserved on output              |
| 9  | PDF/A-2b | 2011  | Archival           | Preserved on output              |
| 10 | PDF/A-3a | 2012  | Archival + attach  | Preserved on output              |
| 11 | PDF/A-3b | 2012  | Archival + attach  | Preserved on output              |
| 12 | PDF/A-4  | 2020  | Archival           | Preserved on output              |
| 13 | PDF/X-1a | 2001  | Print              | Preserved on output              |
| 14 | PDF/X-3  | 2003  | Print              | Preserved on output              |
| 15 | PDF/X-4  | 2010  | Print              | Preserved on output              |
| 16 | PDF/UA-1 | 2012  | Accessibility      | Tags preserved on output         |
| 17 | PDF/E-1  | 2008  | Engineering        | Preserved on output              |

## Encrypted PDF Support

| #  | Encryption Type              | Support                       |
|----|------------------------------|-------------------------------|
| 18 | PDF 1.4 RC4 40-bit           | Open-password supplied        |
| 19 | PDF 1.5 RC4 128-bit          | Open-password supplied        |
| 20 | PDF 1.6 AES-128              | Open-password supplied        |
| 21 | PDF 1.7 AES-128              | Open-password supplied        |
| 22 | PDF 2.0 AES-256              | Open-password supplied        |
| 23 | Owner-password only (perms)  | Not bypassed — remove locally |
| 24 | Public-key (certificate)     | Not supported                 |

## Document Type / Use Case Compatibility

### Academic & Reference

| #  | Document Type                  | Typical Split Mode              |
|----|--------------------------------|---------------------------------|
| 25 | Dissertation / thesis          | Split by bookmark (by chapter)  |
| 26 | Research paper collection      | Split by page range             |
| 27 | Scanned textbook               | Split by page range             |
| 28 | Lecture notes bundle           | Split by bookmark               |
| 29 | Conference proceedings         | Split by bookmark               |
| 30 | Journal issue                  | Split by bookmark               |
| 31 | Course syllabus packet         | Split by page range             |
| 32 | Exam bank                      | Split every N pages             |
| 33 | Study guide multi-unit         | Split by bookmark               |
| 34 | Bibliography-only extract      | Split by page range             |

### Legal & Compliance

| #  | Document Type                  | Typical Split Mode              |
|----|--------------------------------|---------------------------------|
| 35 | Court filing with exhibits     | Split by bookmark per exhibit   |
| 36 | Contract bundle                | Split by page range             |
| 37 | Deposition transcript          | Split by page range             |
| 38 | Discovery document set         | Split by page range             |
| 39 | Witness statement packet       | Split by bookmark               |
| 40 | Regulatory filing              | Split by bookmark               |
| 41 | Insurance claim bundle         | Split every N pages             |
| 42 | Compliance audit report        | Split by bookmark               |
| 43 | Arbitration exhibit packet     | Split by page range             |
| 44 | Patent application             | Split by bookmark               |

### Finance & Business

| #  | Document Type                  | Typical Split Mode              |
|----|--------------------------------|---------------------------------|
| 45 | Annual report                  | Split by bookmark per section   |
| 46 | Invoice statement batch        | Split by bookmark per invoice   |
| 47 | Bank statement archive         | Split every N pages             |
| 48 | Credit card statement bundle   | Split every N pages             |
| 49 | Tax return with schedules      | Split by page range             |
| 50 | Audit workpapers               | Split by bookmark               |
| 51 | Board meeting packet           | Split by bookmark               |
| 52 | Financial prospectus           | Split by bookmark               |
| 53 | Expense report bundle          | Split every N pages             |
| 54 | Payroll document packet        | Split every N pages             |

### Publishing & Print

| #  | Document Type                  | Typical Split Mode              |
|----|--------------------------------|---------------------------------|
| 55 | Book / eBook manuscript        | Split by bookmark per chapter   |
| 56 | Magazine issue                 | Split by bookmark per article   |
| 57 | Newsletter archive             | Split by page range             |
| 58 | Catalog by category            | Split by bookmark               |
| 59 | Product brochure set           | Split by page range             |
| 60 | Art portfolio                  | Split by page range             |
| 61 | Comic / graphic novel          | Split by bookmark per issue     |
| 62 | Textbook with chapter quizzes  | Split by bookmark               |
| 63 | Anthology                      | Split by bookmark per story     |
| 64 | Cookbook by section            | Split by bookmark               |

### Engineering, Technical & Scientific

| #  | Document Type                  | Typical Split Mode              |
|----|--------------------------------|---------------------------------|
| 65 | Technical drawing set          | Split by page range             |
| 66 | CAD export bundle              | Split by page range             |
| 67 | Engineering specification      | Split by bookmark               |
| 68 | Scientific paper supplement    | Split by page range             |
| 69 | Lab protocol collection        | Split by bookmark               |
| 70 | Clinical trial report          | Split by bookmark               |
| 71 | Datasheet compendium           | Split by bookmark               |
| 72 | Product manual multi-device    | Split by bookmark               |
| 73 | Safety data sheet binder       | Split by bookmark               |
| 74 | Maintenance logbook            | Split every N pages             |

### Government & Education Forms

| #  | Document Type                  | Typical Split Mode              |
|----|--------------------------------|---------------------------------|
| 75 | Government benefit application | Split by page range             |
| 76 | Passport / visa form packet    | Split by page range             |
| 77 | School enrollment bundle       | Split by page range             |
| 78 | Medical intake packet          | Split by page range             |
| 79 | Employment onboarding packet   | Split by bookmark               |
| 80 | Grant application              | Split by page range             |
| 81 | Building permit filing         | Split by bookmark               |
| 82 | Licensing exam packet          | Split every N pages             |
| 83 | Customs declaration bundle     | Split by page range             |
| 84 | Tender / RFP response          | Split by bookmark               |

## Output Options

| #  | Format   | Container | Notes                                                  |
|----|----------|-----------|--------------------------------------------------------|
| 85 | PDF 1.7  | .pdf      | Default output, opens in any modern PDF reader         |
| 86 | ZIP      | .zip      | Auto-bundle when 2+ result files (Deflate compression) |

## Browser & Device Compatibility

| #  | Browser / Runtime    | Minimum           | Notes                              |
|----|----------------------|-------------------|------------------------------------|
| 87 | Google Chrome        | 90                | All platforms                      |
| 88 | Mozilla Firefox      | 88                | All platforms                      |
| 89 | Apple Safari         | 14                | macOS 11+, iOS 14+                 |
| 90 | Microsoft Edge       | 90                | Chromium-based only                |
| 91 | Opera                | 76                | Chromium base                      |
| 92 | Brave                | 1.20              | Chromium base                      |
| 93 | Samsung Internet     | 14                | Android                            |
| 94 | Vivaldi              | 3.7               | Chromium base                      |
| 95 | DuckDuckGo Browser   | Latest            | Mobile                             |

## OS Compatibility

| #   | Operating System       | Notes                           |
|-----|------------------------|---------------------------------|
| 96  | Windows 10             | 64-bit recommended              |
| 97  | Windows 11             | Native support                  |
| 98  | macOS 11 Big Sur       | Intel and Apple Silicon         |
| 99  | macOS 12 Monterey      | Intel and Apple Silicon         |
| 100 | macOS 13 Ventura       | Intel and Apple Silicon         |
| 101 | macOS 14 Sonoma        | Intel and Apple Silicon         |
| 102 | macOS 15 Sequoia       | Apple Silicon preferred         |
| 103 | Ubuntu 20.04 / 22.04   | Any Chromium-family browser     |
| 104 | Fedora 38+             | Any Chromium-family browser     |
| 105 | Debian 11+             | Any Chromium-family browser     |
| 106 | ChromeOS               | Native Chrome                   |
| 107 | iOS 14+ / iPadOS 14+   | Safari or Chrome                |
| 108 | Android 10+            | Chrome, Samsung Internet, etc.  |

## Interface Language Support

| #   | Language              | Subdomain / Path      |
|-----|-----------------------|-----------------------|
| 109 | English               | `y2pal.com`           |
| 110 | Deutsch (German)      | `de.y2pal.com`        |
| 111 | Français (French)     | `fr.y2pal.com`        |
| 112 | 日本語 (Japanese)     | `ja.y2pal.com`        |
| 113 | 简体中文 (Chinese)    | `zh.y2pal.com`        |

---

## Need a format or document type not listed?

PDF Splitter is updated regularly. Check the [Releases page](https://github.com/AndrewYao93/y2pal-pdf-splitter/releases) for changes.

**Missing format?** [Open a Feature Request →](https://github.com/AndrewYao93/y2pal-pdf-splitter/issues/new?template=feature_request.md)

---

[← Back to README](../README.md)
