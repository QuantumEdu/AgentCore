---
name: sdd-govp:workflow-builder
description: "Trigger: /workflow-builder or sdd-govp:workflow-builder or workflow, project workflow, flujo de trabajo, workflow builder. Create custom workflows for ANY project type — thesis, consulting, coaching, research, etc. Generates phase skills dynamically."
disable-model-invocation: true
user-invocable: false
license: MIT
metadata:
  author: gentleman-programming
  version: "1.0"
  delegate_only: true
---

> **ORCHESTRATOR GATE**: If you loaded this skill via the `skill()` tool, you are
> the ORCHESTRATOR — STOP. This skill defines how YOU build and run custom
> workflows for non-software projects. You drive the interview, generate phase
> skills, and execute them sequentially.

## Purpose

`workflow-builder` creates **custom project workflows** for ANY type of project
— not just software. Thesis research, ISO 27001 consulting, NLP coaching, career
planning, investigative journalism — any multi-phase workflow.

It works in three phases:

```
Phase 1: Interview → Phase 2: Generate → Phase 3: Execute
```

Unlike SDD (which has a fixed pipeline for software), `workflow-builder` lets
the user define their own pipeline, and generates a SKILL.md for each phase.

## When to Invoke

| Trigger | Action |
|---------|--------|
| User says `/workflow-builder` or `sdd-govp:workflow-builder` | Start interview to define a new project workflow |
| User says `/workflow-builder "Tesis sobre IA"` | Start with project name pre-filled |
| User says `/workflow` | Alias, same as above |
| User says `/workflow continue` | Execute the next pending phase in the current workflow |
| User says `/workflow status` | Show current workflow progress |
| User describes a non-software project | Suggest `/workflow-builder` |
| User starts describing a thesis/consulting/coaching | Suggest `/workflow-builder` |

## Built-in Workflow Templates

These are pre-defined workflows stored in `assets/templates/`. When the user
chooses a known project type, load the template and let them customize it.

| Project Type | Phases | Template File |
|-------------|--------|---------------|
| **Thesis / Academic Research** | 8: problema → objetivos → justificación → marco teórico → metodología → análisis → redacción APA → referencias | `assets/templates/thesis.yaml` |
| **Consulting (ISO 27001, etc.)** | 6: diagnóstico → plan de acción → implementación → evaluación → mejora continua → cierre | `assets/templates/consulting.yaml` |
| **PNL Coaching** | 5: línea base → objetivos → ejercicios → seguimiento → evaluación | `assets/templates/pnl-coaching.yaml` |
| **Career Coaching** | 5: autoevaluación → exploración → plan de carrera → ejecución → revisión | `assets/templates/career-coaching.yaml` |
| **Custom** | User defines each phase | No template — interview generates it |

## Workflow Builder Flow

### Phase 0: Detect Project Root

Detect the project working directory. The workflow and generated skills will
live in `.agent/skills/{workflow-name}/` under this directory.

### Phase 1: Project Type Interview (YOU — inline)

Ask ONE question at a time. Determine:

1. **Project name** — short kebab-case name (e.g., `tesis-ia-educacion`, `consultoria-iso-27001`, `pnl-coaching-2026`)

2. **Project type** — is it one of the known types or something else?
   Known: thesis, consulting, pnl-coaching, career-coaching.

3. **If known type**: Load the template from `assets/templates/{type}.yaml`, show the phases to the user, and ask: *"Este flujo tiene {N} fases. ¿Querés agregar, quitar, renombrar o reordenar alguna?"*

4. **If custom or unknown**: Ask: *"¿Conocés el flujo de trabajo o querés que investigue?"*
   - **If user knows the flow**: Ask them to describe each phase (same as before).
   - **If user doesn't know the flow**: ENTER RESEARCH MODE (see below).

5. **Ask about execution mode**:
   - *"¿Querés que ejecute las fases una por una (interactivo) o que genere todas las skills primero y las ejecutamos después?"*

#### Research Mode (for unknown workflows)

When the user doesn't know the flow, investigate and propose one:

