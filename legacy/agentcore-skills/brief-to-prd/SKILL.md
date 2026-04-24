---
name: brief-to-prd
description: Skill principal de AgentCore v2.0 que genera PRD profesional + stack_config.yml desde un PROJECT-BRIEF-FULL.yaml completo. Activa cuando el usuario proporciona un Brief completo o dice "generar PRD del brief", "crear PRD desde brief", "procesar brief", o cuando el archivo PROJECT-BRIEF-FULL.yaml está presente en el directorio de trabajo. Este skill coordina todo el flujo: leer el brief, calcular complejidad, hacer preguntas interactivas para secciones faltantes, cargar configuración específica del stack y generar ambos artefactos en UN SOLO comando.
---

# Brief to PRD Generator — AgentCore v2.0

Este skill es el corazón del flujo de trabajo de AgentCore v2.0. Convierte un PROJECT-BRIEF-FULL.yaml en dos artefactos esenciales: un PRD profesional y un stack_config.yml de configuración del stack seleccionado.

## Stack de referencia

Este skill es AGNÓSTICO al stack — coordina pero no genera. Delega la generación del PRD a los skills específicos:
- **prd-nextjs15**: Para stacks Next.js 15 App Router
- **prd-fastapi**: Para stacks FastAPI + Python
- **prd-go-wails**: Para stacks Go + Fiber + Wails

## Paso 1 — Load and Parse Brief

### Ubicación del Brief
El Brief debe estar en la raíz del proyecto:
```
PROJECT-BRIEF-FULL.yaml
```

### Validación
1. **Verificar existencia del archivo**:
   - Si no existe: "❌ Error: No encontré PROJECT-BRIEF-FULL.yaml. Por favor crea el brief primero."
   - Si existe: continuar.

2. **Validar contra schema**:
   ```yaml
   brief-schema.json:  # Esquema de validación (si existe)
   ```
   - Si existe brief-schema.json: validar estructura YAML contra schema
   - Si falla la validación: reportar errores específicos
   - Si no existe schema: proceder con validación básica

3. **Detectar stack seleccionado**:
   ```yaml
   stack_seleccionado: "nextjs15" | "fastapi" | "go-wails"
   ```
   - Leer el campo `stack_seleccionado` del brief
   - Validar que sea uno de los stacks soportados
   - Si es inválido: mostrar stacks disponibles y pedir corrección

4. **Identificar secciones completadas vs vacías**:
   - Iterar sobre todas las secciones del brief
   - Marcar como COMPLETA si tiene contenido no nulo
   - Marcar como VACÍA si es null, "", o []
   - Crear lista de secciones_faltantes para questioning

5. **Calcular complexity_score preliminar**:
   - Basado en los campos presentes en el brief
   - Ver Paso 2 para el algoritmo completo

### Validación básica de campos críticos
Si el stack ya está seleccionado, verificar que estos campos no sean nulos:

| Campo | Descripción |
|-------|-------------|
| `nombre_proyecto` | Nombre del sistema a construir |
| `tipo_entrega` | Tipo de sistema (web, desktop, móvil, híbrido) |
| `criticalidad` | Nivel de criticidad del sistema |
| `team_size` | Tamaño del equipo de desarrollo |
| `timeframe` | Plazo estimado de desarrollo |
| `bounded_contexts` | Lista de contextos delimitados |
| `multi_tenant` | Si es sistema multi-tenant |
| `ai_features` | Si tiene características de IA |
| `ai_tools` | Herramientas de IA a usar (mcp, pycaret, fastai, huggingface, adk, ninguno) |

Si alguno de estos es nulo, hacer pregunta en Paso 3.

## Paso 2 — Calculate Complexity Score

El `complexity_score` es un número de 1 a 10 que indica la complejidad general del proyecto. Se usa para ajustar el nivel de detalle del PRD y las decisiones técnicas.

### Algoritmo de cálculo

