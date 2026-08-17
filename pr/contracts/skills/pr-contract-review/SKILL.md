---
name: pr-contract-review
title: Puerto Rico Contract Review (Código Civil 2020)
description: Reviews or drafts a contract against the requirements and default rules of Puerto Rico's Código Civil de 2020 (Ley 55-2020) — elements of a valid contract, formalities, common clause pitfalls, and language/forum considerations specific to Puerto Rico. Use when the user says "revisa este contrato bajo la ley de Puerto Rico", "redacta un contrato conforme al Código Civil de PR", or shares a contract governed by Puerto Rico law for review.
author: legal-skills-pr
author_url: https://github.com/ericalopezfebo/legal-skills-pr
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pr
practice: contracts
language: es
---

# Puerto Rico Contract Review (Código Civil 2020)

## When to apply

- Reviewing a contract that states it is governed by Puerto Rico law, or where the parties/performance are in Puerto Rico and no other governing law is specified.
- Drafting a new contract intended to be enforced in Puerto Rico.
- **Out of scope:** contracts governed by another jurisdiction's law even if one party is in Puerto Rico (confirm the choice-of-law clause first); specialized contract types with their own statutory regime (e.g., insurance under the Código de Seguros, consumer contracts under specific consumer-protection statutes, collective bargaining agreements) — flag that a specialized statute may add requirements beyond the general Civil Code rules.

## Algorithm

1. **Confirm the governing code.** The Código Civil de Puerto Rico was replaced in full by **Ley Núm. 55-2020**, effective November 28, 2020. Contracts executed before that date may still be governed by the 1930 Civil Code's transitional rules for some purposes — ask the user for the execution date if it's not obvious, and flag which code version applies before citing specific articles.
2. **Check the elements of a valid contract**: consentimiento (consent free of error, dolo, violencia, or intimidación), objeto cierto (definite object/subject matter), and causa (lawful cause/consideration). Flag any clause that suggests a defect in one of these — e.g., unconscionable terms, illusory consideration, or an object that's illegal or outside commerce.
3. **Check formalities.** Puerto Rico generally does not require a contract to be in writing except where the Civil Code or a specific statute requires it (e.g., real property transfers, certain long-term leases, contracts required to be in a public deed for recordation). Flag if the contract type in front of you is one that requires a particular form to be enforceable or recordable.
4. **Review standard clauses against PR-specific defaults**, since the Civil Code supplies default rules the parties may or may not have displaced:
   - **Governing law / forum selection** — confirm it's explicit; if silent, PR law defaults and PR courts apply absent a valid forum-selection clause.
   - **Language** — confirm which language version controls if the contract exists in both Spanish and English; Commonwealth courts operate in Spanish.
   - **Interest/late payment** — check against any applicable usury limits before validating an interest clause.
   - **Termination and cure periods** — the Civil Code's default remedies for breach (resolución, cumplimiento forzoso, daños) apply unless the contract displaces them; confirm the contract states its own remedy scheme if the parties intend something different from the statutory default.
   - **Indemnification, limitation of liability, and waiver clauses** — flag anything that purports to waive liability for dolo (fraud) or gross negligence, since such waivers are generally unenforceable under PR public policy.
5. **Flag anything requiring specialized statutory review** outside the general Civil Code — labor terms (pair with a PR employment-law review), consumer protection, real estate recordation (Registro de la Propiedad), or regulated industries.

## Output contract

```markdown
# Revisión de Contrato — [nombre/tipo de contrato]

## Ley aplicable confirmada
[Código Civil 2020 (Ley 55-2020) / versión anterior — y por qué]

## Elementos del contrato
| Elemento | Evaluación | Observación |
|---|---|---|
| Consentimiento | OK / Señalado | [detalle] |
| Objeto | OK / Señalado | [detalle] |
| Causa | OK / Señalado | [detalle] |
| Formalidades | OK / Señalado | [detalle] |

## Cláusulas señaladas
1. [Cláusula] — [riesgo/observación] — [sugerencia de redacción, si aplica]

## Vacíos o ambigüedades
[Lo que el contrato no cubre y que el Código Civil suplirá por defecto — indicar cuál sería la regla supletoria]

## Recomendaciones
[Lista priorizada]
```

Close with the mandatory disclaimer from `pr/CLAUDE.md`.
