---
name: pr-motion-extension-time
title: Puerto Rico Motion for Extension of Time
description: Drafts a Puerto Rico civil motion requesting an extension of time, calculating and explaining the existing deadline only from verified dates and rules, and stating supported good cause without inventing facts.
author: legal-skills-pr
author_url: https://github.com/ericalopezfebo/legal-skills-pr
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pr
practice: litigation
language: es
---

# Puerto Rico Motion for Extension of Time

## When to apply
- Requesting additional time to answer, oppose, comply with an order, complete discovery, or file another civil-court submission in Puerto Rico.

## Workflow
1. Identify the document/order/event that triggered the deadline and obtain the exact date of service, notice or entry.
2. Identify the governing rule, statute, scheduling order or prior extension. Do not calculate from memory when the source is not verified.
3. Determine the present deadline and whether the request is being filed before or after it. If after, flag the need to analyze the applicable standard for late relief.
4. Obtain the exact extension requested: number of days or proposed new date.
5. State good cause using only facts supplied by the user. Do not embellish workload, illness, scheduling conflicts, discovery needs, settlement discussions or opposing counsel's position.
6. If the other side consented, opposed or took no position, characterize that position exactly. If unknown, omit it or mark `[POR CONFIRMAR]`.
7. Explain why the requested extension will not cause undue prejudice only if facts support that proposition.
8. Recalculate the proposed date under the current Puerto Rico computation-of-time rules and any order governing the case.

## Guardrails
- Never invent a deadline or assume that electronic notice, weekends, holidays or an extension operate a particular way without verifying the governing rule.
- Never state that opposing counsel consented unless the user supplies that fact.
- Do not describe an extension as automatic.
- If the deadline may be jurisdictional, statutory, non-extendable or tied to post-judgment/appellate review, stop and require specific verification before drafting as an ordinary extension.
- Apply `pr-civil-deadlines`, `pr/CLAUDE.md`, and `pr-filing-readiness` where available.

## Output structure
Draft a concise motion containing:
- caption;
- title identifying the filing for which more time is requested;
- current deadline and verified source;
- supported good cause;
- precise requested new deadline;
- statement regarding the opposing party only if known;
- prayer for relief;
- signature and service certification as applicable.

Close with the mandatory disclaimer from `pr/CLAUDE.md`.
