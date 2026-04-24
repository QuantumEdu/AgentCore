---
name: prd-fastapi
description: Genera PRDs completos y profesionales para sistemas de software usando el stack FastAPI + Python + SQLAlchemy + Jinja2/HTMX o React. Usar SIEMPRE que el usuario pida un PRD, documento de requerimientos o especificación de sistema con Python como backend. También activar cuando el usuario diga "crea el PRD", "necesito el PRD", "genera los requerimientos", "especificación del sistema" o cuando describa un sistema con FastAPI, SQLAlchemy, Pydantic, Alembic, Jinja2, PyWebview, o mencione VitaCare, Clean Architecture Python. Si el usuario quiere rapidez de desarrollo o ya domina Python, sugerir este stack. Activar también para apps desktop Python con PyWebview o sistemas clínicos/médicos donde Python es la elección natural por su ecosistema de librerías.
---

# PRD Generator — Stack FastAPI + Python + SQLAlchemy

Genera PRDs completos, técnicos y vendibles para sistemas de software usando el stack FastAPI moderno. Basado en proyectos reales: VitaCare, VetCare, Clínica Médica del Valle.

## Stack de referencia

### Stack A — Web SSR (apps internas, dashboards, sistemas clínicos)
```
Package mgr: uv
Backend:     FastAPI 0.115+ + Python 3.12+
ORM:         SQLAlchemy 2.0 (Mapped[], mapped_column)
Migraciones: Alembic 1.13+
Validación:  Pydantic v2 — BaseModel + BaseSettings
Auth:        Argon2id (argon2-cffi) + JWT (python-jose)
Frontend:    Jinja2 3.1+ + PicoCSS 2.x + HTMX 2.0 (CDN)
Admin:       SQLAdmin 0.16+
Testing:     pytest + pytest-asyncio — 80% coverage mínimo
Linter:      ruff
Export:      openpyxl
HTTP client: httpx
DB dev:      SQLite (aiosqlite)
DB prod:     PostgreSQL 16+
```

### Stack B — SPA moderna (producto vendible, UI táctil)
```
Backend:     FastAPI — igual que Stack A
Frontend:    React 18 + TypeScript 5 + Vite 5 + MUI v6
Fetching:    TanStack Query v5
WS:          WebSocket nativo FastAPI — tiempo real
Forms:       React Hook Form + Zod
Estado:      Zustand v4
```

### Stack C — Desktop (app instalada en PC)
```
Base:        FastAPI corriendo en hilo local (localhost:8765)
Shell:       PyWebview — ventana nativa, WebView del SO
Empaquetado: PyInstaller — .exe standalone ~50–80 MB
Impresora:   python-escpos
Hardware:    pyserial — báscula, lector serial
Biométrico:  ctypes → DLL (DigitalPersona, etc.)
```

## Proceso de generación

### Paso 1 — Elegir el sub-stack correcto

Preguntar si no está claro:

| Si el sistema es... | Sub-stack recomendado |
|---|---|
| App interna, dashboard, sistema clínico/médico | Stack A — Jinja2 + HTMX |
| Producto vendible con UI táctil (POS, restaurante) | Stack B — FastAPI + React |
| App desktop instalada en PC | Stack C — PyWebview |
| Híbrido: app instalada + admin web | Stack C para caja + Stack A/B para admin |

**Regla:** Si el usuario ya mencionó PyWebview o app de escritorio → Stack C. Si mencionó React o MUI → Stack B. Si mencionó Jinja2 o HTMX → Stack A.

### Paso 2 — Recopilar contexto

Si el usuario ya tiene un brief completo, leerlo primero:
- **YAML**: `.claude/templates/PROJECT-BRIEF-FULL-Quantum.yaml` (35 secciones, parsing automático)
- **Markdown**: `.claude/templates/PROJECT-BRIEF-FULL.md` (35 secciones, llenado manual)

Preguntar SOLO las secciones CRÍTICAS que estén vacías. En orden de prioridad:

**Sección 2 — Negocio (CRÍTICO):**
- ¿Cuál es el problema concreto que resuelve el sistema y a quién afecta?
- ¿Cliente único o producto SaaS para vender?
- ¿Cuántos usuarios simultáneos?
- ¿Necesita funcionar offline?

**Sección 11 — Agentes AI (si tipo_entrega == agente_ai):**
- ¿Qué topología de agentes? (Sequential / Hierarchical / Graph)
- ¿Presupuesto máximo por run?

**Técnico (Secciones 4–10):**
- ¿Qué módulos son core? ¿Qué puede esperar para v2?
- ¿Hay hardware físico? (impresora, báscula, lector) → Sección 20
- ¿Multi-sucursal desde v1? → afecta multi-tenant en Sección 12

### Paso 3 — Estructura del PRD

Generar SIEMPRE estas secciones:

