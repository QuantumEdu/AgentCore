# Repo Publication Map

## Purpose

Definir exactamente qué debe salir de este repositorio hacia `sdd-govplan`, qué debe salir hacia `agent-core-v3`, qué debe quedarse local, y qué no debería publicarse.

## Source repository

Este repo (`agentcore_publish`) funciona como:

- fuente local de consolidación;
- overlay operativo de `/ai`;
- base maestra temporal para cerrar lo inconcluso;
- punto de decisión antes de publicar a otros repos.

---

## A. Publish to `sdd-govplan`

### Role of `sdd-govplan`

Debe convertirse en el **repo maestro de gobernanza y flujo**.

Ahí debe vivir la narrativa principal, el flujo integral y los artefactos canónicos del proceso.

### Publish as canonical docs

| Source in this repo | Suggested target in `sdd-govplan` | Why |
|---|---|---|
| `README.md` | `README.md` | Debe explicar la visión integral, evolución y propósito del sistema maestro |
| `AGENTS.md` | `AGENTS.md` or equivalent root guidance | Entry point operativo del repo maestro |
| `ai/README.md` | `docs/ai-layer.md` or merge into README | Explica el overlay local y la relación entre capas |
| `ai/context/system-boundaries.md` | `docs/system-boundaries.md` | Cierra la frontera entre runtime, core reusable y overlay local |
| `ai/migration/sdd-govplan-master-plan.md` | `docs/master-plan.md` | Explica el rol de `sdd-govplan` como repo maestro |

### Publish as governance layer

| Source in this repo | Suggested target in `sdd-govplan` |
|---|---|
| `ai/governance/00-start-here.md` | `governance/00-start-here.md` |
| `ai/governance/02-decision-gates.md` | `governance/02-decision-gates.md` |
| `ai/governance/03-aidlc-lite.md` | `governance/03-aidlc-lite.md` |
| `ai/governance/04-workflow-map.md` | `governance/04-workflow-map.md` |
| `ai/governance/05-quick-start-by-scenario.md` | `governance/05-quick-start-by-scenario.md` |

### Publish as core process skills

| Source in this repo | Suggested target in `sdd-govplan` |
|---|---|
| `ai/skills/brief-inception/SKILL.md` | `skills/brief-inception/SKILL.md` |
| `ai/skills/brief-to-prd/SKILL.md` | `skills/brief-to-prd/SKILL.md` |
| `ai/skills/prd-to-spec/SKILL.md` | `skills/prd-to-spec/SKILL.md` |
| `ai/skills/spec-to-tasks/SKILL.md` | `skills/spec-to-tasks/SKILL.md` |
| `ai/skills/change-review/SKILL.md` | `skills/change-review/SKILL.md` |
| `ai/skills/rule-migration-plan/SKILL.md` | `skills/rule-migration-plan/SKILL.md` |
| `ai/skills/improvement-loop/SKILL.md` | `skills/improvement-loop/SKILL.md` |
| `ai/skills/local-retrospective/SKILL.md` | `skills/local-retrospective/SKILL.md` |
| `ai/skills/project-memory-fallback/SKILL.md` | `skills/project-memory-fallback/SKILL.md` |
| `ai/skills/project-stack-decider/SKILL.md` | `skills/project-stack-decider/SKILL.md` |
| `ai/skills/add-endpoint/SKILL.md` | `skills/add-endpoint/SKILL.md` |
| `ai/skills/coding-conventions/SKILL.md` | `skills/coding-conventions/SKILL.md` |
| `ai/skills/prompt-improver/SKILL.md` | `skills/prompt-improver/SKILL.md` |
| `ai/skills/geek-tech-tone/SKILL.md` | `skills/geek-tech-tone/SKILL.md` *(optional utility tier)* |

### Publish as canonical templates

| Source in this repo | Suggested target in `sdd-govplan` |
|---|---|
| `ai/templates/PROJECT-BRIEF-FULL.yaml` | `templates/PROJECT-BRIEF-FULL.yaml` |
| `ai/templates/PROJECT-BRIEF-LITE.yaml` | `templates/PROJECT-BRIEF-LITE.yaml` |
| `ai/templates/spec-template.md` | `templates/spec-template.md` |
| `ai/templates/tasks-template.md` | `templates/tasks-template.md` |
| `ai/templates/change-review-template.md` | `templates/change-review-template.md` |
| `ai/templates/retrospective-template.md` | `templates/retrospective-template.md` |
| `ai/templates/rule-migration-template.md` | `templates/rule-migration-template.md` |
| `ai/templates/decision-adr-template.md` | `templates/decision-adr-template.md` |
| `ai/templates/roadmap-template.md` | `templates/roadmap-template.md` |

### Publish as reference assets

| Source in this repo | Suggested target in `sdd-govplan` |
|---|---|
| `ai/skills/patterns/*` | `reference/patterns/*` or `skills/patterns/*` with README |

### Optional local wrappers to include only if the repo wants role helpers

| Source in this repo | Suggested target |
|---|---|
| `ai/agents/project-inception-architect.md` | `agents/project-inception-architect.md` |
| `ai/agents/change-reviewer.md` | `agents/change-reviewer.md` |
| `ai/agents/migration-guardian.md` | `agents/migration-guardian.md` |
| `ai/agents/endpoint-designer.md` | `agents/endpoint-designer.md` |

