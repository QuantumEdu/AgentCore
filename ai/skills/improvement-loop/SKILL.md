---
name: sdd-govp:improvement-loop
description: "Trigger: sdd-govp:improvement-loop or /improvement-loop. Captura errores repetidos, identifica causa raíz y propone una regla, checklist o ajuste de flujo para evitar que vuelvan a ocurrir."
---

# Improvement Loop

## Goal

Convertir errores repetidos en aprendizaje operativo.

## When to use

- cuando el mismo error aparece varias veces;
- cuando una revisión rechaza cambios por la misma causa;
- cuando hay fallas repetidas en tests, seguridad, naming o arquitectura;
- cuando se quiere formalizar una mejora de proceso.

## Inputs

- error o fallo observado;
- contexto del cambio;
- ocurrencias previas si existen;
- regla actual o ausencia de ella.

## Workflow

1. Describir el error repetido.
2. Contar ocurrencias conocidas.
3. Clasificar el patrón:
   - arquitectura
   - naming
   - validación
   - seguridad
   - testing
   - documentación
   - flujo/proceso
4. Identificar causa raíz probable.
5. Elegir la respuesta mínima eficaz:
   - nueva regla
   - checklist
   - ajuste de skill
   - template
   - decisión registrada
6. Definir cómo medir si la mejora funcionó.

## Output format

### 1. Repeated Pattern
- qué se repite
- cuántas veces
- en qué contexto

### 2. Root Cause
- causa probable
- por qué el sistema actual no lo frenó

### 3. Proposed Improvement
- regla, checklist o ajuste concreto
- dónde debe vivir

### 4. Example
- before
- after

### 5. Validation
- cómo comprobar si el problema disminuye

## Rules

- no crear reglas grandilocuentes para problemas menores;
- preferir la corrección más pequeña que prevenga la repetición;
- si el problema es local, no volverlo política global;
- registrar el cambio en memoria persistente si Engram está disponible;
- si Engram no está disponible, registrar en `/ai/context/pitfalls.md` y `/ai/context/decisions.md`.

## Local fallback

Si no hay Engram:

- documentar el error repetido en `/ai/context/pitfalls.md`
- documentar la mejora acordada en `/ai/context/decisions.md`
- si el ajuste es temporal, anotarlo también en `/ai/context/working-memory.md`
