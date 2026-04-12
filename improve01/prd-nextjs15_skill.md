---
name: prd-nextjs15
description: Genera PRDs completos y profesionales para sistemas de software usando el stack Next.js 15 App Router como monolito full-stack con React 19, Prisma, Zod, NextAuth y Tailwind. Usar SIEMPRE que el usuario pida un PRD, documento de requerimientos o especificación de sistema con Next.js, React o TypeScript como base. También activar cuando el usuario diga "crea el PRD", "necesito el PRD", "genera los requerimientos", "especificación del sistema" o cuando describa un sistema con Next.js, App Router, Server Components, Server Actions, Prisma, Zod, NextAuth, shadcn/ui o Tailwind. Si el usuario quiere un stack TypeScript full-stack en un solo proyecto y un solo deploy, este es el skill correcto. Activar también para sistemas web modernos con React táctil (POS, gestión, dashboards) donde Python no es la elección preferida.
---

# PRD Generator — Stack Next.js 15 Full-Stack

Genera PRDs completos para sistemas usando Next.js 15 App Router como monolito. Un proyecto, un deploy, frontend y backend unificados. Basado en proyecto real: RestaurantOS.

## Stack de referencia

```
Runtime:      Node.js 20 LTS
Framework:    Next.js 15 (App Router)
React:        React 19 — Server + Client Components
Lenguaje:     TypeScript 5.x
CSS:          Tailwind CSS v3.4+
Componentes:  shadcn/ui (sobre Tailwind)
ORM:          Prisma 5.x (PostgreSQL prod / SQLite dev)
Validación:   Zod v3.23+ — schema compartido front ↔ back
Auth:         NextAuth v5 (Auth.js) — Credentials + PIN rápido
Hash:         bcrypt v5.x — en Server Actions
WS real-time: Socket.io v4.7+ — KDS, mesas, caja
Cache:        Redis (ioredis) — rooms WebSocket + cache
Impresora:    node-escpos — ESC/POS desde API Route
Estado:       Zustand v4.x — turno activo, caja, auth
Fetching:     TanStack Query v5.x — Client Components
Forms:        React Hook Form + Zod resolver
Gráficas:     Recharts v2.x
Testing:      Vitest + Testing Library
```

## Proceso de generación

### Paso 1 — Recopilar contexto

Preguntas si no están en el mensaje del usuario:

**Negocio:**
- ¿Cliente único o producto SaaS para vender?
- ¿Cuántos usuarios simultáneos máximo?
- ¿Necesita funcionar sin internet temporalmente?

**Dispositivos:**
- ¿Qué dispositivos usarán el sistema? (tablet, PC, celular)
- ¿Hay hardware físico? (impresora, cajón, báscula)
- ¿Multi-sucursal desde v1?

**Módulos:**
- ¿Cuáles son los módulos core?
- ¿Qué puede esperar para v2? (CFDI, mobile, delivery)

### Paso 2 — Criterio Server vs Client Component

**Aplicar SIEMPRE esta tabla antes de asignar tipo a cada vista:**

| Condición | Tipo de componente |
|---|---|
| Interactividad (click, estado, efectos) | Client Component |
| WebSocket / datos tiempo real | Client Component |
| Formulario con validación en tiempo real | Client Component |
| Datos estáticos o cacheados | Server Component |
| Query a DB sin interactividad | Server Component |
| Página de listado, reporte, dashboard | Server Component |

**Regla práctica:** Las páginas de administración son Server Components. Las interfaces operativas (mesero, cocina, caja) son Client Components.

### Paso 3 — Estructura del PRD

Generar SIEMPRE estas secciones:

