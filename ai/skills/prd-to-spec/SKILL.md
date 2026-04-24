---
name: prd-to-spec
description: Convierte un PRD en una spec operativa y verificable, separando requisitos, escenarios, restricciones, decisiones pendientes y criterios de aceptación.
---

# PRD to Spec

## Goal

Tomar un PRD y transformarlo en una spec clara para implementación y verificación.

## When to use

- cuando ya existe un PRD y hay que bajar a especificación;
- cuando el alcance está claro pero todavía no hay escenarios verificables;
- cuando se quiere reducir ambigüedad antes de tasks o apply.

## Inputs

- PRD principal;
- decisiones iniciales o ADRs si existen;
- restricciones del proyecto;
- dudas abiertas del brief, si siguen vivas.

## Workflow

1. Leer el PRD completo.
2. Identificar:
   - objetivo del cambio o producto;
   - actores;
   - capacidades esperadas;
   - restricciones;
   - riesgos.
3. Reescribir en formato de requisitos verificables.
4. Convertir ambigüedades en:
   - decisión pendiente;
   - supuesto explícito; o
   - pregunta bloqueante.
5. Generar escenarios o acceptance criteria observables.
6. Cerrar con alcance, no alcance y riesgos.

## Output format

### 1. Summary
- qué cubre la spec
- qué no cubre

### 2. Requirements
Usar formato consistente:
- **Requirement**
- **Why**
- **Acceptance criteria**

### 3. Key Scenarios
- happy path
- edge cases
- errores relevantes
- permisos o seguridad si aplica

### 4. Constraints
- técnicas
- negocio
- operación

### 5. Open Decisions
- decisiones aún no cerradas
- impacto de no resolverlas

### 6. Verification Notes
- cómo se sabrá que está bien implementado

## Rules

- no copiar el PRD de forma mecánica;
- convertir lenguaje aspiracional en comportamiento verificable;
- distinguir entre requisito, preferencia y suposición;
- si falta información crítica, señalarla sin inventarla.

## Recommended template

Usar `/ai/templates/spec-template.md` como base cuando convenga materializar el resultado en archivo.