---

## B. Publish to `agent-core-v3`

### Role of `agent-core-v3`

Debe ser el **core reusable e instalable**.

Solo debe recibir lo que tenga sentido como asset global multi-tool.

### Publish as global skills

| Source in this repo | Suggested target in `agent-core-v3` | Publish? |
|---|---|---|
| `ai/skills/brief-inception/SKILL.md` | `skills/brief-inception/SKILL.md` | Yes |
| `ai/skills/brief-to-prd/SKILL.md` | `skills/brief-to-prd/SKILL.md` | Yes |
| `ai/skills/prd-to-spec/SKILL.md` | `skills/prd-to-spec/SKILL.md` | Yes |
| `ai/skills/spec-to-tasks/SKILL.md` | `skills/spec-to-tasks/SKILL.md` | Yes |
| `ai/skills/change-review/SKILL.md` | `skills/change-review/SKILL.md` | Already aligned, update if needed |
| `ai/skills/rule-migration-plan/SKILL.md` | `skills/rule-migration/SKILL.md` or align naming | Yes |
| `ai/skills/improvement-loop/SKILL.md` | `skills/improvement-loop/SKILL.md` | Already aligned, update if needed |
| `ai/skills/project-memory-fallback/SKILL.md` | `skills/memory-fallback/SKILL.md` or align naming | Yes |
| `ai/skills/local-retrospective/SKILL.md` | `skills/local-retrospective/SKILL.md` | Already aligned, update if needed |
| `ai/skills/project-stack-decider/SKILL.md` | `skills/project-stack-decider/SKILL.md` | Yes |
| `ai/skills/add-endpoint/SKILL.md` | `skills/add-endpoint/SKILL.md` | Yes |
| `ai/skills/coding-conventions/SKILL.md` | `skills/coding-conventions/SKILL.md` | Yes |
| `ai/skills/prompt-improver/SKILL.md` | `skills/prompt-improver/SKILL.md` | Optional |
| `ai/skills/geek-tech-tone/SKILL.md` | `skills/geek-tech-tone/SKILL.md` | Optional |

### Publish as global templates/assets

| Source in this repo | Suggested target in `agent-core-v3` |
|---|---|
| `ai/templates/PROJECT-BRIEF-FULL.yaml` | `skills/sdd-govplan/assets/project-brief-full.yaml` or equivalent |
| `ai/templates/PROJECT-BRIEF-LITE.yaml` | `skills/sdd-govplan/assets/project-brief-lite.yaml` or equivalent |
| `ai/templates/spec-template.md` | `skills/prd-to-spec/assets/spec-template.md` |
| `ai/templates/tasks-template.md` | `skills/spec-to-tasks/assets/tasks-template.md` |
| `ai/templates/change-review-template.md` | `skills/change-review/assets/change-review-template.md` |
| `ai/templates/retrospective-template.md` | `skills/local-retrospective/assets/retrospective-template.md` |
| `ai/templates/rule-migration-template.md` | `skills/rule-migration/assets/rule-migration-template.md` |
| `ai/templates/decision-adr-template.md` | `skills/sdd-govplan/assets/decision-adr-template.md` |
| `ai/templates/roadmap-template.md` | `skills/sdd-govplan/assets/roadmap-template.md` |

### Publish as global docs

| Source in this repo | Suggested target |
|---|---|
| parts of `README.md` about boundaries and incomplete evolution | `README.md` sections in `agent-core-v3` |
| `ai/migration/ai-docs-site-separate-pr-plan.md` *(concept only)* | not copied as-is; use as planning input |

---

## C. Keep only local in project overlays

These should remain repo-local and should **not** be blindly published to `agent-core-v3`:

| Keep local | Why |
|---|---|
| `ai/README.md` | Onboarding of the local repo |
| `ai/governance/04-workflow-map.md` | Local routing for this repo |
| `ai/governance/05-quick-start-by-scenario.md` | Local operating guide |
| `ai/context/decisions.md` | Local project decisions |
| `ai/context/pitfalls.md` | Local project pitfalls |
| `ai/context/working-memory.md` | Local short-term context |
| `notes.md` | Internal note, not canonical public artifact |

---

## D. Do not publish directly

| Artifact | Action |
|---|---|
| `.atl/` | Keep ignored locally |
| `.pi/` | Keep ignored locally |
| `agentcore-y-sdd.md` | Keep private or archive intentionally |
| `ai-docs-site/` | Separate PR / separate publication decision |
| historical backup / legacy material | Do not copy blindly into the new master repos |

---

## Recommended publication order

### Phase 1 — `sdd-govplan`
1. Rebuild README as master narrative
2. Add governance docs
3. Add full/lite briefs and canonical templates
4. Add flow-bridge skills (`brief → PRD → spec → tasks`)
5. Add boundary docs

### Phase 2 — `agent-core-v3`
1. Export reusable skills
2. Export reusable templates/assets
3. Align naming (`rule-migration-plan` vs `rule-migration`, `project-memory-fallback` vs `memory-fallback`)
4. Update npm-facing README

### Phase 3 — local overlays
1. Keep `/ai` lean per project
2. Keep local routing and context docs
3. Add only project-specific wrappers and state

---

## Final rule

- `sdd-govplan` = master governance narrative and flow
- `agent-core-v3` = master reusable distribution
- local `/ai` = master project adaptation layer
