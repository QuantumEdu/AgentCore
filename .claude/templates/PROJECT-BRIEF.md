# PROJECT-BRIEF - [Nombre del Proyecto]

**Fecha**: [YYYY-MM-DD]
**Autor**: [Nombre]
**Versión**: 1.0

---

## 1️⃣ Contexto & Stack Base

**Nombre del Sistema**: [Nombre]

**Tipo de Entrega**:
- [ ] Web SaaS / Dashboard
- [ ] App Desktop (instalable)
- [ ] Híbrido (Desktop + Admin Web)
- [ ] API/Backend only

**Stack Principal**:
- [ ] Next.js 15 (Monolito full-stack: React 19 + Prisma + NextAuth)
- [ ] Go + Fiber + Wails v2 (Backend + Desktop/Web)
- [ ] FastAPI Stack A: SSR (Jinja2 + HTMX + PicoCSS)
- [ ] FastAPI Stack B: SPA (React 18 + TS + MUI)
- [ ] FastAPI Stack C: Desktop (PyWebview + PyInstaller)

**Criticalidad**:
- [ ] low
- [ ] medium
- [ ] high
- [ ] critical

**Team Size**:
- [ ] 1
- [ ] 2-5
- [ ] 6-15
- [ ] 15+

**Timeframe**:
- [ ] MVP-2sem
- [ ] short-1mes
- [ ] medium-3mes
- [ ] long-6mes+

## 2️⃣ Arquitectura & Límites de Dominio

**Patrón Arquitectónico**:
- [ ] Hexagonal ligera (Ports & Adapters dentro de monolito)
- [ ] Clean Architecture (domain → application → infrastructure → adapters)
- [ ] Capas FastAPI (domain/ → usecases/ ← ports/ ← adapters/)
- [ ] Otro: [Especificar]

**Bounded Contexts / Módulos Core** (marcar los aplicables):
- [ ] auth-users
- [ ] catalog-products
- [ ] orders-sales
- [ ] inventory
- [ ] reporting
- [ ] notifications
- [ ] Otro: [Especificar]

**Tipo de Ejecución**:
- [ ] sync (request/response)
- [ ] async (colas/background)
- [ ] event-driven (pub/sub)
- [ ] hybrid
- [ ] streaming/real-time

**Justificación**: [Explicar por qué este tipo de ejecución]

## 3️⃣ Estrategia de Datos

**Bases de Datos**:
- **Dev/Local**: [ ] SQLite (go-sqlite3 / aiosqlite) [ ] Dockerized PostgreSQL [ ] MongoDB Atlas [ ] None
- **Producción**: [ ] PostgreSQL 16+ [ ] MySQL/MariaDB [ ] MongoDB [ ] DynamoDB [ ] None (stateless)

**ORM & Migraciones**:
- [ ] Prisma 5.x + prisma migrate
- [ ] GORM + golang-migrate
- [ ] SQLAlchemy 2.0 (Mapped[]) + Alembic

**IDs**:
- [ ] cuid() (Prisma)
- [ ] UUID v4 (Go)
- [ ] AUTO_INCREMENT / INTEGER (FastAPI v1)

**Cache & Estado Global**:
- **Cache Server**: [ ] Redis (ioredis / go-redis / python-redis) [ ] In-memory [ ] None
- **Estado Cliente**: [ ] Zustand v4 [ ] React Context [ ] Redux Toolkit [ ] None
- **Data Fetching**: [ ] TanStack Query v5 [ ] SWR [ ] HTMX (hx-get/hx-swap) [ ] Server Components (Next.js)

**Retención & Backup**:
- **Retención**: [30 | 90 | 180 | 365 | indefinite] días
- **Soft-delete**: [yes | no]
- **Backup**: [automated-daily | point-in-time | manual]

## 4️⃣ Frontend, UI & Tiempo Real

**Renderizado / Interfaz**:
- [ ] React 19 (Server + Client Components)
- [ ] Jinja2 SSR + HTMX + PicoCSS
- [ ] React 18 SPA + MUI
- [ ] Wails v2 WebView
- [ ] PyWebview Shell

**Validación & Formularios**:
- [ ] Zod (compartido front/back) + React Hook Form
- [ ] Pydantic v2
- [ ] go-playground/validator
- [ ] HTMX native validation