```python
def calculate_complexity_score(brief):
    score = 1  # Base

    # 1. Criticalidad (0-2 puntos)
    criticality_map = {
        "baja": 0,
        "media": 1,
        "alta": 2,
        "crítica": 2
    }
    score += criticality_map.get(brief.get("criticalidad", "media"), 1)

    # 2. Team size (0-2 puntos)
    team_size = brief.get("team_size", 1)
    if team_size == 1:
        score += 0
    elif team_size <= 3:
        score += 1
    else:
        score += 2

    # 3. Timeframe (0-1 punto)
    timeframe = brief.get("timeframe", "1-3 meses")
    if "1-2 meses" in timeframe or "1 mes" in timeframe:
        score += 0  # Ajustado - MVP rápido
    elif "3-6 meses" in timeframe:
        score += 1

    # 4. Tipo de ejecución (0-1 punto)
    tipo_ejecucion = brief.get("tipo_ejecucion", "monolito")
    if tipo_ejecucion == "microservicios":
        score += 1
    elif tipo_ejecucion == "modular":
        score += 0.5

    # 5. Bounded contexts (0-1 punto)
    bounded_contexts = brief.get("bounded_contexts", [])
    if len(bounded_contexts) <= 2:
        score += 0
    elif len(bounded_contexts) <= 5:
        score += 0.5
    else:
        score += 1

    # 6. Multi-tenant (0-1 punto)
    if brief.get("multi_tenant", False):
        score += 1

    # 7. AI features (0-1 punto)
    ai_features = brief.get("ai_features", [])
    if ai_features and len(ai_features) > 0:
        score += 1

    # 8. Hardware integration (0-1 punto)
    hardware = brief.get("hardware", [])
    if hardware and len(hardware) > 0:
        score += 1

    # Normalizar a rango 1-10
    return min(max(int(score), 1), 10)
```

### Interpretación del score

| Score | Significado | Ajustes en PRD |
|-------|-------------|----------------|
| 1-3 | MVP simple | Enfoque en features core, arquitectura simplificada |
| 4-6 | Proyecto estándar | Arquitectura completa con patrones esenciales |
| 7-10 | Sistema complejo | Arquitectura avanzada, múltiples patrones, alta robustez |

## Paso 3 — Interactive Questioning

Para cada sección con valores nulos/vacíos, hacer preguntas AL TIEMPO. NO hacer una pregunta por vez — agruparlas.

### Reglas de questioning

1. **Preguntar solo si CRÍTICA para el stack**:
   - Cada stack tiene una lista de campos críticos
   - Si el campo no es crítico, usar valor por defecto del stack

2. **Usar valores por defecto del stack**:
   - Cargar desde `.claude/stacks/{stack}/config.yaml`
   - Aplicar automáticamente si el usuario no responde

3. **Marcar como [N/A] si no aplica**:
   - Si el usuario indica que una sección no aplica, marcarla como tal

4. **Agrupar preguntas por categoría**:
   - No hacer una pregunta por vez
   - Agrupar por: Negocio, Técnico, Arquitectura, Integraciones

### Campos críticos por stack

#### Next.js 15
```yaml
campos_criticos:
  - nombre_proyecto
  - tipo_entrega
  - criticalidad
  - team_size
  - timeframe
  - bounded_contexts
  - multi_tenant
  - frontend_framework
  - ui_library
  - realtime_required
  - ai_tools  # "mcp" | "pycaret" | "fastai" | "huggingface" | "adk" | "ninguno"
```

#### FastAPI
```yaml
campos_criticos:
  - nombre_proyecto
  - tipo_entrega
  - criticalidad
  - team_size
  - timeframe
  - bounded_contexts
  - multi_tenant
  - python_version
  - frontend_type  # "ssr" | "spa" | "desktop"
  - hardware
  - ai_tools  # "mcp" | "pycaret" | "fastai" | "huggingface" | "adk" | "ninguno"
```

#### Go Wails
```yaml
campos_criticos:
  - nombre_proyecto
  - tipo_entrega
  - criticalidad
  - team_size
  - timeframe
  - bounded_contexts
  - multi_tenant
  - go_version
  - frontend_type  # "spa" | "desktop"
  - hardware
  - websocket_required
  - ai_tools  # "mcp" | "pycaret" | "fastai" | "huggingface" | "adk" | "ninguno"
```

### Formato de preguntas interactivas

