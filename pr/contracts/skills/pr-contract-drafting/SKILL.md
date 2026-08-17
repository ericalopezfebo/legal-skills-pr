---
name: pr-contract-drafting
title: Puerto Rico Contract Drafting
description: Drafts, revises, adapts, and prepares individual contract clauses under Puerto Rico law. Use when the user asks to create a contract, agreement, addendum, amendment, contractual clause, or revised contractual language governed by Puerto Rico law. Distinguishes drafting from review and identifies missing facts instead of inventing material terms.
author: legal-skills-pr
author_url: https://github.com/ericalopezfebo/legal-skills-pr
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pr
practice: contracts
language: es
---

# Puerto Rico Contract Drafting

## When to apply

Use this skill when the user asks to:
- draft a contract or agreement governed by Puerto Rico law;
- draft an addendum, amendment, exhibit, schedule, or contractual clause;
- revise or adapt contractual language;
- convert agreed business terms into a contract;
- prepare a Puerto Rico version of an existing contract.

Do not use this skill merely to evaluate an existing contract for risks. Route that task to `pr-contract-review`.

## Core rule

Do not treat contract drafting as template completion. First identify the transaction, applicable legal regime, essential business terms, formal requirements, and risk-sensitive clauses.

Never invent a material term merely to complete the document. If an essential fact is missing, ask for it or use a conspicuous placeholder such as `[POR DEFINIR]`.

## Source hierarchy

Apply the jurisdiction-wide source rules in `pr/CLAUDE.md`.

For substantive propositions, prefer:
1. Puerto Rico Constitution, when applicable.
2. Código Civil de Puerto Rico de 2020 and applicable special statutes.
3. Valid regulations.
4. Controlling Tribunal Supremo de Puerto Rico precedent.
5. Other persuasive judicial authority when appropriate.
6. Secondary sources only for orientation.

A secondary article is not authority for a proposition when the primary source can be identified.

## Algorithm

### 1. Classify the transaction

Identify:
- type of agreement;
- parties and their legal capacity;
- commercial or personal objective;
- whether the relationship implicates employment, consumer, government, real-estate, intellectual-property, corporate, federal, or other special law;
- governing law and forum, if known.

### 2. Build a missing-information matrix

Separate information into:
- **essential before drafting** — party identity/capacity, object or services, consideration/payment where applicable, duration when material, and any fact without which the requested agreement cannot be meaningfully drafted;
- **important but placeholder-compatible** — addresses, notice emails, dates, exhibit numbers, account details;
- **optional/business preference** — renewal mechanics, cure periods, insurance limits, dispute-resolution mechanics, etc.

Ask only for genuinely necessary missing information. Do not interrogate the user about facts that can safely remain as placeholders.

### 3. Check validity and form

Before drafting, evaluate:
- consent;
- object;
- cause;
- capacity/authority;
- legality, morality, and public order;
- whether a writing, private instrument, public instrument, notarization, registration, approval, or other formality is legally required;
- whether a special statute displaces or supplements the Código Civil.

Do not state that every Puerto Rico contract must be written. Determine whether the particular transaction requires a specific form.

### 4. Build the clause map

Classify proposed clauses as:
- essential;
- legally mandatory;
- transaction-specific;
- recommended risk allocation;
- optional.

Typical subjects include:
- identification and representations of the parties;
- definitions;
- object/scope;
- consideration and payment;
- term and renewal;
- obligations of each party;
- deliverables/acceptance;
- confidentiality;
- intellectual property;
- representations and warranties;
- compliance with law;
- insurance;
- indemnification;
- limitation of liability;
- force majeure;
- assignment;
- termination and cure;
- remedies;
- notices;
- governing law/forum;
- integration, amendment, severability, waiver and counterparts.

Include only clauses justified by the transaction.

### 5. Run heightened review on risk-sensitive clauses

Do not insert these mechanically:
- non-compete/non-solicitation;
- option clauses;
- assignment/cession;
- adhesion or non-negotiated terms;
- penalty/liquidated-damages provisions;
- limitation/exculpation of liability;
- indemnification;
- arbitration/forum-selection;
- automatic renewal;
- unilateral modification;
- government-contract mandatory clauses.

For each, determine current Puerto Rico law and any applicable federal overlay before finalizing.

### 6. Draft for legal clarity

Use:
- clear headings;
- defined terms only when useful;
- short, direct provisions;
- consistent terminology;
- active voice where natural;
- precise obligations (`shall/deberá` only where an obligation is intended);
- one concept per clause when practical;
- consistent dates, amounts, cross-references and party names.

Avoid archaic legalese, decorative recitals, unnecessary duplication, and language that obscures who must do what and when.

### 7. Consistency audit

Before delivery verify:
- party names and defined terms are consistent;
- dates and durations do not conflict;
- payment terms reconcile;
- termination provisions match the term/renewal provisions;
- remedies do not contradict liability limitations;
- exhibits and cross-references exist;
- assignment, successor and third-party language is coherent;
- signature blocks match the parties and representative capacities;
- no bracketed placeholder is hidden or ambiguous.

### 8. Authority and hallucination check

For every legal proposition that materially affects the drafting:
- verify the source exists;
- verify it supports the proposition;
- distinguish current law from historical law;
- do not fabricate statutes, case names, quotations, docket numbers or citations;
- mark uncertain propositions `[VERIFICAR]`.

### 9. Deliver

If the user requested a finished agreement, provide the agreement first. When useful, follow it with a concise drafting note identifying:
- unresolved placeholders;
- clauses requiring heightened attorney review;
- formalities still required;
- assumptions made.

## Modes

### `draft`
Create a new agreement from facts/business terms.

### `revise`
Rewrite specified provisions while preserving the deal structure unless instructed otherwise.

### `adapt`
Adapt an existing agreement to Puerto Rico law. Do not assume a mainland-U.S. or foreign template is valid in Puerto Rico.

### `clause`
Draft one or more clauses and explain any material Puerto Rico-specific constraint only when useful.

## Relationship to other skills

- Use `pr-contract-review` to audit an existing agreement.
- Use `pr-legal-research` when the drafting turns on an unsettled or specialized legal issue.
- Use `pr-legal-citation` when citations are requested or included.
- A specialized practice-area skill should control the substantive law when it is more specific than this general drafting skill.

## Reference routing

Read on demand:
- `references/contract-law-pr.md` — validity, form, source hierarchy and drafting safeguards.
- `references/drafting-style.md` — Puerto Rico legal-writing and contract-drafting style.
- `references/risk-sensitive-clauses.md` — clause categories requiring current-law verification.
- `references/sources.md` — research leads and secondary-source provenance.

## Output contract

A completed contract must:
1. reflect only known terms or conspicuous placeholders;
2. identify the parties and capacities consistently;
3. use coherent sections and numbering;
4. avoid unsupported legal conclusions;
5. flag unresolved legal/formality issues;
6. comply with the disclaimer and verification rules in `pr/CLAUDE.md`.

Do not present a generated contract as ready for signature or filing when material facts, formalities, or current-law questions remain unresolved.
