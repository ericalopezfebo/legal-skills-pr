---
name: pr-default-relief
title: Puerto Rico Default and Default Judgment Relief
description: Analyzes and drafts Puerto Rico civil requests related to entry of default, default judgment, or relief from default, with service, notice, proof, and procedural safeguards.
author: legal-skills-pr
author_url: https://github.com/ericalopezfebo/legal-skills-pr
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pr
practice: litigation
language: es
---

# Puerto Rico Default and Default Judgment Relief

## When to apply
- A plaintiff seeks entry of default or judgment after a defendant failed to plead or otherwise defend.
- A party seeks to set aside an entry of default or challenge a default judgment.

## Workflow
1. Obtain the operative pleading, summons, proof of service or waiver, service date, response deadline, appearances by the opposing party, and relevant orders.
2. Confirm the forum and identify whether the requested relief is governed by Regla 45 of the Puerto Rico Rules of Civil Procedure or a more specific procedure, such as a special statutory or Rule 60 collection proceeding.
3. Distinguish carefully among: (a) entry/anotación of default, (b) judgment after default, and (c) relief from/set-aside of default or judgment. Do not collapse these into one step.
4. Verify that service and the time to respond support the requested procedural step. Do not infer proper service from absence of an answer.
5. Identify whether the requested damages/remedy are liquidated, require proof, or require a hearing. A default does not authorize inventing damages or relief beyond what law and the pleadings permit.
6. Identify notice requirements that may arise from a prior appearance or other circumstances and verify them under current law.
7. If seeking to set aside default, organize the facts relevant to the governing Puerto Rico standard without inventing excusable neglect, good cause, meritorious defenses, prejudice, or promptness.
8. Draft the precise procedural relief supported by the record.

## Guardrails
- Never state that a party is in default without calculating the applicable response term from verified service/notice facts.
- Never treat default as an automatic admission of the amount of damages.
- Verify the current text of Regla 45 and any special rule/statute before filing.
- Distinguish ordinary civil default practice from special procedures such as Regla 60.
- Pair with `pr-civil-deadlines`, `pr-legal-research`, and `pr-filing-readiness`.

## Output structure
When requested, draft the appropriate Puerto Rico filing with:
- caption and title;
- service and procedural chronology;
- verified governing rule;
- explanation of the requested default-related step;
- proof/damages discussion where relevant;
- exact relief requested;
- signature and service certification.

Close with the mandatory disclaimer from `pr/CLAUDE.md`.
