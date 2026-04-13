---
tags:
  - claude
  - prompts
  - skills
  - referencia
type: referencia
created: 2026-04-04
source: ~/.claude/skills/special-instruction/SKILL.md
---

# special-instruction — Plantillas

> Skill activo en Claude Code como `/special-instruction`.  
> Guía para crear prompts, skills, agentes o tools con la estructura correcta.

---

## Guía de Selección

| Tipo | Úsalo cuando... |
|------|-----------------|
| **Prompt básico** | Instrucción única, system prompt, directiva de comportamiento, bloque de texto reutilizable sin pasos |
| **Skill (workflow)** | Workflow repetible con múltiples pasos y criterios de éxito por paso |
| **Agente** | Entidad autónoma que necesita identidad, fortalezas y lineamientos de comportamiento |
| **Tool / Referencia** | Función con inputs/outputs/restricciones — o una tabla de decisión/documentación |

---

## Tipo 1: PROMPT BÁSICO

```markdown
# [Nombre del Prompt]

## Context
[Cuándo y para qué se usa este prompt]

## Instruction
[El prompt en sí — claro, directo, sin ambigüedad]

## Variables (si aplica)
- `{{variable}}`: [descripción]

## Example
Input: [ejemplo de entrada]
Output: [ejemplo de salida esperada]
```

---

## Tipo 2: SKILL (Workflow Steps)

```markdown
# [Nombre del Skill]

## Goal
[Una frase clara describiendo el objetivo principal del skill]

## Steps

### 1. [Nombre del Paso 1]
[Descripción detallada de qué hacer en este paso]
**Success criteria**: [Cómo saber que este paso está completo]

### 2. [Nombre del Paso 2]
[Descripción detallada]
**Success criteria**: [Criterio de éxito]

### 3. [Nombre del Paso 3]
[Descripción detallada]
**Success criteria**: [Criterio de éxito]

## Rules
- [Regla importante 1]
- [Regla importante 2]
- [Regla importante 3]

## Examples
[Ejemplos concretos de uso]
```

---

## Tipo 3: AGENTE (Identity + Strengths + Guidelines)

```markdown
# [Nombre del Agente]

You are a [role/persona] for [context].

[Restricciones críticas — READ-ONLY, scope limits, etc.]

## Your strengths
- [Strength 1]
- [Strength 2]
- [Strength 3]

## Guidelines
- [Guideline 1]
- [Guideline 2]
- [Guideline 3]

## When to use
[Cuándo invocar este agente vs otros disponibles]

## Examples
[Ejemplo de invocación y resultado esperado]
```

---

## Tipo 4: TOOL / REFERENCIA (Sections + Tables)

```markdown
# [Tool/Feature Name]

[Introducción breve — qué es y por qué importa]

| Parameter | Description | Examples |
|-----------|-------------|----------|
| [param1]  | [desc]      | [ex 1], [ex 2] |
| [param2]  | [desc]      | [ex 1], [ex 2] |

## When to Use This Tool
1. [Condición 1] — ejemplo: [...]
2. [Condición 2] — ejemplo: [...]

## How This Tool Works
[Explicación paso a paso del mecanismo]

## Examples

### GOOD — Use [Tool]:
[Ejemplo 1]

### BAD — Don't use [Tool]:
[Ejemplo 1]

## Important Notes
- [Nota 1]
- [Nota 2]
```

---

## Reglas del Skill

- Nunca generar un template con placeholders sin llenar, a menos que el usuario pida la versión en blanco
- Si el usuario pide tipo X pero el contenido encaja mejor en Y, explicarlo y dejarlo decidir
- Proponer un default antes de preguntar en abstracto
- Eliminar secciones opcionales que no se usan — no dejarlas vacías
- Siempre ofrecer guardar en la ruta correcta después de generar

---

*Archivo sincronizado con `~/.claude/skills/special-instruction/SKILL.md`*
