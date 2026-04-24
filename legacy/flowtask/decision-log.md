# Decision Log - FlowTask Inc.

Última actualización: 2026-04-12

---

## [1] Use SQLite as database

**Fecha**: 2026-04-05
**Autor**: AgentCore Team
**Estado**: Aceptada

### Context

SaaS system for small team, < 10 concurrent users, initial version, local deployment.

### Decision

Use SQLite as database for this version.

### Alternatives Considered

- **PostgreSQL (Supabase)**: Rejected because unnecessary for this version
- **PostgreSQL self-hosted**: Rejected because infrastructure complexity

### Rationale

SQLite sufficient for low concurrency, zero configuration, portable, simple to back up.

### Consequences

**Positivas**:
- Zero configuration for development
- Single file for backup/restore
- Fast queries for small datasets

**Negativas**:
- Limited concurrent writes (not an issue for < 10 users)
- No built-in replication (not needed yet)

**Módulos Afectados**:
- Database module
- Deployment module

**Costo de Implementación**:
- Estimación: 1 día
- Riesgos: None significant

### Related Decisions
- None

---

## [2] Tables in English snake_case WITHOUT prefix

**Fecha**: 2026-04-05
**Autor**: AgentCore Team
**Estado**: Aceptada

### Context

Team is English-speaking, API consumed by English-speaking developers.

### Decision

Tables in English snake_case WITHOUT prefix: users, projects, tasks, subtasks, activity_logs, sprints, event_logs.

### Alternatives Considered

- **Spanish names**: Rejected because team and domain are English-speaking
- **Table prefix (ft_)**: Rejected because unnecessary in a dedicated database

### Rationale

English names align with team language, no prefix needed for dedicated database.

### Consequences

**Positivas**:
- Consistent with team language
- Simpler table names
- Better alignment with API naming

**Negativas**:
- None significant

**Módulos Afectados**:
- Database module
- Domain module

**Costo de Implementación**:
- Estimación: 1 día
- Riesgos: None significant

### Related Decisions
- None

---

## [3] Include expanded user fields

**Fecha**: 2026-04-05
**Autor**: AgentCore Team
**Estado**: Aceptada

### Context

User profile needs support for remote teams across time zones.

### Decision

Include expanded user fields: full_name, email, avatar_url, timezone, last_seen_at.

### Alternatives Considered

- **Only basic fields (name, email)**: Rejected because insufficient for remote team UX

### Rationale

Expanded profile supports timezone-aware features and last-seen presence indicators.

### Consequences

**Positivas**:
- Timezone-aware features
- Presence indicators
- Better UX for remote teams

**Negativas**:
- Slightly more complex user model

**Módulos Afectados**:
- Domain module
- Schemas
- API

**Costo de Implementación**:
- Estimación: 1 día
- Riesgos: None significant

### Related Decisions
- None

---

## [4] Expand TaskCategory enum

**Fecha**: 2026-04-05
**Autor**: AgentCore Team
**Estado**: Aceptada

### Context

Task management requires flexible categorization for different work types.

### Decision

Expand TaskCategory enum to: FEATURE, BUG, CHORE, DOCS, TEST, INFRA, DESIGN, OTHER.

### Alternatives Considered

- **Only 3 types (FEATURE, BUG, OTHER)**: Rejected because too coarse for planning and reporting
- **Free-text category**: Rejected because inconsistent data, hard to filter

### Rationale

8 categories provide meaningful grouping for sprint planning and velocity tracking without excessive granularity.

### Consequences

**Positivas**:
- Better task categorization
- Improved sprint planning
- More accurate velocity tracking

**Negativas**:
- Slightly more complex enum
- Potential for category confusion

**Módulos Afectados**:
- Domain module
- Schemas

**Costo de Implementación**:
- Estimación: 0.5 días
- Riesgos: None significant

### Related Decisions
- None

---

## [5] Use budget terminology

**Fecha**: 2026-04-05
**Autor**: AgentCore Team
**Estado**: Aceptada

### Context

Budget tracking requires clear and unambiguous financial terminology.

### Decision

Use terminology: budget_used (consumed), budget_allocated (assigned), budget_remaining (balance).

### Alternatives Considered

- **debit/credit/balance**: Rejected because less intuitive for non-finance developers
- **spent/available**: Rejected because ambiguous for budget_allocation vs remaining distinction

### Rationale

budget_ prefix makes all financial fields immediately identifiable; used/allocated/remaining are self-explanatory.

### Consequences

**Positivas**:
- Clear and unambiguous terminology
- Self-explanatory field names
- Consistent naming convention

**Negativas**:
- Longer field names

**Módulos Afectados**:
- Domain module
- Schemas
- API
- Templates

**Costo de Implementación**:
- Estimación: 0.5 días
- Riesgos: None significant

### Related Decisions
- [6] Budget allocation dual registration

---

## [6] Budget allocation dual registration

**Fecha**: 2026-04-05
**Autor**: AgentCore Team
**Estado**: Aceptada

### Context

Budget allocation is an upfront assignment of funds to a project.

### Decision

Budget allocation is stored as a field in the projects table AND recorded as an entry in activity_logs (append-only audit trail).

### Alternatives Considered

- **Only field in projects**: Rejected because no audit trail of budget changes
- **Only in activity_logs**: Rejected because no fast reference on the project itself

### Rationale

Dual registration: project field for fast read + activity_log entry for full auditability and budget history reconstruction.

### Consequences

**Positivas**:
- Fast read access
- Full audit trail
- Budget history reconstruction
- Data consistency

**Negativas**:
- Slightly more complex write operations
- Need to keep both in sync

**Módulos Afectados**:
- Domain module
- Services
- API

**Costo de Implementación**:
- Estimación: 1 día
- Riesgos: Data synchronization

### Related Decisions
- [5] Use budget terminology
