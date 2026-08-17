---
name: pr-ethics-conflict-check
title: Puerto Rico Professional Responsibility Conflict Check
description: Screens a proposed representation or a drafted communication against the Cánones de Ética Profesional del Colegio de Abogados de Puerto Rico — conflicts of interest, confidentiality, and attorney advertising/solicitation rules. Use when the user says "hay conflicto de interés aquí?", "revisa esto conforme a los Cánones de Ética", or asks whether representing a new client, or a piece of communication, raises a professional-responsibility issue under Puerto Rico rules.
author: legal-skills-pr
author_url: https://github.com/ericalopezfebo/legal-skills-pr
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pr
practice: professional-responsibility
language: es
---

# Puerto Rico Professional Responsibility Conflict Check

## When to apply

- Screening a proposed new client or matter against existing/former clients for a conflict of interest under Puerto Rico's Cánones de Ética Profesional (4 LPRA Ap. IX).
- Reviewing a piece of attorney communication or advertising for compliance with the Cánones' advertising/solicitation rules.
- Reviewing whether a disclosure risks breaching the duty of confidentiality.
- **Out of scope:** this is a screening aid, not a substitute for the attorney's own judgment or for consulting the Colegio de Abogados y Abogadas de Puerto Rico's ethics guidance on a specific fact pattern; it does not file anything and does not replace a formal conflicts-check system of record.

## Algorithm

1. **Gather the relevant parties.** For a conflicts check: the prospective client, the matter, and every current and former client of the firm/attorney that might be adverse or related. For a communication/advertising review: the full text and its intended audience.
2. **Apply the core conflict rules**: no representation directly adverse to a current client without informed written consent from both; no representation materially adverse to a former client in the same or a substantially related matter without informed consent; screen for imputed conflicts across an entire firm, not just the individual attorney.
3. **Check confidentiality.** Flag any disclosure of client information — including in a drafted document, email, or public filing — that isn't clearly authorized by the client or required/permitted by an exception (e.g., to prevent a crime, to establish a claim/defense in a fee dispute or malpractice matter).
4. **If reviewing advertising/solicitation**, check for: false or misleading claims (including specific-result guarantees), improper comparisons or superiority claims, and direct in-person or live solicitation of a specific prospective client who hasn't sought the attorney out — historically restricted areas under the Cánones. Flag anything that reads as a guarantee of outcome or an unverifiable claim.
5. **Classify the result**: no conflict/issue identified; potential issue requiring informed consent or further disclosure; clear conflict/violation requiring the attorney decline or withdraw, or revise the communication before it goes out. Never resolve a genuine conflict question for the user — flag it and require attorney sign-off; this skill screens, it does not clear.

## Output contract

```markdown
# Verificación Ética — [asunto/comunicación]

## Resumen
[Conflicto / posible conflicto / sin conflicto identificado — o evaluación de la comunicación]

## Análisis
| Factor | Observación | Regla aplicable (Cánones) |
|---|---|---|
| [p. ej. cliente actual adverso] | [detalle] | [cánon citado en términos generales — verificar número exacto] |

## Confidencialidad
[Cualquier divulgación señalada]

## Recomendación
[Obtener consentimiento informado por escrito / declinar representación / revisar comunicación / sin objeción — requiere confirmación del abogado supervisor en todo caso]
```

- Never state a canon number with certainty unless it's been confirmed against the current text of 4 LPRA Ap. IX — say "cánon aplicable (verificar número vigente)" if unsure.
- This tool flags; it does not clear a conflict or approve a communication. The supervising attorney makes the final call.
- Close with the mandatory disclaimer from `pr/CLAUDE.md`.
