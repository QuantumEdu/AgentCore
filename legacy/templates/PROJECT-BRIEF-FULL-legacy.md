# PROJECT-BRIEF — [Nombre del Proyecto]

> **Template v2.0** · Llenar secciones marcadas como `CRÍTICO` antes de iniciar cualquier diseño técnico.
> Las secciones marcadas `OPCIONAL` solo se llenan si el proyecto las requiere.
> Usar `N/A` para campos que explícitamente no aplican. Dejar vacío significa "pendiente de definir".

**Código de proyecto**: _______________
**Fecha**: _______________
**Autor**: _______________
**Versión**: 1.0
**Repositorio**: _______________

---

## SECCIÓN 1 · CONTEXTO & STACK BASE `CRÍTICO`

**Nombre del Sistema**: _______________

**Tipo de Entrega** (marcar uno):
- [ ] Web SaaS / Dashboard
- [ ] App Desktop instalable
- [ ] Híbrido (Desktop + Admin Web)
- [ ] API / Backend only
- [ ] CLI Tool
- [ ] Sistema de Agentes AI

**Stack Principal** (marcar uno):
- [ ] Next.js 15 — React 19 + Prisma + NextAuth + Tailwind
- [ ] Go + Fiber + Wails v2 — Desktop/Web, binario nativo
- [ ] FastAPI SSR — Jinja2 + HTMX + PicoCSS
- [ ] FastAPI SPA — React 18 + TypeScript + MUI
- [ ] FastAPI Desktop — PyWebview + PyInstaller
- [ ] Electron + React + Vite
- [ ] Otro: _______________

**Criticalidad**:
- [ ] low — falla tolerable, fix en días
- [ ] medium — falla impacta operación, fix en horas
- [ ] high — falla bloquea negocio, fix inmediato
- [ ] critical — SLA contractual, pérdida legal/económica

**Team Size**: [ ] 1  [ ] 2-5  [ ] 6-15  [ ] 15+

**Timeframe**: [ ] MVP-2sem  [ ] short-1mes  [ ] medium-3mes  [ ] long-6mes+

---

## SECCIÓN 2 · CONTEXTO DE NEGOCIO & PROBLEM STATEMENT `CRÍTICO`

> ⚠️ Esta es la primera pregunta que hace un arquitecto senior. Sin el "por qué", cualquier decisión de stack es arbitraria.

**El problema que este sistema resuelve**:
> Completar: "El sistema existe porque [problema concreto] que afecta a [quién] y cuesta [impacto medible]."

_____________________________________________
_____________________________________________

**Solución propuesta** (1-3 oraciones, sin jerga técnica):

_____________________________________________
_____________________________________________

**Estado actual del proyecto**:
- [ ] Greenfield — proyecto nuevo desde cero
- [ ] Brownfield — reemplaza o extiende sistema existente → Sistema actual: _______________
- [ ] Migración — mueve datos/funciones de otro sistema → Origen: _______________
- [ ] Prototipo — MVP para validar hipótesis

**Modelo de negocio**:
- [ ] B2B SaaS  [ ] B2C  [ ] Interno  [ ] Open Source  [ ] Gobierno  [ ] Educativo  [ ] Mixto

**KPIs de éxito del negocio** (no son métricas técnicas):

| KPI | Meta | Plazo |
|-----|------|-------|
| | | |
| | | |
| | | |

**Restricciones de negocio** (limitaciones no técnicas que condicionan el diseño):
- _______________
- _______________

**Fuera de alcance** (qué explícitamente NO va en este proyecto):
- _______________
- _______________

---

## SECCIÓN 3 · STAKEHOLDERS & PERSONAS `CRÍTICO`

**Decision Makers** (personas con poder de aprobar o bloquear):

| Nombre | Rol | Qué espera | Qué teme |
|--------|-----|-----------|---------|
| | | | |
| | | | |

**Usuario Primario** (el que más usa el sistema día a día):

