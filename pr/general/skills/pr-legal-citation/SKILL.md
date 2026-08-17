---
name: pr-legal-citation
title: Puerto Rico Legal Citation Checker
description: Checks and formats citations to Puerto Rico primary law — statutes codified in LPRA, Tribunal Supremo opinions (DPR reporter), Tribunal de Apelaciones docket numbers, and Reglamentos — into the conventions Puerto Rico practitioners and courts expect. Use when the user says "revisa esta cita", "formatea esta cita legal", "cita conforme a LPRA", "cómo se cita esta sentencia del Tribunal Supremo", or pastes a Puerto Rico legal citation to check or fix.
author: legal-skills-pr
author_url: https://github.com/ericalopezfebo/legal-skills-pr
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pr
practice: general
language: es
---

# Puerto Rico Legal Citation Checker

## When to apply

- The user pastes a citation to a Puerto Rico statute, Tribunal Supremo opinion, Tribunal de Apelaciones resolution, or agency regulation and asks whether it's correctly formatted.
- The user gives a case name, statute name, or docket number and asks for the citation in the correct form.
- The user is drafting a motion, brief, or memo and needs citations checked before filing.
- **Out of scope:** verifying that a citation is still good law (Shepardizing/checking subsequent history) — this skill checks *form*, not *validity*. Say so and point the user to LexJuris, Microjuris, or Westlaw PR for validity checks.

## Algorithm

1. Identify what kind of authority is being cited: statute (LPRA), Tribunal Supremo opinion, Tribunal de Apelaciones resolution/opinion, agency regulation, or federal authority applicable in Puerto Rico.
2. Apply the matching format below. If a required element is missing (volume, page, year, LPRA section, docket number), **do not invent it** — list exactly what's missing and ask the user to supply it or verify it against LexJuris (https://www.lexjuris.com) or the Rama Judicial site (https://www.ramajudicial.pr).
3. Flag common errors:
   - Citing the pre-2020 Civil Code (old 31 LPRA sections) as if it still governs — the 2020 Código Civil (Ley 55-2020) renumbered nearly everything.
   - Citing a Tribunal de Apelaciones resolution as binding precedent — it is persuasive/intermediate authority only; Tribunal Supremo opinions bind.
   - Mixing English and Spanish case-name conventions inconsistently within one document.
   - Missing the "según enmendada" qualifier on a frequently amended statute (Reglas de Procedimiento Civil, LPAU, etc.) when precision matters.
4. Return the corrected citation(s) plus a short note on any element the user must independently confirm.

### Format reference

| Authority | Format | Example |
|---|---|---|
| Statute (LPRA codification) | Art. [núm.], [nombre de la ley], Ley Núm. [núm.]-[año], [título] LPRA § [sección] | Art. 1064, Código Civil de PR, Ley Núm. 55-2020, 31 LPRA § 7401 |
| Session law only (no LPRA cite yet) | Ley Núm. [núm.] de [día] de [mes] de [año] | Ley Núm. 4-2017 |
| Tribunal Supremo opinion | *[Parte] v. [Parte]*, [volumen] DPR [página] ([año]) | *Meléndez González et al. v. M. Cuebas, Inc.*, 193 DPR 100 (2015) |
| Tribunal de Apelaciones | *[Parte] v. [Parte]*, [docket KLAN/KLRA/KLCE-año-número], [fecha de la sentencia/resolución] | *[Parte] v. [Parte]*, KLAN202400123, sentencia de [fecha] |
| Reglas de Procedimiento Civil / Evidencia | Regla [núm.], Reglas de Procedimiento Civil de 2009, según enmendadas, 32 LPRA Ap. V | Regla 36, Reglas de Procedimiento Civil de 2009, 32 LPRA Ap. V |
| Agency regulation | Reglamento Núm. [núm.], [agencia], [título], [fecha de vigencia] | Reglamento Núm. 9223, Departamento del Trabajo |
| Federal authority applied in PR | Standard Bluebook federal form; note when persuasive vs. binding (First Circuit binds; other circuits are persuasive) | *[Case]*, [vol.] F.3d [page] (1st Cir. [year]) |

## Output contract

- Return the corrected/formatted citation(s) in a code block or table, not prose.
- Explicitly list any element you could not verify and need the user to confirm.
- Include the mandatory disclaimer from `pr/CLAUDE.md`: this checks form only, confirm currency and validity independently.
