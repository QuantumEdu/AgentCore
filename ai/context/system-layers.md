# System Layers

## Arquitectura objetivo

### 1. Orquestación
- **gentle-ai**
- memoria con Engram
- delegación y SDD

### 2. Gobierno liviano
- `/ai/governance`
- project brief
- preguntas de intake
- decision gates

### 3. Capacidades portables
- `/ai/skills`
- skills neutrales a herramienta cuando sea posible

### 3.5 Memoria fallback local
- `/ai/context/decisions.md`
- `/ai/context/pitfalls.md`
- `/ai/context/working-memory.md`
- usar solo cuando Engram no esté disponible o como respaldo humano

### 4. Especialización opcional
- `/ai/agents`
- agentes solo cuando la tarea requiere entrevista, priorización o juicio continuo

### 5. Archivo histórico
- `/legacy`

## Decisión principal

AgentCore ya no debe ser el cerebro principal.
Debe quedar solo como **fuente rescatada de mejores prácticas**, con el resto archivado en `legacy/`.