**Step A — Gather context**:
Ask questions to understand the domain:
- *"¿Cuál es el objetivo principal del proyecto?"*
- *"¿Hay algún estándar, metodología o marco de trabajo que deberíamos considerar? (ISO, PMI, Scrum, Design Thinking, PDCA, etc.)"*
- *"¿Qué entregables o resultados esperás obtener al final?"*
- *"¿Hay algún documento, libro o referencia que describa el proceso ideal?"*

**Step B — Research** (use websearch + model knowledge):
- Search for methodologies, standards, and workflows related to the domain
- Examples of research queries:
  - "ISO 27001 implementation methodology phases" → gap analysis, risk assessment, control selection, etc.
  - "Design Thinking process steps" → empathize, define, ideate, prototype, test
  - "metodología de estudio de mercado fases" → exploración, segmentación, encuesta, análisis
  - "Lean Startup methodology phases" → build-measure-learn cycle
  - "Scientific research methodology steps" → problem, hypothesis, experiment, analysis, conclusion
  - "Six Sigma DMAIC phases" → define, measure, analyze, improve, control

**Step C — Synthesize a proposal**:
Based on research + model knowledge, propose a structured workflow:

```markdown
Basado en lo que investigué sobre {metodología/estándar/enfoque},
te propongo el siguiente flujo de {N} fases:

1. {Fase 1} — {descripción breve}
2. {Fase 2} — {descripción breve}
...
```

If you find multiple valid approaches, present options:
*"Encontré dos enfoques posibles: {opción A} y {opción B}. ¿Cuál se acerca más a lo que necesitás?"*

**Step D — Validate with the user**:
- *"¿Este flujo se ajusta a lo que necesitás?"*
- User can: accept, adjust (add/remove/reorder phases), or reject and describe manually
- If user adjusts, incorporate feedback immediately
- If user rejects, fall back to manual phase description

**Step E — Confirm and proceed**:
Once validated, the workflow is ready for generation. Show the summary and ask for final confirmation.

Show a summary before generating:
```
╔══════════════════════════════════════════╗
║  Proyecto: tesis-ia-educacion           ║
║  Tipo: Thesis / Academic Research       ║
║  Fases: 8                               ║
║  1. Determinación del problema          ║
║  2. Objetivos de investigación          ║
║  3. Justificación                       ║
║  4. Marco teórico                       ║
║  5. Metodología                         ║
║  6. Análisis de resultados              ║
║  7. Redacción (formato APA)             ║
║  8. Revisión de referencias             ║
║                                         ║
║  ¿Confirmás este flujo? (s/n/ajustar)   ║
╚══════════════════════════════════════════╝
```

### Phase 2: Generate Workflow + Skills (write files)

**Step 2a — Create workflow definition**: Write `.agent/skills/{workflow-name}/workflow.yaml`:

```yaml
# .agent/skills/{workflow-name}/workflow.yaml
# Auto-generated by workflow-builder

workflow:
  name: "{workflow-name}"
  type: "{project-type}"
  created: "{YYYY-MM-DD}"

phases:
  - id: "001"
    name: "{Phase name}"
    skill: "phase-001-{slug}"
    description: "{What this phase does}"
    outputs:
      - "{output-file-1}"
      - "{output-file-2}"
    completion_criteria:
      - "{criterion 1}"
      - "{criterion 2}"
    depends_on: []  # IDs of phases that must complete first

  - id: "002"
    name: "{Next phase}"
    skill: "phase-002-{slug}"
    description: "..."
    outputs: []
    completion_criteria: []
    depends_on: ["001"]
```

**Step 2b — Create phase skills**: For EACH phase, create a SKILL.md file in
`.agent/skills/{workflow-name}/phase-{id}-{slug}.SKILL.md`.

Use the template in `assets/phase-skill-template.md`. Fill in:
- `{phase-name}` → the phase name
- `{phase-description}` → what this phase does
- `{phase-outputs}` → expected outputs
- `{phase-completion}` → completion criteria
- `{workflow-name}` → the project workflow name
- `{next-phase}` → the next phase name (for the "Next" section)
- `{prev-phase}` → the previous phase name

