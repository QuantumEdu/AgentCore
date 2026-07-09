# AgentCore Overlay

Overlay portable de governance, skills, agents y templates para trabajar con `gentle-ai`.

Un `npx agentcore-overlay init` y tenés toda la estructura operativa dentro de tu proyecto, sin tocar el core del orquestador.

---

## Instalación

Actualmente desde GitHub (el paquete npm está próximo a publicarse):

```bash
npx -p git+https://github.com/QuantumEdu/AgentCore.git agentcore-overlay init
```

O clonando y ejecutando local:

```bash
git clone https://github.com/QuantumEdu/AgentCore.git
node AgentCore/bin/agentcore-overlay.js init .
```

En un directorio específico:

```bash
npx -p git+https://github.com/QuantumEdu/AgentCore.git agentcore-overlay init apps/mi-proyecto
```

Sobrescribir archivos existentes (actualizar overlay):

```bash
npx -p git+https://github.com/QuantumEdu/AgentCore.git agentcore-overlay init . --force
```

Ver qué copiaría sin escribir nada:

```bash
npx -p git+https://github.com/QuantumEdu/AgentCore.git agentcore-overlay init sandbox --dry-run
```

> Próximamente: `npx agentcore-overlay init` (cuando el paquete esté en npm).

**Qué copia**: `ai/` (completo) + `AGENTS.md`. No copia README.md, FAQ.md ni CHANGELOG.md porque son docs del repositorio fuente, no del overlay operativo.

---

## Qué es AgentCore Overlay

Es una **capa portable** que se instala dentro de cualquier proyecto para sumar:

- **Governance**: puertas de entrada, mapas de flujo, quick-start por escenario
- **Skills**: capacidades operativas reutilizables (15 skills + workflow-builder)
- **Agents**: especialistas simples que componen skills (4 agents)
- **Templates**: briefs, ADRs, specs, roadmaps, retrospectivas (10 templates)
- **Context**: memoria local, decisiones, pitfalls, system-layers
- **AGENTS.md**: entrypoint operativo del overlay dentro del proyecto

No reemplaza a `gentle-ai`. gentle-ai orquesta; AgentCore Overlay aporta la guía y estructura portable.

### Naming Convention

Todas las skills usan el prefijo `sdd-govp:` (como `ospx:` en OpenSpec).

```
sdd-govp:brief-inception → sdd-govp:brief-to-prd → sdd-govp:prd-to-spec → sdd-govp:spec-to-tasks
```

---

## Flujo canónico

El pipeline completo para un proyecto con discovery desde cero:

```
sdd-govp:brief-inception → sdd-govp:brief-to-prd → sdd-govp:prd-to-spec → sdd-govp:spec-to-tasks
```

Cada skill produce el input de la siguiente:

1. **brief-inception** → brief clasificado con huecos detectados
2. **brief-to-prd** → PRD corto con decisiones y riesgos
3. **prd-to-spec** → spec verificable con escenarios y criterios de aceptación
4. **spec-to-tasks** → tareas ejecutables con dependencias y criterios de done

Después, según el escenario:

| Necesidad | Skill |
|-----------|-------|
| Revisar un cambio antes de integrar | `sdd-govp:change-review` |
| Migrar reglas sin romper producción | `sdd-govp:rule-migration-plan` |
| Agregar un endpoint nuevo | `sdd-govp:add-endpoint` |
| Error repetido o fricción recurrente | `sdd-govp:improvement-loop` |
| Continuidad sin Engram | `sdd-govp:project-memory-fallback` |
| Proyecto no-software (tesis, consultoría) | `sdd-govp:workflow-builder` |
| Retrospectiva post-cambio | `sdd-govp:local-retrospective` |
| Decidir stack técnico | `sdd-govp:project-stack-decider` |
| Mejorar prompts | `sdd-govp:prompt-improver` |
| Tono técnico/geek | `sdd-govp:geek-tech-tone` |
| Convenciones de código | `sdd-govp:coding-conventions` |

