---
name: change-review
description: Revisa un cambio antes de integrarlo, buscando riesgos de ruptura, drift de documentación, impactos operativos y huecos de validación.
---

# Change Review

## Goal

Reducir el riesgo de romper algo antes de integrar un cambio.

## When to use

- antes de merge o release;
- cuando un cambio toca reglas, contratos, integraciones o comportamiento crítico;
- cuando se reemplaza un flujo existente por uno nuevo.

## Workflow

1. Identificar qué cambia y qué permanece igual.
2. Revisar impacto en:
   - contratos
   - reglas
   - datos
   - permisos
   - documentación
   - operación
3. Clasificar riesgos:
   - breaking
   - behavior drift
   - config mismatch
   - migration gap
   - missing validation
4. Verificar mitigaciones presentes.
5. Recomendar:
   - aprobar
   - aprobar con condiciones
   - no integrar todavía

## Output format

### 1. Change Summary
- qué cambia
- qué no debe romperse

### 2. Risk Review
- riesgo
- severidad
- evidencia

### 3. Missing Safeguards
- tests faltantes
- rollout faltante
- fallback faltante
- documentación faltante

### 4. Recommendation
- approved
- approved with conditions
- blocked

## Rules

- enfocarse en riesgo real, no en microestilo;
- distinguir ruptura técnica de cambio intencional;
- si el sistema ya está en operación, exigir rollout, fallback o reversión clara.
