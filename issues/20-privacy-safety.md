---
title: "Y2Pal PDF Splitter Privacy — Is It Safe to Upload PDFs?"
labels: faq
---

# Y2Pal PDF Splitter Privacy — Is It Safe?

A fair question for any cloud-processed tool. Here's the detailed answer for Y2Pal PDF Splitter.

## Data Handling Summary

| Aspect                     | Y2Pal PDF Splitter Behavior                           |
|----------------------------|-------------------------------------------------------|
| Upload transport           | HTTPS with TLS 1.3                                    |
| Source PDF retention       | Session duration only; removed after session ends     |
| Output PDF retention       | Session duration only; removed after session ends     |
| Logs                       | Anonymized operational logs only; no file contents    |
| User account               | Not required for free tier                            |
| Training / AI use          | Uploaded PDFs are not used for training or AI         |
| Third-party sharing        | None                                                  |
| Region                     | EU & US cloud regions                                 |

## Is It Safe for Confidential Documents?

For most everyday confidential documents — tax returns, contracts, academic papers — yes. The combination of HTTPS transit and session-end deletion meets typical professional privacy expectations.

However, Y2Pal is not a zero-knowledge tool. Files transit through Y2Pal's infrastructure for processing. For the most sensitive workflows, local processing is still safer.

## When to Use a Local Tool Instead

- HIPAA-covered PHI without a Business Associate Agreement in place.
- Attorney-client privileged documents with strict "no third-party disclosure" protocols.
- Classified or export-controlled documents.
- Documents under strict retention policies that prohibit any cloud transit.

For these cases, command-line tools (`qpdf`, `pdftk`, `pdfcpu`) or desktop applications (Adobe Acrobat, PDF Expert) process the file entirely locally.

## What Y2Pal Does Not Do

- Does not index file contents for search.
- Does not train AI/ML models on user uploads.
- Does not share files with advertisers, data brokers, or affiliates.
- Does not retain files beyond the session end.
- Does not read or cache encryption passwords beyond in-memory use for decryption.

## Account-Holder Users (Lifetime License)

Users with a lifetime license have an account tied to their purchase email. This account is used for entitlement verification only; it does not change the file-retention rules above.

## Questions or Concerns?

- Review the privacy policy at `y2pal.com/privacy-policy` for legal-grade wording.
- Contact `contact@y2pal.com` for specific data-handling questions.

---

**[Open Y2Pal PDF Splitter →](https://y2pal.com/split-pdf)** | **[Back to README →](https://github.com/AndrewYao93/y2pal-pdf-splitter)**
