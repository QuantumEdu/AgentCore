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

Preguntas si no están respondidas:

**Negocio:**
- ¿Cliente único o producto SaaS para vender?
- ¿Cuántos usuarios simultáneos?
- ¿Necesita funcionar offline?

**Técnico:**
- ¿Qué módulos son core? ¿Qué puede esperar para v2?
- ¿Hay hardware físico? (impresora, báscula, lector)
- ¿Multi-sucursal desde v1?

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