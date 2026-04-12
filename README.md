# AgentCore

A reusable `.claude/` infrastructure template for AI-assisted backend development with Claude Code.

AgentCore gives your AI agents **institutional memory and guardrails** — so they stop re-inventing the stack on every session and start building consistent, production-grade code from day one.

---

## The Problem

When you use Claude Code (or any AI coding assistant) without structure, you get:

- Agents that pick the wrong library (bcrypt when you said argon2id)
- Endpoints that use pip when your project uses uv
- Database tables named however the AI felt like that day
- No memory of the architectural decisions you already made
- Every session starts from zero

AgentCore solves this by giving your AI agents a structured set of rules, memory, validators, and workflows to follow — enforced before any code is written.

---

## What's Inside

```
.claude/
├── AGENT_GUIDE.md          # Who the agents are and what they must do
├── MANDATORY_CHECKS.md     # What every agent reads before coding (enforced)
├── PORTABILITY.md          # How to adapt this template to any project
├── stack_config.json       # Single source of truth for tech stack choices
│
├── agents/
│   ├── architect.agent     # Validates architecture vs. decision log + stack
│   ├── backend-developer.agent   # Stack-aware implementation agent
│   └── security-expert.agent    # Enforces argon2id, JWT, RBAC
│
├── rules/
│   ├── api-design.rules    # RESTful conventions, schemas, status codes
│   ├── architecture.rules  # Clean Architecture (3 layers), domain models
│   ├── database.rules      # SQLAlchemy 2.0 patterns, soft delete, append-only
│   ├── deploy.rules        # Docker, GHCR, GitHub Actions CI/CD
│   ├── discovery.rules     # Initial consultation and stack decision process
│   ├── security.rules      # Argon2id, JWT, RBAC, OWASP Top 10
│   └── testing.rules       # Pytest fixtures, coverage >= 80%, AAA pattern
│
├── swarms/
│   ├── add-endpoint.yaml       # Add a new REST endpoint
│   ├── agile_cycle.yaml        # Full agile dev cycle with quality gates
│   ├── create-module.yaml      # Create a complete domain module
│   ├── discovery_swarm.yaml    # Initial discovery and tech proposal
│   ├── kaizen_improvement.yaml # Detect error patterns, auto-generate rules
│   └── write-tests.yaml        # Generate tests for existing code
│
├── validators/
│   ├── check_stack.py          # Verify stack before coding
│   └── check_dependencies.py   # Verify no forbidden packages installed
│
└── memory/
    ├── audit_log.md            # Append-only log of architectural changes
    ├── decision_log.json       # Documented decisions with rationale
    └── backlog/
        └── roadmap.md          # 10-phase implementation roadmap
```

---

## What's New in v2.0

AgentCore v2.0 is a major upgrade that adds **multi-stack support** and **interactive PRD generation**.

### 🚀 Key Features

1. **Multi-Stack Support**: Support for Next.js 15, Go+Wails, and FastAPI (3 sub-stacks)
2. **Interactive Brief-to-PRD**: Generate PRD + stack_config.yml in ONE command
3. **Structured PROJECT-BRIEF**: YAML format with validation schema
4. **Stack-Specific Configurations**: Each stack has its own decisions, patterns, and modules
5. **Reusable Patterns**: hexagonal, SOLID, design patterns, testing patterns
6. **Utility Scripts**: init_project, stack_selector, project_brief_parser, decision_adr_converter
7. **Template System**: Reusable templates for Brief, ADR, and Roadmap

### 📊 Improvements

| Metric | v1.3 | v2.0 | Improvement |
|--------|-------|-------|-------------|
| Stacks supported | 1 (FastAPI only) | 4+ (Next.js, Go, FastAPI×3, Laravel) | +300% |
| Brief sections mapped | 11/23 (47.8%) | 23/23 (100%) | +52.2% |
| PRD generation time | Manual (2-4h) | Automated (30-45min) | -75% |
| Code patterns | Embedded in rules | Separate, reusable | +200% |
| Extensibility | Low | High | +200% |

### 🔄 Migration from v1.3

See [CHANGELOG.md](./CHANGELOG.md) for detailed migration guide.

