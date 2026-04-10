# Terminal Environment — Guía práctica

> tmux · zellij · fish · nushell · alacritty · kitty · ghostty

---

## Resumen rápido — para qué sirve cada uno

| Tool | Categoría | Para qué |
|------|-----------|----------|
| `tmux` | Multiplexer | Múltiples terminales en una sola ventana, sesiones persistentes |
| `zellij` | Multiplexer | Alternativa moderna a tmux, más visual y amigable |
| `fish` | Shell | Shell con autocompletado inteligente out-of-the-box |
| `nushell` | Shell | Shell con outputs estructurados (como tablas), scripting moderno |
| `alacritty` | Terminal | Emulador GPU-accelerated, minimalista, muy rápido |
| `kitty` | Terminal | GPU-accelerated con soporte de imágenes y configuración extensa |
| `ghostty` | Terminal | Terminal moderno, nativo, rápido con buena integración en macOS |

---

## tmux — sesiones que sobreviven todo

### ¿Para qué sirve?

- **Sesiones persistentes**: cierras la terminal, el trabajo sigue corriendo
- **Múltiples paneles**: frontend, backend y logs en la misma pantalla
- **Pair programming / SSH**: conectarte a una sesión remota compartida

### Prefix

Todos los atajos de tmux empiezan con el **prefix**: `Ctrl+b`

```
Ctrl+b [acción]
```

### Sesiones

```bash
tmux                          # nueva sesión sin nombre
tmux new -s trabajo           # nueva sesión con nombre
tmux ls                       # listar sesiones activas
tmux attach -t trabajo        # reconectarse a una sesión
tmux kill-session -t trabajo  # cerrar una sesión
```

Dentro de tmux:

| Atajo | Acción |
|-------|--------|
| `Ctrl+b d` | **detach** — salir sin cerrar (la sesión sigue viva) |
| `Ctrl+b s` | lista de sesiones para cambiar |
| `Ctrl+b $` | renombrar sesión actual |

### Ventanas (tabs)

| Atajo | Acción |
|-------|--------|
| `Ctrl+b c` | nueva ventana |
| `Ctrl+b ,` | renombrar ventana |
| `Ctrl+b n` | siguiente ventana |
| `Ctrl+b p` | ventana anterior |
| `Ctrl+b 1` | ir a ventana 1 (o 2, 3…) |
| `Ctrl+b &` | cerrar ventana |

### Paneles (splits)

| Atajo | Acción |
|-------|--------|
| `Ctrl+b %` | split vertical |
| `Ctrl+b "` | split horizontal |
| `Ctrl+b ←→↑↓` | moverse entre paneles |
| `Ctrl+b z` | zoom al panel actual (toggle) |
| `Ctrl+b x` | cerrar panel actual |

### Flujo de trabajo — proyecto con tmux

```bash
# Una vez, al inicio del proyecto
tmux new -s mi-proyecto

# Ventana 1: editor
Ctrl+b c  → nueva ventana
# nvim .

# Ventana 2: servidor / docker
Ctrl+b c
# docker compose up

# Ventana 3: git y comandos
Ctrl+b c
# git log, tests, etc.

# Navegar entre ventanas: Ctrl+b 1 / 2 / 3

# Fin del día: Ctrl+b d  → detach
# Al día siguiente: tmux attach -t mi-proyecto
```

---

## zellij — multiplexer moderno sin memorizar tanto

Más visual que tmux. Las opciones aparecen en la pantalla.

```bash
zellij                        # nueva sesión
zellij list-sessions          # ver sesiones activas
zellij attach nombre          # reconectarse
zellij delete-session nombre  # eliminar sesión
```

### Atajos principales

| Atajo | Acción |
|-------|--------|
| `Ctrl+p` + `n` | nuevo panel |
| `Ctrl+p` + `d` | dividir hacia abajo |
| `Ctrl+p` + `r` | dividir a la derecha |
| `Ctrl+p` + `←→↑↓` | moverse entre paneles |
| `Ctrl+p` + `x` | cerrar panel |
| `Ctrl+t` + `n` | nueva tab |
| `Ctrl+t` + `←→` | cambiar tab |
| `Ctrl+o` + `d` | detach (la sesión sigue corriendo) |

> **¿tmux o zellij?** Si ya sabes tmux, quédate con tmux. Si estás empezando,
> zellij es más amigable — las instrucciones aparecen en pantalla.

