# .claude/PORTABILITY.md
# Portability Guide - AgentCore Template v1.3

**VERSION**: 1.3
**DATE**: 2026-04-05
**CURRENT PROJECT**: FlowTask Inc. - Task Management Platform

---

## Purpose

This template provides a `.claude/` infrastructure that **PREVENTS common omissions** such as:

- Using bcrypt when argon2id was specified
- Using pip when uv was specified
- Ignoring architecture rules
- Not reading stack_config.json before implementing

---

## Files That MUST BE ADAPTED per Project

When reusing this template in a new project, the following files **MUST** be modified:

### Always Adapt (project-specific)

| File | What to Change |
|------|---------------|
| `stack_config.json` | Name, type, scale, tables, enums, roles, terminology, business rules |
| `rules/architecture.rules` | Project name, directory structure, domain models, schemas, endpoints |
| `rules/database.rules` | Project name, tables, relationships, enums, naming conventions, specific decisions |
| `rules/security.rules` | Project name, roles (UserRole enum), permission matrix, protected endpoints |
| `rules/api-design.rules` | Project name, endpoints, schemas, request/response examples |
| `rules/testing.rules` | Project name, test structure, fixtures, test examples |
| `rules/discovery.rules` | Project name, stack and decision examples |
| `memory/decision_log.json` | Reset with new project decisions |
| `memory/audit_log.md` | Reset with new project name |
| `memory/backlog/roadmap.md` | Rewrite with new project milestones |
| `AGENT_GUIDE.md` | Project name, specific roles if they change |

### Generally Reusable (minimal changes)

| File | What to Review |
|------|---------------|
| `MANDATORY_CHECKS.md` | Only verify compatibility tables apply |
| `PORTABILITY.md` | Update version, date, project name |
| `validators/check_stack.py` | Works if stack_config.json is configured correctly |
| `validators/check_dependencies.py` | Same |

### Reusable Without Changes

| File | Reason |
|------|--------|
| `agents/architect.agent` | Generic validation logic |
| `agents/backend-developer.agent` | Dynamically reads stack_config.json |
| `agents/security-expert.agent` | Generic stack enforcement |
| `swarms/discovery_swarm.yaml` | Generic workflow |
| `swarms/agile_cycle.yaml` | Generic workflow |
| `swarms/create-module.yaml` | Generic template |
| `swarms/add-endpoint.yaml` | Generic template |
| `swarms/write-tests.yaml` | Generic template |
| `swarms/kaizen_improvement.yaml` | Generic workflow |

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
