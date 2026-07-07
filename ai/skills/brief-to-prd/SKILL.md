---
name: sdd-govp:brief-to-prd
description: "Trigger: sdd-govp:brief-to-prd or /brief-to-prd. Convierte un brief canónico o parcial en un PRD corto, claro y profesional. Detecta vacíos críticos, pide solo lo faltante y entrega decisiones iniciales, riesgos y siguiente paso recomendado."
---

# Brief to PRD

## Goal

Transformar un `PROJECT-BRIEF-FULL.yaml` o un brief informal en un PRD útil, no burocrático.

## Source of truth

- Brief canónico: `/ai/templates/PROJECT-BRIEF-FULL.yaml`
- Validación opcional mínima: `/ai/schemas/brief-schema.json`

## Validation note

El schema valida solo la estructura base estable.
La interpretación profunda, los vacíos críticos y la consistencia real del brief la resuelve esta skill.

## When to use

- cuando el usuario ya tiene un brief y quiere aterrizarlo;
- cuando hay que pasar de idea a PRD corto;
- cuando se necesita ordenar alcance, decisiones y riesgos antes de spec o implementación.

## Workflow

1. Leer el brief o material fuente.
2. Validar si están claros estos mínimos:
   - problema
   - usuario o stakeholder principal
   - tipo de entrega
   - estado del proyecto
   - alcance inicial
3. Si faltan piezas críticas, hacer hasta 7 preguntas agrupadas.
4. Clasificar el proyecto:
   - greenfield / brownfield / migración / prototipo
   - simple / estándar / complejo
   - riesgo bajo / medio / alto
5. Producir un PRD corto y accionable.
6. Cerrar con:
   - decisiones iniciales
   - riesgos
   - supuestos
   - siguiente artefacto recomendado

## Design guidance

Si el usuario ya muestra una preferencia técnica, capturarla como hipótesis, no como verdad cerrada.

Incluir patrón arquitectónico o de diseño solo cuando:

- afecta alcance o complejidad;
- cambia la estrategia de entrega;
- el usuario lo pide explícitamente.

## Output format

### 1. Executive Summary
- qué se va a construir
- para quién
- por qué importa

### 2. Problem Statement
- problema actual
- impacto
- oportunidad

### 3. Users and Stakeholders
- usuario principal
- actores relevantes

### 4. Scope
- in scope
- out of scope

### 5. Functional Expectations
- capacidades clave del MVP o primera fase

### 6. Constraints and Risks
- restricciones de negocio o técnicas
- riesgos principales

### 7. Initial Technical Direction
- tipo de entrega
- stack tentativo o criterios para decidirlo
- patrón arquitectónico/diseño si ya está justificado

### 8. Recommended Next Step
- spec
- ADR
- exploration brownfield
- stack decision

## Quality bar

- no inventar requisitos;
- no volverlo un documento inflado;
- distinguir hechos, supuestos y decisiones pendientes;
- dejar claro qué falta antes de construir.
