---
name: pr-motion-dismiss
title: Puerto Rico Motion to Dismiss (Regla 10.2)
description: Analyzes and drafts a Puerto Rico civil motion to dismiss under Regla 10.2, separating procedural defenses, the applicable standard, preservation issues, and claim-specific analysis.
author: legal-skills-pr
author_url: https://github.com/ericalopezfebo/legal-skills-pr
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pr
practice: litigation
language: es
---

# Puerto Rico Motion to Dismiss (Regla 10.2)

## When to apply
- A party seeks dismissal of a complaint or claim in the Puerto Rico Court of First Instance before or in lieu of an answer when procedurally permitted.
- The user asks about defenses traditionally raised under Regla 10.2 of the Puerto Rico Rules of Civil Procedure.

## Workflow
1. Confirm the forum. This skill is for Puerto Rico Commonwealth civil procedure, not Fed. R. Civ. P. 12.
2. Obtain the operative complaint, summons/service history, amendments, prior responsive pleadings and relevant orders.
3. Identify each proposed Rule 10.2 ground separately. Verify the current text and numbering of the rule before filing.
4. Check waiver/preservation and sequencing. Some defenses may be waived if omitted from the first permitted Rule 10 motion or responsive pleading; do not assume every defense can be raised at any time.
5. For failure-to-state-a-claim arguments, identify each challenged cause of action and the elements supplied by verified Puerto Rico substantive law. Map the well-pleaded allegations to those elements without adding facts.
6. Distinguish allegations that the court must assume for purposes of the motion from legal conclusions, documents properly considered, and matters outside the pleadings. If outside materials could alter the procedural treatment, flag that issue rather than silently relying on them.
7. Analyze whether dismissal is sought with or without prejudice and whether amendment may be relevant. Do not request preclusive relief without legal support.
8. Draft separate sections for each ground and a precise prayer for relief.

## Guardrails
- Never invent a defect in service, jurisdiction, venue, capacity, standing or the allegations of the complaint.
- Do not cite federal Rule 12 standards as controlling Puerto Rico law unless a verified Puerto Rico authority adopts or uses them appropriately.
- Verify every Rule 10.2 subsection, current case citation, pin cite and proposition before filing.
- Do not convert disputed facts into dismissal arguments unless the procedural vehicle permits their consideration.
- Pair with `pr-legal-research`, `pr-citation-verifier`, `pr-motion-drafting`, and `pr-filing-readiness`.

## Output structure
When requested, produce:
1. caption and title;
2. procedural background;
3. applicable Regla 10.2 standard, with verified authority;
4. separately headed dismissal grounds;
5. claim-by-claim application where appropriate;
6. requested disposition and whether it is sought with/without prejudice only when supported;
7. signature and service certification.

Use `[VERIFICAR AUTORIDAD]` or `[POR COMPLETAR]` rather than inventing support.

Close with the mandatory disclaimer from `pr/CLAUDE.md`.
