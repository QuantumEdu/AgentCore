# Gentle AI — Manual de Uso

> Ecosistema completo para superpoderes en tu agente de IA: memoria persistente,
> flujo de trabajo estructurado (SDD), skills curadas y persona de mentor.

---

## ¿Para qué sirve?

**No es un instalador de agentes** — es un configurador del ecosistema.
Tomas tu agente favorito (Claude Code, Cursor, Windsurf, etc.) y lo convierte en
algo que realmente enseña, recuerda y planea.

**Antes**: "Instalé Claude Code. Es un chatbot que escribe código."
**Después**: Tu agente tiene memoria cross-sesión, skills por stack, flujo de
planeación estructurada y una persona que te explica el *por qué*.

---

## Instalación

### macOS / Linux

```bash
# Homebrew (recomendado)
brew tap Gentleman-Programming/homebrew-tap
brew install gentle-ai

# O con el script directo
curl -fsSL https://raw.githubusercontent.com/Gentleman-Programming/gentle-ai/main/scripts/install.sh | bash
```

### Windows

```powershell
scoop bucket add gentleman https://github.com/Gentleman-Programming/scoop-bucket
scoop install gentle-ai

# o con PowerShell
irm https://raw.githubusercontent.com/Gentleman-Programming/gentle-ai/main/scripts/install.ps1 | iex
```

### Con Go

```bash
go install github.com/gentleman-programming/gentle-ai/cmd/gentle-ai@latest
```

---

## Configurar tu agente (TUI interactivo)

```bash
gentle-ai
```

Te lanza una interfaz interactiva donde eliges:
- Qué agentes configurar (Claude Code, Cursor, Windsurf…)
- Qué componentes instalar (Engram, SDD, Skills, GGA…)
- Qué preset usar

### O directo por flags

```bash
# Setup completo para Claude Code y Cursor
gentle-ai install \
  --agent claude-code,cursor \
  --preset full-gentleman

# Solo lo esencial
gentle-ai install \
  --agent claude-code \
  --preset minimal

# Preview sin aplicar cambios
gentle-ai install --dry-run \
  --agent claude-code \
  --preset full-gentleman
```

### Presets disponibles

| Preset | Incluye |
|--------|---------|
| `full-gentleman` | Todo: Engram + SDD + Skills + Context7 + GGA + Persona + Permisos + Tema |
| `ecosystem-only` | Core sin tema ni permisos |
| `minimal` | Solo Engram + SDD |
| `custom` | Tú eliges componente por componente |

---

## Setup en cada proyecto nuevo

Después de instalar el ecosistema globalmente, cuando abres un proyecto nuevo
en tu agente corres dos comandos **una sola vez**:

```
/sdd-init
```
```
/skill-registry
```

Listo. El orquestador se encarga del resto.

---

## ¿Qué es `sdd-init`?

`/sdd-init` es el **bootstrapper de contexto del proyecto**. Cuando lo corres dentro
de un proyecto hace tres cosas:

1. **Detecta el stack** — lenguaje, frameworks, librerías
2. **Detecta capacidades de testing** — si encuentra un test runner, activa el modo Strict TDD
3. **Registra el contexto en Engram** — para que todos los sub-agentes lo tengan disponible en sesiones futuras

### ¿Cuándo volver a correrlo?

- Primera vez en un proyecto nuevo
- Cuando agregas o quitas frameworks de testing
- Cuando migras de librería principal

> El orquestador SDD lo corre automáticamente si detecta que no existe contexto.
> Pero si algo cambió en el proyecto, es mejor correrlo manualmente.

---

## ¿Qué es `gga init`?

**GGA = Gentleman Guardian Angel** — el switcher de proveedores de IA.

`gentle-ai` instala el binario `gga` globalmente en tu máquina, pero
**no activa los hooks en ningún repositorio automáticamente** — eso es una
decisión explícita tuya por repo.

```bash
# Dentro del repositorio donde lo quieres activar:
gga init
gga install
```

Después de esto, GGA intercepta las llamadas al agente y puede rutear a
diferentes proveedores según el contexto.

---

## Flujos de trabajo reales

### Flujo 1 — Proyecto nuevo de cero

