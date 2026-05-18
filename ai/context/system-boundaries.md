# System Boundaries

## Purpose

Definir con claridad qué pertenece al core distribuible `agent-core-v3`, qué pertenece al runtime `gentle-ai`, y qué debe permanecer local dentro de un proyecto.

## Boundary model

### 1. Runtime / Orchestration
**Owner:** `gentle-ai`

Responsabilidades:
- orquestación
- Engram
- SDD
- delegación
- subagentes
- ejecución conversacional

### 2. Global distributable core
**Owner:** `agent-core-v3`

Responsabilidades:
- skills universales instalables por npm
- templates base reusables
- assets comunes multi-tool
- instalación para OpenCode, Claude, Cursor, Codex, Copilot, Gemini, Gentle AI y similares

### 3. Local project overlay
**Owner:** `/ai` dentro del repo

Responsabilidades:
- onboarding del repo
- governance específica del proyecto
- workflow map
- quick start por escenario
- decisiones locales
- pitfalls locales
- memoria fallback local
- agentes simples adaptados al proyecto
- contratos de salida elegidos por el proyecto

## Current conclusion

La dirección correcta es:

- `gentle-ai` = runtime
- `agent-core-v3` = core reusable
- `/ai` = overlay local del proyecto

## Practical rule

Si algo debe instalarse igual en muchos repos y herramientas, debe vivir en `agent-core-v3`.

Si algo explica cómo operar ESTE repo, debe vivir en `/ai`.