```
1.  Resumen Ejecutivo
    - Descripción del producto
    - Objetivos y non-goals
    - Contexto del negocio (tabla)

2.  Stack Tecnológico
    - pyproject.toml completo con versiones reales
    - Tabla por capa con justificación
    - Por qué Argon2id sobre bcrypt
    - Por qué PicoCSS sobre Tailwind (Stack A)
    - Por qué PyWebview sobre Electron (Stack C)

3.  Arquitectura del Sistema — Hexagonal (Ports & Adapters, no rígida)
    - Diagrama ASCII hexagonal:
      [HTTP Router] → [Application Services / Use Cases] → [Domain]
                                                              ↑
                                              [Repository Interface / Port]
                                                              ↑
                                              [SQLAlchemy Adapter / Infra]
    - Puerto de entrada (Driving): FastAPI router — adapter HTTP
    - Puerto de salida (Driven): AbstractRepository — interfaz Python pura
    - Regla de oro: domain/ y usecases/ nunca importan FastAPI, SQLAlchemy ni frameworks
    - Beneficio práctico: puedes cambiar SQLAlchemy por otro ORM sin tocar la lógica de negocio
    - Flujo de un request típico con los puertos explícitos
    - Patrones de diseño aplicados (ver sección de referencia al final)

4.  Estructura de Directorios
    - Árbol completo del proyecto
    - Descripción de cada archivo/carpeta clave

5.  Módulos y Requisitos Funcionales
    - H3 por módulo
    - Tabla ID | Función | Descripción | Prioridad
    - Prioridades: Crítica / Alta / Media / Baja

6.  Modelo de Dominio Python
    - Clases SQLAlchemy con Mapped[] y mapped_column
    - Relaciones con relationship()
    - Campos comunes: created_at, updated_at, deleted_at
    - Soft delete en entidades principales

7.  Enums y Constantes
    - Clases Python Enum para todos los estados y roles

8.  Seguridad
    - Argon2id con argon2-cffi
    - JWT con python-jose
    - Dependency get_current_user
    - require_role(*roles) decorator

9.  Módulos específicos del stack
    - Stack A: HTMX — cómo funciona, ejemplos de hx-* attributes
    - Stack B: TanStack Query hooks tipados
    - Stack C: PyWebview main.py — arranque FastAPI + ventana
    - Hardware: python-escpos, pyserial si aplica

10. Configuración
    - Pydantic BaseSettings completo
    - .env.example

11. Requisitos No Funcionales
    - Rendimiento, disponibilidad, seguridad, usabilidad

12. Historias de Usuario
    - US-001 a US-00N con criterios de aceptación [ ]

12.1 Domain Modeling (opcional, si complexity_score >= 4)
    - Entidades de dominio (no modelos de DB)
    - Value Objects (Email, Dinero, RFC, etc.)
    - Eventos de dominio
    - Aggregates y Aggregate Roots
    - Ejemplos de código Python con Pydantic

12.2 Modelo de Errores (opcional, si complexity_score >= 4)
    - Jerarquía de excepciones personalizadas
    - Códigos de error estandarizados
    - Manejo de errores en FastAPI (exception handlers)
    - Respuestas de error consistentes
    - Ejemplos de código Python

12.3 Consistencia & Transacciones (opcional, si complexity_score >= 7)
    - Patrón Unit of Work
    - Transacciones atómicas
    - Manejo de concurrencia (optimistic locking)
    - Eventual consistency si aplica
    - Ejemplos de código Python con SQLAlchemy

12.4 Performance & Escalabilidad (opcional, si complexity_score >= 9)
    - Estrategias de caching (Redis, in-memory)
    - Query optimization (N+1, índices)
    - Paginación y filtering
    - Async/await para I/O
    - Horizontal scaling (load balancer, containers)
    - Métricas y monitoreo

12.5 Configuración & Secretos (opcional, si complexity_score >= 7)
    - Separación de config por ambiente (dev/staging/prod)
    - Manejo de secretos (vault, env variables)
    - Configuración de DB por ambiente
    - Feature flags
    - Ejemplos de .env.example y config.yaml

12.6 UX & Flujos (opcional, si complexity_score >= 4)
    - Diagramas de flujo de usuario
    - Estados de las entidades (state machines)
    - Validaciones de negocio
    - Mensajes de error amigables
    - Accesibilidad (a11y)

12.7 Data Lifecycle (opcional, si complexity_score >= 9)
    - Retención de datos (policies)
    - Archivo y backup
    - Anonimización / GDPR compliance
    - Soft delete vs hard delete
    - Auditoría y logging
    - Ejemplos de políticas de retención

13. Roles y Permisos
    - Tabla Módulo | rol1 | rol2 | ... por todos los roles

14. Multi-sucursal (si aplica)
    - BaseRepository con filtro sucursal_id

15. Testing
    - pytest con 80% coverage sobre app/usecases/
    - Tests críticos obligatorios listados

16. GitHub Actions
    - .yml completo con test + lint + build

17. Docker
    - Dockerfile con uv
    - docker-compose.yml con db

18. Roadmap de Desarrollo
    - Fases con entregables claros

19. Riesgos y Mitigación

20. Hardware Recomendado (si aplica)

21. Plan de Capacitación (si aplica)

22. Modelo de Negocio SaaS (si es producto vendible)
    - Precios en MXN + SLA

23. Glosario
```

### Paso 4 — Decisiones técnicas automáticas

Aplicar SIEMPRE sin preguntar:

