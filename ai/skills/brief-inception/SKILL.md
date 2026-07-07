---
name: sdd-govp:brief-inception
description: "Trigger: sdd-govp:brief-inception or /brief-inception. Usa el PROJECT-BRIEF-FULL canónico como motor de discovery inicial. Clasifica el proyecto, detecta huecos, hace hasta 7 preguntas críticas y propone el siguiente artefacto correcto sin saltar directo a implementación."
---

# Brief Inception

## Cuándo usar

- cuando el usuario trae una idea difusa;
- cuando hay que decidir tipo de proyecto o stack;
- cuando existe un brief parcial;
- cuando se quiere pasar de brief a PRD/spec con orden.

## Fuente principal

Tomar como base `/ai/templates/PROJECT-BRIEF-FULL.yaml`.

Para proyectos pequeños o rápidos, se puede usar `/ai/templates/PROJECT-BRIEF-LITE.yaml`.

## Validación

- usar `/ai/schemas/brief-schema.json` solo como validación estructural mínima;
- la validación real del brief es contextual y la hace este workflow;
- si el schema y el brief difieren, priorizar el brief canónico y registrar la divergencia.

## Comportamiento

1. Leer el brief o el input del usuario.
2. Detectar vacíos críticos.
3. Hacer máximo 7 preguntas agrupadas, incluyendo patrón arquitectónico o de diseño cuando sea relevante.
4. Clasificar:
   - tipo de proyecto
   - estado del proyecto
   - complejidad
   - nivel de riesgo
5. Recomendar el siguiente paso:
   - PRD corto
   - spec
   - ADR
   - exploración brownfield

## Preguntas sugeridas

- problema y usuario principal;
- estado del proyecto: greenfield, brownfield o migración;
- tipo de entrega principal;
- restricción dominante;
- módulos core y bounded contexts;
- integraciones inevitables;
- patrón arquitectónico o patrón de diseño preferido, si ya existe una intención clara.


## Recomendación de diseño

El `PROJECT-BRIEF-FULL.yaml` conviene más como:

- **template base**;
- **skill operativa** para procesarlo;
- y opcionalmente un **agente** cuando se necesita entrevista continua.

## Pros y contras

### Como skill
- más portable
- más simple
- más barata en contexto
- ideal para brief → PRD/spec

### Como agente
- mejor para discovery conversacional
- mejor para entrevistar y priorizar
- más flexible con huecos ambiguos
- pero más costoso y más fácil de sobrepensar

## Recomendación final

Usarlo como **skill primero** y como **agente opcional** solo para inception compleja.

## Heurística práctica

- proyecto pequeño / rápido / exploratorio → preferir brief lite;
- proyecto mediano o grande / con riesgo / con muchas integraciones → usar brief full.
