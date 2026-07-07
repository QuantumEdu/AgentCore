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
1. `sdd-govp:brief-inception`
2. `sdd-govp:project-stack-decider` *(si el stack no está claro)*
3. `sdd-govp:brief-to-prd`
4. `sdd-govp:prd-to-spec`
5. `sdd-govp:spec-to-tasks`

## Change types

### A. New project or major initiative
Skills obligatorias:
- `sdd-govp:brief-inception`
- `sdd-govp:brief-to-prd`
- `sdd-govp:prd-to-spec`
- `sdd-govp:spec-to-tasks`

Skills opcionales:
- `sdd-govp:project-stack-decider`
- `sdd-govp:rule-migration-plan` *(si reemplaza algo existente)*

### B. Brownfield change in existing system
Skills obligatorias:
- `sdd-govp:change-review`
- `sdd-govp:prd-to-spec` *(si ya existe PRD o equivalente)*
- `sdd-govp:spec-to-tasks`

Skills opcionales:
- `sdd-govp:rule-migration-plan`
- `sdd-govp:add-endpoint`
- `sdd-govp:project-memory-fallback` *(si no hay Engram)*

### C. New endpoint or API change
Skills obligatorias:
- `sdd-govp:add-endpoint`
- `sdd-govp:change-review`

Skills opcionales:
- `sdd-govp:prd-to-spec`
- `sdd-govp:spec-to-tasks`
- `sdd-govp:rule-migration-plan` *(si rompe o reemplaza contrato/regla)*

### D. Production-safe rule replacement
Skills obligatorias:
- `sdd-govp:rule-migration-plan`
- `sdd-govp:change-review`

Skills opcionales:
- `sdd-govp:local-retrospective`
- `sdd-govp:improvement-loop`

### E. Repeated errors or process drift
Skills obligatorias:
- `sdd-govp:improvement-loop`

Skills opcionales:
- `sdd-govp:local-retrospective`
- `sdd-govp:project-memory-fallback`

### F. No Engram / low-memory continuity mode
Skills obligatorias:
- `sdd-govp:project-memory-fallback`

Skills opcionales:
- `sdd-govp:local-retrospective`
- `sdd-govp:improvement-loop`

## Review / learning flow

Al terminar un cambio relevante:
1. `sdd-govp:change-review`
2. `sdd-govp:local-retrospective`
3. `sdd-govp:improvement-loop` *(si hubo error repetido o fricción recurrente)*

## Style / support skills

Usar según necesidad:
- `sdd-govp:geek-tech-tone` → cuando quieras tono geek, técnico y proactivo
- `sdd-govp:prompt-improver` → cuando haya que mejorar prompts
- `sdd-govp:coding-conventions` → para revisar base de arquitectura/API/security/testing

## Anti-chaos rule

Si una tarea es pequeña, no dispares cinco skills.
Si el cambio es grande, no saltes directo a implementación.
