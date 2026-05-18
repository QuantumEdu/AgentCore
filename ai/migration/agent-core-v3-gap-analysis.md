# Agent Core v3 Gap Analysis

## Goal

Cerrar la parte inconclusa entre el sistema local `/ai` y el paquete global `agent-core-v3`.

## Reading of the evolution

1. **AgentCore clásico** mezclaba template, reglas, ejemplo, memoria, flujos y runtime implícito.
2. **sdd-govplan** extrajo la parte inicial de governance.
3. **agent-core-v3** resolvió la distribución global de un subconjunto de skills.
4. **/ai** en este repo reconstruyó el flujo local completo que había quedado afuera.

## What v3 already solves

- instalación por npm
- distribución multi-tool
- skills globales de governance, review, migration, improvement y fallback

## What remained incomplete and was recovered locally

### Missing flow bridge
- `brief-inception`
- `brief-to-prd`
- `prd-to-spec`
- `spec-to-tasks`

### Missing project guidance
- `ai/README.md`
- `04-workflow-map.md`
- `05-quick-start-by-scenario.md`

### Missing project-operational assets
- `PROJECT-BRIEF-FULL.yaml`
- `PROJECT-BRIEF-LITE.yaml`
- `spec-template.md`
- `tasks-template.md`
- review / retrospective / migration templates

### Missing local wrappers and role helpers
- `project-inception-architect`
- `change-reviewer`
- `migration-guardian`
- `endpoint-designer`

## Strategic conclusion

`agent-core-v3` should NOT be treated as a full replacement of `/ai`.

It should become:
- the **global reusable core**

And `/ai` should remain:
- the **local repo overlay**
