---
name: pr-motion-drafting
title: Puerto Rico Motion Drafting
description: Drafts and revises motions, oppositions, replies, and procedural requests for Puerto Rico court practice. Use for a generic motion-drafting task when no more specific skill controls. Identifies the requested relief, procedural posture, governing rule, factual support, authority, and filing structure without inventing record facts or citations.
author: legal-skills-pr
author_url: https://github.com/ericalopezfebo/legal-skills-pr
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pr
practice: litigation
language: es
---

# Puerto Rico Motion Drafting

## When to apply

Use when the user asks to draft or revise:
- a motion;
- an opposition;
- a reply;
- a procedural request;
- a filing seeking an order from a Puerto Rico court;

and no more specific drafting skill fully controls the task.

A specialized skill such as `pr-summary-judgment-motion` controls over this general skill on its specialized requirements.

## Core rule

A motion is not a generic essay. It is a request for judicial relief grounded in a procedural vehicle, a record, and applicable authority.

Never invent:
- procedural history;
- filing dates;
- docket entries;
- exhibits;
- testimony;
- quotations;
- statutes, rules, cases, citations, or holdings.

Use `[POR COMPLETAR]` or `[VERIFICAR]` when necessary.

## Algorithm

### 1. Identify posture
Determine:
- court and case type;
- moving/responding party;
- stage of proceedings;
- exact relief requested;
- whether the filing is a motion, opposition, reply, reconsideration, informative motion, extension, withdrawal, or another procedural vehicle.

### 2. Identify governing authority
Locate the procedural rule, statute, regulation, order, or controlling precedent authorizing or constraining the requested relief.

If the rule or deadline is uncertain, research before drafting.

### 3. Determine required facts and record support
Separate:
- record-supported facts supplied by the user;
- procedural facts that require docket verification;
- legal propositions;
- missing facts.

Do not convert allegations into established facts unless the posture permits it.

### 4. Choose structure
Unless a specialized rule requires another format, use only the sections needed:
1. caption;
2. title identifying the relief;
3. appearance/opening;
4. relevant procedural background;
5. relevant facts;
6. applicable law/standard;
7. argument/application;
8. requested relief;
9. signature/certificate sections if requested and factually supported.

### 5. Draft the argument
Use a rule → application → conclusion structure.
- Lead with the requested legal result.
- State the governing standard accurately.
- Apply the rule to the supplied record.
- Address the strongest foreseeable counterargument when appropriate.
- Avoid adjectives and rhetoric that do not advance the legal analysis.

### 6. Citation discipline
Route citation questions to `pr-legal-citation`.
For every authority:
- verify existence;
- verify current validity;
- verify that it supports the proposition;
- distinguish binding from persuasive authority;
- do not fabricate pinpoint cites.

### 7. Drafting quality
Use:
- clear headings;
- short paragraphs;
- professional and respectful tone;
- active voice where natural;
- precise descriptions of requested relief;
- consistent party labels;
- correct cross-references.

### 8. Filing-readiness audit
Before delivery check:
- requested relief is explicit;
- procedural vehicle matches the relief;
- cited authority exists;
- deadlines or jurisdictional assertions are verified;
- factual assertions have a supplied or identified source;
- exhibits mentioned actually exist or are marked as placeholders;
- specialized rule requirements have been satisfied;
- no confidential template facts leaked into the new matter.

## Template/example rule

Prior motions may be used to learn formatting, section order, tone, and recurring drafting conventions.

Never:
- copy names, case numbers, addresses, facts, medical information, financial information, or other matter-specific data from a template;
- treat a prior motion as legal authority;
- assume an old template reflects current law;
- silently transplant arguments from a different procedural posture.

## Relationship to specialized skills

Use this skill as the drafting engine. A specialized substantive/procedural skill supplies the controlling legal workflow.

Examples:
- summary judgment → `pr-summary-judgment-motion` + this drafting framework;
- legal research → `pr-legal-research`;
- citation checking → `pr-legal-citation`.

## Output contract

The motion must:
1. identify the requested relief;
2. distinguish facts from legal argument;
3. rely only on supplied/verified record facts;
4. contain no invented authority;
5. flag missing filing-specific information;
6. follow any specialized procedural requirements;
7. comply with `pr/CLAUDE.md`.

If the user asks for a finished filing, provide the filing rather than a generic explanation, while preserving conspicuous placeholders for missing matter-specific information.