```
📋 **Proyecto: {nombre_proyecto}**
🔧 **Stack: {stack_seleccionado}**
⚡ **Complejidad: {complexity_score}/10**

---

### 🔍 Necesito completar algunas secciones del Brief:

#### 📊 Negocio
1. ¿Qué es el sistema? (1-2 líneas)
2. ¿Para quién es? (target: dueño único, SaaS, etc.)
3. ¿Cuál es el objetivo principal del MVP?

#### 💻 Técnico
1. ¿Qué frameworks/tecnologías prefieres para el frontend?
2. ¿Necesitas tiempo real? (WebSocket, polling, etc.)
3. ¿Hay integraciones con servicios externos? (pagos, email, etc.)
4. ¿Usaras herramientas de IA? (MCP, PyCareT, FastAI, Hugging Face, ADK, ninguno)

#### 🏗️ Arquitectura
1. ¿Cuántos bounded contexts necesitas?
2. ¿Es multi-tenant? (múltulos clientes en una instancia)
3. ¿Hay restricciones de seguridad o compliance?

---

**Responde con:**
- Respuestas directas a las preguntas, o
- "Usa defaults del stack {nombre}" para usar configuración predefinida, o
- "[N/A]" para secciones que no aplican

**Si prefieres editar el brief manualmente:**
Edita PROJECT-BRIEF-FULL.yaml y vuelve a ejecutar el comando.
```

## Paso 4 — Load Stack-Specific Configuration

### Ubicación de la configuración del stack

```
.claude/stacks/{stack_seleccionado}/config.yaml
```

### Estructura de config.yaml

```yaml
stack:
  name: "nextjs15"
  display_name: "Next.js 15 App Router Full-Stack"
  version: "1.0.0"

defaults:
  # Valores por defecto para campos del brief
  criticalidad: "media"
  team_size: 2
  timeframe: "3-6 meses"
  tipo_ejecucion: "monolito"
  multi_tenant: false

  # Next.js 15 específicos
  node_version: "20 LTS"
  nextjs_version: "15.0.0"
  react_version: "19.0.0"
  typescript_version: "5.3.0"
  prisma_version: "5.7.0"
  tailwind_version: "3.4.0"
  shadcn_version: "latest"

  # Decisiones técnicas automáticas
  ids_type: "cuid"
  auth_method: "nextauth_credentials"
  hash_method: "bcrypt"
  orm: "prisma"
  validation: "zod"
  state_management: "zustand"
  fetching: "tanstack_query"

technical_decisions:
  # Lista de decisiones aplicadas automáticamente
  - decision: "ID Type"
    value: "cuid()"
    reason: "Next.js/Prisma standard, evita colisiones sin UUID overhead"

  - decision: "Auth Method"
    value: "NextAuth Credentials + PIN"
    reason: "Sin backend separado, integración nativa con App Router"

  - decision: "Hash Method"
    value: "bcrypt en Server Actions"
    reason: "Seguro, estándar, funciona en Edge Runtime"

  - decision: "ORM"
    value: "Prisma 5.x"
    reason: "Schema declarativo, type-safe, migraciones automáticas"

patterns:
  # Patrones de diseño a aplicar
  required:
    - repository
    - factory
    - strategy
    - observer

  optional:
    - unit_of_work
    - value_object
    - adapter

code_patterns:
  # Patrones de código específicos del stack
  server_action: |
    "use server"
    export async function crearRecurso(input: InputType) {
      const session = await auth()
      const tenantId = session.user.tenantId
      const data = schema.parse(input)

      const resultado = await prisma.$transaction(async (tx) => {
        // operaciones atómicas
      })

      revalidatePath("/ruta")
      return { success: true, data: resultado }
    }

  singleton_prisma: |
    // lib/prisma.ts
    import { PrismaClient } from "@prisma/client"
    const globalForPrisma = globalThis as unknown as { prisma: PrismaClient }
    export const prisma = globalForPrisma.prisma ?? new PrismaClient()
    if (process.env.NODE_ENV !== "production") globalForPrisma.prisma = prisma

file_structure:
  # Estructura de directorios esperada
  root:
    - app/
    - lib/
    - components/
    - prisma/
    - public/
```

### Aplicar configuración

1. **Cargar config.yaml**:
   - Leer archivo de configuración del stack
   - Parsear YAML a estructura de datos