| Decisión | Valor FastAPI |
|---|---|
| Package manager | uv (no pip/pipenv) |
| IDs | INTEGER autoincrement en v1 (no UUID) |
| Hash passwords | Argon2id (argon2-cffi) — no bcrypt |
| Auth | JWT en cookies HttpOnly (SSR) o headers (SPA) |
| ORM syntax | Mapped[] y mapped_column (SQLAlchemy 2.0) — no Column() legacy |
| Soft delete | deleted_at en todas las entidades principales |
| Campos comunes | created_at + updated_at en todas las tablas |
| Arquitectura | Hexagonal ligera: domain/ → usecases/ ← repositories/(port) ← data/(adapter) ← web/ |
| Patrones de diseño | Repository, Factory, Strategy, Observer — ver sección referencia |
| Admin panel | SQLAdmin para superadmin técnico |
| Testing | pytest sobre usecases/ únicamente — no testear FastAPI |
| CSS (SSR) | PicoCSS — semántico, sin clases |
| Interactividad SSR | HTMX — no React, no JavaScript manual |

### Paso 5 — Patrones de código clave

#### Modelo SQLAlchemy 2.0 (Mapped[])
```python
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

class Entidad(Base):
    __tablename__ = "entidades"
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(150), nullable=False)
    campo_opcional: Mapped[str | None] = mapped_column(String(255), nullable=True)
    activo: Mapped[bool] = mapped_column(Boolean, default=True)
    deleted_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(default=datetime.utcnow, onupdate=datetime.utcnow)
```

#### Argon2id (argon2-cffi)
```python
from argon2 import PasswordHasher
ph = PasswordHasher()
hash = ph.hash("contraseña")
ph.verify(hash, "contraseña")  # True o VerifyMismatchError
```

#### HTMX fragment endpoint
```python
@router.get("/htmx/entidades", response_class=HTMLResponse)
async def htmx_entidades(request: Request, uc: EntidadUseCase = Depends()):
    items = await uc.listar()
    return templates.TemplateResponse("components/lista_entidades.html", {
        "request": request, "items": items
    })
```

```html
<!-- Template usa HTMX para actualizar sin recargar -->
<div hx-get="/htmx/entidades"
     hx-trigger="every 30s"
     hx-target="#lista-entidades">
  {% include "components/lista_entidades.html" %}
</div>
```

#### PyWebview + FastAPI local
```python
# main.py — Stack C desktop
import threading, webview, uvicorn, time
from app.main import app as fastapi_app

def start_server():
    uvicorn.run(fastapi_app, host="127.0.0.1", port=8765, log_level="warning")

if __name__ == "__main__":
    t = threading.Thread(target=start_server, daemon=True)
    t.start()
    time.sleep(1.5)
    window = webview.create_window("App", "http://127.0.0.1:8765",
                                    width=1280, height=800)
    webview.start()
```

#### BaseRepository con filtro automático
```python
class BaseRepository:
    def __init__(self, db: AsyncSession, sucursal_id: int | None = None):
        self.db = db
        self.sucursal_id = sucursal_id

    def _filtrar(self, query, model):
        if self.sucursal_id:
            return query.where(model.sucursal_id == self.sucursal_id)
        return query  # admin ve todo
```

#### WhatsApp link sin API
```python
from urllib.parse import quote
def link_whatsapp(telefono: str, mensaje: str) -> str:
    tel = telefono.replace("+","").replace(" ","").replace("-","")
    if not tel.startswith("52"): tel = f"52{tel}"
    return f"https://wa.me/{tel}?text={quote(mensaje)}"
```

### Paso 6 — Adaptaciones por dominio

**Sistema clínico / médico (VitaCare style):**
- Roles: admin, medico, recepcionista, paciente
- Expediente con soft delete
- Citas con máquina de estados
- Recetas con items
- Stack A (Jinja2 + HTMX) — no necesita React

**Veterinaria:**
- Cliente → muchas Mascotas (multi-especie)
- Hospitalización con CuidadoTurno
- Vacunas con próxima_dosis
- AdjuntoExpediente (PDF/imagen, max 10 MB)
- Portal dueños con login separado (/portal/)

**POS desktop (báscula, impresora):**
- Stack C (PyWebview)
- python-escpos para tickets
- pyserial para báscula serial
- better-sqlite3 / aiosqlite para SQLite local
- PyInstaller para .exe

**Sistema web con inventario:**
- Alertas de stock mínimo y vencimientos
- Exportación Excel con openpyxl
- Reportes accionables del día

### Paso 7 — Calidad del PRD

Verificar antes de entregar:

- [ ] pyproject.toml con versiones reales y actuales
- [ ] Modelos con Mapped[] (SQLAlchemy 2.0) — no Column() legacy
- [ ] Argon2id — no bcrypt
- [ ] deleted_at en entidades principales
- [ ] BaseRepository con filtro sucursal/tenant
- [ ] Sección de HTMX si es Stack A
- [ ] main.py PyWebview si es Stack C
- [ ] Dockerfile usando uv
- [ ] Tests sobre usecases/ únicamente
- [ ] Roles y permisos como tabla completa
- [ ] Glosario con términos del dominio
- [ ] Arquitectura hexagonal reflejada en estructura de directorios (domain/ aislado)
- [ ] Al menos 1 patrón de diseño documentado en sección de patrones