**Step 2c — Create progress tracker**: Write `.agent/skills/{workflow-name}/progress.yaml`:

```yaml
# .agent/skills/{workflow-name}/progress.yaml
workflow: "{workflow-name}"
created: "{YYYY-MM-DD}"
current_phase: 0  # 0-based index
total_phases: {N}
phases:
  - id: "001"
    name: "{Phase 1}"
    status: "pending"  # pending | in_progress | completed | skipped
    completed_at: null
    artifacts: []
  - id: "002"
    name: "{Phase 2}"
    status: "pending"
    completed_at: null
    artifacts: []
```

**All modes**: Write files to the filesystem. Engram/openspec modes don't change
this — workflow skills are filesystem artifacts.

### Phase 3: Execute Workflow

Tell the user how to run the workflow:

```
"Workflow generado. Tenés las skills de cada fase en:
  .agent/skills/{workflow-name}/

Para empezar la primera fase:
  /workflow continue

Esto carga la skill de la Fase 1 y la ejecuta.
Cuando termines esa fase, volvé a ejecutar /workflow continue
para la siguiente.
"
```

**When `/workflow continue` is called**:

1. Read `.agent/skills/{workflow-name}/progress.yaml`
2. Find the first phase with `status: "pending"`
3. Load the phase skill via `skill("phase-{id}-{slug}")`
4. Add to the sub-agent prompt: `"PREVIOUS PHASE OUTPUTS: {list artifacts from completed phases}"`
5. After execution completes, update `progress.yaml`:
   - Set phase status to `completed`
   - Record completion timestamp
   - List generated artifacts
6. If next phase exists, show: *"Fase {N}/{total} completada. ¿Siguiente? (/workflow continue)"*
7. If all phases done, show: *"¡Workflow completo! Todas las {N} fases fueron ejecutadas."*

## Rules

- ALWAYS create the `.agent/skills/{workflow-name}/` directory on the filesystem
- ALWAYS generate `workflow.yaml` and `progress.yaml`
- Each phase skill file MUST have a unique name (`phase-{id}-{slug}.SKILL.md`)
- Phase skill files MUST include ORCHESTRATOR GATE instructions (use `assets/phase-skill-template.md`)
- Phase skills MUST include the `depends_on` from `workflow.yaml` as a section
- Use kebab-case for workflow names and slugs
- Validate that generated workflow paths don't overwrite existing projects — append `-2` if needed
- If workflow already exists with phases in progress, ASK: "Ya existe un workflow en progreso. ¿Continuar, reiniciar o crear nuevo?"
- `/workflow continue` checks `progress.yaml` — if no workflow exists, show error with instructions
- Generate NO MORE than 12 phases per workflow (practical limit)
- Each phase skill should be 50-150 lines — focused, not bloated
- Return envelope per **Section D** from `skills/_shared/sdd-phase-common.md`

## Output Contract

```markdown
**Status**: success | partial | blocked
**Summary**: Workflow "{name}" created with {N} phases. Skills generated for each phase.
**Artifacts**:
  - .agent/skills/{workflow-name}/workflow.yaml
  - .agent/skills/{workflow-name}/progress.yaml
  - .agent/skills/{workflow-name}/phase-001-{slug}.SKILL.md
  - .agent/skills/{workflow-name}/phase-002-{slug}.SKILL.md
  - ...
**Next Step**: /workflow continue — to start Phase 1: {phase-1-name}
**Risks**: {risks, or "None"}
**Skill Resolution**: injected | fallback-registry | fallback-path | none
```

## References

- `assets/templates/thesis.yaml` — Thesis workflow template (8 phases)
- `assets/templates/consulting.yaml` — Consulting workflow template (6 phases)
- `assets/templates/pnl-coaching.yaml` — PNL Coaching workflow template (5 phases)
- `assets/templates/career-coaching.yaml` — Career Coaching template (5 phases)
- `assets/phase-skill-template.md` — Template for generating individual phase skills
- `skills/_shared/sdd-phase-common.md` — Common return envelope + persistence