```
1.  Resumen Ejecutivo
    - Descripción del producto
    - Tabla de por qué Next.js para este sistema
    - Objetivos y non-goals

2.  Stack Tecnológico
    - package.json completo con versiones reales
    - Tabla por capa con rol
    - Nota sobre Node.js 20 LTS (no Bun/Deno por compatibilidad)

3.  Arquitectura del Sistema — Hexagonal adaptada al monolito Next.js
    - Diagrama ASCII hexagonal en monolito:
      [Page/Route] → [Server Action / API Route] → [Use Case] → [Prisma Adapter]
    - Puerto de entrada: Page Server Component o API Route (adapter HTTP)
    - Puerto de salida: Repository interface TypeScript — Prisma como adapter
    - Regla de oro: Use Cases y Domain no importan next/headers ni Prisma directamente
    - Tabla Server vs Client Components por vista
    - Flujo de pedido/acción principal con Server Actions
    - Multi-tenant via session.user.tenantId
    - Patrones de diseño aplicados (ver sección referencia al final)

4.  Módulos y Requisitos Funcionales
    - H3 por módulo
    - Tabla ID | Función | Descripción | Prioridad
    - Prioridades: Crítica / Alta / Media / Baja

5.  Requisitos No Funcionales
    - Latencia Server Actions (<200ms P95)
    - Core Web Vitals LCP (<2.5s)
    - Tamaño bundle JS (<150KB con Server Components)
    - Compatibilidad navegadores/tablets

6.  Historias de Usuario
    - US-001 a US-00N con COMO/QUIERO/PARA
    - Criterios [ ] checkbox

7.  Modelo de Dominio Prisma Schema
    - Schema completo con todos los modelos
    - IDs con @default(cuid())
    - tenantId en TODOS los modelos de negocio
    - Enums para estados y roles
    - Relaciones @relation con campos y referencias
    - Índices @@index para performance

8.  Server Actions y API Routes
    - Server Actions principales con código TypeScript real
    - Transacciones Prisma para operaciones compuestas
    - revalidatePath() después de mutations
    - emitirEvento() WebSocket después de mutations
    - Schemas Zod compartidos — ejemplo de uso en form y action
    - NextAuth config completa con Credentials + PIN

9.  WebSocket — Socket.io
    - lib/socket.ts — servidor con Redis adapter
    - hooks/use-socket.ts — cliente React
    - Rooms: `${sala}:${tenantId}`

10. Consideraciones Técnicas
    - Árbol de directorios completo
    - middleware.ts — protección de rutas por rol
    - Singleton PrismaClient

11. Roadmap de Desarrollo
    - Tabla Fase | Semanas | Objetivo | Entregables

12. Riesgos y Mitigación
    - Técnicos, Operativos, Negocio

13. Hardware Recomendado (si aplica)
    - Tabla con precios MXN

14. Plan de Capacitación (si aplica)
    - Por rol con minutos exactos

15. Checklist de Implementación

16. Modelo de Negocio SaaS (si es producto vendible)
    - Planes en MXN + SLA

17. Glosario
    - Términos Next.js 15 y del dominio
```

### Paso 4 — Decisiones técnicas automáticas

Aplicar SIEMPRE sin preguntar:

| Decisión | Valor Next.js |
|---|---|
| IDs Prisma | `@default(cuid())` — no UUID manual |
| Autenticación | NextAuth Credentials + Credentials PIN por separado |
| Hash contraseñas | bcrypt en Server Action — no en cliente |
| tenantId source | Siempre de `session.user.tenantId` — nunca del request body |
| Mutations | Server Actions con `"use server"` — no endpoints REST separados |
| Invalidar UI | `revalidatePath()` en Server Action tras mutation |
| Tiempo real | Socket.io con Redis adapter para multi-instancia |
| Estado global | Zustand — turno activo, caja abierta, socket status |
| Cache cliente | TanStack Query — staleTime para offline temporal |
| Validación | Zod schema definido en `lib/schemas/` — importado en form y action |
| Forms | React Hook Form + zodResolver — no estado manual |
| Multi-tenant | `tenantId` en todos los modelos — filtro automático desde sesión |
| Protección rutas | `middleware.ts` con auth() de NextAuth |
| Impresora | API Route server-side con node-escpos |
| Arquitectura | Hexagonal ligera: domain/types → lib/repositories(port) → prisma(adapter) → actions/ |
| Patrones | Repository (siempre), Factory (tickets/reportes), Strategy (pagos), Observer (Server Actions) |
| Gráficas | Recharts en Client Component |

### Paso 5 — Patrones de código obligatorios

#### Schema Zod compartido
```typescript
// lib/schemas/ejemplo.ts — se importa en form Y en server action
"use server" NO va aquí — es puro Zod, no action
export const crearRecursoSchema = z.object({
  nombre: z.string().min(1).max(200),
  tenantId: z.string().cuid(),  // NO incluir — viene de la sesión
})
export type CrearRecursoInput = z.infer<typeof crearRecursoSchema>
```