### Paso 8 — Formato de entrega

- Generar el PRD en **Markdown descargable** via `create_file`
- Ruta: `/mnt/user-data/outputs/PRD_{NombreSistema}_FastAPI.md`
- Presentar con `present_files`
- Resumen de 3–5 puntos clave después del archivo

---

## Referencia rápida — Módulos frecuentes

### Auth completo FastAPI
```
Usuario: email, password_hash (Argon2id), rol, pin (opcional)
JWT payload: sub (user_id), rol, sucursal_id, exp
Dependency: get_current_user → lee cookie/header → decode JWT
Decorator: require_role("admin", "gerente")
Portal separado: create_portal_token(cliente_id) con type="portal"
```

### Expediente clínico/veterinario
```
Mascota/Paciente → Consultas → Vacunas
                            → AdjuntoExpediente (PDF/imagen)
                            → Recetas → RecetaItems
                            → EstudiosLaboratorio → AdjuntoExpediente
Hospitalizacion → CuidadoTurno (alimentacion, medicamento, observacion)
```

### POS con caja
```
TurnoCaja: fondo_inicial, efectivo_final, diferencia
Venta: cajero_id, cliente_id, total, metodo_pago
VentaItem: producto_id, descripcion, cantidad, precio_unitario, subtotal
Producto: categoria, precio_venta, precio_compra, stock, stock_minimo
```

### HTMX — patterns más usados
```html
<!-- Actualización automática -->
hx-get="/htmx/recurso" hx-trigger="every 30s" hx-target="#div-id"

<!-- Búsqueda en tiempo real -->
hx-get="/htmx/buscar" hx-trigger="keyup changed delay:300ms" hx-target="#resultados"

<!-- Acción sin recargar -->
hx-post="/htmx/accion/123" hx-target="#fila-123" hx-swap="outerHTML"

<!-- Modal inline -->
hx-get="/htmx/form/nuevo" hx-target="#modal-container"
```

---

## Arquitectura Hexagonal — Referencia Rápida (FastAPI)

### Principio central
El Domain y los Use Cases son el núcleo. Todo lo demás (FastAPI, SQLAlchemy,
Redis, archivos, email) son adaptadores intercambiables. No al revés.

```
┌─────────────────────────────────────────────────────────┐
│                    ADAPTADORES ENTRADA                  │
│         FastAPI Router / HTMX endpoints / CLI           │
└────────────────────┬────────────────────────────────────┘
                     │ llama a
┌────────────────────▼────────────────────────────────────┐
│              APPLICATION SERVICES (Use Cases)           │
│    CrearOrdenUseCase / CobrarOrdenUseCase / etc.        │
│    — orquesta, no tiene lógica de negocio pura —        │
└──────────┬──────────────────────────┬───────────────────┘
           │ usa                      │ usa interfaz (Port)
┌──────────▼──────────┐   ┌──────────▼───────────────────┐
│      DOMAIN         │   │   PORTS (interfaces Python)  │
│  Entidades, VOs     │   │   AbstractOrdenRepository     │
│  Reglas de negocio  │   │   AbstractEmailService        │
│  Eventos de dominio │   │   AbstractPrinterService      │
└─────────────────────┘   └──────────┬───────────────────┘
                                      │ implementado por
                           ┌──────────▼───────────────────┐
                           │   ADAPTADORES SALIDA (Infra) │
                           │   SQLAlchemyOrdenRepository  │
                           │   SMTPEmailAdapter           │
                           │   EscposPrinterAdapter       │
                           └──────────────────────────────┘
```

### Estructura de directorios hexagonal (FastAPI)
```
app/
├── domain/                  # Núcleo — CERO imports de frameworks
│   ├── entities/            # Clases de negocio puras (no SQLAlchemy)
│   │   ├── orden.py
│   │   └── usuario.py
│   ├── value_objects/       # VOs inmutables (Email, Dinero, UUID)
│   ├── events/              # Eventos de dominio (OrdenCreada, etc.)
│   └── exceptions.py        # Excepciones de negocio tipadas
│
├── application/             # Use Cases — orquesta, no implementa infra
│   ├── ports/               # Interfaces (contratos) que el dominio necesita
│   │   ├── orden_repository.py   # AbstractOrdenRepository (ABC)
│   │   └── printer_service.py    # AbstractPrinterService (ABC)
│   └── use_cases/
│       ├── crear_orden.py
│       └── cobrar_orden.py
│
├── infrastructure/          # Adaptadores — implementan los ports
│   ├── persistence/
│   │   ├── models.py        # SQLAlchemy models (mapeo DB)
│   │   └── sqlalchemy_orden_repo.py  # Implementa AbstractOrdenRepository
│   ├── printing/
│   │   └── escpos_adapter.py
│   └── email/
│       └── smtp_adapter.py
│
└── adapters/                # Adaptadores de entrada
    ├── http/                # FastAPI routers
    │   ├── ordenes.py
    │   └── auth.py
    └── desktop/             # PyWebview si aplica
        └── main.py
```