---

## fish — el shell que autocompleta desde el día uno

Fish sugiere comandos mientras escribes (en gris). `Tab` para aceptar,
`→` para aceptar la sugerencia completa.

```bash
fish                          # entrar a fish desde zsh
# o configúralo como shell default:
chsh -s $(which fish)
```

### Lo que hace fish automáticamente

- Autocompletado de argumentos y flags de cualquier CLI
- Historial inteligente (sugiere el comando completo mientras escribes)
- Colores en la sintaxis mientras escribes
- `cd -` para ir al directorio anterior

### Diferencias con bash/zsh

```fish
# Variables
set MI_VAR "valor"           # no se usa export, no se usa =

# Funciones
function saluda
    echo "Hola $argv[1]"
end

# Condicionales
if test $MI_VAR = "valor"
    echo "coincide"
end
```

> Fish no es 100% compatible con bash. Si tienes scripts `.sh` existentes,
> córrelos con `bash script.sh`, no directamente.

---

## nushell — el shell con superpoderes de datos

Nushell trata los outputs como **tablas estructuradas**, no texto plano.
Esto lo hace ideal para explorar datos, procesos, archivos.

```bash
nu                            # entrar a nushell
```

### Lo diferente de nushell

```nushell
# ls devuelve una tabla
ls | sort-by size | reverse

# ps también
ps | where cpu > 5 | select pid name cpu

# git log como tabla
git log | lines | first 10

# Trabajar con JSON
open package.json | get dependencies

# Filtrar archivos
ls **/*.go | where size > 10kb
```

### Pipeline como en bash pero con datos estructurados

```nushell
ls | where name =~ ".go" | get name | each { |f| open $f | lines | length }
```

> Nushell tiene su propia sintaxis. No es compatible con bash/zsh.
> Úsalo para exploración interactiva, no para scripts de producción (aún).

---

## Terminales — cuál usar

Tienes tres instalados. Todos son rápidos y GPU-accelerated.

| Terminal | Mejor para |
|----------|-----------|
| **ghostty** | Uso diario en macOS, integración nativa, configuración simple |
| **kitty** | Soporte de imágenes en terminal, muy configurable |
| **alacritty** | Máxima velocidad, mínima complejidad, config en YAML |

### Recomendación

Con macOS: **ghostty** como principal. Alacritty si quieres algo ultra-minimalista.

### Configs rápidas

```bash
# Ghostty
~/.config/ghostty/config

# Kitty
~/.config/kitty/kitty.conf

# Alacritty
~/.config/alacritty/alacritty.yml
```

---

## Flujos de trabajo integrados

### Flujo 1 — Día de trabajo completo con tmux

```bash
# Mañana: retomar donde dejaste
tmux attach -t proyecto

# Ya tienes:
# - Ventana 1: nvim con el código abierto
# - Ventana 2: servidor corriendo
# - Ventana 3: git/tests

# Fin del día:
Ctrl+b d   # detach, todo sigue vivo
```

### Flujo 2 — Debug con paneles

```bash
tmux new -s debug

# Panel principal: código
nvim main.go

# Ctrl+b %  → split vertical
# Panel derecho: logs en vivo
tail -f logs/app.log | bat --paging never

# Ctrl+b z  → zoom al panel que necesitas leer
# Ctrl+b z  → vuelve a la vista dividida
```

### Flujo 3 — Explorar datos con nushell

```bash
nu
ls **/*.go | where size > 5kb | sort-by size | reverse
# → tabla con todos los archivos Go grandes del proyecto

ps | where name =~ "node" | select pid name cpu mem
# → qué procesos node están corriendo y cuánto consumen
```

### Flujo 4 — Fish para el día a día rápido

```bash
# Fish recuerda tus comandos y los sugiere en gris
# Solo escribe las primeras letras y presiona →

docker c[→ autocompleta: docker compose up -d]
git ch[→ autocompleta: git checkout main]
```

### Flujo 5 — Setup rápido de proyecto nuevo

```bash
# 1. Terminal nueva con ghostty/alacritty
# 2. tmux new -s nombre-proyecto
# 3. fish (ya en el shell, los suggestions empiezan de inmediato)
# 4. z nombre-proyecto  (zoxide para saltar directo)
# 5. Ctrl+b c → nueva ventana para nvim
# 6. nvim .
```