2. **Aplicar defaults**:
   - Para cada campo nulo en el brief
   - Si existe default en config.yaml
   - Asignar valor al brief

3. **Validar campos críticos**:
   - Después de aplicar defaults
   - Verificar que todos los campos críticos tienen valor
   - Si faltan: hacer preguntas en Paso 3

4. **Cargar patrones de código**:
   - Guardar patrones para usar en generación del PRD
   - Disponibles para el skill específico del stack

## Paso 5 — Generate Both Artifacts

Este es el paso de ORQUESTACIÓN. El skill `brief-to-prd` NO genera el PRD directamente — DELEGA al skill específico del stack.

### 5.1 Generate PRD (Stack-Specific Skill)

#### Identificar el skill a usar

```python
def get_prd_skill(stack_seleccionado):
    skill_map = {
        "nextjs15": "prd-nextjs15",
        "fastapi": "prd-fastapi",
        "go-wails": "prd-go-wails"
    }
    return skill_map.get(stack_seleccionado)
```

#### Preparar el contexto para el skill

El contexto que se pasa al skill específico debe incluir:

```yaml
context:
  brief:
    # Todo el contenido de PROJECT-BRIEF-FULL.yaml
  stack_config:
    # Configuración cargada desde .claude/stacks/{stack}/config.yaml
  complexity_score: 7
  patterns:
    # Patrones de código del stack
  technical_decisions:
    # Decisiones técnicas automáticas
```

#### Llamar al skill específico

```bash
# NOTA: Esta es una abstracción. En la implementación real,
# el skill brief-to-prd invoca el skill correspondiente
# pasándole el contexto preparado.

SKILL: prd-{stack}
INPUT: {context preparado}
OUTPUT: PRD Markdown
```

### 5.2 Generate stack_config.yml

#### Estructura de stack_config.yml

```yaml
# ========================================
# AgentCore Stack Configuration
# ========================================
project:
  name: "{nombre_proyecto}"
  version: "1.0.0"
  created_at: "2026-04-12"

stack:
  selected: "{stack_seleccionado}"
  display_name: "{display_name del stack}"
  complexity_score: {complexity_score}

  # Versiones de tecnologías
  technologies:
    # Stack Next.js 15
    node: "20 LTS"
    nextjs: "15.0.0"
    react: "19.0.0"
    typescript: "5.3.0"
    prisma: "5.7.0"
    tailwind: "3.4.0"
    shadcn: "latest"

    # Stack FastAPI
    python: "3.12+"
    fastapi: "0.115+"
    sqlalchemy: "2.0+"
    alembic: "1.13+"
    pydantic: "2.0+"

    # Stack Go Wails
    go: "1.22+"
    fiber: "v2"
    gorm: "latest"
    wails: "v2"

# Decisiones técnicas aplicadas
technical_decisions:
  - name: "ID Type"
    value: "{ids_type}"
    reason: "{razón desde config.yaml}"
    applied_at: "2026-04-12"

  - name: "Auth Method"
    value: "{auth_method}"
    reason: "{razón desde config.yaml}"
    applied_at: "2026-04-12"

  - name: "Hash Method"
    value: "{hash_method}"
    reason: "{razón desde config.yaml}"
    applied_at: "2026-04-12"

  - name: "ORM"
    value: "{orm}"
    reason: "{razón desde config.yaml}"
    applied_at: "2026-04-12"

# Patrones de diseño a implementar
patterns:
  required:
    - repository
    - factory
    - strategy
    - observer

  optional:
    - unit_of_work
    - value_object
    - adapter

# Patrones de código predefinidos
code_patterns:
  singleton_database:
    description: "Singleton para conexión a base de datos"
    file: "lib/prisma.ts"  # o lib/db.py o internal/db/db.go
    template: |
      {template desde config.yaml}

  server_action:
    description: "Patrón estándar para Server Actions o handlers"
    file: "app/actions/crear-recurso.ts"
    template: |
      {template desde config.yaml}

# Arquitectura
architecture:
  type: "{tipo_ejecución}"  # monolito | microservicios | modular
  pattern: "hexagonal"

  bounded_contexts:
    - name: "{context1}"
      modules:
        - "{modulo1}"
        - "{modulo2}"

    - name: "{context2}"
      modules:
        - "{modulo3}"

# Multi-tenant
multi_tenant: {multi_tenant}
tenant_strategy: "row_level"  # | schema_level | database_level

# Features
features:
  ai: {boolean}
  ai_providers:
    - "{provider1}"

  realtime: {boolean}
  realtime_method: "{websocket|polling}"

  offline: {boolean}
  offline_strategy: "{zustand_persist|localstorage|pwa}"

# Integraciones
integrations:
  - name: "{integracion1}"
    type: "payment|email|storage|analytics|other"
    provider: "{provider}"
    required: true

# Testing
testing:
  framework: "{vitest|pytest|testify}"
  coverage_target: 80
  e2e: {boolean}

# Deployment
deployment:
  platform: "{vercel|docker|bare_metal}"
  ci_cd: "{github_actions|gitlab_ci|other}"

# Security
security:
  auth: "{auth_method}"
  hash: "{hash_method}"
  encryption: "{encryption_method}"
  rate_limiting: true
  cors_enabled: true
```