### Port (interfaz) — ejemplo Python
```python
# app/application/ports/orden_repository.py
from abc import ABC, abstractmethod
from app.domain.entities.orden import Orden

class AbstractOrdenRepository(ABC):
    @abstractmethod
    async def save(self, orden: Orden) -> Orden: ...

    @abstractmethod
    async def find_by_id(self, orden_id: int) -> Orden | None: ...

    @abstractmethod
    async def find_activas_por_mesa(self, mesa_id: int) -> list[Orden]: ...
```

### Adapter (implementación) — SQLAlchemy
```python
# app/infrastructure/persistence/sqlalchemy_orden_repo.py
from app.application.ports.orden_repository import AbstractOrdenRepository
from app.domain.entities.orden import Orden

class SQLAlchemyOrdenRepository(AbstractOrdenRepository):
    def __init__(self, db: AsyncSession):
        self.db = db

    async def save(self, orden: Orden) -> Orden:
        # aquí sí usamos SQLAlchemy — el domain nunca sabe que existe
        ...
```

### Inyección de dependencia en FastAPI (wire-up)
```python
# app/adapters/http/ordenes.py
async def get_orden_repo(db: AsyncSession = Depends(get_db)):
    return SQLAlchemyOrdenRepository(db)  # inyectamos el adapter concreto

@router.post("/ordenes")
async def crear_orden(
    data: CrearOrdenInput,
    repo: AbstractOrdenRepository = Depends(get_orden_repo)
):
    uc = CrearOrdenUseCase(repo)  # use case solo conoce la interfaz
    return await uc.execute(data)
```

---

## Patrones de Diseño — Referencia Rápida (FastAPI)

Usar los patrones que resuelven el problema concreto del sistema. No aplicar todos.

### Repository Pattern
**Cuándo:** Siempre — es la base de la arquitectura hexagonal.
```python
# Abstrae el acceso a datos. El use case no sabe si es PostgreSQL o SQLite.
class AbstractClienteRepository(ABC):
    @abstractmethod
    async def find_by_email(self, email: str) -> Cliente | None: ...
```

### Factory Pattern
**Cuándo:** Crear objetos complejos con lógica de construcción (tickets, reportes, documentos).
```python
class TicketFactory:
    @staticmethod
    def crear_desde_orden(orden: Orden, config: TenantConfig) -> Ticket:
        lineas = [TicketLinea(item.nombre, item.cantidad, item.precio)
                  for item in orden.items]
        return Ticket(numero=orden.numero, lineas=lineas, total=orden.total,
                      logo=config.logo, pie=config.pie_ticket)
```

### Strategy Pattern
**Cuándo:** Múltiples algoritmos intercambiables — métodos de pago, cálculo de precios, impresoras.
```python
class AbstractMetodoPago(ABC):
    @abstractmethod
    async def procesar(self, monto: float) -> ResultadoPago: ...

class PagoEfectivo(AbstractMetodoPago):
    async def procesar(self, monto: float) -> ResultadoPago:
        return ResultadoPago(exitoso=True, cambio=monto)

class PagoTarjeta(AbstractMetodoPago):
    async def procesar(self, monto: float) -> ResultadoPago:
        # integración con terminal
        ...

# Use case no sabe cuál se usa — solo llama .procesar()
```

### Observer / Event Pattern
**Cuándo:** Acciones que disparan efectos secundarios — orden creada → notificar KDS, descontar inventario, registrar auditoría.
```python
# Evento de dominio
@dataclass
class OrdenCreada:
    orden_id: int
    tenant_id: int
    mesa_id: int
    timestamp: datetime

# Handlers que reaccionan al evento (desacoplados)
class NotificarKDSHandler:
    async def handle(self, evento: OrdenCreada): ...

class DescontarInventarioHandler:
    async def handle(self, evento: OrdenCreada): ...
```

### Value Object (VO)
**Cuándo:** Datos que tienen reglas de validación propias — Email, Dinero, RFC, CURP.
```python
@dataclass(frozen=True)  # inmutable
class Email:
    value: str

    def __post_init__(self):
        if "@" not in self.value:
            raise ValueError(f"Email inválido: {self.value}")

    def __str__(self) -> str:
        return self.value

# En la entidad:
class Usuario:
    email: Email  # no un str plano — lleva su validación
```

### Unit of Work
**Cuándo:** Múltiples operaciones que deben ser atómicas — crear orden + descontar inventario + registrar en caja.
```python
class UnitOfWork:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.ordenes = SQLAlchemyOrdenRepository(db)
        self.inventario = SQLAlchemyInventarioRepository(db)

    async def commit(self): await self.db.commit()
    async def rollback(self): await self.db.rollback()

# Use case usa UoW — atomicidad garantizada
async def execute(self, data):
    async with self.uow:
        orden = await self.uow.ordenes.save(nueva_orden)
        await self.uow.inventario.descontar(orden)
        await self.uow.commit()
```

---

## Comparación Argon2id vs bcrypt

| Característica | Argon2id | bcrypt |
|---|---|---|
| Ganador PHC 2015 | ✅ Sí | ❌ No |
| Resistencia GPU/ASIC | ✅ Memory-hard | ❌ No memory-hard |
| Configurabilidad | ✅ Alta (time, memory, parallelism) | ⚠️ Baja (solo cost factor) |
| Velocidad | ⚠️ Más lento (pero aceptable) | ✅ Más rápido |
| Madurez | ⚠️ Más nuevo (2015) | ✅ Muy maduro (1999) |
| Librería Python | argon2-cffi | bcrypt |
| Recomendación 2024+ | ✅ **Recomendado** | ⚠️ Aceptable pero no óptimo |