#### Server Action estándar
```typescript
"use server"
export async function crearRecurso(input: CrearRecursoInput) {
  const session = await auth()
  if (!session) throw new Error("No autenticado")
  const data = crearRecursoSchema.parse(input)
  const tenantId = session.user.tenantId  // siempre de la sesión

  const resultado = await prisma.$transaction(async (tx) => {
    // operaciones atómicas aquí
  })

  await emitirEvento(`sala:${tenantId}`, "evento", datos)
  revalidatePath("/ruta")
  return { success: true }
}
```

#### Singleton PrismaClient
```typescript
// lib/prisma.ts
import { PrismaClient } from "@prisma/client"
const globalForPrisma = globalThis as unknown as { prisma: PrismaClient }
export const prisma = globalForPrisma.prisma ?? new PrismaClient()
if (process.env.NODE_ENV !== "production") globalForPrisma.prisma = prisma
```

#### Middleware protección
```typescript
// middleware.ts — rutas protegidas por rol
export default auth((req) => {
  // leer session desde req.auth — nunca re-autenticar
  // redirigir según rol y ruta
})
```

### Paso 6 — Adaptaciones por dominio

**Restaurante / Bar / Cafetería:**
- Socket.io obligatorio — KDS, plano mesas, caja
- Mesa enum: DISPONIBLE/OCUPADA/CUENTA_PENDIENTE
- TurnoCaja + SalidaCaja + Pago con meseroId para propinas
- VariantePlatillo con precioDelta
- ModificadorAplicado como snapshot (no FK activa)
- Estacion en Platillo para filtros KDS

**Clínica / Veterinaria / Salud:**
- No Socket.io — Server Components con revalidación
- Expediente con soft delete (deletedAt)
- Citas con máquina de estados (enum EstadoCita)
- AdjuntoExpediente — upload con Next.js y S3/local
- Portal pacientes/dueños con sesión separada

**POS General / Tienda / Inventario:**
- Productos por unidad y por peso (unidad: "kg"|"pza")
- TurnoCaja simplificado — sin propinas
- Proveedor y Compra para gestión de abastecimiento

**Dashboard / Admin / Panel interno:**
- Mayormente Server Components — mínimo Client Components
- TanStack Query solo donde hay interactividad
- Sin Socket.io si no hay tiempo real requerido

### Paso 7 — Calidad del PRD

Verificar antes de entregar:

- [ ] package.json con versiones reales 2026
- [ ] Schema Prisma con todos los modelos y relaciones
- [ ] `cuid()` como ID en todos los modelos
- [ ] `tenantId` en todos los modelos de negocio
- [ ] Enums Prisma para todos los estados
- [ ] Server Actions con auth() + parse(Zod) + prisma.$transaction
- [ ] revalidatePath() y emitirEvento() en actions que los necesiten
- [ ] NextAuth con dos Credentials (email+pass y PIN)
- [ ] middleware.ts con protección por rol
- [ ] Socket.io si el sistema tiene tiempo real
- [ ] Tabla Server vs Client Components por vista
- [ ] Riesgo de seguridad multi-tenant documentado
- [ ] Estructura de directorios refleja separación domain/use-cases/infra
- [ ] Repository interface TypeScript documentada como Port
- [ ] Patrones de diseño mencionados en sección de arquitectura

### Paso 8 — Formato de entrega

- Generar el PRD en **Markdown descargable** via `create_file`
- Ruta: `/mnt/user-data/outputs/PRD_{NombreSistema}_NextJS15.md`
- Presentar con `present_files`
- Resumen de 3–5 puntos clave después del archivo

---

## Diferencias clave vs otros stacks

| Aspecto | Next.js 15 | FastAPI + Jinja2 | Go + Wails |
|---|---|---|---|
| Backend | Server Actions + API Routes | Endpoints FastAPI | Handlers Fiber |
| Frontend | React 19 Server/Client | Jinja2 SSR + HTMX | React + MUI |
| ORM | Prisma (schema declarativo) | SQLAlchemy 2.0 (Mapped[]) | GORM |
| Validación | Zod (compartida) | Pydantic v2 | go-playground/validator |
| Auth | NextAuth Credentials | JWT + Argon2id | golang-jwt + bcrypt |
| Desktop | No nativo (PWA) | PyWebview + PyInstaller | Wails — binario nativo |
| Deploy | Vercel / 1 servicio | Docker multi-container | Binario único + Docker |
| Lenguaje | TypeScript full-stack | Python backend | Go backend + TS frontend |
| Ideal para | Productos web modernos | Apps Python / IA | Desktop apps / POS ligero |

