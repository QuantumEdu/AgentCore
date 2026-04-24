# Workflow Map

## Purpose

Este mapa dice **cuándo usar cada skill**, en qué orden, y cuáles son obligatorias según el tipo de cambio.

Para una versión más práctica por escenario real, ver `05-quick-start-by-scenario.md`.

## Core rule

No usar todas las skills siempre.
Usar solo las necesarias para el tipo de trabajo.

## Canonical flow

### 1. Inception / Discovery
Usar cuando la idea todavía está difusa o faltan decisiones base.

Orden recomendado:
1. `brief-inception`
2. `project-stack-decider` *(si el stack no está claro)*
3. `brief-to-prd`
4. `prd-to-spec`
5. `spec-to-tasks`

## Change types

### A. New project or major initiative
Skills obligatorias:
- `brief-inception`
- `brief-to-prd`
- `prd-to-spec`
- `spec-to-tasks`

Skills opcionales:
- `project-stack-decider`
- `rule-migration-plan` *(si reemplaza algo existente)*

### B. Brownfield change in existing system
Skills obligatorias:
- `change-review`
- `prd-to-spec` *(si ya existe PRD o equivalente)*
- `spec-to-tasks`

Skills opcionales:
- `rule-migration-plan`
- `add-endpoint`
- `project-memory-fallback` *(si no hay Engram)*

### C. New endpoint or API change
Skills obligatorias:
- `add-endpoint`
- `change-review`

Skills opcionales:
- `prd-to-spec`
- `spec-to-tasks`
- `rule-migration-plan` *(si rompe o reemplaza contrato/regla)*

### D. Production-safe rule replacement
Skills obligatorias:
- `rule-migration-plan`
- `change-review`

Skills opcionales:
- `local-retrospective`
- `improvement-loop`

### E. Repeated errors or process drift
Skills obligatorias:
- `improvement-loop`

Skills opcionales:
- `local-retrospective`
- `project-memory-fallback`

### F. No Engram / low-memory continuity mode
Skills obligatorias:
- `project-memory-fallback`

Skills opcionales:
- `local-retrospective`
- `improvement-loop`

## Review / learning flow

Al terminar un cambio relevante:
1. `change-review`
2. `local-retrospective`
3. `improvement-loop` *(si hubo error repetido o fricción recurrente)*

## Style / support skills

Usar según necesidad:
- `geek-tech-tone` → cuando quieras tono geek, técnico y proactivo
- `prompt-improver` → cuando haya que mejorar prompts
- `coding-conventions` → para revisar base de arquitectura/API/security/testing

## Anti-chaos rule

Si una tarea es pequeña, no dispares cinco skills.
Si el cambio es grande, no saltes directo a implementación.
