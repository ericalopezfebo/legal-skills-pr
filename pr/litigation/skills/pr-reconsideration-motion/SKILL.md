---
name: pr-reconsideration-motion
title: Puerto Rico Motion for Reconsideration
description: Analyzes and drafts a Puerto Rico civil motion for reconsideration, with deadline screening, identification of the challenged ruling, precise grounds, and preservation of appellate consequences.
author: legal-skills-pr
author_url: https://github.com/ericalopezfebo/legal-skills-pr
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pr
practice: litigation
language: es
---

# Puerto Rico Motion for Reconsideration

## When to apply
- A party seeks reconsideration of an order, resolution, judgment, or other determination in a Puerto Rico civil case.

## Workflow
1. Obtain the challenged decision, its entry/notification date, the exact relief granted or denied, and the procedural posture.
2. Determine whether Regla 47 or another specific statute/rule governs the reconsideration request. Verify the current rule text and term before stating a deadline.
3. Determine whether the motion is timely and whether filing it may affect appellate or other review periods. Treat these consequences as high-risk and require current-law verification.
4. Identify the exact asserted error: overlooked controlling authority, manifest legal error, overlooked record evidence, newly relevant procedural development, or another recognized basis supported by current Puerto Rico law.
5. Do not merely repeat the prior motion. Tie each reconsideration ground to a specific part of the challenged ruling and explain why correction matters.
6. Use only evidence already in the record unless current procedure permits consideration of additional material; flag any attempt to introduce new evidence.
7. State the precise modification, vacatur, or other relief requested.

## Guardrails
- Never calculate a reconsideration or appellate deadline from memory.
- Never state that a reconsideration automatically tolls or interrupts another term unless the current governing rule and the motion's compliance requirements have been verified.
- Do not invent the contents or reasoning of the challenged ruling.
- Verify all case law, pin cites, rule numbers, and current validity before filing.
- Pair with `pr-civil-deadlines`, `pr-legal-research`, `pr-citation-verifier`, and `pr-filing-readiness`.

## Output structure
Draft, when requested:
- caption and title;
- identification of the challenged determination and date;
- timeliness/jurisdictional section using verified law;
- concise procedural background;
- specific grounds for reconsideration;
- application to the record;
- precise prayer for relief;
- signature and service certification.

Use `[VERIFICAR TÉRMINO]` rather than supplying an unverified deadline.

Close with the mandatory disclaimer from `pr/CLAUDE.md`.