- **Persona**: _______________ (nombre ficticio, ej: "Ana la cajera")
- **Perfil**: _______________ (edad, habilidad técnica, contexto)
- **Job to be Done**: "Cuando _______________, quiero _______________ para _______________."
- **Pain points actuales**: _______________
- **Frecuencia de uso**: [ ] Diaria  [ ] Semanal  [ ] Ocasional

---

## SECCIÓN 4 · ARQUITECTURA & LÍMITES DE DOMINIO `CRÍTICO`

**Patrón Arquitectónico**:
- [ ] Hexagonal ligera (Ports & Adapters dentro de monolito)
- [ ] Clean Architecture (domain → application → infrastructure → adapters)
- [ ] Capas FastAPI (domain/ → usecases/ ← ports/ ← adapters/)
- [ ] MVC simple (proyectos pequeños o prototipos)
- [ ] Otro: _______________

**Bounded Contexts / Módulos Core** (marcar los que este sistema POSEE):
- [ ] auth-users           [ ] catalog-products    [ ] orders-sales
- [ ] inventory            [ ] reporting           [ ] notifications
- [ ] billing-payments     [ ] appointments        [ ] users-management
- [ ] Propios: _______________

**Tipo de Ejecución**:
- [ ] sync — request/response
- [ ] async — colas/background jobs
- [ ] event-driven — pub/sub
- [ ] hybrid
- [ ] streaming

**Justificación**: _______________

**Integraciones externas** (sistemas con los que se comunica):

| Sistema | Tipo | Protocolo | Dirección |
|---------|------|-----------|-----------|
| | | | →  /  ← |
| | | | →  /  ← |

---

## SECCIÓN 5 · ESTRATEGIA DE DATOS `CRÍTICO`

**Bases de Datos**:
- Dev/Local: [ ] SQLite  [ ] PostgreSQL Docker  [ ] MongoDB local  [ ] None
- Producción: [ ] PostgreSQL  [ ] MySQL  [ ] MongoDB  [ ] DynamoDB  [ ] None

**ORM**: [ ] Prisma  [ ] GORM  [ ] SQLAlchemy + Alembic  [ ] Mongoose

**IDs**:
- [ ] cuid — URL-safe, colisión-safe (Prisma)
- [ ] UUID — estándar industria
- [ ] AUTO_INCREMENT — simple, expone volumen
- [ ] ULID — sortable + UUID-safe

**Cache**: [ ] Redis  [ ] In-memory  [ ] None &nbsp;&nbsp; TTL default: _______________

**Estado cliente**: [ ] Zustand  [ ] React Context  [ ] Redux  [ ] None

**Data Fetching**: [ ] TanStack Query  [ ] SWR  [ ] HTMX  [ ] Server Components

**Retención de datos**: _______________ días (0 = indefinido)

**Soft-delete**: [ ] Sí (deleted_at)  [ ] No (DELETE físico)

**Backup**:
- Estrategia: [ ] Automatizado diario  [ ] Point-in-time  [ ] Manual  [ ] None
- RPO (máx pérdida de datos aceptable): _______________
- RTO (tiempo máx para restaurar): _______________
- Testing de restore: [ ] Mensual  [ ] Trimestral  [ ] Anual  [ ] Nunca

---

## SECCIÓN 6 · FILE STORAGE & MEDIA `OPCIONAL`

- [ ] **Activar esta sección** (sistema maneja archivos adjuntos o generados)

**Proveedor**: [ ] S3  [ ] GCS  [ ] MinIO (self-hosted)  [ ] Local filesystem  [ ] None

**Tipos de archivo**: _______________

**Acceso**: [ ] Público  [ ] Privado  [ ] Signed URLs  [ ] Mixto

**CDN**: [ ] Sí — Proveedor: _______________  [ ] No

**Tamaño máximo por archivo**: _______________ MB

---

## SECCIÓN 7 · SEARCH & INDEXING `OPCIONAL`

- [ ] **Activar esta sección** (sistema tiene búsqueda full-text o semántica)

**Motor**: [ ] PostgreSQL FTS  [ ] Meilisearch  [ ] Elasticsearch  [ ] Algolia  [ ] None