---

## Arquitectura Hexagonal — Referencia Rápida (Next.js 15)

### Principio central adaptado al monolito
Next.js es un monolito — todo vive en un repo. Pero eso no significa que todo
se mezcle. La arquitectura hexagonal se aplica como separación de capas dentro
del mismo proyecto, no como microservicios.

```
┌─────────────────────────────────────────────────────────┐
│              ADAPTADORES ENTRADA                        │
│    Page (Server Component) / API Route / Server Action  │
└────────────────────┬────────────────────────────────────┘
                     │ llama a
┌────────────────────▼────────────────────────────────────┐
│              USE CASES / APPLICATION                    │
│    lib/use-cases/crear-orden.ts                         │
│    lib/use-cases/cobrar-orden.ts                        │
└──────────┬──────────────────────────┬───────────────────┘
           │ usa                      │ usa interface (Port)
┌──────────▼──────────┐   ┌──────────▼───────────────────┐
│   DOMAIN TYPES      │   │   PORTS (interfaces TS)      │
│   types/orden.ts    │   │   OrdenRepository interface  │
│   types/usuario.ts  │   │   PrinterService interface   │
│   Validaciones Zod  │   │                              │
└─────────────────────┘   └──────────┬───────────────────┘
                                     │ implementado por
                          ┌──────────▼───────────────────┐
                          │   ADAPTADORES SALIDA         │
                          │   lib/repositories/prisma-   │
                          │   orden-repository.ts        │
                          │   lib/printing/escpos.ts     │
                          └──────────────────────────────┘
```

### Estructura de directorios hexagonal (Next.js)
```
├── app/                         # Adaptadores de entrada (Next.js routing)
│   ├── (app)/
│   │   ├── mesero/page.tsx      # Server Component — llama use case
│   │   └── caja/page.tsx
│   ├── actions/                 # Server Actions — orquestan use cases
│   │   ├── ordenes.ts
│   │   └── caja.ts
│   └── api/                     # API Routes — WebSocket, impresión
│       └── print/route.ts
│
├── lib/
│   ├── domain/                  # Tipos y reglas de negocio puras
│   │   ├── types.ts             # Interfaces TypeScript (no Prisma types)
│   │   ├── schemas.ts           # Schemas Zod compartidos front/back
│   │   └── errors.ts            # Errores de negocio tipados
│   │
│   ├── use-cases/               # Lógica de aplicación
│   │   ├── crear-orden.ts       # Solo conoce interfaces/ports
│   │   └── cobrar-orden.ts
│   │
│   ├── ports/                   # Interfaces (contratos)
│   │   ├── orden-repository.ts  # interface OrdenRepository
│   │   └── printer-service.ts   # interface PrinterService
│   │
│   └── infrastructure/          # Adaptadores concretos
│       ├── prisma-orden-repo.ts  # Implementa OrdenRepository con Prisma
│       ├── escpos-printer.ts
│       └── prisma.ts            # Singleton PrismaClient
│
├── components/                  # UI — Client Components
├── hooks/                       # Custom hooks React
└── prisma/                      # Schema y migraciones
```

### Port (interface TypeScript)
```typescript
// lib/ports/orden-repository.ts
import type { Orden, CreateOrdenInput } from '@/lib/domain/types'

// El Use Case solo conoce esta interfaz — nunca Prisma directamente
export interface OrdenRepository {
  save(input: CreateOrdenInput, tenantId: string): Promise<Orden>
  findById(id: string, tenantId: string): Promise<Orden | null>
  findActivasByMesa(mesaId: string, tenantId: string): Promise<Orden[]>
  update(id: string, data: Partial<Orden>, tenantId: string): Promise<Orden>
}
```

### Adapter Prisma (implementa el port)
```typescript
// lib/infrastructure/prisma-orden-repo.ts
import { prisma } from '@/lib/infrastructure/prisma'
import type { OrdenRepository } from '@/lib/ports/orden-repository'
import type { Orden } from '@/lib/domain/types'

export class PrismaOrdenRepository implements OrdenRepository {
  async save(input: CreateOrdenInput, tenantId: string): Promise<Orden> {
    return prisma.orden.create({
      data: { ...input, tenantId },
      include: { items: true, mesa: true }
    })
  }
  // ...
}
```

