# AgentCore Publish

Repositorio de transición para convertir AgentCore en una capa más **agnóstica, guiada y portable**, manteniendo compatibilidad con gentle-ai sin tocar su núcleo.

## Objetivo

- dejar a **gentle-ai** como orquestador;
- mover la guía inicial, gobierno liviano y briefing a `/ai`;
- rescatar mejores prácticas hacia `/ai` y dejar lo demás archivado;
- preparar skills/agentes más personales, estructurados y profesionales.

## Estructura recomendada

```text
/ai
  /agents
  /context
  /governance
  /migration
  /skills
  /templates
/legacy
  /docs
  /scratch
/legacy
AGENTS.md
```

## Regla operativa

1. Para iniciar un proyecto o cambio grande, leer `AGENTS.md`.
2. Luego leer `/ai/governance/00-start-here.md`.
3. Usar el brief como gate de entrada antes de PRD/spec/tareas.
4. Tratar `/legacy` como archivo histórico, no como flujo activo.

## Estado actual

- Se agregó una capa `/ai` con gobierno tipo AI-DLC-lite.
- Se definió un agente de inception y skills de brief, tono y mejora de prompts.
- Los archivos claramente sobrantes quedaron en `legacy/`.
- `READMEv2.md` queda archivado como referencia histórica.
