# AgentCore to gentle-ai migration plan

## Objetivo

Reducir AgentCore a convenciones exportables y dejar a gentle-ai como orquestador estable.

## Qué se conserva

- brief canónico
- reglas reutilizables
- scripts de soporte
- plantillas
- documentación histórica útil

## Qué se promueve a flujo principal

- `AGENTS.md`
- `/ai/governance/*`
- `/ai/skills/*`
- `/ai/agents/*`
- `/ai/context/*`

## Qué queda como archivo histórico

- guías antiguas de AgentCore
- reglas y agentes acoplados al ejemplo FlowTask
- stacks, scripts y skills heredadas no migradas a `/ai`

## Criterio de limpieza

Mover a `legacy/` solo lo claramente:

- experimental
- duplicado
- de scratch
- reemplazado por una versión nueva canónica

## Resultado de fase 2

La fuente activa ahora es `/ai`.
`/legacy` guarda únicamente material histórico o demasiado acoplado para seguir en el flujo principal.