#### Generar el archivo

```bash
# Crear stack_config.yml en .claude/
OUTPUT: .claude/stack_config.yml
FORMAT: YAML
```

## Paso 6 — Output

### Generar ambos archivos

```bash
# 1. Generar PRD
OUTPUT: .claude/outputs/PRD_{nombre_proyecto}_{stack}.md
FORMAT: Markdown

# 2. Generar stack_config.yml
OUTPUT: .claude/stack_config.yml
FORMAT: YAML
```

### Presentar resumen con formato

```
✅ **Brief procesado exitosamente**

📋 **Proyecto**: {nombre_proyecto}
🔧 **Stack**: {display_name}
⚡ **Complejidad**: {complexity_score}/10

---

### 📄 Artefactos generados:

1. **PRD Profesional**
    📁 `.claude/outputs/PRD_{nombre_proyecto}_{stack}.md`
    - Requisitos funcionales y no funcionales
    - Arquitectura hexagonal completa
    - Patrones de diseño aplicados
    - Roadmap de desarrollo
    - Riesgos y mitigaciones

2. **Configuración del Stack**
   📁 `.claude/stack_config.yml`
   - Decisiones técnicas documentadas
   - Versiones de tecnologías
   - Patrones de código predefinidos
   - Configuración de arquitectura
   - Integraciones y testing

---

### 🚀 Próximos pasos:

1. **Revisar el PRD**: Verificar que cubre todos los requisitos
2. **Ajustar configuración**: Modificar stack_config.yml si es necesario
3. **Iniciar desarrollo**: Usar los patrones de código predefinidos
4. **Configurar CI/CD**: Basarse en la sección de deployment

---

**¿Deseas:**
- [ ] Ver el PRD generado
- [ ] Ver la configuración del stack
- [ ] Ajustar alguna sección
- [ ] Comenzar con el primer módulo
```

## Example Session

