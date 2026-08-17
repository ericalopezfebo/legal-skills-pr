---
name: pr-agency-appeal-lpau
title: Puerto Rico Administrative Agency Appeal (LPAU)
description: Structures a recurso de revisión judicial from a Puerto Rico administrative agency's final order or resolution to the Tribunal de Apelaciones under the Ley de Procedimiento Administrativo Uniforme (LPAU), including public-employee appeals to the Comisión Apelativa del Sistema de Administración de Recursos Humanos (CASARH, formerly CASP). Use when the user says "recurso de revisión administrativa", "apelar una resolución de la agencia", "CASP" or "CASARH", "LPAU", or is challenging a Puerto Rico agency's final decision.
author: legal-skills-pr
author_url: https://github.com/ericalopezfebo/legal-skills-pr
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pr
practice: administrative
language: es
---

# Puerto Rico Administrative Agency Appeal (LPAU)

## When to apply

- The user has received a final order/resolution from a Puerto Rico executive-branch agency and wants to challenge it.
- The user is a public employee appealing a personnel action (suspension, dismissal, demotion) to the Comisión Apelativa del Sistema de Administración de Recursos Humanos del Servicio Público (CASARH) — the body created by Ley 8-2017 that assumed the functions of the former Comisión Apelativa del Servicio Público (CASP); practitioners still commonly say "CASP".
- **Out of scope:** the internal agency adjudicative hearing itself (this skill starts at the point of seeking judicial/appellate review of a *final* decision) and agencies with their own specialized review statute that displaces LPAU (confirm whether the enabling act sets a different route or deadline before applying the general LPAU rule).

## Algorithm

1. **Confirm the order is final and reviewable.** LPAU review (Ley Núm. 38-2017, 3 LPRA § 9601 et seq.) generally applies to a final order or resolution of an agency, after exhausting whatever administrative reconsideration the agency's own rules provide. Ask the user to confirm: (a) the order says it is final, and (b) whether a motion for reconsideration was filed and, if so, when it was resolved or deemed denied — this restarts the appeal clock.
2. **Identify the correct forum and deadline.** The default route under LPAU is a recurso de revisión judicial to the **Tribunal de Apelaciones**, filed within the statutory deadline running from notice of the final order (confirm the current deadline in the text of Ley 38-2017 and any amendments — do not assume a specific number of days without checking, since LPAU and several enabling acts have been amended). For CASARH/CASP personnel appeals specifically, confirm whether the case is still within CASARH's own adjudicative process (a hearing before the Commission) or already at the stage of seeking Tribunal de Apelaciones review of CASARH's decision — these are different stages with different rules.
3. **Check for a special enabling-act deadline or forum.** Some agencies (e.g., certain labor, environmental, or licensing boards) have their own statute setting a different deadline or a different reviewing body. Ask the user to confirm the agency's enabling act before relying on the general LPAU timeline.
4. **Identify the standard of review.** LPAU review of agency fact-finding is deferential (substantial evidence in the record as a whole); questions of law are reviewed de novo, though courts give some weight to agency expertise on matters within its specialized competence. State which standard applies to each issue raised.
5. **Draft the recurso** per the output contract, flagging any deadline or forum element the user must independently confirm before filing — a missed LPAU deadline is typically jurisdictional and not curable.

## Output contract

```markdown
[CAPTION DEL TRIBUNAL DE APELACIONES]

RECURSO DE REVISIÓN ADMINISTRATIVA

AL HONORABLE TRIBUNAL:

COMPARECE [parte peticionaria] y respetuosamente EXPONE Y SOLICITA:

I. JURISDICCIÓN Y OPORTUNIDAD DEL RECURSO
[Cita a la LPAU o al estatuto habilitador específico; fecha de notificación de la resolución final; fecha límite; confirmación de que el recurso se presenta a tiempo — o solicitud de prórroga si aplica]

II. RELACIÓN DEL TRÁMITE ADMINISTRATIVO
[Historial procesal ante la agencia]

III. SEÑALAMIENTOS DE ERROR
1. [Error señalado, con estándar de revisión aplicable — evidencia sustancial / cuestión de derecho]
2. [...]

IV. DISCUSIÓN
[Argumentación por cada señalamiento, con cita al récord administrativo y a la ley/reglamento aplicable]

V. SÚPLICA
POR TODO LO CUAL, se solicita respetuosamente que este Honorable Tribunal [revoque / modifique / confirme] la resolución recurrida.

[Lugar y fecha]
[Firma y datos de la representación legal]
```

- Mark the jurisdictional deadline section with `[VERIFICAR PLAZO VIGENTE — LPAU Y ESTATUTO HABILITADOR]` unless the user has confirmed the current deadline — this is the single most consequential fact in the document.
- Close with the mandatory disclaimer from `pr/CLAUDE.md`.
