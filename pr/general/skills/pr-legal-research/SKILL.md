---
name: pr-legal-research
title: Puerto Rico Legal Research Workflow
description: Structures legal research on a Puerto Rico question — routes to the right primary source (LPRA statute, Tribunal Supremo/Tribunal de Apelaciones case law, agency regulation, or federal authority), tracks what was found vs. still needs verification, and produces a research memo with citations. Use when the user says "investiga esto en la ley de Puerto Rico", "busca jurisprudencia sobre...", "qué dice el estatuto sobre...", or asks a substantive question about PR law that requires checking sources rather than just drafting.
author: legal-skills-pr
author_url: https://github.com/ericalopezfebo/legal-skills-pr
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pr
practice: general
language: es
---

# Puerto Rico Legal Research Workflow

## When to apply

- The user asks a substantive question about Puerto Rico law and wants sourced authority, not just a drafted document.
- The user needs to know whether a statute, rule, or agency regulation applies to a fact pattern.
- The user wants a research memo they can attach to a file or hand to a supervising attorney.
- **Out of scope:** giving a final legal opinion or advice — this produces a sourced research memo for attorney review, per the mandatory disclaimer in `pr/CLAUDE.md`.

## Algorithm

1. **Frame the question.** Restate the legal issue as a precise question (parties, facts, forum, timeframe). If the forum matters (Commonwealth court vs. federal court vs. an administrative agency), identify it — it changes which rules and which citation conventions apply.
2. **Route to the right source type**, in this order of priority per `pr/CLAUDE.md`:
   - Constitutional text (federal or ELA) if a constitutional question is presented.
   - Governing statute, located by LPRA title/section or by popular name — search LexJuris (https://www.lexjuris.com) or the Departamento de Estado's registry for the current, in-force text.
   - Applicable procedural rule (Reglas de Procedimiento Civil, Reglas de Evidencia, or an agency's own procedural regulation).
   - On-point Tribunal Supremo jurisprudence interpreting the statute/rule.
   - Tribunal de Apelaciones decisions — note these are persuasive, not binding, and many are unpublished.
   - Agency regulations and adjudications if the matter is administrative.
   - Federal authority only if federal law governs or as persuasive analogy where PR law is silent — say explicitly when you're reasoning by analogy rather than citing controlling PR authority.
3. **Track source status** for every authority found: confirmed current / needs verification / could not locate. Never present something as settled law without saying which bucket it's in.
4. **Check for recent recodification.** Several core PR codes were recently replaced (Código Civil in 2020 via Ley 55-2020; LPAU in 2017 via Ley 38-2017). If the issue touches one of these areas, explicitly confirm whether the source predates or postdates the recodification.
5. **Draft the research memo** per the output contract below.

## Output contract

```markdown
# Memo de Investigación — [tema]

## Pregunta presentada
[Pregunta jurídica precisa]

## Respuesta breve
[1–3 oraciones, con nivel de certeza indicado]

## Autoridad aplicable
| Fuente | Cita | Estado |
|---|---|---|
| [estatuto/regla/caso] | [cita formateada] | Confirmado vigente / Requiere verificación / No localizado |

## Análisis
[Aplicación de la autoridad a los hechos, con cita a cada proposición]

## Advertencias
- [Cualquier vacío, autoridad contradictoria, o área donde la ley cambió recientemente]

## Próximos pasos recomendados
[P. ej.: verificar en LexJuris/Microjuris, confirmar con la secretaría del tribunal, consultar al supervisor]
```

Always close with the mandatory disclaimer from `pr/CLAUDE.md`.
