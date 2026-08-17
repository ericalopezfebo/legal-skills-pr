---
name: pr-summary-judgment-motion
title: Puerto Rico Summary Judgment Motion Builder (Regla 36)
description: Structures a moción de sentencia sumaria or its opposition under Regla 36 of Puerto Rico's Reglas de Procedimiento Civil, including the numbered statement of uncontested material facts the Tribunal Supremo requires. Use when the user says "prepara una moción de sentencia sumaria", "necesito oponerme a sentencia sumaria", "hechos incontrovertidos Regla 36", or is drafting/opposing summary judgment in a Puerto Rico civil case.
author: legal-skills-pr
author_url: https://github.com/ericalopezfebo/legal-skills-pr
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pr
practice: litigation
language: es
---

# Puerto Rico Summary Judgment Motion Builder (Regla 36)

## When to apply

- Drafting a moción de sentencia sumaria (motion for summary judgment) or an oposición a sentencia sumaria in a Puerto Rico Commonwealth civil case.
- Reviewing whether a draft complies with Regla 36's numbered-facts requirement before filing.
- **Out of scope:** federal court summary judgment under Fed. R. Civ. P. 56 (different standard and local rules) — confirm the forum before applying this skill; and arguing the merits of a specific cause of action, which requires substantive research (pair with the `pr-legal-research` skill).

## Algorithm

1. **Confirm the forum and the governing rule.** This skill applies to Regla 36, Reglas de Procedimiento Civil de 2009, según enmendadas, 32 LPRA Ap. V — Commonwealth court only. If the case is in the U.S. District Court for the District of Puerto Rico, stop and flag that Fed. R. Civ. P. 56 and the district's local rules govern instead.
2. **Gather the record citations.** Every material fact asserted must cite to a specific page/paragraph of the record (deposición, declaración jurada, documento, admisión, contestación a interrogatorio). A fact without a pinpoint record citation cannot go in the numbered list — flag it back to the user rather than inventing a citation.
3. **Draft the numbered statement of uncontested material facts** — short, separately numbered, one fact per paragraph, each ending in a record citation. This is the part the Tribunal Supremo has repeatedly held is not optional: a court may disregard facts not presented this way.
4. **If opposing:** for each numbered fact, state whether it is admitted, denied, or denied in part, with a record citation for any denial or qualification, and add any additional material facts the moving party omitted, in the same numbered format.
5. **Apply the standard.** State the standard for summary judgment under Puerto Rico law — no genuine issue of material fact, movant entitled to judgment as a matter of law, evidence and reasonable inferences viewed in the light most favorable to the non-movant. When citing the controlling articulation of the standard, cite the specific Tribunal Supremo opinion the user or the record relies on (e.g., practitioners frequently cite *Meléndez González et al. v. M. Cuebas, Inc.*, 193 DPR 100 (2015), on the appellate standard of review for summary judgment) — **verify the pin cite and confirm the case is still good law before filing; do not rely on this skill's memory of the holding.**
6. **Assemble the motion** per the output contract, leaving explicit placeholders for anything not yet confirmed (missing record cite, unconfirmed case holding, deadline).

## Output contract

```markdown
[CAPTION DEL TRIBUNAL Y CASO]

MOCIÓN DE SENTENCIA SUMARIA
(u OPOSICIÓN A MOCIÓN DE SENTENCIA SUMARIA)

AL HONORABLE TRIBUNAL:

COMPARECE [parte], por conducto de la representación legal que suscribe, y respetuosamente EXPONE Y SOLICITA:

I. INTRODUCCIÓN
[Resumen breve de la solicitud y fundamento]

II. RELACIÓN DE HECHOS MATERIALES INCONTROVERTIDOS
1. [Hecho]. [Cita al récord].
2. [Hecho]. [Cita al récord].
[...]

III. DERECHO APLICABLE
[Estándar de Regla 36 con cita, y derecho sustantivo aplicable a la causa de acción]

IV. ARGUMENTACIÓN
[Aplicación del derecho a los hechos incontrovertidos]

V. SÚPLICA
POR TODO LO CUAL, se solicita que este Honorable Tribunal [dicte sentencia sumaria a favor de / deniegue la sentencia sumaria solicitada por] [parte].

[Lugar y fecha]
[Firma y datos de la representación legal]
```

- Every numbered fact must carry a record citation or an explicit `[FALTA CITA AL RÉCORD]` placeholder — never fabricate one.
- Every case citation carries a note to verify pin cite and current validity.
- Close with the mandatory disclaimer from `pr/CLAUDE.md`.
