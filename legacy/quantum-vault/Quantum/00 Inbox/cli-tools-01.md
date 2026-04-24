# CLI Tools Modernos — Guía práctica

> bat · fd · sd · eza · fzf · zoxide · atuin · starship · carapace

---

## Resumen rápido — para qué sirve cada uno

| Tool | Reemplaza a | Para qué |
|------|-------------|----------|
| `bat` | `cat` | Ver archivos con sintaxis coloreada y número de líneas |
| `eza` | `ls` | Listar archivos con colores, íconos y árbol |
| `fd` | `find` | Buscar archivos por nombre, rápido y con sintaxis amigable |
| `sd` | `sed` | Buscar y reemplazar texto en archivos/pipes |
| `fzf` | — | Fuzzy finder interactivo: filtra cualquier lista |
| `zoxide` | `cd` | Saltar a carpetas frecuentes con `z nombre` |
| `atuin` | historial de shell | Historial de comandos con búsqueda fuzzy mejorada |
| `starship` | prompt del shell | Prompt inteligente que muestra git, lenguaje, errores |
| `carapace` | completion básico | Autocompletado avanzado para cientos de CLIs |

---

## bat — cat con superpoderes

```bash
bat archivo.txt              # ver archivo con sintaxis coloreada
bat src/main.go              # detecta el lenguaje automáticamente
bat -n archivo.txt           # solo números de línea, sin decoración
bat -A archivo.txt           # muestra caracteres especiales (tabs, espacios)
bat archivo1.txt archivo2.txt # ver múltiples archivos
```

**En pipes:**

```bash
git diff | bat               # diff con colores
curl -s url | bat --language json   # respuesta JSON coloreada
```

---

## eza — ls con personalidad

```bash
eza                          # lista básica con colores e íconos
eza -l                       # lista larga (permisos, tamaño, fecha)
eza -la                      # incluye archivos ocultos
eza --tree                   # árbol del directorio
eza --tree --level=2         # árbol con profundidad limitada
eza -l --sort=size           # ordenar por tamaño
eza -l --sort=modified       # ordenar por fecha de modificación
```

---

## fd — find sin dolor de cabeza

```bash
fd nombre                    # busca archivos que contengan "nombre"
fd "\.go$"                   # busca por extensión (regex)
fd -e go                     # busca por extensión (flag directo)
fd -e go src/                # busca solo dentro de src/
fd -t f config               # solo archivos (f), no carpetas
fd -t d components           # solo directorios
fd --hidden .env             # incluye archivos ocultos en la búsqueda
fd -e go -x bat              # busca .go y abre cada uno con bat
```

---

## sd — sed sin memorizar regex rara

```bash
# Buscar y reemplazar en un archivo
sd 'viejo' 'nuevo' archivo.txt

# En múltiples archivos
fd -e go | xargs sd 'OldName' 'NewName'

# Con pipes
echo "hello world" | sd 'world' 'Neovim'

# Reemplazar con regex
sd 'console\.log\((.*)\)' 'fmt.Println($1)' archivo.js
```

---

## fzf — el fuzzy finder que cambia todo

Solo instalar `fzf` ya te da tres superpoderes en el shell:

| Atajo | Qué hace |
|-------|---------|
| `Ctrl+r` | Búsqueda fuzzy en el historial de comandos |
| `Ctrl+t` | Selecciona un archivo del directorio actual |
| `Alt+c` | Cambia a un directorio seleccionado con fzf |

```bash
# Buscar y abrir un archivo en nvim
nvim $(fzf)

# Preview del archivo mientras buscas
fzf --preview 'bat --color=always {}'

# Buscar procesos para matar
kill -9 $(ps aux | fzf | awk '{print $2}')

# Combinar con fd
fd -e go | fzf | xargs nvim
```

---

## zoxide — el cd inteligente

Aprende a qué carpetas vas más seguido. Después solo escribes parte del nombre.

```bash
z projects          # va a ~/code/projects (si has ido antes)
z obsidian          # va a ~/code/obsidian
z -                 # regresa al directorio anterior (como cd -)
zi                  # abre una lista interactiva con fzf para elegir
```

> La primera vez tienes que `cd` normal para que zoxide aprenda.
> Después de 2-3 visitas ya puedes usar `z`.

---

## atuin — historial de comandos con esteroides

```bash
Ctrl+r              # búsqueda fuzzy en historial (reemplaza el Ctrl+r del shell)
atuin search        # buscar en historial desde terminal
atuin stats         # estadísticas de tus comandos más usados
atuin sync          # sincroniza historial entre máquinas (si tienes cuenta)
```

> La magia es que el historial es cross-sesión y cross-máquina. También guarda
> el directorio donde corriste cada comando y el exit code.

---

## starship — el prompt que se configura solo

Ya está corriendo si lo instalaste y lo agregaste al shell. Muestra:
- Rama de git actual + estado (dirty, ahead, behind)
- Lenguaje del proyecto (Go, Node, Python, Rust…)
- Tiempo de ejecución del último comando
- Exit code si falló

```bash
# Ver la config actual
cat ~/.config/starship.toml

# Si no existe, genera una desde cero
starship init zsh             # para zsh
starship init fish            # para fish

# Explorar presets
starship preset nerd-font-symbols -o ~/.config/starship.toml
```

---

## carapace — autocompletado para todo

Ya debería estar activo si lo configuraste en tu shell. Agrega completado
inteligente para más de 500 CLIs (docker, git, kubectl, etc.).

```bash
carapace _carapace            # ver todos los completados disponibles
carapace --list               # lista de comandos soportados
```

---

## Flujos de trabajo del día a día

### Flujo 1 — Navegar el proyecto

```bash
z mi-proyecto                 # saltar directo sin cd largo
eza --tree --level=2          # ver estructura del proyecto
fd -e go                      # qué archivos Go hay
```

### Flujo 2 — Buscar y editar un archivo que no recuerdas dónde está

```bash
# Opción A: con fd + fzf + nvim
fd -e go | fzf --preview 'bat --color=always {}' | xargs nvim

# Opción B: solo fzf
nvim $(fzf --preview 'bat {}')
```

### Flujo 3 — Refactor de nombre en todo el proyecto

```bash
fd -e go | xargs sd 'OldServiceName' 'NewServiceName'
# Verificar que quedó bien:
fd -e go -x bat | grep 'NewServiceName'
```

### Flujo 4 — Repetir un comando complejo que corriste hace días

```bash
Ctrl+r                        # abre atuin
# escribes parte del comando, ej: "docker compose"
# aparecen todos los comandos que matchean con fecha y directorio
# seleccionas con flechas, Enter para ejecutar
```

### Flujo 5 — Explorar un archivo de respuesta grande

```bash
curl -s https://api.ejemplo.com/data | bat --language json
# o si es muy largo:
curl -s https://api.ejemplo.com/data | bat --language json --paging always
```

### Flujo 6 — Inicio del día en el proyecto

```bash
z mi-proyecto                 # jump directo
eza -la --sort=modified       # ver qué archivos cambiaron recientemente
git log --oneline -10 | bat   # ver últimos commits con colores
fd -e go | xargs sd --preview 'grep TODO' {}   # buscar TODOs pendientes
```