**Conclusión:** Argon2id es el estándar moderno 2024+. Más seguro contra ataques con GPU/ASIC. La diferencia de velocidad es despreciable para autenticación web (100-200ms es aceptable). Usar siempre Argon2id en nuevos proyectos.

---

## Matriz de decisión para sub-stacks

| Factor | Stack A (SSR) | Stack B (SPA) | Stack C (Desktop) |
|---|---|---|---|
| Tiempo de desarrollo | ✅ Más rápido | ⚠️ Más lento | ⚠️ Más lento |
| UX móvil | ⚠️ Media | ✅ Excelente | ❌ N/A (desktop) |
| Offline | ❌ No | ⚠️ Service Worker | ✅ Sí (local) |
| Hardware integración | ❌ Difícil | ❌ Difícil | ✅ Fácil |
| Tamaño bundle | ✅ Pequeño (HTMX) | ⚠️ Grande (React) | ✅ Medio (PyWebView) |
| Mantenimiento | ✅ Simple | ⚠️ Más complejo | ⚠️ Más complejo |
| Ideal para | Apps internas, dashboards | Productos vendibles, POS | POS desktop, kioscos |
| Complejidad | ✅ Baja | ⚠️ Media-Alta | ⚠️ Media-Alta |
| Python skills | ✅ 90% | ⚠️ 60% + React/TS | ✅ 90% + PyWebView |
| Escalabilidad frontend | ⚠️ Limitada | ✅ Alta | ⚠️ Limitada |

**Decisión rápida:**
- App interna/dashboard → Stack A
- Producto vendible con UI táctil → Stack B
- POS desktop con hardware → Stack C
- Híbrido desktop + web → Stack C (caja) + Stack A/B (admin)

---

## Ejemplos de dominios

### Fintech (Sistema de pagos)

**Entidades principales:**
- Usuario (email, password, rol, kyc_status)
- Cuenta (saldo, moneda, tipo)
- Transaccion (monto, tipo, estado, referencia)
- Beneficiario (nombre, cuenta, banco)
- Tarjeta (numero, expiracion, cvv, activa)

**Patrones clave:**
- Value Objects: Dinero, Moneda, IBAN, RFC
- Unit of Work: Transacciones atómicas (debitar origen + acreditar destino)
- Event Pattern: TransaccionCompletada → notificar por email, actualizar saldo
- Strategy Pattern: Multiples métodos de pago (spei, tarjeta, oxxo)

**Consideraciones especiales:**
- Argon2id obligatorio para passwords
- Logs de auditoría para todas las transacciones
- Soft delete NUNCA para transacciones (hard delete con retención legal)
- Crytography para datos sensibles (numero tarjeta)

### EdTech (Plataforma de cursos)

**Entidades principales:**
- Usuario (estudiante, instructor, admin)
- Curso (titulo, descripcion, precio, categoria)
- Leccion (titulo, contenido, orden, video_url)
- Inscripcion (usuario_id, curso_id, progreso, fecha_inicio)
- Certificado (usuario_id, curso_id, fecha_emision, codigo)

**Patrones clave:**
- Repository Pattern con filtros (cursos por categoria, por instructor)
- Factory Pattern: CertificadoFactory para generar PDFs
- Observer Pattern: InscripcionCompletada → enviar email de bienvenida
- Value Objects: Email, Dinero (precio curso)

**Consideraciones especiales:**
- HTMX para dashboard de estudiantes (Stack A)
- React para reproductor de video interactivo (Stack B)
- Caching con Redis para cursos populares
- WebSockets para chat en vivo durante clase

### Healthcare (Sistema clínico)

**Entidades principales:**
- Paciente (nombre, email, telefono, fecha_nacimiento, sangre)
- Medico (nombre, especialidad, cedula, horario)
- Cita (paciente_id, medico_id, fecha, hora, estado)
- Consulta (cita_id, diagnostico, notas, receta)
- Receta (consulta_id, medicamentos)
- Expediente (paciente_id, adjuntos, historial)

**Patrones clave:**
- Repository con soft delete (expedientes nunca se borran)
- State Machine: Cita (PROGRAMADA → CONFIRMADA → EN_CURSO → COMPLETADA → CANCELADA)
- Value Objects: Email, Telefono, CURP, RFC
- Event Pattern: CitaConfirmada → notificar paciente por WhatsApp
- Observer Pattern: ConsultaCompletada → actualizar expediente, enviar receta a farmacia

**Consideraciones especiales:**
- Stack A (Jinja2 + HTMX) — suficiente, no necesita React
- RGPD compliance: anonimización de datos después de X años
- Audit logging obligatorio para cambios en expedientes
- Backups diarios con retención de 7 años
- Argon2id obligatorio para passwords
- Roles: admin, medico, recepcionista, paciente

---

## Secciones opcionales (12.1-12.7)

Estas secciones se agregan según el complexity_score del proyecto:

