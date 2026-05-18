# AgentCore for Dev

Repositorio reorganizado para convertir el enfoque original de AgentCore en un sistema más **agnóstico, ordenado, guiado y portable**, manteniendo a **gentle-ai** como orquestador y usando `/ai` como capa principal de gobierno y trabajo.

## Qué es este repo ahora

Este repo ya no está centrado en `.claude/` como sistema activo.

Ahora el corazón del proyecto vive en `/ai` y se enfoca en:

- gobierno liviano;
- flujo estructurado de discovery a ejecución;
- skills composables;
- agentes simples por rol;
- memoria fallback cuando no hay Engram;
- migración segura de reglas en sistemas en operación.

## Qué problema resuelve

Cuando solo hay prompts sueltos o reglas dispersas, el agente suele:

- empezar sin suficiente contexto;
- mezclar descubrimiento, diseño y ejecución;
- repetir errores;
- perder continuidad entre sesiones;
- tomar decisiones técnicas sin una guía clara.

Este sistema busca resolver eso con una capa `/ai` que ordena el trabajo sin competir con gentle-ai.

## Principio central

- **gentle-ai** = orquestación, memoria persistente, delegación, SDD.
- **agent-core-v3** = core global reusable e instalable por npm.
- **/ai** = guía, flujo, skills, agentes simples, templates y fallback local.

## Límites del sistema

Este sistema queda mejor entendido en tres capas:

1. **gentle-ai** como runtime/orquestador.
2. **agent-core-v3** como core global distribuible.
3. **/ai** como overlay local del proyecto.

La transición histórica dejó partes inconclusas entre AgentCore, `sdd-govplan` y `agent-core-v3`.
Este repo cierra localmente el flujo que faltaba y sirve como fuente para completar profesionalmente la migración hacia v3.

## Flujo lógico recomendado

### Flujo de uso
1. **governance**
2. **quick-start**
3. **workflow map**
4. **schema mínimo**
5. **templates**
6. **skills**
7. **agents**
8. **context**
9. **memory fallback**
10. **migration planning**

### Flujo canónico de trabajo

`brief-inception` → `brief-to-prd` → `prd-to-spec` → `spec-to-tasks`

Luego, según el caso:

- review → `change-review`
- migration → `rule-migration-plan`
- repeated errors → `improvement-loop`
- no Engram → `project-memory-fallback`

## Casos básicos que cubre

### 1. Arrancar un proyecto desde cero
- `brief-inception`
- `project-stack-decider`
- `brief-to-prd`
- `prd-to-spec`
- `spec-to-tasks`

### 2. Idea difusa
- `brief-inception`
- `brief-to-prd`
- `project-stack-decider` si falta dirección técnica

### 3. Endpoint nuevo
- `add-endpoint`
- `change-review`

### 4. Reemplazar una regla en producción sin romper
- `rule-migration-plan`
- `change-review`
- `local-retrospective`

### 5. Error repetido o fricción recurrente
- `improvement-loop`
- `local-retrospective`

### 6. No hay Engram
- `project-memory-fallback`

## Innovación / qué lo hace distinto

Este repo no intenta ser otro orquestador.
Su innovación está en separar responsabilidades con más claridad:

- gobierno liviano sin invadir la ejecución;
- skills pequeñas y composables en lugar de workflows rígidos gigantes;
- agentes simples como wrappers de rol, no “megaagentes”;
- memoria fallback local cuando Engram no está disponible;
- migración de reglas con shadow mode, rollout gradual y rollback claro;
- brief full y brief lite según complejidad del proyecto.

## Briefs disponibles

- `ai/templates/PROJECT-BRIEF-FULL.yaml` — para cambios grandes, complejos o sensibles.
- `ai/templates/PROJECT-BRIEF-LITE.yaml` — para proyectos pequeños, rápidos o exploratorios.

## Ejemplos de uso

### 1. Proyecto grande desde cero
- Usa `PROJECT-BRIEF-FULL.yaml` como gate.
- Flujo: `brief-inception` → `brief-to-prd` → `prd-to-spec` → `spec-to-tasks`.
- Si hay riesgos: registra ADR y valida en **decision gates**.

### 2. Proyecto ligero o pequeño
- Usa `PROJECT-BRIEF-LITE.yaml`.
- Flujo corto: `brief-inception` → `brief-to-prd` → `spec-to-tasks` (si aplica).

### 3. Proyecto ya en marcha
- Entra por `change-review` para acotar impacto.
- Si hay reglas existentes: `rule-migration-plan` antes de tocar producción.

### 4. Crear una issue
- Parte de un brief mínimo y define: objetivo, alcance, validación.
- Luego deriva a `spec-to-tasks` para desglose ejecutable.

### 5. Revisar una parte del ciclo de desarrollo
- Usa **decision gates** para evaluar estado y bloqueos.
- Si hay fricción recurrente: `improvement-loop` y `local-retrospective`.

## Estructura del repo

```text
/ai
  /agents        # agentes simples por rol
  /context       # contexto estable + memoria fallback local
  /governance    # gates, workflow map, quick start
  /migration     # notas y estrategia de transición
  /schemas       # validación estructural mínima
  /skills        # capacidades operativas
  /templates     # formatos de salida y briefs

/legacy          # archivo histórico y materiales rescatados

AGENTS.md        # entry point operativo del repo
README.md        # onboarding público del sistema
```

## Cómo empezar

### Inicio rápido
1. Leer `AGENTS.md`
2. Leer `ai/README.md`
3. Leer `ai/governance/00-start-here.md`
4. Elegir entre:
   - `ai/governance/04-workflow-map.md`
   - `ai/governance/05-quick-start-by-scenario.md`

### Si vienes desde GitHub y quieres entender el sistema rápido
- visión estructural → `ai/governance/04-workflow-map.md`
- guía por situaciones reales → `ai/governance/05-quick-start-by-scenario.md`

## Estado actual

- `/ai` es la capa activa principal.
- `.claude/` y `.agent/` quedaron como stubs mínimos.
- `legacy/` conserva el sistema anterior y material histórico.

## Nota sobre el legado

El sistema anterior no se eliminó de forma destructiva.
Se movió a `legacy/` para conservar:

- referencia histórica;
- comparación viejo vs nuevo;
- recuperación si alguna pieza debe rescatarse.

## Nota sobre v3

`agent-core-v3` no debe leerse como reemplazo 1:1 del overlay local `/ai`.

La lectura correcta es:

- `agent-core-v3` = base reusable global;
- `/ai` = capa local operativa del repo.

## Regla operativa

1. Para iniciar un proyecto o cambio grande, leer `AGENTS.md`.
2. Luego leer `ai/governance/00-start-here.md`.
3. Usar el brief como gate de entrada antes de PRD/spec/tareas.
4. Tratar `legacy/` como archivo histórico, no como flujo activo.
