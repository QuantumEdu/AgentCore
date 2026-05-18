# Agent Core v3 Publish Checklist

## Goal

Usar este repo como fuente para completar profesionalmente la evolución hacia `agent-core-v3`.

## Before publishing to v3

- [ ] Confirm the boundary model: runtime vs global core vs local overlay
- [ ] Move only reusable skills/assets to v3
- [ ] Keep local governance and repo-specific docs in `/ai`
- [ ] Normalize names between local and global skills
- [ ] Ensure templates referenced by exported skills exist in v3
- [ ] Decide whether utility skills (`geek-tech-tone`, `prompt-improver`) belong in core or optional tier
- [ ] Add README guidance in v3 explaining what remains local by design

## Recommended migration sequence

1. Export flow-bridge skills:
   - `brief-inception`
   - `brief-to-prd`
   - `prd-to-spec`
   - `spec-to-tasks`
2. Export templates required by those skills
3. Export `add-endpoint`, `project-stack-decider`, `coding-conventions`
4. Keep `/ai/governance/*` local unless a generic version is created intentionally
5. Update `agent-core-v3` README to explain the local overlay pattern

## Final criterion

The migration is complete only when:

- `agent-core-v3` covers the reusable core intentionally
- `/ai` is explicitly documented as the local overlay
- the two no longer compete or overlap ambiguously