### Server Action con Use Case
```typescript
// app/actions/ordenes.ts
'use server'
import { auth } from '@/auth'
import { PrismaOrdenRepository } from '@/lib/infrastructure/prisma-orden-repo'
import { CrearOrdenUseCase } from '@/lib/use-cases/crear-orden'
import { crearOrdenSchema } from '@/lib/domain/schemas'

export async function crearOrden(input: unknown) {
  const session = await auth()
  const tenantId = session!.user.tenantId

  const data = crearOrdenSchema.parse(input)

  // Composición manual — sin DI framework
  const repo = new PrismaOrdenRepository()
  const useCase = new CrearOrdenUseCase(repo)
  
  const orden = await useCase.execute(data, tenantId)
  revalidatePath('/mesero')
  return orden
}
```

---

## Patrones de Diseño — Referencia Rápida (Next.js 15)

### Repository Pattern (siempre)
```typescript
// El Use Case trabaja contra la interface — Prisma es un detalle de infra
export class CrearOrdenUseCase {
  constructor(private repo: OrdenRepository) {}  // recibe la interfaz
  
  async execute(input: CreateOrdenInput, tenantId: string): Promise<Orden> {
    const orden = await this.repo.save(input, tenantId)
    return orden
  }
}
```

### Factory Pattern
**Cuándo:** Construir objetos complejos — tickets, emails, reportes Excel.
```typescript
// lib/domain/ticket-factory.ts
export class TicketFactory {
  static crearDesdeOrden(orden: Orden, config: TenantConfig): TicketData {
    return {
      numero: orden.numeroOrden,
      mesa: orden.mesa.numero,
      lineas: orden.items.map(item => ({
        nombre: item.platillo.nombre,
        cantidad: item.cantidad,
        precio: item.precioUnitario,
        subtotal: item.subtotal,
        modificadores: item.modificadores.map(m => m.nombre)
      })),
      total: orden.total,
      fecha: new Date()
    }
  }
}
```

### Strategy Pattern
**Cuándo:** Múltiples implementaciones intercambiables — métodos de pago.
```typescript
// lib/ports/metodo-pago.ts
export interface MetodoPagoStrategy {
  procesar(monto: number): Promise<ResultadoPago>
  nombre(): string
}

// Implementaciones
export class PagoEfectivo implements MetodoPagoStrategy {
  async procesar(monto: number) { return { exitoso: true, cambio: monto } }
  nombre() { return 'efectivo' }
}

export class PagoTarjeta implements MetodoPagoStrategy {
  async procesar(monto: number) { /* integración terminal */ }
  nombre() { return 'tarjeta' }
}

// Use case recibe la estrategia — no sabe cuál
export class CobrarOrdenUseCase {
  async execute(orden: Orden, estrategia: MetodoPagoStrategy) {
    const resultado = await estrategia.procesar(orden.total)
    // ...
  }
}
```

### Observer con Server Actions
**Cuándo:** Una acción dispara múltiples efectos — crear orden → notificar KDS, descontar inventario.
```typescript
// En Next.js, el "observer" es composición directa en el Server Action
export async function crearOrden(input: CreateOrdenInput) {
  const session = await auth()
  const tenantId = session!.user.tenantId

  await prisma.$transaction(async (tx) => {
    // 1. Crear orden (subject)
    const orden = await tx.orden.create({ data: { ...input, tenantId } })

    // 2. Observers síncronos (en la misma transacción)
    await descontarInventario(tx, orden)
    await actualizarEstadoMesa(tx, orden.mesaId, 'OCUPADA')

    // 3. Observer asíncrono (fuera de transacción)
    // emit WebSocket — no bloquea el request
    emitirEvento(`kds:${tenantId}`, 'nueva_orden', orden)
  })
}
```

### Value Object con Zod
```typescript
// lib/domain/value-objects.ts
import { z } from 'zod'

// Zod como mecanismo de VO — validación + tipado en uno
export const EmailSchema = z.string().email('Email inválido').toLowerCase()
export type Email = z.infer<typeof EmailSchema>

export const MontoSchema = z.number().positive('El monto debe ser positivo').multipleOf(0.01)
export type Monto = z.infer<typeof MontoSchema>

// Uso en dominio — el schema valida en el boundary
const email = EmailSchema.parse(rawInput)  // lanza si inválido
```