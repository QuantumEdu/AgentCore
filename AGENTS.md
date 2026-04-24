# AGENTS.md

## Purpose

This repository uses **gentle-ai as the orchestrator** and `/ai` as the portable guidance layer.

## Read Order

1. `/ai/governance/00-start-here.md`
2. `/ai/governance/02-decision-gates.md`
3. `/ai/context/system-layers.md`
4. Only then consult `/legacy` if historical reference is genuinely needed.

## Operating Model

- **gentle-ai**: orchestration, memory, SDD, delegation.
- **/ai/governance**: intake, decision gates, project brief guidance.
- **/ai/skills**: portable reusable behaviors.
- **/ai/agents**: optional specialized agents for discovery/inception.
- **/legacy**: archivo histórico mínimo rescatado desde AgentCore.

## Non-Negotiables

- Do not modify gentle-ai core behavior from this repository.
- Prefer `/ai/*` over reviving legacy assets.
- Treat the project brief as the entry gate before architecture or implementation.
- Ask up to 7 critical questions first when the brief is incomplete.
- When unsure whether something is still used, archive to `legacy/` instead of deleting.

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
