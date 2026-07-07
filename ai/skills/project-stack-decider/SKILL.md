---
name: sdd-govp:project-stack-decider
description: "Trigger: sdd-govp:project-stack-decider or /project-stack-decider. Ayuda a decidir el stack y forma de entrega de un proyecto de manera agnóstica, justificando trade-offs y separando decisión actual, supuestos y alternativas descartadas."
---

# Project Stack Decider

## Goal

Recomendar un stack o una shortlist razonada según el tipo de proyecto, restricciones, equipo y riesgos.

## When to use

- cuando el stack no está decidido;
- cuando hay varias opciones viables;
- cuando el usuario quiere justificar por qué elegir una opción y no otra;
- cuando el brief ya existe pero falta dirección técnica inicial.

## Inputs to evaluate

- tipo de entrega: web, desktop, híbrido, api, cli, agente;
- estado del proyecto: greenfield, brownfield, migración;
- experiencia del equipo;
- plazo y presupuesto;
- criticidad;
- necesidades de UI, tiempo real, integraciones, offline, hardware, IA;
- restricciones de hosting, compliance o mantenimiento.

## Decision process

1. Identificar la restricción dominante.
2. Determinar si la prioridad es:
   - velocidad de entrega
   - mantenibilidad
   - performance
   - compatibilidad con sistema existente
   - experiencia de usuario
3. Generar 2-4 opciones razonables.
4. Compararlas por trade-offs.
5. Recomendar:
   - una opción principal, o
   - una shortlist si aún falta información.

## Output format

### 1. Context Summary
- contexto mínimo de la decisión

### 2. Decision Drivers
- factores que realmente empujan la elección

### 3. Candidate Stacks
Para cada opción:
- stack
- por qué encaja
- costos o límites
- cuándo NO elegirlo

### 4. Recommended Direction
- opción principal
- justificación
- nivel de confianza: alto / medio / bajo

### 5. Alternatives Rejected
- qué se descartó y por qué

### 6. Open Questions
- qué falta saber para cerrar mejor la decisión

## Rules

- no casarse con una tecnología por moda;
- preferir tool-agnostic antes que vendor-locked;
- separar stack de ejecución, patrón arquitectónico y herramientas auxiliares;
- si el usuario ya usa gentle-ai, no proponer nada que dependa de modificar su núcleo;
- si el proyecto es pequeño, evitar sobrearquitectura.

## Pattern note

Cuando sea relevante, distinguir entre:

- **stack**: frameworks, runtime, base de datos, UI;
- **patrón arquitectónico**: layers, hexagonal, clean, modular monolith;
- **patrones de diseño**: strategy, adapter, factory, etc.

No mezclar esos tres niveles en una sola recomendación vaga.
