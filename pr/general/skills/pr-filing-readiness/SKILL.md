---
name: pr-filing-readiness
title: Puerto Rico Filing Readiness Audit
description: Performs a final pre-filing audit of a Puerto Rico legal document for jurisdiction, deadlines, procedural compliance, record support, citations, requested relief, consistency, and unresolved placeholders.
author: legal-skills-pr
author_url: https://github.com/ericalopezfebo/legal-skills-pr
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pr
practice: general
language: es
---

# Puerto Rico Filing Readiness Audit

## Purpose
This is a final quality-control gate, not a substitute for substantive legal research.

## Audit
Check:
- tribunal/agency and caption;
- parties and representative capacity;
- jurisdiction and review vehicle;
- filing/service deadline;
- procedural rule requirements;
- requested relief;
- factual support and record references;
- exhibits/appendix references;
- legal authorities and quotations;
- citation format;
- signatures/certifications where applicable;
- confidential information/redaction issues;
- internal dates, names, defined terms and cross-references;
- unresolved `[POR COMPLETAR]` or `[VERIFICAR]` markers.

## Result
Return one of:
- `READY FOR ATTORNEY FINAL REVIEW`
- `NOT READY — MATERIAL ISSUES`
- `NOT READY — MISSING INFORMATION`

List blocking issues first. Never certify that a filing is legally sufficient merely because formatting checks pass.
