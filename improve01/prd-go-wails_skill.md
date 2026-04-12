---
name: prd-go-wails
description: Genera PRDs completos y profesionales para sistemas de software usando el stack Go + Fiber + React + MUI + Wails. Usar SIEMPRE que el usuario pida un PRD, documento de requerimientos, especificación de producto o sistema usando Go como backend. También activar cuando el usuario diga "crea el PRD", "necesito el PRD", "genera los requerimientos", "especificación del sistema", "documento de producto" o cuando describa un sistema de software que deba construirse con Go, especialmente apps desktop (POS, clínica, veterinaria, restaurante, gimnasio) o sistemas web con API REST. Si el usuario menciona Wails, Fiber, GORM, o Go como lenguaje, usar este skill sin excepción.
---

# PRD Generator — Stack Go + Fiber + React + MUI + Wails

Genera PRDs completos, técnicos y vendibles para sistemas de software usando el stack Go moderno. Basado en proyectos reales: RestaurantOS, VetCare, POS Pescadería.

## Stack de referencia

```
Backend:    Go 1.22 + Fiber v2 + GORM + golang-migrate
Auth:       golang-jwt/jwt v5 + bcrypt (golang.org/x/crypto)
Validación: go-playground/validator v10
Cache:      Redis (go-redis/v9) — para WebSocket scale y cache
IDs:        UUID (google/uuid) — todas las entidades
DB dev:     SQLite (go-sqlite3)
DB prod:    PostgreSQL 16+
Auditoría:  zerolog — acciones críticas
Testing:    testify v1.9+

Docs API:   swaggo/swag v1.16+ — OpenAPI/Swagger desde comentarios Go
            swaggo/fiber-swagger v1.3+ — middleware que sirve /swagger/index.html
            swaggo/files — archivos estáticos del UI

Frontend:   React 18 + TypeScript 5 + Vite 5
UI:         MUI v6 (Material UI) — táctil y responsivo
Fetching:   TanStack Query v5
WS:         WebSocket API nativa — tiempo real
Forms:      React Hook Form + Zod
Estado:     Zustand v4
Routing:    React Router v6

Desktop:    Wails v2 — instalador ~10 MB, binario nativo
Impresora:  go-escpos (Epson TM-T20, Xprinter, Star)
Caché off:  Zustand persist — 5 min offline

Deploy:     Docker + docker-compose + GitHub Actions
```

## Proceso de generación

### Paso 1 — Recopilar contexto

Antes de generar el PRD, hacer estas preguntas si no están respondidas en el mensaje:

**Negocio:**
- ¿El sistema es nuevo o reemplaza uno existente?
- ¿Es para un cliente único o producto para vender (SaaS)?
- ¿Cuántos usuarios simultáneos máximo?
- ¿Necesita funcionar offline o siempre hay internet?

**Dispositivos:**
- ¿Qué dispositivos usarán el sistema? (tablet, PC, celular)
- ¿Hay hardware físico? (impresora, lector, báscula, cajón)
- ¿App instalada en PC o solo web en browser?

**Módulos:**
- ¿Cuáles son los módulos core del sistema?
- ¿Qué puede esperar para v2? (CFDI, mobile, delivery, etc.)

**No preguntar si el usuario ya los respondió.** Inferir del contexto cuando sea posible.

### Paso 2 — Estructura del PRD

Generar SIEMPRE estas secciones:

```
1.  Resumen Ejecutivo
    - Descripción del producto
    - Objetivos del proyecto
    - Contexto del negocio (tabla)

2.  Stack Tecnológico
    - Tabla Backend Go completa con versiones
    - Tabla Frontend React completa con versiones
    - Desktop Wails si aplica
    - go.mod con dependencias reales
    - package.json frontend

3.  Arquitectura del Sistema
    - Diagrama ASCII capas Clean Architecture
    - Diagrama ASCII arquitectura multi-dispositivo
    - Flujo de datos principal (ASCII)
    - Multi-tenant si aplica

4.  Módulos y Requisitos Funcionales
    - Una sección H3 por módulo
    - Tabla ID | Función | Descripción | Prioridad
    - Prioridades: Crítica / Alta / Media / Baja
    - Flujos de estado con ASCII cuando aplique

5.  Requisitos No Funcionales
    - Rendimiento (latencia, concurrencia — números reales)
    - Disponibilidad (uptime, offline, backup, RTO/RPO)
    - Escalabilidad
    - Seguridad (TLS, hash, OWASP, rate limiting)
    - Usabilidad (curva aprendizaje en minutos)
    - Compatibilidad OS/browser

6.  Historias de Usuario y Criterios de Aceptación
    - US-001 a US-00N numeradas
    - Formato COMO / QUIERO / PARA
    - Lista de criterios con [ ] checkbox
    - Prioridad y complejidad por historia

7.  Arquitectura Hexagonal y Modelo de Dominio Go
    - Diagrama ASCII hexagonal adaptado a Go:
      [Fiber Handler] → [Service / Use Case] → [Domain Struct]
                                                    ↑
                                         [Repository Interface]
                                                    ↑
                                         [GORM Adapter / Infra]
    - Puerto de entrada: Fiber handler — adapter HTTP
    - Puerto de salida: interface Repository — contrato Go puro
    - Regla de oro: domain/ no importa Fiber, GORM ni ningún framework
    - Patrones de diseño aplicados: Repository, Factory, Strategy, Observer
    - Structs GORM completos con tags json y gorm
    - IDs como string UUID
    - tenant_id en todas las entidades de negocio
    - Relaciones con Preload
    - Índices críticos SQL al final

8.  API, Swagger y WebSocket
    - Sección de Swagger/OpenAPI: configuración swaggo + ejemplo de anotaciones
    - Tabla de rutas por módulo con método HTTP
    - Eventos WebSocket con JSON de ejemplo
    - Configuración seguridad (JWT, rate limit)
    - Variables de entorno .env.example

9.  Consideraciones Técnicas
    - Estructura de directorios completa (árbol)
    - Patrón de auditoría de acciones críticas
    - Middleware de tenant

10. Roadmap de Desarrollo
    - Tabla Fase | Duración | Objetivo | Entregables
    - Fases numeradas con semanas estimadas
    - MVP claramente marcado

11. Riesgos y Mitigación
    - Tabla Riesgo | Prob | Impacto | Mitigación | Owner
    - Tres categorías: Técnicos, Operativos, Negocio

12. Hardware Recomendado (si aplica)
    - Tabla Dispositivo | Modelo | Precio MXN | Notas

13. Plan de Capacitación (si aplica)
    - Por rol con minutos exactos

14. Checklist de Implementación (si aplica)
    - Pre-instalación y Go-Live

15. Modelo de Negocio SaaS (si es producto vendible)
    - Planes con precios MXN
    - Add-ons
    - SLA formal

16. Glosario
    - Términos técnicos y de negocio del dominio
```

### Paso 3 — Decisiones técnicas automáticas

Aplicar SIEMPRE sin preguntar:

| Decisión | Valor |
|---|---|
| IDs | UUID string en todas las entidades |
| Modificadores en órdenes | Tabla separada con snapshot (no JSONB) |
| Variantes de producto | VariantePlatillo con precio_delta |
| Multi-tenant | tenant_id UUID + filtro automático en BaseRepository |
| WebSocket rooms | `{evento}:{tenant_id}` para aislamiento |
| Hash passwords | bcrypt via golang.org/x/crypto |
| Cache | Redis para WebSocket scale + cache frecuente |
| Auditoría | zerolog en middleware para acciones críticas |
| Arquitectura | Hexagonal ligera: domain → application/ports → infrastructure/adapters → handlers |
| Patrones | Repository (siempre), Factory (tickets/reportes), Strategy (pagos/impresoras), Observer (eventos) |
| Desktop | Wails v2 con bindings autogenerados |
| Impresora | go-escpos + apertura cajón en pago efectivo |
| Docs API | swaggo/swag SIEMPRE — comentarios en handlers, ruta /swagger/index.html |

### Paso 4 — Adaptaciones por dominio

**Restaurante / Bar / Cafetería:**
- KDS con WebSocket obligatorio
- Mesa con estado: disponible → ocupada → cuenta_pendiente
- TurnoCaja con fondo inicial + salidas + corte parcial
- TurnoPersonal para propinas por mesero
- Modificadores y Variantes en platillos
- Estación en Platillo para filtros KDS

**Clínica / Veterinaria:**
- Expediente por paciente/mascota
- Hospitalización con CuidadoTurno
- Vacunas con próxima dosis
- AdjuntoExpediente para radiografías (max 10 MB)
- Portal para dueños/pacientes (solo lectura)

**POS General (tienda, pescadería, etc.):**
- Productos por peso (kg) vs por unidad
- Báscula serial (go.bug.st/serial)
- Merma como entidad separada
- Reportes de margen por producto

**Gimnasio / Control de acceso:**
- Lector biométrico (ctypes → DLL, o go.bug.st/serial)
- Membresía con fecha de vencimiento
- Registro de entrada/salida
- Control de acceso automático

**Sistema web sin desktop:**
- Omitir sección Wails
- Frontend como React SPA pura
- Panel admin accesible por browser