**Tipo de búsqueda**: [ ] Full-text  [ ] Fuzzy  [ ] Semántica (embeddings)  [ ] Facetas

**Búsqueda vectorial**: [ ] Sí → DB: [ ] pgvector  [ ] Chroma  [ ] Pinecone  [ ] Qdrant

---

## SECCIÓN 8 · FRONTEND, UI & TIEMPO REAL `CRÍTICO si hay UI`

**Renderizado**: [ ] React 19  [ ] Jinja2+HTMX  [ ] React 18 SPA  [ ] Wails  [ ] PyWebview

**UI Library**: [ ] shadcn/ui  [ ] MUI  [ ] AntD  [ ] PicoCSS  [ ] Tailwind headless

**Validación**: [ ] Zod  [ ] Pydantic  [ ] go-validator  [ ] HTMX native

**Tiempo Real**: [ ] Socket.io  [ ] WebSocket  [ ] SSE  [ ] HTMX polling  [ ] None

**Internacionalización**:
- [ ] Activar  — Idioma default: _______________ Idiomas adicionales: _______________
- [ ] No aplica

**Accesibilidad**:
- Nivel WCAG: [ ] AA (mínimo)  [ ] AAA  [ ] No requerido
- Testing: [ ] axe  [ ] Lighthouse  [ ] Manual  [ ] None

---

## SECCIÓN 9 · CONTRATOS, APIs & DOCUMENTACIÓN `CRÍTICO`

**Especificación API**: [ ] OpenAPI 3.1  [ ] FastAPI autodocs  [ ] gRPC  [ ] GraphQL  [ ] None

**Puertos Inbound**: [ ] HTTP/REST  [ ] Server Actions  [ ] WebSocket  [ ] HTMX  [ ] CLI

**Puertos Outbound**: [ ] Repository Interfaces  [ ] PrinterService  [ ] PaymentGateway  [ ] ExternalAPI

**Rate Limiting**: [ ] Sí — Límite: _______________  [ ] No

**ADRs (Architecture Decision Records)**: [ ] Sí → ubicación: _______________  [ ] No

**Runbooks operacionales**: [ ] Sí  [ ] No

---

## SECCIÓN 10 · ESTRATEGIA AI + FALLBACK `OPCIONAL`

- [ ] **Activar esta sección** (sistema integra LLM)

**Casos de uso**: [ ] Generación contenido  [ ] RAG  [ ] Clasificación  [ ] Asistente  [ ] Análisis

**Proveedor**: [ ] OpenAI  [ ] Anthropic  [ ] Google  [ ] Local Ollama  [ ] Multi-router

**Modelo**: _______________ &nbsp; **Modelo fallback**: _______________

**Fallback strategy**: [ ] Retry backoff  [ ] Proveedor secundario  [ ] Cache  [ ] Regla estática

**Guardrails**: [ ] Schema validation  [ ] LLM-as-judge  [ ] Filtro contenido  [ ] Rate limit

**Presupuesto mensual LLM**: USD $_______________

**Prompt management**: [ ] Inline código  [ ] Archivos YAML/MD versionados  [ ] LangSmith  [ ] None

---

## SECCIÓN 11 · ARQUITECTURA DE AGENTES `CRÍTICO si tipo_entrega == "agente_ai"`

- [ ] **Activar esta sección**

**Topología**:
- [ ] Sequential — A→B→C (simple, predecible)
- [ ] Parallel — agentes en paralelo con merge
- [ ] Hierarchical — supervisor → sub-agentes especializados
- [ ] Graph (DAG) — LangGraph / Google ADK style
- [ ] Swarm — peer-to-peer sin orquestador central

**Orquestador**: [ ] LangGraph  [ ] Google ADK  [ ] AutoGen  [ ] CrewAI  [ ] Custom

**Agentes definidos**:

| Nombre | Rol | Tools | Modelo | Max tokens | Permisos |
|--------|-----|-------|--------|-----------|---------|
| | | | | | |
| | | | | | |
| | | | | | |

