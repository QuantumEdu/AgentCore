---
name: project-memory-fallback
description: Provee una memoria local mínima basada en archivos cuando Engram no está disponible, para registrar decisiones, pitfalls, contexto de trabajo y continuidad del proyecto.
---

# Project Memory Fallback

## Goal

Mantener continuidad de contexto sin depender de memoria externa.

## When to use

- cuando Engram no está disponible;
- cuando se quiere una copia humana y local de decisiones relevantes;
- cuando el proyecto necesita continuidad básica entre sesiones.

## Files of record

- `/ai/context/decisions.md`
- `/ai/context/pitfalls.md`
- `/ai/context/working-memory.md`

## What goes where

### decisions.md
Guardar:
- decisiones técnicas
- convenciones acordadas
- elecciones de stack o arquitectura
- cambios de flujo estables

### pitfalls.md
Guardar:
- errores recurrentes
- gotchas
- edge cases
- cosas que ya fallaron y conviene no repetir

### working-memory.md
Guardar:
- estado temporal de trabajo
- próximos pasos
- bloqueos actuales
- contexto útil de corto plazo

## Workflow

1. Verificar si Engram está disponible.
2. Si no lo está, usar estos archivos como memoria local.
3. Registrar inmediatamente:
   - decisiones nuevas
   - bugs importantes
   - descubrimientos no obvios
   - estado parcial si una tarea queda a medias
4. Al cerrar una sesión, actualizar working-memory con:
   - qué se logró
   - qué sigue
   - qué quedó bloqueado

## Writing rules

- escribir entradas cortas y buscables;
- separar hechos de hipótesis;
- actualizar en vez de duplicar cuando sea el mismo tema;
- no usar working-memory para decisiones permanentes;
- mover a decisions o pitfalls lo que deje de ser temporal.

## Suggested entry formats

### decisions.md
- **Decision**:
- **Why**:
- **Impact**:
- **Date**:

### pitfalls.md
- **Pitfall**:
- **Symptom**:
- **Fix / Prevention**:
- **Date**:

### working-memory.md
- **Current focus**:
- **Done**:
- **Next**:
- **Blocked by**:

## Relationship with Engram

Si Engram existe, usar Engram como memoria principal.
Estos archivos pueden seguir existiendo como respaldo humano, pero no deben competir con la memoria persistente principal.
