# Patrón de Arquitectura Hexagonal (Ports & Adapters)

## Principios Fundamentales

El dominio debe ser completamente independiente de la infraestructura. Los frameworks y detalles técnicos deben ser detalles de implementación, no parte del dominio.

## Diagrama General

```
┌─────────────────────────────────────────────────────────┐
│              ADAPTADORES ENTRADA                        │
│         HTTP / WebSocket / CLI / Message Queue          │
└────────────────────┬────────────────────────────────────┘
                     │ llama a
┌────────────────────▼────────────────────────────────────┐
│              APPLICATION LAYER                          │
│              Use Cases / Services                       │
└──────────┬──────────────────────────┬───────────────────┘
           │ usa                      │ usa interface (Port)
┌──────────▼──────────┐   ┌──────────▼───────────────────┐
│      DOMAIN         │   │   PORTS (interfaces)        │
│  Entidades, VOs     │   │   Repository, Printer,      │
│  Reglas de negocio  │   │   EmailService, etc.        │
└─────────────────────┘   └──────────┬───────────────────┘
                                   │ implementado por
                        ┌──────────▼───────────────────┐
                        │   ADAPTADORES SALIDA         │
                        │   Database, SMTP, API,      │
                        │   File System, etc.          │
                        └──────────────────────────────┘
```

## Componentes

### 1. Domain Layer (Capa de Dominio)
- Entidades de negocio puras
- Value Objects (inmutables)
- Eventos de dominio
- Excepciones de negocio
- **NO** importa frameworks ni infraestructura

### 2. Ports (Interfaces)
- Definen contratos que el dominio necesita
- Ejemplos: Repository, EmailService, PrinterService
- Son interfaces puras, sin implementación

### 3. Adapters de Entrada (Driving Adapters)
- Implementan puertos de entrada
- Ejemplos: HTTP handlers, WebSocket, CLI, Message Queue consumers
- Traducen protocolos externos a llamadas al dominio

### 4. Adapters de Salida (Driven Adapters)
- Implementan puertos de salida
- Ejemplos: Database adapters, SMTP, API clients, File System
- Traducen llamadas del dominio a protocolos externos

## Ejemplos por Stack

### FastAPI (Python)
- Domain: `app/domain/entities/`
- Ports: `app/application/ports/`
- Use Cases: `app/application/use_cases/`
- Adapters Entrada: `app/adapters/http/`
- Adapters Salida: `app/infrastructure/persistence/`

### Next.js 15 (TypeScript)
- Domain: `lib/domain/`
- Ports: `lib/ports/`
- Use Cases: `lib/use-cases/`
- Adapters Entrada: `app/actions/`, `app/api/`
- Adapters Salida: `lib/infrastructure/`

### Go (Go + Fiber)
- Domain: `internal/domain/`
- Ports: `internal/application/ports/`
- Use Cases: `internal/application/services/`
- Adapters Entrada: `internal/adapters/http/`
- Adapters Salida: `internal/infrastructure/persistence/`

## Anti-Patrones a Evitar

❌ El dominio importa FastAPI/React/Go frameworks
❌ Los Use Cases contienen lógica de infraestructura
❌ Los adaptadores contienen lógica de negocio
❌ Violar la inversión de dependencias (domain depende de infra)

## Beneficios

1. **Testabilidad**: El dominio se puede testear sin infraestructura
2. **Flexibilidad**: Cambiar frameworks es trivial (solo cambiar adapters)
3. **Mantenibilidad**: Lógica de negocio aislada y clara
4. **Escalabilidad**: Fácil agregar nuevos adapters sin tocar el dominio