**Memoria**:
- Short-term: [ ] In-context  [ ] Redis session  [ ] DB episódico
- Long-term: [ ] None  [ ] Vector DB (RAG)  [ ] Relational DB  [ ] Híbrido
- Contexto compartido: [ ] Blackboard  [ ] Message passing  [ ] Event bus

**Context Window**:
- Estrategia: [ ] Full history  [ ] Sliding window  [ ] Summary buffer  [ ] Selective
- Max tokens contexto: _______________ &nbsp; Modelo de resumen: _______________

**Human-in-the-loop**:
- [ ] Activar — Checkpoints: _______________
- Timeout espera: _______________ Canal notificación: _______________

**Evaluación de agentes**:
- [ ] Activar
- Métricas: [ ] Task completion  [ ] Latencia p99  [ ] Costo/run  [ ] Hallucination rate
- Herramienta: [ ] LangSmith  [ ] Helicone  [ ] Phoenix  [ ] Custom

**Seguridad de agentes**:
- [ ] Prompt injection guardrails
- [ ] Scope mínimo de permisos por agente
- [ ] Audit trail de cada decisión automática
- [ ] Rollback de acciones destructivas
- Sandbox: [ ] Docker  [ ] E2B  [ ] Firecracker  [ ] None

**Costos por run**:
- Presupuesto máximo por ejecución: USD $_______________
- Límite de tokens por pipeline: _______________
- [ ] Alerta si se supera presupuesto
- [ ] Detección de runaway (loop infinito) → máx iteraciones: _______________

---

## SECCIÓN 12 · SEGURIDAD, AUTH & COMPLIANCE `CRÍTICO`

**Autenticación**:
- [ ] NextAuth v5  [ ] JWT HttpOnly Cookies  [ ] JWT Headers  [ ] OAuth2/OIDC  [ ] API Key

**Hashing**: [ ] Argon2id (recomendado)  [ ] bcrypt  [ ] scrypt

**Autorización**:
- [ ] RBAC (roles fijos)  [ ] ABAC (atributos dinámicos)  [ ] Permissions granulares  [ ] Ownership

**Multi-tenant**:
- [ ] Single-tenant  [ ] Shared DB + row level (tenant_id)  [ ] Schema por tenant  [ ] DB por tenant

**Encriptación**:
- [ ] AES-256 at rest  [ ] TLS 1.3 in transit  [ ] Field-level PII  [ ] Masking en logs

**Compliance**:
- [ ] LFPDPPP (datos personales México — aplica casi siempre)
- [ ] GDPR  [ ] HIPAA  [ ] PCI-DSS  [ ] SOC2  [ ] ISO 27001  [ ] None

**Auditoría de eventos**: [ ] Activar — Retención: _______________ días

---

## SECCIÓN 13 · TESTING, CALIDAD & HERRAMIENTAS `CRÍTICO`

**Modo TDD**: [ ] Strict  [ ] Flexible  [ ] Test-after  [ ] Minimal

**Cobertura mínima**: Unit: ___%  Integration: [ ] Required  [ ] Optional  [ ] None

**E2E**: [ ] Critical paths  [ ] Full  [ ] None

**Framework**: [ ] Vitest  [ ] go test  [ ] pytest &nbsp; **Package manager**: [ ] pnpm  [ ] go mod  [ ] uv

**Linter**: [ ] ESLint+Prettier  [ ] golangci-lint  [ ] ruff+isort

**Type check**: [ ] tsc --strict  [ ] mypy/pyright  [ ] go vet

---

## SECCIÓN 14 · OBSERVABILIDAD, SLI/SLO & ALERTAS `CRÍTICO`

> ⚠️ Sin SLOs, "¿está fallando?" no tiene respuesta objetiva.

**Contratos de confiabilidad (SLOs)**:
- Uptime target: _______________ % (ej: 99.5%)
- Latencia p99 máxima: _______________ ms
- Error rate máximo: _______________ %
- Error budget mensual: _______________

**Logging**:
- Formato: [ ] JSON estructurado  [ ] Texto plano  [ ] zerolog
- Nivel en prod: [ ] warn  [ ] error &nbsp; Destino: [ ] stdout/Loki  [ ] CloudWatch  [ ] Datadog
- Campos que NUNCA aparecen en logs: _______________

