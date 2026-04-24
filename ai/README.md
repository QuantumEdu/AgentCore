# /ai

Capas portables de guía, memoria fallback, skills, agentes simples y templates para trabajar con `gentle-ai` sin modificar su núcleo.

## Start here

1. `governance/00-start-here.md`
2. `governance/04-workflow-map.md`
3. `governance/05-quick-start-by-scenario.md`

## Directory map

- `governance/` — puertas de paso, mapas de flujo y guía de uso.
- `context/` — contexto estable y memoria fallback local.
- `skills/` — capacidades operativas reutilizables.
- `skills/patterns/` — referencia de patrones, no skills ejecutables.
- `agents/` — agentes simples que componen skills.
- `templates/` — formatos para materializar outputs.
- `schemas/` — validación estructural mínima.
- `migration/` — notas y plan de transición desde el legado.

## Canonical flow

`brief-inception` → `brief-to-prd` → `prd-to-spec` → `spec-to-tasks`

Luego, según el caso:

- review → `change-review`
- migration → `rule-migration-plan`
- repeated errors → `improvement-loop`
- no Engram → `project-memory-fallback`

## Key governance docs

- `governance/04-workflow-map.md` — mapa estructural por tipo de cambio.
- `governance/05-quick-start-by-scenario.md` — guía operativa rápida por escenario.

## Brief options

- `templates/PROJECT-BRIEF-FULL.yaml` — versión completa para cambios grandes o complejos.
- `templates/PROJECT-BRIEF-LITE.yaml` — versión corta para proyectos pequeños, rápidos o exploratorios.

## Notes

- `gentle-ai` sigue siendo el orquestador.
- `/ai` no reemplaza la orquestación; aporta gobierno, estructura y continuidad.
- Si necesitas referencia histórica, usa `/legacy`.