Quick start:
1. Create `PROJECT-BRIEF-FULL.yaml` (use template in `.claude/templates/`)
2. Run: `python .claude/scripts/stack_selector.py`
3. Use `brief-to-prd` skill to generate PRD + config

---

## Core Concepts

### stack_config.json — Single Source of Truth

Every agent reads this file before writing a single line of code. It defines:

- Package manager (`uv`, never `pip`)
- Password hashing algorithm (`argon2id`, never `bcrypt`)
- ORM and database type (`SQLAlchemy 2.0` + `SQLite`)
- Table naming conventions
- Domain enums (roles, statuses, categories)
- Business rules (append-only tables, immutable records)

If a request contradicts `stack_config.json`, agents reject it — with an explanation.

### Validators — Automated Guardrails

```bash
# Check before coding
python .claude/validators/check_stack.py

# Check after installing dependencies
python .claude/validators/check_dependencies.py --verify
```

These scripts detect forbidden packages, wrong library usage, and missing dependencies automatically.

### Agents — Role-Aware Collaborators

Each agent has a defined role and a mandatory reading list before acting:

| Agent | Role | Must Read First |
|-------|------|-----------------|
| `architect` | Validates changes vs. decisions + stack | MANDATORY_CHECKS, stack_config, decision_log |
| `backend-developer` | Implements features following the stack | MANDATORY_CHECKS, stack_config, architecture.rules |
| `security-expert` | Enforces auth, hashing, RBAC | MANDATORY_CHECKS, stack_config, security.rules |

### Rules — Explicit Standards

Rules files (`*.rules`) contain:
- Patterns to follow (with code examples)
- Anti-patterns to avoid (with rejection examples)
- Checklists to verify before approval
- Domain-specific conventions

### Swarms — Multi-Agent Workflows

Swarms coordinate multiple agents in sequence with quality gates:

```
discovery_swarm → agile_cycle → create-module → add-endpoint → write-tests
```

Each swarm defines participants, dependencies, quality gates, and artifact outputs.

### Memory — Institutional Knowledge

- `decision_log.json`: Every architectural decision with context, rationale, and alternatives considered
- `audit_log.md`: Append-only log of what changed and why
- `roadmap.md`: Phased implementation plan

Agents consult these files before making decisions, so they never contradict what was already agreed.

---

## Technology Stack (Example: FlowTask Inc.)

This template ships pre-configured for a **task management SaaS** (FlowTask Inc.):

| Layer | Choice | Rationale |
|-------|--------|-----------|
| Language | Python 3.12 | Stable, widely supported |
| Web Framework | FastAPI | Async, OpenAPI docs, modern |
| ORM | SQLAlchemy 2.0 | Type-safe, Mapped[], async ready |
| Database | SQLite → PostgreSQL | Zero config for MVP, migrate when needed |
| Migrations | Alembic | Industry standard for SQLAlchemy |
| Password Hashing | Argon2id | PHC winner, GPU/ASIC resistant |
| Auth | JWT (HS256) | Stateless, simple, well-understood |
| Package Manager | uv | Faster than pip, better lock files |
| Testing | pytest | Fixtures, parametrize, coverage |
| Linting | ruff | Fast, replaces flake8 + isort |
| Frontend | Jinja2 + PicoCSS | SSR, no JS build step |

### Domain Model (FlowTask Inc.)

| Table | Purpose | Pattern |
|-------|---------|---------|
| `users` | Platform members | Soft delete, full profile |
| `projects` | Work containers | Soft delete, status machine |
| `subtasks` | Reusable work item catalog | Soft delete |
| `tasks` | Work assigned to projects | Soft delete |
| `activity_logs` | Budget ledger | **Append-only** — never UPDATE/DELETE |
| `sprints` | Time-boxed iterations | **Immutable after close** |
| `event_logs` | Full audit trail | **Append-only** — never UPDATE/DELETE |

### Roles

| Role | What They Can Do |
|------|-----------------|
| `ADMIN` | Everything — users, projects, sprints, budgets |
| `MEMBER` | Create and update tasks in assigned projects |
| `VIEWER` | Read-only access to projects and activity |

---

## Quick Start

### 1. Initialize Project

