# Agent Core v3 Export Manifest

## Purpose

Clasificar qué piezas de este repo deberían migrarse al core global `agent-core-v3` y cuáles deben quedarse locales.

## Export to `agent-core-v3`

### Global skills candidates
- `brief-inception`
- `brief-to-prd`
- `prd-to-spec`
- `spec-to-tasks`
- `change-review`
- `rule-migration-plan` / `rule-migration`
- `improvement-loop`
- `project-memory-fallback` / `memory-fallback`
- `local-retrospective`
- `project-stack-decider`
- `add-endpoint`
- `coding-conventions`
- `prompt-improver`
- `geek-tech-tone` *(optional utility tier)*

### Global templates candidates
- `PROJECT-BRIEF-FULL.yaml`
- `PROJECT-BRIEF-LITE.yaml`
- `spec-template.md`
- `tasks-template.md`
- `change-review-template.md`
- `retrospective-template.md`
- `rule-migration-template.md`
- `decision-adr-template.md`
- `roadmap-template.md`

### Global reference assets candidates
- `skills/patterns/*`

## Keep local in `/ai`

### Project overlay docs
- `ai/README.md`
- `governance/00-start-here.md`
- `governance/04-workflow-map.md`
- `governance/05-quick-start-by-scenario.md`
- `context/system-layers.md`
- `context/system-boundaries.md`

### Local state / memory
- `context/decisions.md`
- `context/pitfalls.md`
- `context/working-memory.md`

### Local wrappers
- `agents/project-inception-architect.md`
- `agents/change-reviewer.md`
- `agents/migration-guardian.md`
- `agents/endpoint-designer.md`

## Publish rule

`agent-core-v3` should export the reusable base.

This repo should keep the local operating overlay.
