# Contributing

Thanks for adding a skill. Skills are short Markdown files — no code required.

## How to contribute

1. Fork the repository.
2. Add a folder `pr/{practice}/skills/{slug}/` with a `SKILL.md` inside (use the template below). If the practice area doesn't exist yet under `pr/`, just create it.
3. Open a pull request.

## `SKILL.md` template

```markdown
---
name: my-skill
title: My Skill
description: One-paragraph description of what the skill does and when to use it — this is what an AI agent uses to decide when to invoke it, so be specific about trigger phrases and scope.
author: Your Name
author_url: https://github.com/yourhandle
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pr
practice: litigation
language: es
---

# Skill title

## When to apply
Triggers, example user prompts, what's explicitly out of scope.

## Algorithm
Step-by-step instructions for the agent to follow.

## Output contract
What the answer must contain — format, required citations, the mandatory disclaimer.
```

## Ground rules

- **Never invent a citation.** Every skill must instruct the agent to flag missing/unverified statute sections, case names, docket numbers, or deadlines rather than fabricate them — see [`pr/CLAUDE.md`](pr/CLAUDE.md).
- **State the code/rule version you're relying on.** Puerto Rico has recodified major areas recently (Código Civil in 2020, LPAU in 2017) — a skill that assumes the wrong version is worse than no skill at all.
- **License.** Contributions must be MIT-compatible; by opening a PR you license your contribution under this repository's [LICENSE](LICENSE).
- **This is not legal advice, and neither is anything these skills produce.** Every skill's output must end with the disclaimer in `pr/CLAUDE.md`.
- **No confidential or matter-specific content.** Skills should be general-purpose — don't contribute content tied to a real, identifiable client, judge, or pending matter.

## No exclusivity

You keep all rights to your skill and can publish it elsewhere without notifying anyone.