```bash
# 1. Instalar el ecosistema (una vez, global)
brew install gentle-ai
gentle-ai install --agent claude-code --preset full-gentleman

# 2. Abrir tu agente en el proyecto
# 3. Dentro del agente:
/sdd-init
# → Detecta stack, activa TDD mode, guarda contexto en memoria

/skill-registry
# → Escanea skills disponibles, construye el índice del proyecto
```

A partir de aquí el agente ya sabe qué stack usas, qué patrones seguir
y tiene memoria persistente entre sesiones.

---

### Flujo 2 — Feature nueva mediana/grande (con SDD)

Cuando el task es suficientemente grande, el agente sugiere usar SDD.
También puedes pedirlo explícitamente:

```
Implementa el módulo de autenticación con JWT. Usa SDD.
```

El agente recorre las fases internamente:

```
/sdd-new auth-jwt
```

1. **Explore** — Investiga el codebase actual
2. **Propose** — Propone el approach con tradeoffs
3. **Spec** — Escribe los requisitos y escenarios de aceptación
4. **Design** — Diseña la arquitectura técnica
5. **Tasks** — Divide en tareas concretas con checklist
6. **Apply** — Implementa tarea por tarea
7. **Verify** — Valida que todo cuadre con las specs
8. **Archive** — Cierra el cambio y persiste el estado final

**En modo Interactive** (default), el agente pausa después de cada fase
y te pregunta si quieres ajustar algo antes de continuar. En modo **Automatic**
corre todo sin parar.

---

### Flujo 3 — Continuar trabajo de otra sesión

Gracias a Engram (la memoria persistente), el agente recuerda el contexto:

```
# Nueva sesión, mismo proyecto
# El agente busca automáticamente en memoria al arrancar

Continúa con el módulo de auth del que estábamos hablando.
```

```
/sdd-continue auth-jwt
```

El orquestador recupera exactamente en qué fase quedó y sigue desde ahí.
No necesitas re-explicar el contexto.

---

### Flujo 4 — Actualizar el ecosistema

```bash
# Actualizar gentle-ai
brew upgrade gentle-ai

# Refrescar configs de agentes al nuevo contenido
gentle-ai sync

# Sincronizar solo un agente específico
gentle-ai sync --agent cursor

# Sincronizar solo un componente
gentle-ai sync --component sdd
gentle-ai sync --component skills
```

`sync` es seguro e idempotente — si nada cambió, no hace nada.

---

### Flujo 5 — Agregar skills de frameworks

Las skills de frameworks (React 19, Angular, TypeScript, Tailwind, etc.) viven
en un repo separado mantenido por la comunidad:

```bash
git clone https://github.com/Gentleman-Programming/Gentleman-Skills.git

# Copiar las que necesitas
cp -r Gentleman-Skills/curated/react-19 ~/.claude/skills/
cp -r Gentleman-Skills/curated/typescript ~/.claude/skills/

# O copiar todo el catálogo
cp -r Gentleman-Skills/curated/ ~/.claude/skills/
```

Después de agregar skills, actualiza el registro dentro del agente:

```
/skill-registry
```

El agente detecta automáticamente qué skills son relevantes para el proyecto
actual y las carga — tú no tienes que activarlas manualmente.

---

## Actualizaciones y rollback

Cada `install`, `sync` y `upgrade` genera un backup comprimido automáticamente.
Guarda los 5 más recientes y deduplica si no hubo cambios.

```bash
# Ver y restaurar backups desde la TUI
gentle-ai
# → navega a la sección Backups
# → j/k para moverte, Enter para restaurar, p para pinear
```

---

## Proyecto ya en marcha — ¿Por dónde empiezo?

Esta es la situación más común: tienes un proyecto corriendo, llevas semanas o
meses trabajando en él, y apenas instalas gentle-ai. No pasa nada — `sdd-init`
no requiere haber empezado con SDD desde el día cero.

### Orden recomendado

```bash
# 1. Instalar el ecosistema globalmente (si aún no lo hiciste)
gentle-ai install --agent claude-code --preset full-gentleman
```

Después, **dentro del agente**, parado en la raíz del proyecto:

```
/sdd-init
```