**Métricas**: [ ] Prometheus  [ ] OpenTelemetry  [ ] Cloud-native  [ ] None

**Tracing**: [ ] Sí — Provider: _______________  Sample rate: ___  [ ] No

**Alertas** — canales: [ ] Slack  [ ] PagerDuty  [ ] Email  [ ] Webhook

| Umbral | Valor |
|--------|-------|
| Error rate | > ___% en ___ min |
| Latencia | p99 > ___ ms |
| CPU/Mem | > ___% por ___ min |
| Costo LLM | > $___/día |

---

## SECCIÓN 15 · DEPLOY, RUNTIME & CI/CD `CRÍTICO`

**Plataforma**: [ ] Vercel  [ ] Cloud Run  [ ] Railway  [ ] Fly.io  [ ] Docker Compose  [ ] VPS

**Escalamiento**: [ ] Horizontal  [ ] Vertical  [ ] Serverless  [ ] Manual

**Instancias**: ___ / ___ (min/max) &nbsp; Timeout: ___ seg &nbsp; Health endpoint: _______________

**Pipeline CI/CD** — etapas activas:
- [ ] lint  [ ] type-check  [ ] test  [ ] security-scan  [ ] build
- [ ] deploy-staging  [ ] manual-approval  [ ] deploy-prod  [ ] smoke-test-post-deploy

**Rollback**: [ ] Inmediato  [ ] Blue-green  [ ] Canary  [ ] Feature flag kill-switch

---

## SECCIÓN 16 · ESTRATEGIA MULTI-ENTORNO `OPCIONAL`

- [ ] **Activar** (equipo > 1 o proyecto con staging)

**Entornos**:
- [ ] development — local individual
- [ ] staging — QA y demos, datos sanitizados
- [ ] production — usuarios reales
- [ ] preview — por PR/branch (Vercel/Railway)

**Secretos y variables de entorno**:
- [ ] .env por entorno  [ ] GitHub Secrets  [ ] Vault  [ ] Doppler  [ ] AWS SSM
- Secretos en git: **NUNCA** ✗

---

## SECCIÓN 17 · NOTIFICATIONS & COMUNICACIONES `OPCIONAL`

- [ ] **Activar** (sistema envía notificaciones a usuarios)

**Canales**: [ ] Email  [ ] SMS  [ ] Push Web  [ ] Push Móvil  [ ] WhatsApp  [ ] Telegram

**Proveedores**:
- Email: [ ] SendGrid  [ ] Resend  [ ] SES  [ ] SMTP propio
- SMS: [ ] Twilio  [ ] Vonage  [ ] Infobip
- WhatsApp: [ ] Twilio  [ ] Meta Cloud API  [ ] N8N

**Frecuencia límite**: [ ] Sí — límite: _______________  [ ] No

**Opt-out / Unsubscribe**: [ ] Sí (requerido LFPDPPP)  [ ] No aplica

---

## SECCIÓN 18 · CAPACITY PLANNING `OPCIONAL`

- [ ] **Activar** (proyecto con expectativas de escala definidas)

| Métrica | Actual | 3 meses | 12 meses |
|---------|--------|---------|---------|
| Usuarios totales | | | |
| Usuarios concurrentes peak | | | |
| Requests/segundo promedio | | | |
| Tamaño DB (GB) | | | |

**Eventos de peak traffic**: _______________

---

## SECCIÓN 19 · EVOLUCIÓN, FASES & PRIORIDADES `CRÍTICO`

**API Versioning**: [ ] Semver URL (/v1/)  [ ] Header  [ ] Date-based  [ ] None

**Schema migration**: [ ] Expand & Contract  [ ] Blue-green DB  [ ] Big-bang

**Feature Flags**: [ ] Unleash  [ ] LaunchDarkly  [ ] env_var  [ ] None

**Complexity Score (1-10)**: ___ &nbsp; Factores: _______________