---

## Catálogo de Skills (16)

| Skill | Descripción |
|-------|-------------|
| `sdd-govp:add-endpoint` | Guía la adición segura de un endpoint nuevo: contrato, validación, reglas, pruebas y documentación mínima |
| `sdd-govp:brief-inception` | Usa PROJECT-BRIEF-FULL como motor de discovery inicial. Clasifica el proyecto, detecta huecos, hace hasta 7 preguntas críticas y propone el siguiente artefacto |
| `sdd-govp:brief-to-prd` | Convierte un brief canónico o parcial en un PRD corto, claro y profesional con decisiones iniciales y riesgos |
| `sdd-govp:change-review` | Revisa un cambio antes de integrarlo: riesgos de ruptura, drift de documentación, impactos operativos, huecos de validación |
| `sdd-govp:coding-conventions` | Resume prácticas de arquitectura, API, seguridad y testing como base de implementación o revisión |
| `sdd-govp:geek-tech-tone` | Ajusta respuestas a tono geek, técnico, profesional, proactivo y con pensamiento lateral |
| `sdd-govp:improvement-loop` | Captura errores repetidos, identifica causa raíz y propone regla/checklist/ajuste de flujo |
| `sdd-govp:local-retrospective` | Retrospectiva ligera: qué funcionó, qué falló, qué se repitió, qué ajustar |
| `sdd-govp:prd-to-spec` | Convierte un PRD en spec operativa y verificable con requisitos, escenarios y criterios de aceptación |
| `sdd-govp:project-memory-fallback` | Memoria local mínima basada en archivos cuando Engram no está disponible |
| `sdd-govp:project-stack-decider` | Ayuda a decidir stack y forma de entrega con trade-offs, supuestos y alternativas descartadas |
| `sdd-govp:prompt-improver` | Reestructura prompts con formato profesional, claro y reusable sin cambiar la intención original |
| `sdd-govp:rule-migration-plan` | Diseña migración segura de reglas en sistemas operativos: shadow mode, rollout gradual, rollback |
| `sdd-govp:spec-to-tasks` | Convierte una spec en tareas pequeñas, dependientes y ejecutables con orden y criterios de done |
| `sdd-govp:workflow-builder` | Crea workflows custom para cualquier tipo de proyecto no-software (tesis, consultoría, coaching, investigación). Incluye 4 templates predefinidos |

---

## Agentes (4)

| Agente | Skill que compone | Rol |
|--------|-------------------|-----|
| `change-reviewer` | `sdd-govp:change-review`, `sdd-govp:coding-conventions` | Revisa cambios con foco en riesgo de ruptura, drift y safeguards faltantes |
| `endpoint-designer` | `sdd-govp:add-endpoint`, `sdd-govp:change-review`, `sdd-govp:coding-conventions` | Aterriza endpoints nuevos con contrato, validación, pruebas y compatibilidad |
| `migration-guardian` | `sdd-govp:rule-migration-plan`, `sdd-govp:change-review`, `sdd-govp:project-memory-fallback` | Planea migraciones seguras de reglas o flujos en sistemas operativos |
| `project-inception-architect` | Ninguna directa — agente de discovery | Toma una idea difusa y la convierte en arranque ordenado con preguntas, criterios y siguiente artefacto |

---

## Estructura completa del overlay