### Paso 5 — Calidad del PRD

Verificar antes de entregar:

- [ ] Todas las secciones presentes (1–16)
- [ ] go.mod con versiones reales y actuales (2026)
- [ ] Structs Go con tags gorm y json completos
- [ ] UUID en todos los IDs
- [ ] tenant_id en todas las entidades de negocio
- [ ] Índices SQL críticos definidos
- [ ] Rutas API organizadas por módulo
- [ ] **Sección Swagger presente** con ejemplo de anotación swaggo en al menos 1 handler
- [ ] **go.mod incluye swaggo/swag + swaggo/fiber-swagger**
- [ ] **main.go incluye ruta /swagger/index.html**
- [ ] Evento WebSocket con JSON de ejemplo si hay tiempo real
- [ ] Roadmap con fases y semanas estimadas
- [ ] Riesgos técnicos incluyen curva Go + seguridad multi-tenant
- [ ] Si es producto vendible: pricing MXN + SLA
- [ ] Estructura de directorios refleja hexagonal (domain/ sin imports de Fiber/GORM)
- [ ] Al menos 1 interface Go documentada como Port
- [ ] Patrones de diseño mencionados en sección de arquitectura

### Paso 6 — Formato de entrega

- Generar el PRD en **Markdown descargable** via `create_file` en `/mnt/user-data/outputs/`
- Nombre del archivo: `PRD_{NombreSistema}_Go_Wails.md`
- Presentar el archivo con `present_files`
- Después del archivo, dar un resumen de 3–5 puntos de lo más importante del PRD generado

---

## Referencia rápida de módulos comunes

### Módulo de caja completo (restaurante)
```
TurnoCaja: fondo_inicial, efectivo_final, efectivo_sistema,
           diferencia, total_ventas, total_propinas
SalidaCaja: monto, motivo, usuario_id (gastos operativos)
Pago: monto, propina, metodo_pago, persona_ref (split), mesero_id
Estados: abierto → operando → corte_parcial → cerrado
```

### Módulo de inventario completo
```
Ingrediente: stock, stock_minimo, costo_unitario, fecha_vencimiento
Receta: platillo_id, costo_total (calculado)
RecetaIngrediente: receta_id, ingrediente_id, cantidad
Merma: ingrediente_id, cantidad, motivo, registrado_por
Alerta: cuando stock <= stock_minimo
```

### WebSocket Hub Go
```go
Hub.salas: map[tenant_id]map[sala][]*websocket.Conn
Salas estándar: "cocina", "mesas", "caja", "admin"
Broadcast(tenantID, sala, event, data)
Reconexión frontend: setTimeout 3s en onclose
```

---

## Referencia Swagger / OpenAPI con swaggo

### go.mod — dependencias requeridas
```go
require (
    github.com/swaggo/swag         v1.16.3
    github.com/swaggo/fiber-swagger v1.3.0
    github.com/swaggo/files         v1.0.1
)
```

### Setup en main.go
```go
import (
    _ "github.com/tu-usuario/tu-app/docs" // generado por swag init
    fiberSwagger "github.com/swaggo/fiber-swagger"
)

// @title           RestaurantOS API
// @version         1.0
// @description     API REST para sistema de gestión de restaurante
// @host            localhost:8000
// @BasePath        /api/v1
// @securityDefinitions.apikey BearerAuth
// @in header
// @name Authorization
func main() {
    app := fiber.New()
    // Ruta Swagger UI — solo en dev (condicional con env)
    app.Get("/swagger/*", fiberSwagger.WrapHandler)
    // ...resto de rutas
}
```

### Anotación en handler (patrón obligatorio por endpoint)
```go
// GetOrdenes godoc
// @Summary      Listar órdenes activas
// @Description  Retorna todas las órdenes abiertas del tenant autenticado
// @Tags         ordenes
// @Accept       json
// @Produce      json
// @Security     BearerAuth
// @Param        mesa_id  query  string  false  "Filtrar por mesa UUID"
// @Success      200  {array}   domain.Orden
// @Failure      401  {object}  handlers.ErrorResponse
// @Failure      500  {object}  handlers.ErrorResponse
// @Router       /ordenes [get]
func (h *OrdenHandler) GetOrdenes(c *fiber.Ctx) error {
    // implementación
}
```

### Struct de respuesta de error (requerido para Swagger)
```go
// ErrorResponse es la respuesta estándar de error de la API
// @Description Respuesta de error estándar
type ErrorResponse struct {
    Error   string `json:"error"   example:"recurso no encontrado"`
    Message string `json:"message" example:"El recurso solicitado no existe"`
    Code    int    `json:"code"    example:"404"`
}
```

