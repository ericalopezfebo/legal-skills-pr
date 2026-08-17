---
name: pr-motion-compel-discovery
title: Puerto Rico Motion to Compel Discovery
description: Analyzes deficient discovery responses and drafts a Puerto Rico motion to compel, tying each requested item to the actual request, response or objection, meet-and-confer history, and requested relief.
author: legal-skills-pr
author_url: https://github.com/ericalopezfebo/legal-skills-pr
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pr
practice: litigation
language: es
---

# Puerto Rico Motion to Compel Discovery

## When to apply
- A party received incomplete discovery responses, objections, or no response in a Puerto Rico civil case.
- The user needs to organize a motion seeking an order compelling discovery.

## Workflow
1. Obtain the exact discovery requests, responses/objections, dates of service, extensions, and relevant scheduling orders.
2. Build a request-by-request matrix: request number; substance; response/objection; deficiency; relevance/proportionality rationale; relief sought.
3. Identify and document any required good-faith effort to resolve the dispute before court intervention. Use only communications actually supplied by the user.
4. Evaluate objections individually. Do not label an objection improper merely because it is boilerplate; explain the legal and factual reason it is insufficient if support exists.
5. Separate requests for complete answers, document production, privilege-log issues, deposition relief, and sanctions or expenses.
6. If privilege or work-product protection is asserted, do not demand disclosure of protected material merely because the response is incomplete; analyze whether a log, description, redaction or judicial review may be appropriate under current law.
7. Draft narrowly tailored relief keyed to specific discovery requests.
8. Request sanctions, expenses or fees only when the governing rule and facts support them.

## Guardrails
- Never invent a discovery request, response, meet-and-confer communication, deadline, prejudice, or refusal.
- Do not characterize silence as willful noncompliance without facts.
- Verify the current Puerto Rico Rules of Civil Procedure governing the discovery device and motion practice before filing.
- Preserve confidential and privileged material.
- Pair with `pr-discovery-drafting`, `pr-discovery-response`, `pr-legal-research`, and `pr-filing-readiness`.

## Output structure
When asked for a finished motion, draft:
- caption and title;
- concise discovery history;
- good-faith resolution efforts, if supported;
- governing rule and standard with verified authority;
- numbered deficiencies tied to the actual requests/responses;
- precise relief requested, including dates if appropriate;
- any supported request for expenses/sanctions;
- signature and service certification.

Close with the mandatory disclaimer from `pr/CLAUDE.md`.
