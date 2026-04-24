---
name: spec-to-tasks
description: Convierte una spec en tareas pequeñas, dependientes y ejecutables, con orden de implementación, criterios de done y riesgos visibles.
---

# Spec to Tasks

## Goal

Transformar una spec en un plan de ejecución realista, ordenado y fácil de delegar.

## When to use

- cuando la spec ya está aprobada o suficientemente estable;
- cuando hay que pasar de requisitos a implementación;
- cuando se quiere evitar tareas vagas o demasiado grandes.

## Workflow

1. Leer la spec completa.
2. Identificar piezas de trabajo:
   - dominio
   - contratos
   - persistencia
   - UI/API
   - seguridad
   - pruebas
   - documentación
3. Separar tareas por dependencia.
4. Dividir tareas grandes en pasos verificables.
5. Añadir criterio de done por tarea.
6. Señalar bloqueos, riesgos y paralelización posible.

## Output format

### 1. Execution Summary
- qué se construirá primero
- qué depende de qué

### 2. Task List
Para cada tarea incluir:
- **Task**
- **Why**
- **Depends on**
- **Done when**

### 3. Parallel Work
- qué puede hacerse en paralelo

### 4. Risks / Blockers
- bloqueos técnicos
- decisiones pendientes

## Task quality rules

- una tarea debe ser lo bastante chica para ejecutarse y validarse;
- evitar tareas tipo “hacer todo el backend”;
- incluir pruebas y documentación cuando correspondan;
- respetar el orden natural de dependencias;
- separar refactor, feature y hardening si el riesgo lo exige.

## Recommended template

Usar `/ai/templates/tasks-template.md` como base cuando convenga materializar el resultado en archivo.
