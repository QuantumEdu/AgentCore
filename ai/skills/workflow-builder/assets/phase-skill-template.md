---
name: "sdd-govp:{phase-slug}"
description: "Trigger: /workflow continue or phase {phase-name}. {phase-description}"
disable-model-invocation: true
user-invocable: false
license: MIT
metadata:
  author: workflow-builder
  version: "1.0"
  delegate_only: true
---

> **ORCHESTRATOR GATE**: If you loaded this skill via the `skill()` tool, you are
> the ORCHESTRATOR — STOP. This skill defines ONE PHASE of the workflow
> `{workflow-name}`. You execute it, update progress, and move to the next phase.

## Phase: {phase-name}

**Workflow**: {workflow-name}
**Phase ID**: {phase-id}
**Depends on**: {phase-dependencies}

### Purpose

{phase-description}

### What to Do

1. Review outputs from previous phases (if any):
   {previous-outputs-list}

2. Execute the phase activities:
   - {activity 1}
   - {activity 2}
   - {activity 3}

3. Generate the following outputs:
   {outputs-list}

4. Verify completion criteria:
   {completion-list}

### Expected Outputs

- {output-file-1} — {description}
- {output-file-2} — {description}

### Completion Criteria

All of the following MUST be true before marking this phase complete:
- [ ] {criterion 1}
- [ ] {criterion 2}
- [ ] All output files exist and are populated

### On Completion

Update `.agent/skills/{workflow-name}/progress.yaml`:
- Set this phase status to `completed`
- Record completion timestamp
- List generated artifact paths

Then tell the user:
*"Fase {phase-name} completada. Ejecutá `/workflow continue` para la siguiente fase."*

### Next Phase

{next-phase-name}: {next-phase-description}

### Previous Phase

{prev-phase-name}: {prev-phase-description}
