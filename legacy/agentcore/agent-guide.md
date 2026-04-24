# .claude/AGENT_GUIDE.md
# Agent Guide - AgentCore v2.3

This guide documents the available agents and their **MANDATORY WORKFLOW** to prevent omissions.

---

## CRITICAL CHANGE v1.3: Stack Verification + File Path Header

**ALL agents MUST**:

1. Read `MANDATORY_CHECKS.md` before any action
2. Verify `stack_config.json` before writing code
3. NOT substitute technologies without explicit justification
4. **Include the file path as a comment on the first line of every file created**

---

## Skills Directory (.agent/skills/)

AgentCore v2.0 incluye un sistema de skills reutilizables ubicados en `.agent/skills/`. Los skills son programas especializados que ejecutan tareas específicas.

### Skills Principales

1. **brief-to-prd**: Generador interactivo de PRDs desde los templates de 35 secciones
   - Ubicación: `.agent/skills/brief-to-prd/`
   - Input aceptado:
     - `PROJECT-BRIEF-FULL-Quantum.yaml` — formato YAML estructurado (parsing automático)
     - `PROJECT-BRIEF-FULL.md` — formato Markdown (llenado manual por humanos)
   - Función: Lee el Brief, pregunta secciones faltantes (CRÍTICO → OPCIONAL), detecta stack, genera PRD + stack_config.yml
   - Comando único: Genera ambos artefactos en una ejecución
   - Las 35 secciones cubren: negocio, arquitectura, datos, frontend, AI, agentes, seguridad, observabilidad, CI/CD, costos y más

2. **stack-generator**: Generador de configuración de stack
   - Ubicación: `.agent/skills/stack-generator/`
   - Función: Convierte `PROJECT-BRIEF-FULL-Quantum.yaml` a stack_config.yml
   - Soporta: Next.js 15, Go+Wails, FastAPI (3 sub-stacks)
   - Mapea los 35 campos del brief a decisiones técnicas concretas del stack

### Uso de Skills

Los skills se activan automáticamente cuando el usuario ciertos triggers:
- "genera PRD desde brief"
- "del brief al PRD"
- "interpreta mi brief"
- O cuando se detecta un `PROJECT-BRIEF-FULL-Quantum.yaml` o `PROJECT-BRIEF-FULL.md`

Los skills delegan la generación del PRD a skills específicos del stack (prd-nextjs15, prd-fastapi, prd-go-wails).

---

## Multi-Stack Support

AgentCore v2.0 soporta múltiples stacks tecnológicos, cada uno con su propia configuración:

### Stacks Disponibles

1. **Next.js 15** (`.claude/stacks/nextjs15/`)
   - React 19 + Prisma + NextAuth
   - Ideal para: SaaS web modernos, dashboards

2. **Go + Wails** (`.claude/stacks/go-wails/`)
   - Backend Go + Desktop nativo
   - Ideal para: POS, apps instalables, sistemas con hardware

3. **FastAPI** (`.claude/stacks/fastapi/`)
   - Python async con 3 sub-stacks:
     - Stack A (SSR): Jinja2 + HTMX + PicoCSS
     - Stack B (SPA): React 18 + MUI + Zustand
     - Stack C (Desktop): PyWebview + PyInstaller
   - Ideal para: Sistemas médicos, de datos, apps internas

### Configuración por Stack

Cada stack tiene su propia configuración en `.claude/stacks/{stack}/config.yaml`:
- Decisiones técnicas automáticas
- Patrones de código específicos
- Módulos reutilizables (auth, database, testing, frontend, hardware)
- Estructura de directorios
- Comandos de ejecución

### Cambio de Stack

Para cambiar de stack, usa el script `stack_selector.py`:
```bash
python .claude/scripts/stack_selector.py
```

O modifica `PROJECT-BRIEF-FULL-Quantum.yaml` (YAML) / `PROJECT-BRIEF-FULL.md` (Markdown) y usa el skill `brief-to-prd`.

---

## Available Agents

Los agentes en AgentCore v2.0 son ahora **stack-aware**, lo que significa que validan la configuración contra el stack seleccionado.

### Archivos de Lectura Obligatoria

Cada agente tiene una lista de `required_files` que incluye:
1. `MANDATORY_CHECKS.md` (siempre primero)
2. `stack_config.yml` (configuración dinámica del stack activo)
3. `.claude/stacks/{stack}/config.yaml` (configuración específica del stack)
4. `rules/architecture.rules`
5. `rules/database.rules`
6. `rules/security.rules`

### Validación Stack-Aware

Los agentes ahora verifican que:
- El stack seleccionado en `stack_config.yml` es válido
- Las decisiones técnicas (auth, ORM, etc.) coinciden con el stack
- No hay inconsistencias entre el Brief y el stack_config

### Ejemplo

Si el stack seleccionado es FastAPI:
- ✅ Acepta: Argon2id, SQLAlchemy 2.0, uv
- ❌ Rechaza: bcrypt, SQLAlchemy 1.4, pip

Si el stack seleccionado es Next.js 15:
- ✅ Acepta: NextAuth, Prisma, pnpm
- ❌ Rechaza: JWT manual, GORM, npm

---

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

**VERSION**: 2.3
**LAST UPDATED**: 2026-04-14
**PROJECT**: AgentCore v2.3 - Multi-Stack Agent System
