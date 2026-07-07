# /ai

Capas portables de guía, memoria fallback, skills, agentes simples y templates para trabajar con `gentle-ai` sin modificar su núcleo.

## Strategic role

`/ai` es la capa portable que este paquete instala dentro de otro proyecto para sumar governance, flujo y soporte operativo sin tocar el núcleo de `gentle-ai`.

Contexto histórico:

- `sdd-govplan` cubrió parte de la capa inicial de governance;
- `agent-core-v3` era el destino pensado para la distribución reusable;
- este paquete usa directamente `/ai` como overlay instalable.

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

`sdd-govp:brief-inception` → `sdd-govp:brief-to-prd` → `sdd-govp:prd-to-spec` → `sdd-govp:spec-to-tasks`

Luego, según el caso:

- review → `sdd-govp:change-review`
- migration → `sdd-govp:rule-migration-plan`
- repeated errors → `sdd-govp:improvement-loop`
- no Engram → `sdd-govp:project-memory-fallback`

## Key governance docs

- `governance/04-workflow-map.md` — mapa estructural por tipo de cambio.
- `governance/05-quick-start-by-scenario.md` — guía operativa rápida por escenario.

## Brief options

- `templates/PROJECT-BRIEF-FULL.yaml` — versión completa para cambios grandes o complejos.
- `templates/PROJECT-BRIEF-LITE.yaml` — versión corta para proyectos pequeños, rápidos o exploratorios.

## Notes

- `gentle-ai` sigue siendo el orquestador.
- `/ai` no reemplaza la orquestación; aporta gobierno, estructura y continuidad.
- Las menciones a `sdd-govplan` y `agent-core-v3` en esta carpeta son contexto de migración, no prerequisitos para usar el paquete.

## Installed through the CLI

Después de correr `npx agentcore-overlay init` o `agentcore-overlay init`, abrí en este orden:

1. `governance/00-start-here.md`
2. `governance/04-workflow-map.md`
3. `governance/05-quick-start-by-scenario.md`
