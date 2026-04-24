# Start Here

Esta es la capa de guía inicial que faltaba para complementar gentle-ai sin competir con él.

## Propósito

Antes de diseñar o construir, obligar una conversación corta pero útil para entender:

- qué tipo de proyecto es;
- qué problema resuelve;
- qué tan incierto o crítico es;
- qué artefactos hacen falta antes de implementar.

## Flujo de entrada

1. Leer el brief canónico: `/ai/templates/PROJECT-BRIEF-FULL.yaml`.
2. Detectar campos críticos vacíos.
3. Hacer máximo **7 preguntas críticas** agrupadas por negocio, arquitectura, patrones de diseño y delivery.
4. Clasificar el proyecto:
   - greenfield / brownfield / migración / prototipo
   - web / desktop / híbrido / api / cli / agente
   - simple / estándar / complejo
5. Generar o actualizar:
   - PRD corto
   - decisiones iniciales
   - spec o plan siguiente
6. Recién después pasar a implementación.

## Regla clave

gentle-ai **orquesta**.
Esta guía solo **gobierna el paso** y reduce ambigüedad al inicio.

## Artefactos mínimos esperados

- brief suficiente o parcialmente completado con vacíos explícitos
- decisión de stack inicial
- riesgos principales
- siguiente artefacto recomendado

## Preguntas mínimas sugeridas

1. ¿Qué problema real resuelve y para quién?
2. ¿Es greenfield, brownfield o migración?
3. ¿Cuál es el tipo de entrega principal?
4. ¿Cuál es la restricción dominante: tiempo, riesgo, costo o compliance?
5. ¿Qué módulos o bounded contexts son core y qué patrón arquitectónico/diseño prefieres si ya lo sabes?
6. ¿Qué integraciones externas son inevitables?
7. ¿Qué queda explícitamente fuera de alcance?
