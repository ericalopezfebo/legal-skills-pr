---
name: pr-civil-deadlines
title: Puerto Rico Civil Litigation Deadlines
.description: Calculates and audits Puerto Rico civil litigation deadlines from verified triggering events, current rules, statutes, court orders, and applicable computation-of-time provisions, while flagging jurisdictional or non-extendable terms.
author: legal-skills-pr
author_url: https://github.com/ericalopezfebo/legal-skills-pr
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pr
practice: litigation
language: es
---

# Puerto Rico Civil Litigation Deadlines

## Purpose
Calculate procedural dates only from verified sources and facts. This skill is a deadline-audit engine, not a memory-based calendar.

## Required inputs
- forum and case type;
- triggering event;
- exact triggering date and, when relevant, date/method of service or notice;
- governing rule/statute/order if known;
- any prior extensions, stays, amended orders, or special procedures;
- target filing or act.

## Workflow
1. Confirm that Puerto Rico Commonwealth civil procedure governs. If the forum is federal, appellate, administrative, criminal, bankruptcy, or another special forum, stop or route to the appropriate rules.
2. Identify the legal source creating the term: Rules of Civil Procedure, statute, special law, court order, scheduling order, or another controlling source.
3. Verify the current text and effective version of that source before calculating.
4. Identify the triggering event precisely. Distinguish filing, entry, notice, service, personal service, electronic notice, mailing, hearing date, and judgment date.
5. Apply the current Puerto Rico computation-of-time rule, including weekends, legal holidays, and any source-specific treatment. Do not add days for method of service unless current law actually requires it.
6. Check for amendments, extensions, stays, court orders, special proceedings, and jurisdictional/non-extendable terms.
7. Produce the calculation transparently: source; trigger; trigger date; interval; computation rule; adjustments; resulting date.
8. State confidence and unresolved assumptions. If any fact or legal source is missing, give a conditional calculation rather than pretending certainty.

## High-risk deadlines
Treat post-judgment, reconsideration, appeal/review, certiorari, removal/remand, jurisdictional, statutory, and special-proceeding terms as high risk. Require current-law verification before the user relies on the date.

## Guardrails
- Never calculate a deadline solely from model memory.
- Never assume that a court may extend a term.
- Never assume that a timely motion tolls or interrupts another deadline without verifying the legal effect and compliance requirements.
- Never infer a service date from a filing date.
- If the record contains conflicting dates, show the alternatives and explain what fact controls.
- Apply `pr/CLAUDE.md` and cite the verified rule/statute/order used.

## Output contract
```markdown
# Cómputo de término — [acto]

- Foro: [foro]
- Fuente del término: [regla/estatuto/orden verificada]
- Evento que activa el término: [evento]
- Fecha activadora: [fecha]
- Término: [duración]
- Regla de cómputo aplicada: [fuente]
- Ajustes: [fines de semana/feriados/orden/etc.]
- Fecha resultante: **[fecha]**
- Nivel de certeza: [alto/condicional/requiere verificación]

## Advertencias
[asunciones, posible término jurisdiccional, extensión, efecto de otra moción, etc.]
```

Close with the mandatory disclaimer from `pr/CLAUDE.md`.
