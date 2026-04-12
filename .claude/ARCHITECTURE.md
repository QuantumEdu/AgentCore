# Architecture - AgentCore v2.0

**Version**: 2.0
**Last Updated**: 2026-04-12

---

## Overview

AgentCore v2.0 is a reusable `.claude/` infrastructure template for AI-assisted backend development. It provides institutional memory, guardrails, and multi-stack support for AI coding assistants.

### Key Components

1. **Skills Directory** (`.agent/skills/`) - Reusable AI skills
2. **Stacks Directory** (`.claude/stacks/`) - Multi-stack configurations
3. **Rules Directory** (`.claude/rules/`) - Architecture and coding standards
4. **Agents** (`.claude/agents/`) - Role-aware AI collaborators
5. **Swarms** (`.claude/swarms/`) - Multi-agent workflows
6. **Validators** (`.claude/validators/`) - Automated guardrails
7. **Memory** (`.claude/memory/`) - Institutional knowledge

---

## Data Flow

### Brief → PRD + Config Flow

```
┌─────────────────────────────────────────────────────────┐
│ PROJECT-BRIEF-FULL.yaml                                │
│ (Structured YAML with 23 sections)                     │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│ brief-to-prd Skill                                     │
│ 1. Validate against brief-schema.json                  │
│ 2. Detect stack automatically                          │
│ 3. Calculate complexity score (1-10)                  │
│ 4. Interactive questioning (missing sections)           │
│ 5. Load stack-specific configuration                    │
└──────────┬──────────────────────┬──────────────────────┘
           │                      │
           ▼                      ▼
┌──────────────────────┐  ┌──────────────────────┐
│ Generate PRD         │  │ Generate Config       │
│ (Stack-specific)     │  │ (stack_config.yml)    │
└──────────────────────┘  └──────────────────────┘
           │                      │
           ▼                      ▼
┌─────────────────────────────────────────────────────────┐
│ improve01/outputs/PRD_{name}_{stack}.md              │
│ .claude/stack_config.yml                               │
└─────────────────────────────────────────────────────────┘
```

### AI Coding Flow

```
┌─────────────────────────────────────────────────────────┐
│ User Request (e.g., "Add endpoint X")                   │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│ Architect Agent                                         │
│ 1. Read MANDATORY_CHECKS.md                          │
│ 2. Read stack_config.yml                               │
│ 3. Read .claude/stacks/{stack}/config.yaml            │
│ 4. Verify against decision_log.md                      │
│ 5. Read rules/architecture.rules                       │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│ Backend-Developer Agent                                │
│ 1. Read stack_config.yml                               │
│ 2. Read .claude/stacks/{stack}/patterns.md             │
│ 3. Apply stack-specific patterns                       │
│ 4. Generate code following rules                       │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│ Security-Expert Agent                                  │
│ 1. Read stack_config.yml                               │
│ 2. Verify auth, hashing, RBAC                          │
│ 3. Check against rules/security.rules                   │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│ Generated Code                                         │
│ 4. Add file path comment on first line                │
│ 5. Implement following stack decisions                 │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│ Validators (Automated)                                  │
│ 1. python .claude/validators/check_stack.py           │
│ 2. python .claude/validators/check_dependencies.py    │
└─────────────────────────────────────────────────────────┘
```

---

## Stack System

### Stack Architecture

```
.claude/stacks/
├── registry.yaml              # Registry of all stacks
├── template.yaml              # Base template for new stacks
│
├── nextjs15/                  # Next.js 15 stack
│   ├── config.yaml
│   ├── decisions.yaml
│   ├── patterns.md
│   └── prd_skill.md
│
├── go-wails/                  # Go + Wails stack
│   ├── config.yaml
│   ├── decisions.yaml
│   ├── patterns.md
│   └── prd_skill.md
│
├── fastapi/                   # FastAPI stack (principal)
│   ├── config.yaml            # Complete configuration
│   ├── decisions.yaml         # Architecture decisions (ADR)
│   ├── patterns.md            # Code patterns with examples
│   ├── modules/               # Reusable modules
│   │   ├── auth.yaml
│   │   ├── database.yaml
│   │   ├── testing.yaml
│   │   ├── frontend.yaml
│   │   └── hardware.yaml
│   ├── substacks/             # 3 sub-stacks
│   │   ├── ssr.yaml
│   │   ├── spa.yaml
│   │   └── desktop.yaml
│   └── prd_skill.md
│
└── laravel/                   # Laravel (extensibility example)
    ├── config.yaml
    └── README.md
```

### Stack Configuration Flow

1. **Selection**: User selects stack via `PROJECT-BRIEF-FULL.yaml` or `stack_selector.py`
2. **Load**: `stack_generator` loads `.claude/stacks/{stack}/config.yaml`
3. **Map**: Maps Brief fields to stack configuration
4. **Generate**: Generates `stack_config.yml` with project-specific overrides
5. **Validate**: `check_stack.py` validates consistency with Brief

### Stack Detection Rules

The system detects the stack from the Brief using rules in `registry.yaml`:

| Trigger | Stack | Confidence |
|---------|-------|------------|
| "[x] Next.js 15" | nextjs15 | 1.0 |
| "[x] FastAPI Stack A" | fastapi_ssr | 1.0 |
| "React" | nextjs15 | 0.7 |
| "Python" | fastapi | 0.7 |
| "Go" | go-wails | 0.7 |

If confidence < 0.7, the system asks the user to confirm.

---

## Skill System

### Skill Architecture

```
.agent/skills/
├── _shared/                   # Shared conventions
│   ├── engram-convention.md
│   ├── persistence-contract.md
│   └── openspec-convention.md
│
├── brief-to-prd/              # Main PRD generator
│   └── SKILL.md
│
└── stack-generator/           # Config generator
    └── SKILL.md
```