```bash
# Clone or create your project
cd your-project

# Initialize with AgentCore
python .claude/scripts/init_project.py .

# Select your stack
python .claude/scripts/stack_selector.py
```

### 2. Fill PROJECT-BRIEF

Edit `improve01/PROJECT-BRIEF-FULL.yaml` with your project details:
- Fill in all required fields
- Select your stack principal
- Describe your architecture, data strategy, security, etc.

### 3. Generate PRD + Config

Use the `brief-to-prd` skill:
- It will ask you for missing sections (interactive)
- It will detect your stack automatically
- It will generate BOTH PRD and stack_config.yml in ONE command

### 4. Start Coding

Agents will now:
- Read your stack configuration
- Apply stack-specific decisions
- Follow architecture rules
- Generate code matching your stack

### 5. Validate

```bash
# Validate your stack configuration
python .claude/validators/check_stack.py

# Validate dependencies
python .claude/validators/check_dependencies.py --verify
```

---

## Adapting to Your Project

AgentCore is a template. To use it for a different project:

### 1. Clone and copy

```bash
git clone git@github.com:QuantumEdu/AgentCore.git
cp -r AgentCore/.claude /path/to/your-project/.claude
```

### 2. Edit stack_config.json

Change the project name, tables, enums, roles, and business rules to match your domain.

### 3. Adapt the rules files

Each `.rules` file has a footer with the project name. Update:
- Domain model names and relationships
- Enum values
- API endpoint examples
- Role names and permissions
- Fixture names in testing.rules

### 4. Reset memory

```bash
cd your-project/.claude/memory

# Reset with your project name
echo '{"_filepath":".claude/memory/decision_log.json","project_name":"Your Project","decisions":[]}' > decision_log.json
echo "# .claude/memory/audit_log.md\n\n## Change Log - Your Project" > audit_log.md
```

### 5. Run the validator

```bash
python .claude/validators/check_stack.py
```

### Files that need adaptation

| File | What to change |
|------|---------------|
| `stack_config.json` | Everything domain-specific |
| `rules/architecture.rules` | Domain models, directory structure |
| `rules/database.rules` | Table names, relationships, enums |
| `rules/security.rules` | Roles, permission matrix |
| `rules/api-design.rules` | Endpoints, schema examples |
| `rules/testing.rules` | Fixtures, test examples |
| `rules/discovery.rules` | Project context examples |
| `memory/decision_log.json` | Reset with your decisions |
| `memory/audit_log.md` | Reset with your project name |
| `memory/backlog/roadmap.md` | Rewrite for your milestones |
| `AGENT_GUIDE.md` | Agent roles, project name |

### Files you can reuse unchanged

| File | Why |
|------|-----|
| `agents/*.agent` | Dynamically read stack_config.json |
| `swarms/*.yaml` | Generic workflows |
| `validators/*.py` | Driven by stack_config.json |
| `MANDATORY_CHECKS.md` | Universal pre-coding checklist |

---

## Mandatory Flow (Enforced for Every Agent)

```
1. Read MANDATORY_CHECKS.md
2. Read stack_config.json
3. Run: python .claude/validators/check_stack.py
4. Read relevant rules/ files
5. Add file path comment to first line of every file created
6. Implement
7. Run: python .claude/validators/check_stack.py --verify
8. Update memory/ if decisions were made
```

---

## Key Patterns

### Append-Only Tables
`activity_logs` and `event_logs` never get UPDATE or DELETE. Every state change is a new INSERT. This gives you a complete, tamper-evident audit trail.

### Soft Delete
All standard models have a `deleted_at` column. `db.delete()` is forbidden. Queries always filter `WHERE deleted_at IS NULL`.

### Immutable Records
`sprints` are immutable after closing. An integrity hash verifies the record was not altered.

### Budget Dual Registration
Budget allocation is stored as a field on `projects` (fast reads) AND as an entry in `activity_logs` (full audit history). Both writes happen in the same transaction.

### File Path Headers
Every file created by agents contains its own path as a comment on line 1:
```python
# app/services/projects.py
```
This makes grep and navigation trivial in any codebase.

---

## License

MIT — use this in any project, commercial or otherwise.

---

Built with Claude Code · Maintained by [QuantumEdu](https://github.com/QuantumEdu)
