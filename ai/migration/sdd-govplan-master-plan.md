# sdd-govplan Master Plan

## Purpose

Definir cómo usar este repo como base para reconstruir `sdd-govplan` como archivo maestro de todo lo trabajado en esta sesión.

## Strategic position

`sdd-govplan` no debería quedarse solo como skill inicial de governance.

Debe evolucionar a:
- repositorio maestro de la capa de gobernanza;
- referencia integral del flujo `brief -> PRD -> spec -> tasks -> review -> migration -> retrospective`;
- fuente desde la cual se decide qué parte se queda local y qué parte se exporta a `agent-core-v3`.

## What should move conceptually into `sdd-govplan`

### Governance layer
- `00-start-here.md`
- `02-decision-gates.md`
- `04-workflow-map.md`
- `05-quick-start-by-scenario.md`

### Core process skills
- `brief-inception`
- `brief-to-prd`
- `prd-to-spec`
- `spec-to-tasks`
- `change-review`
- `rule-migration-plan`
- `improvement-loop`
- `local-retrospective`
- `project-memory-fallback`
- `project-stack-decider`

### Base templates
- `PROJECT-BRIEF-FULL.yaml`
- `PROJECT-BRIEF-LITE.yaml`
- `spec-template.md`
- `tasks-template.md`
- review/migration/retrospective templates

### Boundary docs
- `system-boundaries.md`
- `agent-core-v3-gap-analysis.md`
- `agent-core-v3-export-manifest.md`

## What should NOT be copied blindly into `sdd-govplan`

- local state files (`decisions.md`, `pitfalls.md`, `working-memory.md`)
- repo-specific notes unless recast as official docs
- local runtime/tooling artifacts (`.atl/`, `.pi/`)

## Recommended repo model

### `sdd-govplan`
Master repo for governance and flow.

### `agent-core-v3`
Installable package that distributes the reusable subset.

### project-local `/ai`
Overlay that adapts the model to each repository.

## Publish sequence

1. Consolidate canonical docs and flows in `sdd-govplan`.
2. Export reusable skills/templates to `agent-core-v3`.
3. Keep repo-local overlays lean and contextual.

## Final rule

`sdd-govplan` should become the master narrative.
`agent-core-v3` should become the master distribution.
`/ai` should remain the master local adaptation layer.