**Top 3 Riesgos**:
1. Riesgo: _______________ → Mitigación: _______________
2. Riesgo: _______________ → Mitigación: _______________
3. Riesgo: _______________ → Mitigación: _______________

**Enfoque de entrega**: [ ] MVP iterativo  [ ] Vertical slice  [ ] Horizontal layer

**Fases**:

| Fase | Alcance | Fecha objetivo | Criterio de éxito |
|------|---------|---------------|-----------------|
| Fase 1 – MVP | | | |
| Fase 2 – Core | | | |
| Fase 3 – Scale | | | |

**Prioridades**:
- P0 (bloqueante del MVP): _______________
- P1 (importante): _______________
- P2 (nice-to-have): _______________

---

## SECCIÓN 20 · HARDWARE FÍSICO `OPCIONAL`

- [ ] **Activar** (sistema controla periféricos físicos)

- [ ] Impresora térmica → Lib: ___  Modelo: ___  Precio MXN: $___
- [ ] Báscula serial → Lib: ___  Protocolo: ___  Modelo: ___
- [ ] Biométrico → Tipo: ___  Lib: ___  Modelo: ___

---

## SECCIÓN 21 · DOMAIN MODELING `OPCIONAL (activar si complexity > 5)`

- [ ] **Activar**

**Entidades**: _______________
**Value Objects**: _______________
**Aggregates**: _______________

**Invariantes de negocio** (reglas que NUNCA pueden violarse):
- _______________
- _______________

**Eventos de dominio**: [ ] Sí → lista: _______________  [ ] No

---

## SECCIÓN 22–24 · CONSISTENCIA, RESILIENCIA & PERFORMANCE `OPCIONAL`

**Consistencia**: [ ] Fuerte (ACID)  [ ] Eventual  [ ] Mixta

**Estrategia**: [ ] Transacciones DB  [ ] Saga coreografía  [ ] Saga orquestación

**Concurrencia**: [ ] Optimistic locking  [ ] Pessimistic locking  [ ] Ninguna

**Resiliencia**:
- [ ] Retry backoff  [ ] Circuit breaker  [ ] Timeout  [ ] Bulkhead  [ ] Graceful degradation
- Fallback general: _______________

**Performance**:
- Caching: [ ] Read-through  [ ] Write-through  [ ] Cache-aside  [ ] None
- Pagination: [ ] Offset  [ ] Cursor
- Índices explícitos: [ ] Sí  [ ] No

---

## SECCIÓN 25 · MODELO DE ERRORES `CRÍTICO`

**Formato**: [ ] RFC 7807 (estándar industria)  [ ] Custom

**Tipos**: [ ] Domain errors  [ ] Validation errors  [ ] Auth errors  [ ] Infra errors  [ ] AI errors

**Error tracking**: [ ] Sentry  [ ] Glitchtip (self-hosted)  [ ] None

---

## SECCIÓN 26 · SEGURIDAD AVANZADA `OPCIONAL (activar si criticalidad >= high)`

- [ ] Threat modeling: [ ] STRIDE  [ ] Básico  [ ] None
- [ ] OWASP Top 10 review antes de release
- [ ] Dependency scan (Snyk / Safety / Dependabot)
- [ ] Secret scan en repo (TruffleHog / git-secrets)
- [ ] Penetration test profesional

---

## SECCIÓN 27 · CONFIGURACIÓN & SECRETOS `CRÍTICO`

**Estrategia de config**: [ ] .env por entorno  [ ] Config por entorno (YAML)  [ ] Config service

**Gestión de secretos**: [ ] env_vars  [ ] GitHub Secrets  [ ] HashiCorp Vault  [ ] Doppler  [ ] AWS SSM

**Rotación de secretos**: [ ] Sí — frecuencia: _______________  [ ] No

---

## SECCIÓN 28 · DATA LIFECYCLE & CLASIFICACIÓN `OPCIONAL`

- [ ] **Activar** (sistema maneja datos personales o datos con compliance)

**Clasificación de datos**:

| Tipo de dato | Nivel | Ley aplicable |
|-------------|-------|--------------|
| | público / interno / confidencial / restringido | lfpdppp / gdpr / hipaa / none |
| | | |

