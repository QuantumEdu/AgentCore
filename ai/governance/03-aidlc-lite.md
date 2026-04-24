# AI-DLC Lite over gentle-ai

## Tesis

En este repositorio, AI-DLC-lite no reemplaza a gentle-ai.
Funciona como **capa de gobierno liviana** encima del orquestador.

## Distribución de responsabilidades

| Capa | Responsabilidad |
|------|-----------------|
| gentle-ai | Orquestación, memoria, SDD, delegación |
| /ai/governance | Intake, preguntas, gates, brief y decisiones iniciales |
| /ai/skills | Capacidades portables y reusables |
| /ai/agents | Especialistas opcionales por rol |
| .claude | Compatibilidad heredada y materiales legacy de AgentCore |

## Fases

1. **Inception**: brief, preguntas, clasificación del proyecto.
2. **Construction**: spec, tareas, implementación.
3. **Verification**: pruebas, revisión, ajuste documental.
4. **Operations**: runbooks, rollout, rollback, decisiones operativas.

## Regla de convivencia

Si una capa intenta decidir flujo, memoria y ejecución al mismo tiempo, hay duplicación.
En este diseño:

- gentle-ai decide la orquestación;
- AI-DLC-lite decide las puertas de paso;
- Engram recuerda.