| complexity_score | Secciones a incluir |
|---|---|
| 1-3 | Solo secciones 1-12 (básico) |
| 4-6 | Secciones 1-12 + 12.1 + 12.2 + 12.6 |
| 7-8 | Secciones 1-12 + 12.1 + 12.2 + 12.3 + 12.5 + 12.6 |
| 9-10 | TODAS las secciones (incluyendo 12.4 + 12.7) |

### 12.1 Domain Modeling (complexity_score >= 4)

Incluir cuando el sistema tiene lógica de dominio compleja que justifica DDD.

**Contenido:**
- Entidades de dominio (no modelos SQLAlchemy) con Pydantic
- Value Objects inmutables
- Aggregates y Aggregate Roots
- Eventos de dominio
- Reglas de negocio encapsuladas

**Ejemplo de código:**
```python
from dataclasses import dataclass
from datetime import datetime
from typing import List
from enum import Enum

class OrdenEstado(Enum):
    ABIERTA = "abierta"
    PAGADA = "pagada"
    CANCELADA = "cancelada"

@dataclass(frozen=True)
class OrdenItem:
    producto_id: int
    cantidad: int
    precio_unitario: float

    @property
    def subtotal(self) -> float:
        return self.cantidad * self.precio_unitario

@dataclass
class Orden:
    id: int | None
    numero: str
    items: List[OrdenItem]
    estado: OrdenEstado

    @property
    def total(self) -> float:
        return sum(item.subtotal for item in self.items)

    def agregar_item(self, item: OrdenItem) -> None:
        if self.estado != OrdenEstado.ABIERTA:
            raise ValueError("No se pueden agregar items a una orden cerrada")
        self.items.append(item)

    def cerrar(self) -> None:
        if self.estado != OrdenEstado.ABIERTA:
            raise ValueError("La orden ya está cerrada")
        self.estado = OrdenEstado.PAGADA
```

### 12.2 Modelo de Errores (complexity_score >= 4)

Incluir cuando el sistema necesita manejo de errores consistente y detallado.

**Contenido:**
- Jerarquía de excepciones personalizadas
- Códigos de error estandarizados
- Exception handlers de FastAPI
- Respuestas de error consistentes
- Logging de errores

**Ejemplo de código:**
```python
# app/domain/exceptions.py
class DomainException(Exception):
    """Base exception para errores de dominio"""
    def __init__(self, message: str, code: str):
        self.message = message
        self.code = code
        super().__init__(message)

class ValidationException(DomainException):
    """Error de validación de datos"""
    def __init__(self, message: str):
        super().__init__(message, code="VALIDATION_ERROR")

class NotFoundException(DomainException):
    """Recurso no encontrado"""
    def __init__(self, resource: str, id: int):
        message = f"{resource} con id {id} no encontrado"
        super().__init__(message, code="NOT_FOUND")

class BusinessRuleException(DomainException):
    """Violación de regla de negocio"""
    def __init__(self, message: str):
        super().__init__(message, code="BUSINESS_RULE_ERROR")

# Exception handler de FastAPI
@app.exception_handler(DomainException)
async def domain_exception_handler(request: Request, exc: DomainException):
    return JSONResponse(
        status_code=400,
        content={
            "error": {
                "code": exc.code,
                "message": exc.message,
                "timestamp": datetime.utcnow().isoformat()
            }
        }
    )
```

### 12.3 Consistencia & Transacciones (complexity_score >= 7)

Incluir cuando el sistema tiene operaciones que deben ser atómicas.

**Contenido:**
- Patrón Unit of Work
- Transacciones atómicas con SQLAlchemy
- Manejo de concurrencia (optimistic/pessimistic locking)
- Eventual consistency si aplica (event sourcing, CQRS)
- Deadlock handling

**Ejemplo de código:**
```python
# Unit of Work con SQLAlchemy
class UnitOfWork:
    def __init__(self, session_factory):
        self.session_factory = session_factory

    async def __aenter__(self):
        self.session = self.session_factory()
        self.ordenes = SQLAlchemyOrdenRepository(self.session)
        self.inventario = SQLAlchemyInventarioRepository(self.session)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        try:
            if exc_type is None:
                await self.session.commit()
            else:
                await self.session.rollback()
        finally:
            await self.session.close()

# Uso en use case
async def execute(self, data):
    async with self.uow as uow:
        orden = await uow.ordenes.save(nueva_orden)
        await uow.inventario.descontar(orden.items)
        # Si falla, todo hace rollback automáticamente
```

### 12.4 Performance & Escalabilidad (complexity_score >= 9)

Incluir cuando el sistema necesita manejar alta carga o escalar horizontalmente.

**Contenido:**
- Estrategias de caching (Redis, in-memory)
- Query optimization (evitar N+1, índices)
- Paginación y filtering eficiente
- Async/await para I/O bound
- Horizontal scaling (load balancer, containers)
- Métricas y monitoreo (Prometheus, Grafana)
- Rate limiting
- Database sharding si aplica