**Tiempo Real / WebSocket**:
- [ ] Socket.io + Redis adapter
- [ ] WebSocket nativo (FastAPI/Go)
- [ ] Server-Sent Events (SSE)
- [ ] HTMX polling (hx-trigger="every 30s")
- [ ] None

## 5️⃣ Contratos, APIs & Documentación

**Especificación API**:
- [ ] OpenAPI 3.1 (auto-generado)
- [ ] Swagger UI via swaggo(Go)
- [ ] FastAPI/docs (auto)
- [ ] Next.js API Routes como contrato
- [ ] None

**Ubicación**: ./specs/ | ./docs/ | inline comments | URL externa

**Puertos (Interfaces / Contracts)**:
- **Inbound**: [ ] HTTP/REST [ ] Server Actions [ ] WebSocket [ ] HTMX endpoints [ ] CLI
- **Outbound**: [ ] Repository Interfaces [ ] PrinterService [ ] PaymentGateway [ ] ExternalAPI_Client

**Regla de aislamiento**: [ ] Domain nunca importa infra/frameworks [ ] UseCases solo conocen ports [ ] Tenant filter automático en BaseRepository

**Anti-Corruption Layer (ACL)**:
- Legacy/Externos: [ ] No [ ] Sí → Sistemas: [Especificar]
- Estrategia: [ ] Adapter [ ] Facade [ ] Translator+Queue [ ] Sidecar

## 6️⃣ Estrategia AI + Fallback

**Integración LLM**:
- [ ] No
- [ ] Sí → Casos: [ ] Generación contenido [ ] RAG/Búsqueda [ ] Clasificación [ ] Asistente [ ] Otro: [Especificar]

**Proveedor**: [ ] OpenAI [ ] Anthropic [ ] Google [ ] Local [ ] Multi-router

**Fallback Strategy**:
- [ ] Reintentar backoff (max [n])
- [ ] Proveedor secundario
- [ ] Cache TTL
- [ ] Regla estática
- [ ] Degradación elegante

**Guardrails**: [ ] Schema validation [ ] LLM-as-Judge [ ] Filtro contenido [ ] Rate limit [n] req/min

## 7️⃣ Seguridad, Auth & Compliance

**Autenticación & Hashing**:
- **Auth**: [ ] NextAuth v5 (Credentials/PIN) [ ] JWT + HttpOnly Cookies [ ] JWT Headers [ ] OAuth2/OIDC [ ] mTLS
- **Hashing**: [ ] bcrypt v5 [ ] Argon2id (argon2-cffi) [ ] golang.org/x/crypto/bcrypt

**Autorización & Multi-Tenant**:
- **AuthZ**: [ ] RBAC [ ] ABAC [ ] Permissions granulares [ ] Ownership-based
- **Tenant**: [ ] session.user.tenantId [ ] tenant_idUUID en entidades [ ] sucursal_id filtro automático [ ] Single-tenant

**Protección & Compliance**:
- **Encriptación**: [ ] AES-256 at rest [ ] TLS 1.3 in transit [ ] Field-level PII [ ] Masking en logs
- **Compliance**: [ ] GDPR [ ] HIPAA [ ] SOC 2 [ ] PCI-DSS [ ] None
- **Auditoría**: [ ] zerolog middleware [ ] FastAPI audit endpoints [ ] Next.js server logs [ ] Retención: [30 | 90 | 365] días

## 8️⃣ Testing, Calidad & Herramientas

**Estrategia TDD & Cobertura**:
- **Modo**: [ ] strict [ ] flexible [ ] test-after [ ] minimal
- **Cobertura mínima**: Unit [70% | 80% | 90%] | Integration [required | optional | none] | E2E [critical-paths | full | none]

**Frameworks & Linters**:
- **Testing**: [ ] Vitest + Testing Library [ ] go test + testify [ ] pytest + asyncio (solo usecases/)
- **Package Manager**: [ ] pnpm/npm [ ] go mod [ ] uv (Python)
- **Linter/Format**: [ ] ESLint + Prettier [ ] golangci-lint+gofmt [ ] ruff+isort
- **Type Check**: [ ] tsc --strict [ ] mypy/pyright [ ] go vet

