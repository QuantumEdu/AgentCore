# .claude/memory/backlog/roadmap.md

## Roadmap - FlowTask Inc. - Task Management Platform

**Client**: FlowTask Inc.
**Technical Lead**: Alex Rivera (CTO)

---

## Phase 0: Preparation (NO code)

- [ ] Git repository created
- [ ] FastAPI project structure
- [ ] uv configuration (pyproject.toml)
- [ ] Alembic configuration
- [ ] .env file with SECRET_KEY

---

## Phase 1: Database (CRITICAL)

- [ ] SQLite configured with SQLAlchemy 2.0
- [ ] Create enums: ProjectStatus (ACTIVE, COMPLETED, ARCHIVED, ON_HOLD), ProjectType (INTERNAL, CLIENT, RESEARCH, MAINTENANCE), TaskCategory (8 categories), UserRole (ADMIN, MEMBER, VIEWER)
- [ ] Create tables: users, projects, subtasks, tasks, activity_logs, sprints, event_logs
- [ ] PKs, FKs, and constraints defined
- [ ] Prohibit DELETE on activity_logs and event_logs
- [ ] Initial Alembic migration

---

## Phase 2: Budget Rules (NO UI)

- [ ] Define what generates budget_used (task consumption)
- [ ] Define what generates budget_allocated (project budget assignment)
- [ ] Trigger: tasks → inserts row in activity_logs
- [ ] Activity logs: not recalculated, not overwritten
- [ ] Validate budget always reconciles
- [ ] Budget allocation: project field + activity_log entry

---

## Phase 3: Backend API (Minimal)

- [ ] FastAPI configured with uvicorn
- [ ] JWT authentication with Argon2id
- [ ] Roles: ADMIN, MEMBER, VIEWER
- [ ] Endpoints:
  - [ ] POST /api/v1/projects
  - [ ] POST /api/v1/tasks
  - [ ] POST /api/v1/projects/{id}/complete
  - [ ] GET /api/v1/activity-logs?project_id=
  - [ ] POST /api/v1/sprints/{id}/close
- [ ] Hard validations (do not trust frontend)

---

## Phase 4: Idempotency

- [ ] request_id mandatory on critical endpoints
- [ ] Unique constraints by request_id
- [ ] Retries do NOT generate duplicates
- [ ] Double-send test

---

## Phase 5: Sprint Closing (Automatic)

- [ ] Sprint close job configured
- [ ] Sum activity_logs for the sprint period
- [ ] Insert row in sprints
- [ ] Calculate integrity_hash
- [ ] Block modifications to closed sprints
- [ ] Test: attempt to modify closed sprint → fails

---

## Phase 6: Budget Exports

- [ ] Daily export endpoint (CSV/Excel)
- [ ] Monthly export endpoint (CSV/Excel)
- [ ] Columns: date, description, budget_used, budget_allocated, budget_remaining
- [ ] Reproducible output (same input = same output)

---

## Phase 7: Operational UI (Simple)

- [ ] Login (View 0)
- [ ] Active projects with table (View 1): name, owner, type, status, budget_remaining
- [ ] Project detail with tasks by category (View 2): features, bugs, chores, docs, tests, infra, design, other
- [ ] Create project (View 3): name, description, owner, project_type, budget_allocation
- [ ] Sprint close view
- [ ] No budget logic in frontend

---

## Phase 8: Audit

- [ ] Each relevant action generates event in event_logs
- [ ] event_logs append-only
- [ ] Store original payload
- [ ] Automatic timestamp
- [ ] Ability to reconstruct history

---

## Phase 9: Real-World Testing

- [ ] Real project simulation
- [ ] Multiple task assignments
- [ ] Project completion
- [ ] Sprint close
- [ ] Compare against real numbers
- [ ] Detect discrepancies

---

## Final Acceptance Criteria

- [ ] No duplicates
- [ ] Cannot alter a closed sprint
- [ ] Budget always reconciles
- [ ] Export usable by project manager
- [ ] System understandable without the developer