### Comando para regenerar docs (agregar a Makefile y CI/CD)
```bash
# Instalar swag CLI
go install github.com/swaggo/swag/cmd/swag@latest

# Generar/actualizar docs/ desde anotaciones en handlers/
swag init -g cmd/server/main.go --output docs/

# Agregar al .gitignore si los docs se regeneran en CI
# O incluir docs/ en el repo para deploy sin swag CLI
```

### Comportamiento esperado en el PRD generado
- URL de acceso: `GET /swagger/index.html` — UI interactiva completa
- Autenticación: botón "Authorize" con Bearer token JWT
- Por cada módulo: al menos 1 handler con anotación completa como ejemplo
- En producción: deshabilitar con variable `SWAGGER_ENABLED=false`
- El PRD debe mencionar `swag init` como paso en el Roadmap Fase 1 (Foundation)

### Comparativo honesto vs FastAPI /docs
| Aspecto | swaggo (Go) | FastAPI (Python) |
|---|---|---|
| Setup | Manual — comentarios en código | Zero config — automático |
| Mantenimiento | Comentarios pueden desactualizarse | Siempre en sync con el código |
| Potencia final | Igual — UI idéntica, misma spec OpenAPI | Igual |
| Generación de clientes | openapi-generator funciona igual | openapi-generator funciona igual |
| Recomendación | Incluir siempre — compensa la falta de auto-gen | Ya incluido por defecto |

---

## Arquitectura Hexagonal — Referencia Rápida (Go + Fiber)

### Principio central
El dominio (structs de negocio + reglas) no conoce ni Fiber ni GORM.
Los interfaces Go son los puertos. Las implementaciones concretas son los adaptadores.

```
┌─────────────────────────────────────────────────────────┐
│              ADAPTADORES ENTRADA                        │
│         Fiber Handlers / WebSocket / CLI                │
└────────────────────┬────────────────────────────────────┘
                     │ llama a
┌────────────────────▼────────────────────────────────────┐
│              APPLICATION (Services / Use Cases)         │
│    OrdenService.Crear() / CajaService.Cobrar()          │
└──────────┬──────────────────────────┬───────────────────┘
           │ usa                      │ usa interface (Port)
┌──────────▼──────────┐   ┌──────────▼───────────────────┐
│      DOMAIN         │   │   PORTS (interfaces Go)      │
│  Structs de negocio │   │   OrdenRepository interface  │
│  Enums, errores     │   │   PrinterService interface   │
│  Reglas de negocio  │   │   EmailService interface     │
└─────────────────────┘   └──────────┬───────────────────┘
                                     │ implementado por
                          ┌──────────▼───────────────────┐
                          │   ADAPTADORES SALIDA (Infra) │
                          │   GORMOrdenRepository        │
                          │   EscposPrinterAdapter       │
                          │   SMTPEmailAdapter           │
                          └──────────────────────────────┘
```

### Estructura de directorios hexagonal (Go)
```
internal/
├── domain/                  # Núcleo — CERO imports de Fiber/GORM
│   ├── orden.go             # Structs de negocio + métodos de dominio
│   ├── usuario.go
│   ├── enums.go             # Estados, roles como constantes tipadas
│   └── errors.go            # Errores de negocio tipados

├── application/             # Use cases + ports (interfaces)
│   ├── ports/
│   │   ├── orden_repository.go   # interface OrdenRepository
│   │   └── printer_service.go    # interface PrinterService
│   └── services/
│       ├── orden_service.go
│       └── caja_service.go

├── infrastructure/          # Adaptadores — implementan los ports
│   ├── persistence/
│   │   └── gorm_orden_repo.go    # struct GORMOrdenRepo implements OrdenRepository
│   ├── printing/
│   │   └── escpos_adapter.go
│   └── cache/
│       └── redis_adapter.go

└── adapters/                # Adaptadores de entrada
    ├── http/
    │   ├── orden_handler.go
    │   └── middleware/
    └── websocket/
        └── hub.go
```

### Port (interface Go) — patrón obligatorio
```go
// internal/application/ports/orden_repository.go
package ports

import "github.com/tu-app/internal/domain"

// OrdenRepository es el puerto de salida para persistencia de órdenes.
// El domain y los services solo conocen esta interfaz — nunca GORM.
type OrdenRepository interface {
    Save(ctx context.Context, orden *domain.Orden) (*domain.Orden, error)
    FindByID(ctx context.Context, id string) (*domain.Orden, error)
    FindActivasPorMesa(ctx context.Context, mesaID, tenantID string) ([]*domain.Orden, error)
    Update(ctx context.Context, orden *domain.Orden) error
}
```

