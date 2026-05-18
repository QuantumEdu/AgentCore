# AGENTS.md

## Purpose

This repository uses **gentle-ai as the orchestrator** and `/ai` as the portable guidance layer.

## Read Order

1. `/ai/README.md`
2. `/ai/governance/00-start-here.md`
3. `/ai/governance/04-workflow-map.md`
4. `/ai/governance/05-quick-start-by-scenario.md`
5. `/ai/context/system-layers.md`
6. Only then consult the historical backup only if historical reference is genuinely needed.

## Operating Model

- **gentle-ai**: orchestration, memory, SDD, delegation.
- **sdd-govplan**: master source of the governance layer being consolidated from this work.
- **agent-core-v3**: global/installable distribution target for reusable skills and assets.
- **/ai/governance**: intake, decision gates, project brief guidance.
- **/ai/README.md**: onboarding and system overview.
- **/ai/skills**: portable reusable behaviors.
- **/ai/agents**: optional specialized agents for discovery/inception.
- **historical backup**: material anterior rescatado fuera del flujo activo.

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
