---
name: sdd-govp:rule-migration-plan
description: "Trigger: sdd-govp:rule-migration-plan or /rule-migration-plan. Diseña una migración segura para reemplazar reglas o flujos en sistemas ya operativos, usando shadow mode, rollout gradual, fallback y rollback explícito."
---

# Rule Migration Plan

## Goal

Reemplazar reglas o flujos existentes sin romper operación, contratos ni comportamiento crítico.

## When to use

- cuando ya existe un sistema en producción u operación activa;
- cuando se quiere sustituir una regla vieja por una nueva;
- cuando se migra de un flujo legacy a uno nuevo;
- cuando hay riesgo de behavior drift o de romper consumers existentes.

## Inputs

- regla actual o flujo actual;
- regla nueva o flujo nuevo;
- superficies afectadas;
- criticidad del sistema;
- controles actuales de validación;
- posibilidad de feature flag, rollout gradual o rollback.

## Migration principles

1. no hacer cutover total sin validación previa;
2. observar primero, sustituir después;
3. preferir compatibilidad temporal a ruptura elegante;
4. toda migración debe tener rollback claro;
5. si el riesgo es alto, exigir pilot o canary.

## Workflow

1. Describir el estado actual.
2. Definir qué problema resuelve la nueva regla.
3. Identificar qué no debe romperse:
   - contratos
   - permisos
   - datos
   - integraciones
   - operación diaria
4. Elegir estrategia de introducción:
   - shadow mode
   - feature flag
   - rollout por módulo
   - rollout por entorno
   - canary o piloto
5. Definir validaciones:
   - tests
   - revisión manual
   - métricas o señales
   - feedback operativo
6. Definir fallback y rollback.
7. Definir criterio explícito para retirar la regla vieja.

## Output format

### 1. Current vs Target
- qué existe hoy
- qué se quiere reemplazar
- por qué vale la pena migrar

### 2. Blast Radius
- qué áreas toca
- qué podría romperse
- criticidad

### 3. Migration Strategy
- shadow mode / flag / piloto / rollout gradual
- secuencia propuesta

### 4. Safeguards
- tests
- observabilidad
- revisión
- documentación

### 5. Rollback Plan
- trigger de rollback
- pasos de reversión
- impacto esperado

### 6. Removal Criteria
- cuándo se puede retirar la regla vieja

## Rules

- no migrar reglas críticas en viernes o cierre operativo;
- no retirar la regla vieja antes de tener evidencia suficiente;
- si la regla toca datos o auth, elevar el nivel de validación;
- si no hay métricas, usar al menos checklist operativa y validación manual;
- si la migración cambia comportamiento visible, documentarlo para usuarios o equipo.

## Related skills

- `sdd-govp:change-review`
- `sdd-govp:local-retrospective`
- `sdd-govp:improvement-loop`
- `sdd-govp:project-memory-fallback`

## Recommended template

Usar `/ai/templates/rule-migration-template.md` para materializar el plan.
