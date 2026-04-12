# .claude/PORTABILITY.md
# Portability Guide - AgentCore Template v1.3

**VERSION**: 2.0
**DATE**: 2026-04-12
**CURRENT PROJECT**: AgentCore v2.0 - Multi-Stack Agent System

---

## Purpose

This template provides a `.claude/` infrastructure that **PREVENTS common omissions** such as:

- Using bcrypt when argon2id was specified
- Using pip when uv was specified
- Ignoring architecture rules
- Not reading stack_config.json before implementing

---

## Files That MUST BE ADAPTED

| File | What to change |
|------|---------------|
| `.claude/stacks/{stack}/config.yaml` | EVERYTHING stack-specific |
| `.claude/stacks/{stack}/decisions.yaml` | Technical decisions with rationale |
| `.claude/stacks/{stack}/patterns.md` | Code patterns with examples |
| `.claude/stacks/{stack}/modules/*.yaml` | Domain-specific modules (auth, database, etc.) |
| `.claude/stacks/{stack}/prd_skill.md` | Update with domain-specific details |
| `.claude/memory/decision_log.md` | Reset with your decisions |
| `.claude/memory/audit_log.md` | Reset with your project name |
| `.claude/memory/backlog/roadmap.md` | Rewrite for your milestones |
| `AGENT_GUIDE.md` | Update for your project |
| `MANDATORY_CHECKS.md` | Update for your project |
| `PROJECT-BRIEF-FULL.yaml` | Fill with your project details |

### Generally Reusable (minimal changes)

| File | What to Review |
|------|---------------|
| `rules/architecture.rules` | Update project name and domain models |
| `rules/database.rules` | Update table names and relationships |
| `rules/security.rules` | Update roles and permissions |
| `rules/api-design.rules` | Update endpoints and schemas |
| `rules/testing.rules` | Update fixtures and test examples |
| `PORTABILITY.md` | Update version, date, project name |

### Files You Can Reuse Unchanged

| File | Why |
|------|-----|
| `.claude/stacks/template.yaml` | Generic template for new stacks |
| `.claude/stacks/registry.yaml` | Registry of all available stacks |
| `.agent/skills/brief-to-prd/SKILL.md` | Generic PRD generator (stack-agnostic) |
| `.agent/skills/stack-generator/SKILL.md` | Generic config generator (multi-stack) |
| `.claude/rules/patterns/*` | Reusable patterns (hexagonal, SOLID, design, testing) |
| `.claude/scripts/*` | Utility scripts (stack-agnostic) |
| `.claude/templates/*` | Reusable templates (Brief, ADR, roadmap) |

---

## Stack Configuration

AgentCore v2.0 uses a dynamic stack configuration system:

### Single stack_config.yml

Instead of multiple stack-specific files, v2.0 uses a single `stack_config.yml` that:
- References the selected stack from `.claude/stacks/{stack}/`
- Contains project-specific overrides
- Is auto-generated from `PROJECT-BRIEF-FULL.yaml`

### Stack Selection

To select a stack:
1. Fill `PROJECT-BRIEF-FULL.yaml` with your `stack_principal`
2. Run: `python .claude/scripts/stack_selector.py`
3. Or use the `brief-to-prd` skill (auto-detects from Brief)

### Multi-Stack Projects

For projects that need multiple stacks (e.g., web + desktop):
1. Create multiple `PROJECT-BRIEF-FULL-{stack}.yaml` files
2. Generate separate PRDs and configs for each
3. Use branch strategies or monorepo to manage both

---

## File Path Rule

**MANDATORY in v1.3**: Every file must contain its full path as a comment on the first line.

| File Type | Comment Format |
|-----------|---------------|
| `.py` | `# app/main.py` |
| `.html` | `<!-- app/templates/index.html -->` |
| `.yaml` | `# .claude/swarms/create-module.yaml` |
| `.css` | `/* app/static/css/main.css */` |
| `.js` | `// app/static/js/main.js` |
| `.md` | First line: `# path/to/file.md` (as title) |
| `.rules` | `# .claude/rules/name.rules` |
| `.json` | `"_filepath": ".claude/stack_config.json"` (first key) |
| `.agent` | `# .claude/agents/name.agent` |

---

## Step by Step: Using in a New Project

### 1. Copy Template

```bash
cp -r agentcore/.claude /path/to/new-project/.claude
```

### 2. Configure stack_config.json

Edit `.claude/stack_config.json`:
- `project.name`, `project.type`, `project.description`
- `database.type`, `database.tables`, `database.enums`, `database.terminology`
- `auth.roles`
- `business_rules`

### 3. Adapt Rules

Edit each file in `.claude/rules/`:
- Change project name in title and footer
- Update models, schemas, endpoints with new project domain
- Update roles and permissions
- Update code examples

### 4. Clear Memory

```bash
cd new-project/.claude/memory

# Reset decision_log.json
echo '{"_filepath": ".claude/memory/decision_log.json", "project_name": "New Project", "decisions": []}' > decision_log.json

# Reset audit_log.md
echo "# .claude/memory/audit_log.md" > audit_log.md

# Clear backlog
rm -rf backlog/*
```

### 5. Run Validator

```bash
python .claude/validators/check_stack.py
```

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-01-20 | Initial basic template |
| 2.0 | 2026-01-25 | Automatic validators, MANDATORY_CHECKS, detailed stack_config |
| 1.3 | 2026-02-10 | File path rule, project adaptation table |

---

## Current Adaptation: FlowTask Inc.

### Project Decisions

| Aspect | Decision |
|--------|----------|
| Database | SQLite (this version) |
| Table naming | English snake_case plural, no prefix (users, projects, tasks) |
| Financial terminology | budget_used / budget_allocated / budget_remaining |
| Task categories | FEATURE, BUG, CHORE, DOCS, TEST, INFRA, DESIGN, OTHER |
| Roles | ADMIN, MEMBER, VIEWER |
| Budget allocation | Field on project + entry as activity_log record |
| Append-only tables | activity_logs, event_logs |
| Immutable after close | sprints (once closed) |

### Adapted Files

- [x] `stack_config.json` — Project, tables, enums, roles, business rules
- [x] `rules/architecture.rules` — Task management domain models, domain structure
- [x] `rules/database.rules` — English tables, task management relationships
- [x] `rules/security.rules` — Roles ADMIN/MEMBER/VIEWER, permission matrix
- [x] `rules/api-design.rules` — Task management endpoints
- [x] `rules/testing.rules` — Fixtures and tests for task management domain
- [x] `rules/discovery.rules` — Project context
- [x] `memory/decision_log.json` — Initial decisions
- [x] `memory/audit_log.md` — Change log
- [x] `memory/backlog/roadmap.md` — 10-phase roadmap
- [x] `AGENT_GUIDE.md` — Updated roles
- [x] `MANDATORY_CHECKS.md` — Updated verifications