```
ai/
├── agents/                  ← Agentes simples por rol (4)
│   ├── change-reviewer.md
│   ├── endpoint-designer.md
│   ├── migration-guardian.md
│   └── project-inception-architect.md
├── context/                 ← Contexto estable y memoria fallback local
│   ├── decisions.md         ←   Decisiones registradas
│   ├── migration-checklist.md
│   ├── pitfalls.md          ←   Gotchas y errores conocidos
│   ├── system-layers.md     ←   Mapa de capas del sistema
│   └── working-memory.md    ←   Memoria de trabajo activa
├── governance/              ← Puertas de entrada y mapas de flujo
│   ├── 00-start-here.md     ←   Punto de entrada
│   ├── 02-decision-gates.md
│   ├── 03-aidlc-lite.md
│   ├── 04-workflow-map.md   ←   Vista estructural por tipo de cambio
│   └── 05-quick-start-by-scenario.md  ←  Entrada por caso real
├── migration/               ← Material de transición histórica
├── schemas/                 ← Validación estructural
│   └── brief-schema.json
├── skills/                  ← Capacidades operativas reutilizables (16)
│   ├── add-endpoint/
│   ├── brief-inception/
│   ├── brief-to-prd/
│   ├── change-review/
│   ├── coding-conventions/
│   ├── geek-tech-tone/
│   ├── improvement-loop/
│   ├── local-retrospective/
│   ├── patterns/            ←   Patrones de diseño (no skills ejecutables)
│   ├── prd-to-spec/
│   ├── project-memory-fallback/
│   ├── project-stack-decider/
│   ├── prompt-improver/
│   ├── rule-migration-plan/
│   ├── spec-to-tasks/
│   └── workflow-builder/    ←   Skill + 4 templates de proyecto
│       └── assets/templates/
│           ├── thesis.yaml
│           ├── consulting.yaml
│           ├── pnl-coaching.yaml
│           └── career-coaching.yaml
└── templates/               ← Formatos para materializar outputs (10)
    ├── PROJECT-BRIEF-FULL.yaml
    ├── PROJECT-BRIEF-LITE.yaml
    ├── change-review-template.md
    ├── decision-adr-template.md
    ├── prompt-structures.md
    ├── retrospective-template.md
    ├── roadmap-template.md
    ├── rule-migration-template.md
    ├── spec-template.md
    └── tasks-template.md
```

---

## Casos de uso

### Proyecto nuevo con discovery

```bash
npx agentcore-overlay init
# leer AGENTS.md, luego ai/README.md
# arrancar con brief-inception
```

`sdd-govp:brief-inception` → `sdd-govp:brief-to-prd` → `sdd-govp:prd-to-spec` → `sdd-govp:spec-to-tasks`

### Cambio sensible en sistema existente

`sdd-govp:change-review` → `sdd-govp:rule-migration-plan` (si reemplaza reglas)

### Agregar endpoint

`sdd-govp:add-endpoint` → `sdd-govp:change-review`

### Error repetitivo

`sdd-govp:improvement-loop` → `sdd-govp:local-retrospective`

### Sin Engram

`sdd-govp:project-memory-fallback` (decisions.md, pitfalls.md, working-memory.md)

### Proyecto no-software (tesis, consultoría, coaching)

```bash
sdd-govp:workflow-builder
# elegir template o definir flujo custom
# ejecutar con /workflow continue
```

---

## Templates disponibles (10)

| Template | Uso |
|----------|-----|
| `PROJECT-BRIEF-FULL.yaml` | Brief completo para proyectos serios o complejos |
| `PROJECT-BRIEF-LITE.yaml` | Brief corto para proyectos pequeños o exploratorios |
| `change-review-template.md` | Estructura para revisión de cambio |
| `decision-adr-template.md` | Formato ADR para decisiones arquitectónicas |
| `prompt-structures.md` | Estructuras de prompt reusables |
| `retrospective-template.md` | Guía para retrospectiva post-cambio |
| `roadmap-template.md` | Formato de roadmap |
| `rule-migration-template.md` | Plan de migración de reglas |
| `spec-template.md` | Template de spec operativa |
| `tasks-template.md` | Template de breakdown de tareas |

---

## Desarrollo local

```bash
node bin/agentcore-overlay.js --help
node bin/agentcore-overlay.js init . --force --dry-run
```

---

## Licencia

MIT