### Adapter (implementación GORM)
```go
// internal/infrastructure/persistence/gorm_orden_repo.go
package persistence

type GORMOrdenRepository struct {
    db *gorm.DB
}

// Implementa la interfaz OrdenRepository — Go verifica en compile time
var _ ports.OrdenRepository = (*GORMOrdenRepository)(nil)

func (r *GORMOrdenRepository) Save(ctx context.Context, orden *domain.Orden) (*domain.Orden, error) {
    result := r.db.WithContext(ctx).Create(orden)
    return orden, result.Error
}
```

### Wire-up en Fiber handler
```go
// internal/adapters/http/orden_handler.go
type OrdenHandler struct {
    service *services.OrdenService  // el handler conoce el service
}

// main.go — inyección de dependencias manual (sin frameworks DI)
repo := persistence.NewGORMOrdenRepository(db)
service := services.NewOrdenService(repo)  // service solo conoce el port
handler := http.NewOrdenHandler(service)
```

---

## Patrones de Diseño — Referencia Rápida (Go)

### Repository Pattern (siempre)
```go
// Interface en ports/ — el contrato que el dominio necesita
type ClienteRepository interface {
    FindByEmail(ctx context.Context, email, tenantID string) (*domain.Cliente, error)
    Save(ctx context.Context, cliente *domain.Cliente) error
}
```

### Factory Pattern
**Cuándo:** Construir structs complejos — tickets, reportes, facturas.
```go
// internal/domain/ticket_factory.go
type TicketFactory struct{}

func (f *TicketFactory) CrearDesdeOrden(orden *Orden, config *TenantConfig) *Ticket {
    lineas := make([]TicketLinea, len(orden.Items))
    for i, item := range orden.Items {
        lineas[i] = TicketLinea{
            Nombre: item.Platillo.Nombre,
            Cantidad: item.Cantidad,
            Precio: item.PrecioUnitario,
        }
    }
    return &Ticket{NumeroOrden: orden.NumeroOrden, Lineas: lineas, Total: orden.Total}
}
```

### Strategy Pattern
**Cuándo:** Múltiples implementaciones intercambiables — métodos de pago, impresoras.
```go
// Port — la estrategia abstracta
type MetodoPagoStrategy interface {
    Procesar(ctx context.Context, monto float64) (*ResultadoPago, error)
    Nombre() string
}

// Implementaciones concretas
type PagoEfectivo struct{}
func (p *PagoEfectivo) Procesar(_ context.Context, monto float64) (*ResultadoPago, error) {
    return &ResultadoPago{Exitoso: true, Cambio: monto}, nil
}

type PagoTarjeta struct{ terminal TerminalService }
func (p *PagoTarjeta) Procesar(ctx context.Context, monto float64) (*ResultadoPago, error) {
    return p.terminal.Cobrar(ctx, monto)
}

// Service recibe la estrategia — no sabe cuál es
func (s *CajaService) Cobrar(ctx context.Context, orden *domain.Orden, estrategia MetodoPagoStrategy) error {
    resultado, err := estrategia.Procesar(ctx, orden.Total)
    // ...
}
```

### Observer / Event Pattern (con goroutines)
**Cuándo:** Orden creada → notificar KDS + descontar inventario + auditoría.
```go
// internal/domain/events.go
type OrdenCreadaEvent struct {
    OrdenID  string
    TenantID string
    MesaID   string
    At       time.Time
}

// internal/application/event_bus.go
type EventHandler func(ctx context.Context, event interface{}) error

type EventBus struct {
    handlers map[string][]EventHandler
    mu       sync.RWMutex
}

func (b *EventBus) Subscribe(eventType string, handler EventHandler) {
    b.mu.Lock()
    defer b.mu.Unlock()
    b.handlers[eventType] = append(b.handlers[eventType], handler)
}

func (b *EventBus) Publish(ctx context.Context, event interface{}) {
    // Goroutine por handler — no bloquea el request principal
    typeName := reflect.TypeOf(event).Name()
    for _, h := range b.handlers[typeName] {
        go func(handler EventHandler) {
            handler(ctx, event)
        }(h)
    }
}
```

### Value Object en Go
```go
// internal/domain/value_objects.go
type Email struct {
    value string
}

func NewEmail(s string) (Email, error) {
    if !strings.Contains(s, "@") {
        return Email{}, fmt.Errorf("email inválido: %s", s)
    }
    return Email{value: strings.ToLower(s)}, nil
}

func (e Email) String() string { return e.value }
func (e Email) IsZero() bool   { return e.value == "" }
```