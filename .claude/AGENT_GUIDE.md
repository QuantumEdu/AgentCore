# .claude/AGENT_GUIDE.md
# Agent Guide - FlowTask Inc. v1.3

This guide documents the available agents and their **MANDATORY WORKFLOW** to prevent omissions.

---

## CRITICAL CHANGE v1.3: Stack Verification + File Path Header

**ALL agents MUST**:

1. Read `MANDATORY_CHECKS.md` before any action
2. Verify `stack_config.json` before writing code
3. NOT substitute technologies without explicit justification
4. **Include the file path as a comment on the first line of every file created**

---

## Available Agents

### 1. architect.agent v1.3

**Role**: Software architect with stack validation

**Responsibilities**:
- Validate architecture against decision_log.json
- **VERIFY stack_config.json before approving technologies**
- Approve or reject structural changes

**MUST read**:
- `MANDATORY_CHECKS.md`
- `stack_config.json`
- `decision_log.json`
- `rules/architecture.rules`

**Rejection example**:
```
REQUEST: "Use bcrypt for passwords"
REJECTION: stack_config.json specifies argon2id, bcrypt is in FORBIDDEN
```

---

### 2. backend-developer.agent v1.3

**Role**: Backend developer with stack awareness

**Responsibilities**:
- Implement domain use cases (users, projects, tasks, sprints, activity_logs)
- Create REST endpoints for projects, tasks, sprints, activity_logs
- **RESPECT stack_config.json at all times**

**BEFORE coding MUST**:
1. Read `MANDATORY_CHECKS.md`
2. Verify `stack_config.json`:
   - tools.package_manager → uv
   - auth.password_hash → argon2id
   - database.orm → SQLAlchemy 2.0
   - database.tables → English snake_case plural, no prefix
   - database.enums → project-defined expanded enums

**Correct example**:
```python
# app/core/security.py
from argon2 import PasswordHasher
ph = PasswordHasher()

# DO NOT use:
from passlib.context import CryptContext  # FORBIDDEN
```

---

### 3. security-expert.agent v1.3

**Role**: Security expert with stack enforcement

**Responsibilities**:
- Implement authentication per stack_config.json
- **REJECT unauthorized substitutions**
- Validate permissions by role: ADMIN, MEMBER, VIEWER

**ENFORCE**:
- If stack says `argon2id`, reject `bcrypt`
- If stack says `uv`, reject `pip install`
- Verify `FORBIDDEN` list in stack_config.json

---

### 4. database-designer.agent

**Role**: Domain model designer

**Responsibilities**:
- Create models with mandatory fields (id, created_at, updated_at, deleted_at)
- Tables in English snake_case plural, no prefix: users, projects, tasks, subtasks, activity_logs, sprints, event_logs
- Correct FK relationships with back_populates
- Alembic migrations
- Soft delete with `deleted_at`
- Append-only on activity_logs and event_logs

---

### 5. test-engineer.agent

**Role**: Testing engineer

**Responsibilities**:
- Maintain coverage >= 80%
- Tests for all domain endpoints
- Fixtures: sample_user, sample_project, sample_task, sample_subtask
- Role fixtures: admin_user, member_user, viewer_user

---

### 6. api-designer.agent

**Role**: API and Pydantic schema designer

**Responsibilities**:
- Separate schemas: Create/Update/Response/InDB
- Domain endpoints: /api/v1/projects, /api/v1/tasks, /api/v1/activity-logs, /api/v1/sprints
- Validations with Field()
- Enums: ProjectStatus, ProjectType, TaskCategory, UserRole

---

### 7. pm_orchestrator.agent

**Role**: Project Manager

**Responsibilities**:
- Maintain roadmap.md (10 phases), audit_log.md
- Document decisions in decision_log.json
- Track progress per phase

---

### 8. consultant.agent

**Role**: Business consultant

**Responsibilities**:
- Initial discovery
- Validate requirements with Alex Rivera (CTO, FlowTask Inc.)
- Generate initial stack_config.json

---

## Mandatory Workflow

### For ANY implementation:

```
1. Read MANDATORY_CHECKS.md
2. Read stack_config.json
3. Run: python .claude/validators/check_stack.py
4. Read relevant rules/
5. Add file path comment to first line of every file
6. Implement
7. Run: python .claude/validators/check_stack.py --verify
8. Update memory/ if decisions were made
```

### For architectural changes:

```
1. architect reads decision_log.json
2. architect reads stack_config.json
3. If conflict with stack → REJECT
4. If conflict with decisions → REJECT
5. If OK → Approve
6. pm_orchestrator documents in audit_log.md
```

---

## Cross-Reference Table

| Agent | Files MUST read |
|-------|----------------|
| architect | MANDATORY_CHECKS.md, stack_config.json, decision_log.json |
| backend-developer | MANDATORY_CHECKS.md, stack_config.json, architecture.rules |
| security-expert | MANDATORY_CHECKS.md, stack_config.json, security.rules |
| database-designer | stack_config.json, database.rules |
| test-engineer | stack_config.json, testing.rules |

---

## Common Errors PREVENTED

| Error | Cause | Prevention v1.3 |
|-------|-------|-----------------|
| Using bcrypt when argon2id is specified | Not reading stack_config | MANDATORY_CHECKS.md + validators |
| Using pip when uv is specified | Not verifying tools | check_stack.py |
| Ignoring previous decisions | Not reading decision_log | Checklist in architect.agent |
| Files without identifiable path | Not following v1.3 rule | Mandatory path rule |
| Tables with wrong naming | Not reading database.rules | stack_config.json + database.rules |

---

**VERSION**: 1.3
**LAST UPDATED**: 2026-04-05
**PROJECT**: FlowTask Inc. - Task Management Platform