**Ejemplo de código:**
```python
# Caching con Redis
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache

@router.get("/productos")
@cache(expire=60)  # Cachear por 60 segundos
async def listar_productos():
    return await producto_repo.find_all()

# Paginación eficiente con cursor
async def listar_ordenes(cursor: int | None = None, limit: int = 50):
    query = select(Orden).order_by(Orden.id)
    if cursor:
        query = query.where(Orden.id > cursor)
    query = query.limit(limit)
    result = await db.execute(query)
    return result.scalars().all()
```

### 12.5 Configuración & Secretos (complexity_score >= 7)

Incluir cuando el sistema tiene múltiples ambientes o maneja secretos sensibles.

**Contenido:**
- Separación de config por ambiente (dev/staging/prod)
- Manejo de secretos (vault, env variables, AWS Secrets Manager)
- Configuración de DB por ambiente
- Feature flags
- Rotación de secretos
- .env.example y config.yaml

**Ejemplo de código:**
```python
# app/core/config.py
from pydantic import BaseSettings

class Settings(BaseSettings):
    # Database
    DATABASE_URL: str
    DATABASE_POOL_SIZE: int = 5

    # Security
    SECRET_KEY: str
    ALGORITHM: str = "HS256"

    # Environment
    ENVIRONMENT: str = "development"  # development | staging | production

    # Features
    ENABLE_REGISTRATION: bool = True
    ENABLE_MULTI_TENANT: bool = False

    class Config:
        env_file = ".env"

settings = Settings()
```

### 12.6 UX & Flujos (complexity_score >= 4)

Incluir cuando la experiencia de usuario es crítica para el éxito del sistema.

**Contenido:**
- Diagramas de flujo de usuario (ASCII o Mermaid)
- Estados de las entidades (state machines)
- Validaciones de negocio con mensajes amigables
- Mensajes de error user-friendly
- Accesibilidad (a11y) si aplica
- Animaciones y transiciones (si Stack B)
- Feedback visual en tiempo real (si Stack A con HTMX)

**Ejemplo de flujo:**
```
Flujo de compra en POS:

[Cliente selecciona productos]
        ↓
[Confirma orden]
        ↓
[Selecciona método de pago]
        ↓
┌───────┴───────┐
│  Efectivo     │  Tarjeta
│     ↓         │     ↓
[Ingresar monto] [Procesar terminal]
│     ↓         │     ↓
[Dar cambio]   [Aprobar/rechazar]
└───────┬───────┘
        ↓
[Imprimir ticket]
        ↓
[Actualizar inventario]
        ↓
[Orden completada]
```

### 12.7 Data Lifecycle (complexity_score >= 9)

Incluir cuando el sistema maneja datos sensibles o tiene requisitos de retención legal.

**Contenido:**
- Políticas de retención de datos (GDPR, HIPAA, etc.)
- Archivo y backup (frecuencia, retención)
- Anonimización / Pseudonimización
- Soft delete vs hard delete (cuándo usar cada uno)
- Auditoría y logging obligatorio
- Cumplimiento normativo (LFPDPPP en México, GDPR en UE)
- Procedimientos de exportación/borrado de datos (GDPR right to be forgotten)

**Ejemplo de políticas:**
```python
# Políticas de retención por tipo de dato
RETENTION_POLICIES = {
    "transacciones": {
        "retention_years": 7,
        "anonymize_after": True,
        "legal_basis": "fiscal"
    },
    "expedientes_medicos": {
        "retention_years": 15,
        "anonymize_after": False,  # nunca anonimizar
        "legal_basis": "salud"
    },
    "logs_auditoria": {
        "retention_years": 3,
        "anonymize_after": False,
        "legal_basis": "seguridad"
    },
    "cookies_sesion": {
        "retention_days": 30,
        "anonymize_after": True,
        "legal_basis": "funcional"
    }
}

# Job de retención
async def retention_job():
    for data_type, policy in RETENTION_POLICIES.items():
        cutoff_date = datetime.utcnow() - timedelta(days=policy["retention_years"] * 365)
        await anonymize_old_records(data_type, cutoff_date, policy["anonymize_after"])
```

---

## Conclusión

Este skill genera PRDs completos, técnicos y vendibles para el stack FastAPI moderno. Las decisiones técnicas están predefinidas para optimizar velocidad de desarrollo, seguridad y mantenibilidad. Las secciones opcionales (12.1-12.7) se agregan según la complejidad del proyecto para no sobrediseñar sistemas simples.

**Principios clave:**
1. **Simplicidad primero:** No agregar complejidad innecesaria
2. **Decisions made:** No preguntar lo que ya está decidido
3. **Código real:** Todos los ejemplos son Python funcional, no pseudocódigo
4. **Dominio primero:** Entender el negocio antes de la tecnología
5. **Entregable accionable:** PRD listo para que un developer empiece a codear

**Stacks por dominio:**
- Clínico/Médico → Stack A (HTMX)
- POS vendible → Stack B (React) o Stack C (Desktop)
- Dashboard interno → Stack A (HTMX)
- SaaS multi-tenant → Stack B (React)

**Patrones obligatorios:**
- Repository (siempre)
- Unit of Work (transacciones atómicas)
- Value Objects (validación de datos)
- Service Layer (lógica de negocio)

**Patrones opcionales:**
- Factory (creación compleja)
- Strategy (algoritmos intercambiables)
- Observer (eventos desacoplados)