**Validación de Contratos & Docs**:
- [ ] openapi-validator en CI
- [ ] swag init en pipeline
- [ ] FastAPI auto-docs check
- [ ] HTMX endpoint tests
- [ ] None

## 9️⃣ Observabilidad & Alertas

**Logging**:
- **Formato**: [ ] JSON estructurado [ ] Texto plano [ ] zerolog structured
- **Nivel Prod**: [warn | error]
- **Destino**: [stdout/Loki | Cloud-native | Datadog/NR]

**Métricas & Tracing**:
- **Framework**: [ ] Prometheus [ ] OpenTelemetry [ ] Cloud-native [ ] None
- **Key Metrics**: [ ] request_duration [ ] error_rate [ ] business_metric [ ] queue_depth
- **Tracing**: Habilitado [yes | no] | Provider: [Jaeger | Zipkin | Datadog] | Sample: [0.01 | 0.1 | 1.0]

**Alerting**:
- **Canales**: [ ] Slack [ ] PagerDuty [ ] Email [ ] Webhook
- **Umbrales**: Error >[n]% en [n]min | Latencia p99 >[n] | CPU/Mem >[n]%

## 🔟 Deploy, Runtime & CI/CD

**Plataforma & Runtime**:
- [ ] Vercel
- [ ] Google Cloud Run
- [ ] Railway
- [ ] Kubernetes (EKS/GKE)
- [ ] Docker Compose
- [ ] Binario Nativo (Wails/PyInstaller)

**Escalado & Base**:
- **Estrategia**: [ ] Horizontal [ ] Vertical [ ] Serverless [ ] Manual
- **Instancias**: [n] / [n] | Timeout: [30s | 60s | 300s] | Health: [/health | /ready | /ping]

**Pipeline CI/CD**:
- **Proveedor**: [ ] GitHub Actions [ ] GitLab CI [ ] CircleCI [ ] Jenkins [ ] ArgoCD/Flux
- **Etapas**: [ ] lint [ ] test [ ] type-check [ ] security-scan [ ] build [ ] deploy-staging [ ] manual-approval [ ] deploy-prod
- **Rollback**: [ ] Immediate [ ] Blue-green [ ] Canary [ ] Feature flag kill-switch

## 1️⃣1️⃣ Evolución, Versionado, Complejidad & Hardware

**API Versioning & Migraciones**:
- **Versiones**: [ ] Semver URL (/v1/) [ ] Header [ ] Date-based [ ] None
- **Deprecación**: Aviso [n] días | Sunset +[n] días | Comunicación: [changelog | email | in-app | docs]
- **Schema**: [ ] Expand & Contract [ ] Dual-write [ ] Big-bang [ ] Blue-green DB

**Feature Flags**:
- **Tool**: [ ] Unleash [ ] LaunchDarkly [ ] Flagsmith [ ] env-var
- **Rollout**: [ ] % usuarios [ ] segmento [ ] Canary [ ] Kill switch

**Complejidad & Mitigación**:
- **Score (1-10)**: [n]
- **Factores críticos**: Lógica | Integraciones | Datos | Seguridad
- **Top 3 Riesgos + Mitigación**:
  1. [Riesgo] → [Mitigación]
  2. [Riesgo] → [Mitigación]
  3. [Riesgo] → [Mitigación]
- **Enfoque Entrega**: [ ] MVP iterativo [ ] Vertical slice [ ] Horizontal layer [ ] Big-bang

**Hardware Físico** (si aplica):
- **Impresora**: [ ] node-escpos [ ] go-escpos [ ] python-escpos [ ] None
- **Báscula/Serial**: [ ] pyserial [ ] go.bug.st/serial [ ] WebUSB [ ] None
- **Biométrico/Lector**: [ ] ctypes DLL [ ] HID API [ ] Serial/RS232 [ ] None
- **Modelo/Precio MXN**: [Especificar]

---

## Notas Finales

- Todas las secciones son opcionales excepto las marcadas como **CRÍTICAS**
- Marca con [x] las opciones aplicables
- Rellena _____ con valores específicos
- Elimina las secciones no usadas
- Guarda este archivo como `PROJECT-BRIEF-FULL.yaml` y úsalo como input para el skill `brief-to-prd`