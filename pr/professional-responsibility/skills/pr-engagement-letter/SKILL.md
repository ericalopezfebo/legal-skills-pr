---
name: pr-engagement-letter
title: Puerto Rico Engagement Letter / Hoja de Encargo
description: Drafts a client engagement letter (hoja de encargo / contrato de servicios legales) for a Puerto Rico legal practice, covering scope of representation, fees, termination, confidentiality, and the disclosures Puerto Rico practice expects. Use when the user says "prepara una hoja de encargo", "necesito un contrato de servicios legales", "carta de compromiso con el cliente", or is onboarding a new client/matter.
author: legal-skills-pr
author_url: https://github.com/ericalopezfebo/legal-skills-pr
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pr
practice: professional-responsibility
language: es
---

# Puerto Rico Engagement Letter / Hoja de Encargo

## When to apply

- Onboarding a new client or a new matter for an existing client and formalizing the scope and terms of representation.
- The user wants a fee agreement, engagement letter, or "hoja de encargo" for Puerto Rico practice.
- **Out of scope:** contingency-fee agreements with special statutory or Canon requirements the user hasn't confirmed (flag these for attorney-specific review rather than assuming a standard percentage), and matters where the client is a government entity or otherwise subject to a special contracting regime (flag and route to specialized review).

## Core rule

An engagement letter is a contract with a fiduciary on one side. It must be unambiguous about scope (what the attorney is and is not engaged to do), fees, and how the relationship ends — and it must not overstate the likelihood of a favorable outcome. Never fill in a fee, scope, or contingency term the client and attorney haven't actually agreed on; use a conspicuous placeholder instead.

## Algorithm

1. **Identify the parties and their capacity.** Individual, entity, or multiple clients (if multiple clients, flag the joint-representation conflict considerations under the Cánones — route to `pr-ethics-conflict-check` before finalizing).
2. **Define the scope of the encargo precisely.** State what matter(s) are covered, and just as importantly, what is excluded (e.g., "no incluye representación en apelación," "no incluye asuntos fiscales/contributivos"). An engagement letter that doesn't bound scope invites a claim that everything downstream was included.
3. **Set the fee structure**, only as actually agreed:
   - Fixed fee / presupuesto cerrado.
   - Hourly rate, with billing increments and invoicing frequency.
   - Contingency, with the percentage, what it applies to (gross recovery vs. net of costs), and how costs are handled — flag for attorney review since contingency terms carry their own Canon-level scrutiny.
   - Retainer/anticipo and how it's drawn down or refunded.
   Never invent a rate or percentage; use `[POR DEFINIR]` if not yet agreed.
4. **State costs and expenses** separately from fees (filing fees, expert costs, notary/registro costs) and who advances them.
5. **Include the disclosures a Puerto Rico engagement letter should carry**:
   - No guarantee of outcome — representation is a good-faith professional effort, not a promised result.
   - Possibility of an adverse costs award, where applicable to the matter type.
   - Client's right to be informed of case status and to terminate the representation.
   - Attorney's right to withdraw under the Cánones (e.g., nonpayment, conflict, loss of confidence) subject to any court-approval requirement for pending litigation.
   - Confidentiality of client information under the Cánones de Ética Profesional.
   - Whether the attorney may delegate work to associates/paralegals without additional charge beyond the agreed fee.
   - Applicable law/forum for the engagement itself, and the language of the engagement (confirm which language version controls if bilingual).
6. **Termination mechanics.** How either party ends the engagement, what happens to the file and any unearned retainer, and the client's right to obtain their file.
7. **Signatures.** Space for attorney and client, with date.

## Output contract

```markdown
HOJA DE ENCARGO PROFESIONAL / CONTRATO DE SERVICIOS LEGALES

1. PARTES
   Abogado/a: [nombre, núm. de colegiado(a), dirección]
   Cliente: [nombre/entidad, dirección, contacto]

2. OBJETO DEL ENCARGO
   [Descripción del asunto cubierto]
   Expresamente NO incluye: [exclusiones]

3. HONORARIOS
   [Estructura acordada — o [POR DEFINIR]]

4. GASTOS Y COSTAS
   [Quién los adelanta y cómo se reembolsan]

5. ADVERTENCIAS
   - No se garantiza un resultado favorable.
   - [Posibilidad de condena en costas, si aplica al tipo de asunto]
   - El/la cliente puede solicitar información sobre el estado del asunto en cualquier momento.

6. CONFIDENCIALIDAD
   [Conforme a los Cánones de Ética Profesional, 4 LPRA Ap. IX]

7. TERMINACIÓN
   [Mecánica de terminación por cualquiera de las partes; manejo del expediente y de anticipos no devengados]

8. LEY Y FORO APLICABLE / IDIOMA
   [Confirmar]

FIRMAS
[Abogado/a] ______________  Fecha: ______
[Cliente]   ______________  Fecha: ______
```

- Every unresolved fee or scope term must be marked `[POR DEFINIR]`, never filled in with an assumed number.
- If the matter involves multiple clients or a possible joint-representation conflict, flag it and recommend running `pr-ethics-conflict-check` before the letter is finalized.
- Close with the mandatory disclaimer from `pr/CLAUDE.md`.