El agente escanea lo que ya existe: dependencias, test runner, estructura de
carpetas, frameworks. Guarda ese contexto en Engram. A partir de aquí tiene
memoria del proyecto sin importar que haya empezado sin él.

```
/skill-registry
```

Indexa las skills relevantes para este stack en particular. Si el proyecto tiene
un `CLAUDE.md` o `.cursorrules`, también los lee y los incorpora al registro.

```bash
# 3. Activar GGA en este repo (opcional, si quieres el provider switcher)
gga init
gga install
```

### ¿Es necesario `claude init`?

`claude init` es un comando de **Claude Code** (no de gentle-ai). Lo que hace es
crear o actualizar un archivo `CLAUDE.md` en la raíz del proyecto con contexto
que Claude lee automáticamente en cada sesión.

```bash
claude init
```

**¿Cuándo SÍ conviene correrlo?**

- El proyecto no tiene `CLAUDE.md` todavía
- Quieres que Claude detecte automáticamente el stack, comandos de build/test,
  estructura de carpetas, y los documente en ese archivo
- Es la primera vez que abres el proyecto en Claude Code

**¿Cuándo NO es estrictamente necesario?**

- Si ya tienes un `CLAUDE.md` escrito a mano con las convenciones del proyecto
- Si `sdd-init` ya capturó el contexto en Engram — el agente puede tirar de
  memoria aunque no exista el archivo

> **Relación entre ambos**: `claude init` → genera `CLAUDE.md` (archivo estático,
> commitable al repo). `sdd-init` → guarda contexto en Engram (memoria viva,
> cross-sesión). Son complementarios, no excluyentes. Lo ideal es tener los dos.

### Flujo completo — proyecto existente

```
Situación: proyecto de 3 meses, sin SDD, sin gentle-ai previo.
```

```bash
# Terminal
gentle-ai install --agent claude-code --preset full-gentleman
```

```bash
# Terminal, en la raíz del proyecto
claude init
# → genera CLAUDE.md con stack, comandos, estructura detectada automáticamente
# → revísalo y ajusta lo que detectó mal
```

```
# Dentro del agente (Claude Code)
/sdd-init
→ detecta stack, activa TDD mode, guarda contexto en Engram

/skill-registry
→ indexa skills, lee CLAUDE.md, construye el índice del proyecto
```

Desde aquí el agente ya tiene:
- Contexto del proyecto en memoria persistente
- Skills del stack activas automáticamente
- `CLAUDE.md` como fuente de verdad estática commitable
- Flujo SDD disponible para el próximo cambio grande

### ¿Y si el proyecto ya tiene convenciones establecidas?

Si hay un equipo y ya existen patrones acordados (naming, estructura, testing),
lo mejor es documentarlos **antes** de correr `sdd-init`:

1. Agrega o edita `CLAUDE.md` con las convenciones del equipo
2. Corre `claude init` si el archivo no existe (y ajusta lo que generó)
3. Corre `/sdd-init` — va a leer el `CLAUDE.md` y honrar esas convenciones
4. Corre `/skill-registry` para que el orquestador las propague a los sub-agentes

Así el agente no inventa convenciones — aprende las que ya acordaron.

---

## Referencia rápida de comandos

| Comando | Dónde | Qué hace |
|---------|-------|----------|
| `gentle-ai` | Terminal | Lanza la TUI de configuración |
| `gentle-ai install` | Terminal | Instala/configura el ecosistema |
| `gentle-ai sync` | Terminal | Refresca configs al contenido más reciente |
| `gentle-ai upgrade` | Terminal | Actualiza el binario de gentle-ai |
| `/sdd-init` | Agente | Bootstrap de contexto del proyecto |
| `/skill-registry` | Agente | Indexa skills disponibles del proyecto |
| `/sdd-new <nombre>` | Agente | Inicia un nuevo cambio con flujo SDD |
| `/sdd-continue <nombre>` | Agente | Retoma un cambio desde donde quedó |
| `/sdd-ff <nombre>` | Agente | Fast-forward: proposal → specs → design → tasks |
| `gga init` | Terminal (en repo) | Activa GGA hooks en el repositorio actual |
| `engram tui` | Terminal | Explora memorias guardadas visualmente |
| `engram sync` | Terminal | Exporta memorias a `.engram/` para git |
