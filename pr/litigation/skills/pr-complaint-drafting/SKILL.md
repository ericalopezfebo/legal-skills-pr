---
name: pr-complaint-drafting
title: Puerto Rico Complaint Drafting
description: Drafts Puerto Rico civil complaints from supplied facts and verified causes of action, with jurisdiction, standing, parties, factual allegations, claims, and prayer for relief.
author: legal-skills-pr
author_url: https://github.com/ericalopezfebo/legal-skills-pr
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pr
practice: litigation
language: es
---

# Puerto Rico Complaint Drafting

## Purpose
Draft a complaint without inventing facts, causes of action, damages, jurisdictional allegations, service information, or parties.

## Workflow
1. Identify court, jurisdiction, venue, parties, capacity and standing.
2. Build a chronology using only supplied facts.
3. Identify each proposed cause of action and its elements under current Puerto Rico law.
4. Map factual allegations to each element. Flag unsupported elements.
5. Screen prescription/caducity and required pre-suit steps when relevant.
6. Determine remedies actually available.
7. Draft numbered factual allegations followed by separately identified causes of action.
8. State the prayer for relief precisely.
9. Audit party names, dates, exhibits, amounts, legal authorities and internal cross-references.

## Guardrails
- Do not plead a fact merely because it would strengthen the claim.
- Distinguish information and belief from known facts when legally appropriate.
- Do not manufacture damages amounts.
- Do not cite a cause of action unless its current legal basis has been verified.
- Use `[POR COMPLETAR]` for missing filing information and `[VERIFICAR]` for unresolved legal propositions.
- Apply `pr/CLAUDE.md`, `pr-legal-research`, and `pr-legal-citation` as needed.

## Output
When asked for a finished complaint, produce the pleading rather than a memo about how to write one. Flag material gaps after the draft.
