# AGENTS.md

## Purpose

This repository packages `/ai` plus `AGENTS.md` as a portable overlay for projects that use **gentle-ai as the orchestrator**.

## Read Order

1. `/ai/README.md`
2. `/ai/governance/00-start-here.md`
3. `/ai/governance/04-workflow-map.md`
4. `/ai/governance/05-quick-start-by-scenario.md`
5. `/ai/context/system-layers.md`
6. Only then consult the historical backup only if historical reference is genuinely needed.

## Operating Model

- **gentle-ai**: orchestration, memory, SDD, delegation.
- **this package**: installable overlay that copies `/ai` and `AGENTS.md` into a target project.
- **sdd-govplan**: historical/master governance lineage referenced by some migration docs.
- **agent-core-v3**: historical distribution target still mentioned in transition notes.
- **/ai/governance**: intake, decision gates, project brief guidance.
- **/ai/README.md**: onboarding and system overview.
- **/ai/skills**: portable reusable behaviors.
- **/ai/agents**: optional specialized agents for discovery/inception.
- **historical backup**: material anterior rescatado fuera del flujo activo.

## Naming Convention

All skills in this overlay use the prefix `sdd-govp:` to keep them organized under a common namespace (inspired by `ospx:` from OpenSpec).

### Examples

- `sdd-govp:brief-inception` — brief → PRD flow
- `sdd-govp:change-review` — review gate
- `sdd-govp:rule-migration-plan` — safe rule migration
- `sdd-govp:workflow-builder` — custom workflows for any project type

Use the prefix when invoking skills (e.g., `sdd-govp:brief-inception`) or via the `/command` alias (e.g., `/brief-inception`).

## Non-Negotiables

- Do not modify gentle-ai core behavior from this repository.
- Prefer `/ai/*` over reviving legacy assets.
- Treat the project brief as the entry gate before architecture or implementation.
- Use `PROJECT-BRIEF-LITE` for small/exploratory work and `PROJECT-BRIEF-FULL` for serious, sensitive, or complex work.
- Ask up to 7 critical questions first when the brief is incomplete.
- When unsure whether something is still used, archive it outside the active flow instead of deleting.

## Routing Rule

- If you need the structural view by change type, use `/ai/governance/04-workflow-map.md`.
- If you need the practical “what do I use now?” view, use `/ai/governance/05-quick-start-by-scenario.md`.

## Prompting Standard

When the user asks to improve a prompt, prefer the `/ai/skills/prompt-improver` structure:

1. Goal
2. Scope / assumptions
3. Approach / phases
4. Constraints
5. Output format
6. Quality checks

## Style Standard

If requested, apply the response style from `/ai/skills/geek-tech-tone/SKILL.md`:

- geek but professional
- technical but clear
- proactive
- structured
- with lateral-thinking prompts when useful
