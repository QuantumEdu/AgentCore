# AgentCore Overlay

Overlay reusable para trabajar con `gentle-ai` usando `/ai` como capa portable de gobierno, flujo y soporte operativo.

Este repo ahora se puede usar directamente como paquete Node para instalarlo con `npx` o `npm install -g`, y su objetivo principal es **copiar la capa reusable** dentro de otro proyecto sin tocar el core de `gentle-ai`.

## 1. Qué es este repo

Este repositorio publica una capa de trabajo reusable con:

- `/ai` para governance, workflow, skills, agents, templates y fallback local;
- `AGENTS.md` como entrypoint operativo del proyecto;
- documentación pública para entender cómo adoptarlo.

No intenta reemplazar a `gentle-ai`.

- `gentle-ai` orquesta;
- este repo aporta la capa portable de guía y estructura.

## 2. Por qué siguen apareciendo menciones a `agent-core-v3`

Vas a ver referencias viejas a `agent-core-v3` porque este repo nació como parte de una transición mayor.

En concreto:

1. `sdd-govplan` capturó parte de la capa de governance;
2. `agent-core-v3` era el destino pensado para la distribución global/npm del core reusable;
3. este repo consolidó el overlay `/ai` que faltaba ordenar y publicar.

La idea importante HOY no es `agent-core-v3` como mensaje principal.
La idea importante es esta: **este repo ya sirve por sí mismo como fuente instalable del overlay reusable**.

### 1.1 Naming Convention

All skills in this overlay use the prefix `sdd-govp:` (inspired by `ospx:` from OpenSpec).
Use the prefix when invoking skills, e.g., `sdd-govp:brief-inception` → `sdd-govp:spec-to-tasks`.

## 3. Instalación

### Con `npx`

```bash
npx agentcore-overlay init
```

### Instalación global

```bash
npm install -g agentcore-overlay
agentcore-overlay init
```

### Instalar en un directorio específico

```bash
npx agentcore-overlay init my-project
```

### Sobrescribir archivos existentes

Por defecto, el scaffold **no sobreescribe** archivos existentes.

```bash
npx agentcore-overlay init my-project --force
```

## 4. Qué copia el comando

El CLI copia solamente lo mínimo reusable para incrustar el sistema en otro proyecto:

1. `ai/`
2. `AGENTS.md`

No copia `README.md`, `FAQ.md` ni `CHANGELOG.md` al proyecto destino porque son documentación del repositorio fuente, no parte obligatoria del overlay operativo.

## 5. Uso rápido

### Ejemplo A: inicializar en el directorio actual

```bash
npx agentcore-overlay init
```

Resultado esperado:

- aparece `./ai`
- aparece `./AGENTS.md`

### Ejemplo B: inicializar en un proyecto nuevo

```bash
npx agentcore-overlay init apps/customer-portal
```

Resultado esperado:

- `apps/customer-portal/ai`
- `apps/customer-portal/AGENTS.md`

### Ejemplo C: ver qué haría sin escribir archivos

```bash
npx agentcore-overlay init sandbox --dry-run
```

### Ejemplo D: actualizar un overlay existente

```bash
agentcore-overlay init . --force
```

Esto sobrescribe archivos coincidentes del overlay. No elimina archivos viejos que hayan quedado fuera de versiones anteriores.

## 6. Qué hacer después de `init`

Seguí este orden:

1. leer `AGENTS.md`
2. leer `ai/README.md`
3. leer `ai/governance/00-start-here.md`
4. usar `ai/governance/04-workflow-map.md` si necesitás vista estructural
5. usar `ai/governance/05-quick-start-by-scenario.md` si necesitás entrada por caso real

### Flujo canónico

```
sdd-govp:brief-inception → sdd-govp:brief-to-prd → sdd-govp:prd-to-spec → sdd-govp:spec-to-tasks
```

Después, según necesidad:
- `sdd-govp:change-review` — revisar cambio antes de integrar
- `sdd-govp:rule-migration-plan` — migración segura de reglas
- `sdd-govp:improvement-loop` — error repetido o fricción recurrente
- `sdd-govp:project-memory-fallback` — continuidad sin Engram
- `sdd-govp:workflow-builder` — proyectos no-software (tesis, consultoría, coaching)
- `sdd-govp:add-endpoint` — agregar endpoint nuevo
- `sdd-govp:local-retrospective` — retrospectiva post-cambio

## 7. Estructura

1. `ai/agents` — agentes simples por rol (change-reviewer, endpoint-designer, migration-guardian, project-inception-architect)
2. `ai/context` — contexto estable y memoria fallback local (decisions, pitfalls, working-memory, system-layers)
3. `ai/governance` — gates, quick-start y workflow map
4. `ai/migration` — material de transición y consolidación histórica
5. `ai/schemas` — validación estructural mínima
6. `ai/skills` — capacidades operativas reutilizables (15 skills + workflow-builder con templates)
7. `ai/templates` — briefs, ADRs, roadmaps y otros formatos (10 templates)
8. `AGENTS.md` — entrypoint operativo del overlay dentro del proyecto

## 8. Casos de uso concretos

### Proyecto nuevo con discovery antes de implementar

1. iniciar con `agentcore-overlay init`
2. abrir `AGENTS.md`
3. usar `PROJECT-BRIEF-LITE` o `PROJECT-BRIEF-FULL`
4. avanzar por el flujo canónico: `sdd-govp:brief-inception` → `sdd-govp:brief-to-prd` → `sdd-govp:prd-to-spec` → `sdd-govp:spec-to-tasks`

### Proyecto ya en marcha con cambio sensible

1. inicializar el overlay en el repo
2. entrar por `sdd-govp:change-review`
3. si hay reemplazo de reglas o configuración, usar `sdd-govp:rule-migration-plan`

### Proyecto sin Engram disponible

1. inicializar el overlay
2. usar `sdd-govp:project-memory-fallback`
3. guardar decisiones y contexto en `ai/context`

### Proyecto no-software (tesis, consultoría, coaching)

1. inicializar el overlay
2. ejecutar `sdd-govp:workflow-builder`
3. elegir template (thesis, consulting, pnl-coaching, career-coaching) o definir flujo custom
4. ejecutar fases generadas con `/workflow continue`

## 9. Límites del paquete

Este paquete NO instala ni modifica `gentle-ai`.

Solo scaffolda la capa reusable que este repo mantiene en `/ai` y `AGENTS.md`.

## 10. Desarrollo local de este repo

Para probar el CLI desde este repositorio:

```bash
node bin/agentcore-overlay.js --help
node bin/agentcore-overlay.js init . --force --dry-run
```

## 11. Licencia

Este proyecto se distribuye bajo licencia `MIT`.
