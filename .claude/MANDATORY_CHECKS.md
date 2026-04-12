# .claude/MANDATORY_CHECKS.md
# MANDATORY CHECKS - READ BEFORE ANY IMPLEMENTATION

## CRITICAL WARNING

This file MUST be read by ANY agent or user BEFORE:
- Writing code
- Installing dependencies
- Creating configuration files
- Implementing features

**SKIPPING THESE CHECKS RESULTS IN CODE INCONSISTENT WITH THE DEFINED STACK**

---

## STEP 0: Verificación de Stack

- [ ] Existe `.claude/stack_config.yml`?
  - Si NO: Ejecuta `python .claude/scripts/stack_selector.py`
- [ ] ¿El stack en `stack_config.yml` coincide con tus necesidades?
  - Si NO: Ejecuta `python .claude/scripts/stack_selector.py` para cambiarlo
- [ ] Existe `.claude/stacks/{stack}/config.yaml`?
  - Si NO: El stack no está configurado correctamente, revisa la instalación

---

## STEP 1: File Path Header (REQUIRED v1.3)

**Every file created MUST contain its full path as a comment on the first line.**

| Type | Format |
|------|--------|
| `.py` | `# app/main.py` |
| `.html` | `<!-- app/templates/index.html -->` |
| `.yaml` | `# .claude/swarms/create-module.yaml` |
| `.css` | `/* app/static/css/main.css */` |
| `.js` | `// app/static/js/main.js` |
| `.md` | `# path/to/file.md` (as title) |
| `.rules` | `# .claude/rules/name.rules` |
| `.json` | `"_filepath": "path/to/file.json"` (first key) |

---

## STEP 2: Read stack_config.json (MANDATORY)

```bash
cat .claude/stack_config.json
```

Verify ALL these fields before coding:

| Field | Value in this project | Required Action |
|-------|----------------------|-----------------|
| `tools.package_manager` | **uv** | USE uv sync, uv add |
| `auth.password_hash` | **argon2id** | USE argon2-cffi |
| `tools.python_version` | **3.12** | VERIFY compatibility |
| `database.orm` | **SQLAlchemy 2.0** | USE Mapped[], mapped_column |
| `database.type` | **SQLite** | USE aiosqlite |
| `database.tables` | **English snake_case plural, no prefix** | users, projects, tasks... |
| `database.terminology` | **budget_used/budget_allocated/budget_remaining** | NO cargos/abonos/balance |
| `auth.roles` | **ADMIN, MEMBER, VIEWER** | Only these 3 roles |

---

## STEP 3: Verify Compatibilities

### Password Hashing Compatibility Table

| Algorithm | Python 3.12 | Python 3.13 | Python 3.14 | Recommended |
|-----------|-------------|-------------|-------------|-------------|
| argon2id  | OK          | OK          | OK          | YES         |
| bcrypt    | OK          | OK          | ISSUES      | NO          |
| scrypt    | OK          | OK          | OK          | ALTERNATIVE |
| pbkdf2    | OK          | OK          | OK          | LEGACY      |

**If stack_config.json says `argon2id`, DO NOT use bcrypt under any circumstances.**

### Package Managers

| Manager | Install Command | Add Command | Lock File |
|---------|-----------------|-------------|-----------|
| pip     | pip install -r requirements.txt | pip install X | requirements.txt |
| uv      | uv sync | uv add X | uv.lock |
| poetry  | poetry install | poetry add X | poetry.lock |

**If stack_config.json says `uv`, DO NOT use pip.**

---

## STEP 4: Pre-Implementation Checklist

Before writing ANY code, answer:

### Dependencies
- [ ] Did I read stack_config.json?
- [ ] Do I know which package manager to use? (uv)
- [ ] Are dependencies compatible with Python 3.12?

### Security
- [ ] Do I know which hashing algorithm to use? (argon2id)
- [ ] Did I verify compatibility with Python version?
- [ ] Did I read security.rules?

### Database
- [ ] Do I know which ORM/driver to use? (SQLAlchemy 2.0 + aiosqlite)
- [ ] Are tables in English snake_case plural without prefix?
- [ ] Am I using Numeric(10, 2) for money fields (not Float)?
- [ ] Did I read database.rules?

### API
- [ ] Did I read api-design.rules?
- [ ] Did I read architecture.rules?
- [ ] Do endpoints use English plural nouns? (/api/v1/projects, /api/v1/tasks)

### File
- [ ] Did I include the file path as a comment on the first line?

---

## STEP 5: Verification Commands

Run BEFORE implementing:

```bash
# Verify stack
python .claude/validators/check_stack.py

# Verify no conflicts
python .claude/validators/check_dependencies.py
```

---

## CONSEQUENCES OF OMISSION

If these checks are skipped:

1. **Incompatible code**: Using bcrypt in Python 3.14 causes errors
2. **Inconsistent dependencies**: Using pip when uv was defined causes conflicts
3. **Wrong names**: Tables in wrong naming convention contradict decision_log.json
4. **Rework**: Already-implemented code must be rewritten

---

## EXAMPLE OF CORRECT FLOW

```
1. User requests: "Implement task registration"

2. Agent MUST:
   a) Read .claude/stack_config.json
   b) Verify database.tables → tasks (not task_items)
   c) Verify database.enums.task_category → 8 categories
   d) Verify tools.package_manager = "uv"
   e) Read .claude/rules/database.rules and api-design.rules

3. Agent implements:
   - Task model in app/domain/models.py (with # app/domain/models.py on line 1)
   - Schema TaskCreate in app/schemas/tasks.py
   - Service in app/services/tasks.py
   - Endpoint POST /api/v1/tasks
   - Trigger: inserts activity_log entry in activity_logs table
   - Install with: uv add [dependency]
```

---

## RELATED FILES

| File | Purpose | Read When |
|------|---------|-----------|
| stack_config.json | Stack definition | ALWAYS first |
| security.rules | Security rules | Auth, passwords |
| architecture.rules | Code structure | New modules |
| database.rules | Models and queries | DB, migrations |
| api-design.rules | Endpoints and schemas | APIs |
| decision_log.json | Decisions made | Architectural changes |

---

**VERSION**: 2.0
**LAST UPDATED**: 2026-04-12
**PROJECT**: AgentCore v2.0 - Multi-Stack Agent System