```
Usuario: Generar PRD del brief

Brief-to-PRD Skill:

📋 Cargando PROJECT-BRIEF-FULL.yaml...
✅ Brief encontrado y validado

🔧 Stack detectado: nextjs15
⚡ Calculando complejidad...
✅ Complexity Score: 7/10

---

🔍 **Necesito completar algunas secciones del Brief:**

#### 📊 Negocio
1. ¿Qué es el sistema?
2. ¿Para quién es? (target: dueño único, SaaS, etc.)
3. ¿Cuál es el objetivo principal del MVP?

#### 💻 Técnico
1. ¿Qué frameworks prefieres para el frontend?
2. ¿Necesitas tiempo real?
3. ¿Hay integraciones con servicios externos?
4. ¿Usaras herramientas de IA? (MCP, PyCareT, FastAI, Hugging Face, ADK, ninguno)

---

Usuario:
Es un sistema de gestión de restaurantes con POS, KDS de cocina y gestión de mesas.
Para un restaurante único dueño.
Objetivo MVP: POS funcional con pedidos, cocina y caja en 4 semanas.
Frontend: React + Tailwind (estoy cómodo con React).
Sí, tiempo real para KDS y mesas.
Pagos con terminal, email para comandas.

Brief-to-PRD Skill:

✅ **Brief completado**

🔧 Aplicando configuración de Next.js 15...
✅ Defaults aplicados
✅ Patrones de código cargados

📝 Generando PRD con skill prd-nextjs15...
✅ PRD generado

⚙️ Generando stack_config.yml...
✅ Configuración generada

---

✅ **Brief procesado exitosamente**

📋 **Proyecto**: RestaurantPOS
🔧 **Stack**: Next.js 15 App Router Full-Stack
⚡ **Complejidad**: 7/10

---

### 📄 Artefactos generados:

1. **PRD Profesional**
    📁 `.claude/outputs/PRD_RestaurantPOS_NextJS15.md`
    - Requisitos funcionales y no funcionales
    - Arquitectura hexagonal completa
    - Patrones de diseño aplicados
    - Roadmap de desarrollo
    - Riesgos y mitigaciones

2. **Configuración del Stack**
   📁 `.claude/stack_config.yml`
   - Decisiones técnicas documentadas
   - Versiones de tecnologías
   - Patrones de código predefinidos
   - Configuración de arquitectura
   - Integraciones y testing

---

### 🚀 Próximos pasos:

1. **Revisar el PRD**: Verificar que cubre todos los requisitos
2. **Ajustar configuración**: Modificar stack_config.yml si es necesario
3. **Iniciar desarrollo**: Usar los patrones de código predefinidos
4. **Configurar CI/CD**: Basarse en la sección de deployment

---

**¿Deseas:**
- [ ] Ver el PRD generado
- [ ] Ver la configuración del stack
- [ ] Ajustar alguna sección
- [ ] Comenzar con el primer módulo
```

## Quality Checklist

Antes de finalizar, verificar:

- [ ] **Brief validado**: PROJECT-BRIEF-FULL.yaml existe y es válido YAML
- [ ] **Stack detectado**: stack_seleccionado es válido (nextjs15, fastapi, go-wails)
- [ ] **Complejidad calculada**: complexity_score entre 1 y 10
- [ ] **Secciones faltantes identificadas**: Lista de campos nulos
- [ ] **Preguntas hechas**: Si hay campos críticos nulos, se preguntó
- [ ] **Defaults aplicados**: Campos nulos llenados con defaults del stack
- [ ] **Configuración cargada**: config.yaml del stack existe y es válido
- [ ] **Skill delegado**: PRD generado con el skill específico del stack
- [ ] **stack_config.yml generado**: Archivo YAML válido en .claude/
- [ ] **Archivos creados**:
   - [ ] PRD en .claude/outputs/PRD_{nombre}_{stack}.md
   - [ ] Config en .claude/stack_config.yml
- [ ] **Resumen presentado**: Formato correcto con próximos pasos

## Error Handling

### Errores comunes y manejo

| Error | Mensaje | Acción |
|-------|---------|--------|
| Brief no encontrado | "❌ Error: No encontré PROJECT-BRIEF-FULL.yaml" | Pedir que creen el brief primero |
| Stack inválido | "❌ Error: Stack '{stack}' no soportado. Opciones: nextjs15, fastapi, go-wails" | Mostrar stacks disponibles y pedir corrección |
| Config no encontrada | "⚠️ Warning: No encontré .claude/stacks/{stack}/config.yaml. Usando defaults genéricos." | Continuar con defaults básicos |
| Validación fallida | "❌ Error: Brief inválido. Errores: {lista de errores}" | Mostrar errores y pedir corrección |
| Skill no encontrado | "❌ Error: No encontré skill 'prd-{stack}'. Verificar instalación." | Pedir que instalen el skill |

## Integration con AgentCore

Este skill es parte del ecosistema de AgentCore v2.0. Se integra con:

- **Skill prd-nextjs15**: Generación de PRD para Next.js 15
- **Skill prd-fastapi**: Generación de PRD para FastAPI
- **Skill prd-go-wails**: Generación de PRD para Go Wails
- **Stack generator**: (futuro) Generación de código a partir de stack_config.yml

## Future Enhancements

- [ ] Soporte para más stacks (NestJS, Laravel, Rails, etc.)
- [ ] Validación automática del PRD generado
- [ ] Comparación de PRDs entre stacks
- [ ] Integración con herramientas de planificación (Jira, Notion)
- [ ] Generación de código a partir del PRD
