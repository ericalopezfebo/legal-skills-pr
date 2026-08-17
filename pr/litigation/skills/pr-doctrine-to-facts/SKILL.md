---
name: pr-doctrine-to-facts
title: Puerto Rico Doctrine-to-Facts Argument Builder
description: Polishes a drafted legal argument by connecting each cited authority to the specific facts of the case instead of leaving citations as free-floating quotations. Run this after drafting a motion, complaint, or brief that already contains legal citations but reads as a string of quotes rather than an argument. Use when the user says "conecta la jurisprudencia con los hechos", "esto lee como citas sueltas", "pule la argumentación", or "fortalece este fundamento de derecho".
author: legal-skills-pr
author_url: https://github.com/ericalopezfebo/legal-skills-pr
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pr
practice: litigation
language: es
---

# Puerto Rico Doctrine-to-Facts Argument Builder

## When to apply

- A draft already cites Tribunal Supremo or statutory authority, but each citation sits as an isolated quotation without being applied to the case's facts.
- The user asks to "pulir," "fortalecer," or "conectar" an argument, or complains that a section "reads like a list of quotes."
- **Out of scope:** finding new authority (route to `pr-legal-research`), verifying that cited authority exists and is current (route to `pr-citation-verifier`), and drafting the document from scratch (route to `pr-motion-drafting`, `pr-complaint-drafting`, or `pr-appellate-drafting`). This skill only strengthens the connective tissue between authority already in the draft and facts already in the record.

## Core rule

Every citation left "orphaned" — stated but never applied — is a wasted citation. A legal argument is a syllogism: **doctrina → aplicación a los hechos → conclusión**. This skill enforces that structure on existing citations. It does not add new facts, new case names, or new legal propositions; it only makes explicit the connection between what's already cited and what's already in the record.

## Algorithm

1. **Inventory every citation in the draft.** For each one, extract: the holding or rule it stands for (as already stated or implied in the draft — do not invent a holding that isn't already supported by the text or the user-supplied source), and whether it currently connects to any specific fact.
2. **Build a doctrine-to-facts map.** For each citation, identify which numbered facts, dates, documents, or record citations already in the draft actually fit that rule. If none do, flag the citation as unconnected rather than forcing a fit.
3. **Rewrite each connected citation using the three-part structure:**
   - **Doctrina:** state the rule, accurately and no more broadly than the source supports.
   - **Aplicación:** apply it explicitly to the case using a connector ("en el caso que nos ocupa," "aplicando esta doctrina a los hechos," "según consta en el Hecho [n]"), referencing the specific fact, date, or document already in the draft.
   - **Conclusión:** state the legal consequence that follows — only as strongly as the facts actually support.
4. **Flag orphaned citations** — authority cited but never tied to a fact — and either connect them to a real fact already in the draft or recommend removing them; never manufacture a fact to justify keeping a citation.
5. **Preserve accuracy over persuasion.** Do not upgrade a hedged or uncertain proposition into a categorical one to make the argument read more forcefully. If the underlying support is thin, say so rather than papering over it with confident language.
6. **Run a final check:** every citation is connected to a fact, every fact-to-doctrine link uses the party's actual record citations (not invented ones), and no new legal proposition was introduced that wasn't already in the draft or independently verified.

## Output contract

- Return the revised passage(s), not a rewrite of the entire document unless asked.
- List, separately, any citation you could not connect to a specific fact and why — do not silently drop or silently force it.
- Do not add a case name, statute, or holding that wasn't already in the draft; if the argument needs a new authority to work, say so and route to `pr-legal-research` instead of inventing one.
- Close with the mandatory disclaimer from `pr/CLAUDE.md`.
