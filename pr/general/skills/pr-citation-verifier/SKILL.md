---
name: pr-citation-verifier
title: Puerto Rico Legal Citation Verifier
description: Verifies Puerto Rico legal authorities and citation propositions before a filing or legal document relies on them; detects fabricated, mismatched, obsolete, or unsupported authorities.
author: legal-skills-pr
author_url: https://github.com/ericalopezfebo/legal-skills-pr
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pr
practice: general
language: es
---

# Puerto Rico Legal Citation Verifier

## Purpose
Treat every citation as a claim requiring verification.

## Verification matrix
For each authority determine:
1. Does the source exist?
2. Is the citation/identifier accurate?
3. Is it the correct jurisdiction and court?
4. Is the authority current?
5. Does the cited page/section actually support the proposition?
6. Is quoted language exact?
7. Is the authority binding, persuasive, superseded, amended, reversed, or otherwise limited?
8. Does a newer primary source materially change the proposition?

## Output statuses
- `VERIFIED`
- `VERIFIED WITH QUALIFICATION`
- `NOT VERIFIED`
- `CONTRADICTED`
- `OBSOLETE/SUPERSEDED`

Never “repair” an apparently fabricated case by silently substituting a different authority. Explain the discrepancy and provide a verified alternative only when one is actually located.