### Skill Interaction

```
User Request
    │
    ▼
brief-to-prd Skill (Coordinator)
    │
    ├─► Load PROJECT-BRIEF-FULL.yaml
    ├─► Validate against brief-schema.json
    ├─► Detect stack (registry.yaml)
    ├─► Calculate complexity_score
    ├─► Interactive questioning
    │
    ├─► Delegate to stack-generator
    │   └─► Generate stack_config.yml
    │
    └─► Delegate to prd-{stack}_skill
        └─► Generate PRD (Markdown)
```

### Skill Activation

Skills are activated automatically when:
- User says specific triggers ("genera PRD desde brief")
- PROJECT-BRIEF-FULL.yaml is detected
- Specific keywords are mentioned

---

## Multi-Stack Support

### Why Multi-Stack?

Different projects need different stacks:
- **Web SaaS** → Next.js 15 (React 19 + Prisma)
- **Desktop POS** → Go + Wails (Native app)
- **Internal Dashboard** → FastAPI SSR (Jinja2 + HTMX)
- **Mobile SPA** → FastAPI SPA (React + MUI)
- **Local System** → FastAPI Desktop (PyWebview)

### How It Works

1. **Unified Interface**: All stacks share the same Brief format
2. **Automatic Detection**: System detects stack from Brief
3. **Stack-Specific Decisions**: Each stack has its own automatic decisions
4. **Consistent Structure**: All stacks follow the same config structure
5. **Easy Extension**: Add new stacks by creating new directory in `.claude/stacks/`

### Stack Comparison

| Aspect | Next.js 15 | Go+Wails | FastAPI SSR | FastAPI SPA | FastAPI Desktop |
|--------|------------|-----------|--------------|--------------|------------------|
| Backend | Server Actions | Fiber | FastAPI | FastAPI | FastAPI |
| Frontend | React 19 | React + MUI | Jinja2 | React + MUI | PyWebview |
| ORM | Prisma | GORM | SQLAlchemy | SQLAlchemy | SQLAlchemy |
| Auth | NextAuth | golang-jwt | JWT | JWT | JWT |
| Deploy | Vercel | Binary | Docker | Docker | PyInstaller |
| Ideal for | Web SaaS | Desktop POS | Internal apps | SaaS products | Local systems |

---

## Extension Points

### Adding a New Stack

To add a new stack (e.g., Laravel):

1. **Create directory**: `mkdir .claude/stacks/laravel/`
2. **Copy template**: `cp .claude/stacks/template.yaml .claude/stacks/laravel/config.yaml`
3. **Configure**: Edit `config.yaml` with Laravel-specific decisions
4. **Document**: Create `decisions.yaml` with ADRs
5. **Patterns**: Create `patterns.md` with Laravel patterns
6. **Modules**: Create `modules/` with Laravel modules
7. **Register**: Add to `registry.yaml`
8. **Test**: Run `python .claude/validators/check_stack.py --stack laravel`

### Adding a New Module

To add a new module (e.g., `email` to FastAPI):

1. **Create file**: `.claude/stacks/fastapi/modules/email.yaml`
2. **Define configuration**: SMTP settings, templates, etc.
3. **Add to config**: Update `config.yaml` modules list
4. **Document decisions**: Add to `decisions.yaml`
5. **Create patterns**: Add code examples to `patterns.md`

### Adding a New Pattern

To add a new pattern (e.g., `CQRS`):

1. **Update patterns.md**: Add section for CQRS
2. **Add examples**: Include Python, TypeScript, Go examples
3. **Update config**: Add to `automatic_decisions.patterns` if automatic
4. **Update rules**: Reference in `rules/architecture.rules`

---

## Security Considerations

### Stack Configuration Security

- `stack_config.yml` should be committed to version control
- Secrets should be in `.env` (never in `stack_config.yml`)
- `PROJECT-BRIEF-FULL.yaml` may contain sensitive info → add to `.gitignore`

### Agent Validation

All agents validate against:
1. `stack_config.yml` - Selected stack configuration
2. `.claude/stacks/{stack}/config.yaml` - Stack-specific decisions
3. `decision_log.md` - Architectural decisions
4. `rules/security.rules` - Security best practices

### Forbidden Substitutions

`stack_config.yml` includes `forbidden_substitutions` list:
- FastAPI stack: bcrypt, pip, SQLAlchemy 1.4
- Next.js stack: JWT manual, GORM, npm
- Go stack: bcrypt, pip, SQLAlchemy

---

## Performance Considerations

### Skill Performance

- `brief-to-prd` skill is coordinator only (delegates heavy lifting)
- Stack detection is O(n) where n = number of stacks (currently 4)
- Complexity score calculation is O(1) (fixed number of factors)

### Validator Performance

- `check_stack.py` loads YAML (fast)
- Validates against schema (fast)
- Checks consistency (fast)

### Scalability

- Adding more stacks doesn't affect performance
- Adding more modules has linear impact
- Pattern documentation is read-only

---

## Future Enhancements

### Planned Features

1. **SDD Workflow Integration**: Integrate with Spec-Driven Development
2. **More Stacks**: Add Django, Ruby on Rails, Spring Boot
3. **Visual Brief Builder**: Web UI for filling PROJECT-BRIEF-FULL
4. **Automated Testing**: Auto-generate tests from PRD
5. **CI/CD Integration**: Auto-generate GitHub Actions from stack

### Extension Ideas

- **Marketplace**: Community-contributed stacks and modules
- **Stack Comparison Tool**: Compare stacks side-by-side
- **Migration Assistant**: Auto-migrate from v1.3 to v2.0
- **Documentation Generator**: Auto-generate API docs from PRD