**Operaciones**: [ ] Archivado  [ ] Anonimización  [ ] Eliminación legal (derecho al olvido)  [ ] Pseudonimización

---

## SECCIÓN 29 · INCIDENT RESPONSE & ON-CALL `OPCIONAL (activar si criticalidad >= medium)`

- [ ] **Activar**

- [ ] Runbooks documentados → ubicación: _______________
- [ ] On-call activo → Herramienta: _______________ Rotación: _______________

**Escalación**:
- Nivel 1 (15 min): _______________
- Nivel 2 (1h): _______________
- Nivel 3 (4h): _______________

- [ ] Post-mortem blameless después de incidentes P0/P1

---

## SECCIÓN 30 · TECHNICAL DEBT STRATEGY `OPCIONAL`

- [ ] **Activar**

- [ ] Tracking: [ ] GitHub Issues  [ ] Jira  [ ] Notion  [ ] Ninguno
- Presupuesto para refactor: _______________
- Dependency updates: [ ] Dependabot  [ ] Renovate  [ ] Manual  [ ] Ninguno

---

## SECCIÓN 31 · LEGAL & COMPLIANCE `OPCIONAL (activar si hay usuarios externos)`

- [ ] Términos de Servicio requeridos
- [ ] Política de Privacidad publicada
- [ ] Aviso de Privacidad (LFPDPPP — obligatorio en México si hay datos personales)
- [ ] DPA con proveedores externos (AWS, SendGrid, Stripe, etc.)
- [ ] Auditoría de licencias OSS — licencias prohibidas: _______________

**Propiedad del código**: [ ] Propietario  [ ] MIT  [ ] Apache 2.0  [ ] GPL  [ ] Otro: _______________

---

## SECCIÓN 32 · UX & FLUJOS `OPCIONAL (omitir si api_backend)`

**User Journeys principales**:
1. _______________
2. _______________

**Estados UI a diseñar**:
- [ ] Loading  [ ] Empty state  [ ] Error state  [ ] Success  [ ] Offline

**Dark mode**: [ ] Sí  [ ] No &nbsp; **Wireframes**: [ ] Sí  [ ] No

---

## SECCIÓN 33 · DEVELOPER EXPERIENCE `OPCIONAL`

- [ ] Repo: [ ] Monorepo  [ ] Multirepo
- [ ] Git strategy: [ ] Trunk-based  [ ] Gitflow  [ ] GitHub Flow
- [ ] Convenciones: [ ] Conventional Commits  [ ] Gitmoji  [ ] Ninguno
- Tiempo setup nuevo dev (objetivo < 15 min): ___ min
- [ ] Makefile / Taskfile con comandos estándar
- [ ] CONTRIBUTING.md
- [ ] Branch protection en main

---

## SECCIÓN 34 · EVOLUCIÓN DEL SISTEMA `CRÍTICO`

**Compatibilidad**: [ ] Backward compatible  [ ] Breaking changes permitidos con aviso

**Estrategia**: [ ] Strangler pattern  [ ] Refactor incremental  [ ] Big rewrite (evitar)

---

## SECCIÓN 35 · COSTOS & FINOPS `OPCIONAL`

- [ ] **Activar** (proyecto con costos de nube / SaaS)

**Presupuesto mensual total**: USD $_______________

| Componente | Costo estimado/mes |
|------------|-------------------|
| Hosting | $ |
| DB | $ |
| CDN / Storage | $ |
| LLM APIs | $ |
| Email / SMS | $ |
| Monitoreo | $ |
| **Total** | **$** |

- [ ] Alerta si gasto supera: USD $_______________/mes
- [ ] Dependo de free tiers → servicios: _______________

---

## NOTAS ADICIONALES

_____________________________________________
_____________________________________________

---

> **SIGUIENTE PASO**: Con este brief completo, ejecutar `brief-to-prd` para generar el PRD estructurado.
> Las secciones críticas (1-4, 9, 12, 14, 15, 25, 27, 34) deben estar completas para continuar.
