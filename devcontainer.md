# Devcontainer en OpenCode

## Requisitos

1. **Plugin instalado** en `~/.config/opencode/opencode.json`:
```json
{
  "plugin": ["opencode-devcontainers"]
}
```

2. **CLI instalado**:
```bash
npm install -g @devcontainers/cli
```

3. **Configuración** en `~/.config/opencode/devcontainers/config.json`:
```json
{
  "portRangeStart": 13000,
  "portRangeEnd": 13099
}
```

## Comandos

```bash
# Iniciar un devcontainer para una rama
/devcontainer mi-rama

# Ver estado actual
/devcontainer

# Usar un repo/branch específico
/devcontainer quantumedu/obsidian/main

# Desactivar (volver al host)
/devcontainer off
```

## Cómo funciona

1. El plugin clona el repo en `~/.local/share/opencode/clone/{rama}`
2. Copia los secrets `.env` del repo principal
3. Levanta el contenedor con tu `.devcontainer/devcontainer.json`
4. Asigna un puerto automático del rango configurado
5. Ejecuta los comandos **dentro del contenedor**

## Requisitos del proyecto

Tener `.devcontainer/devcontainer.json` en la raíz del proyecto.

## Cuándo usar qué

| Escenario | Recomendación |
|----------|--------------|
| Proyecto tiene devcontainer.json | `/devcontainer` |
| Solo necesitás aislamiento de git | `/worktree` (más liviano) |
| Proyecto simple | normal (sin aislamiento) |

## Solución de problemas

```bash
# Ver workspaces activos
/workspaces

# Cleanup de workspaces stale
/workspaces cleanup
```