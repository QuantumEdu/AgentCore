# Neovim — Guía práctica desde cero

> Config instalada en `~/.config/nvim/`

---

## Los tres modos — esto es TODO en Neovim

Neovim no es un editor normal. Tienes modos. La mayoría de errores de principiante
son estar en el modo equivocado.

```
NORMAL → es tu estado base. Para moverse, copiar, borrar, buscar.
INSERT → para escribir texto. Como cualquier editor.
VISUAL → para seleccionar bloques de texto.
COMMAND → para ejecutar comandos (:w, :q, :s, etc.)
```

### Cómo entrar y salir de cada modo

| Acción | Tecla |
|--------|-------|
| Normal → Insert (antes del cursor) | `i` |
| Normal → Insert (después del cursor) | `a` |
| Normal → Insert (nueva línea abajo) | `o` |
| Normal → Insert (nueva línea arriba) | `O` |
| Normal → Visual (carácter por carácter) | `v` |
| Normal → Visual (línea completa) | `V` |
| Normal → Visual (bloque rectangular) | `Ctrl+v` |
| Normal → Command | `:` |
| CUALQUIER modo → Normal | `Esc` o `Ctrl+[` |

**Regla de oro**: si algo no funciona, presiona `Esc` primero.

---

## Movimiento en modo Normal

No necesitas el mouse. El teclado es más rápido cuando lo internalizas.

### Básico

| Tecla | Movimiento |
|-------|------------|
| `h` | ← izquierda |
| `l` | → derecha |
| `j` | ↓ abajo |
| `k` | ↑ arriba |
| `w` | siguiente palabra |
| `b` | palabra anterior |
| `e` | al final de la palabra actual |
| `0` | inicio de la línea |
| `$` | final de la línea |
| `gg` | primera línea del archivo |
| `G` | última línea del archivo |
| `Ctrl+d` | media pantalla abajo |
| `Ctrl+u` | media pantalla arriba |

### Saltar con números

```
5j   → baja 5 líneas
10k  → sube 10 líneas
3w   → avanza 3 palabras
```

### Saltar a una línea específica

```
:42    → va a la línea 42
42G    → también va a la línea 42
```

---

## Copiar, cortar y pegar

En Neovim se llama **yank** (copiar), **delete** (cortar) y **put** (pegar).

| Acción | Tecla |
|--------|-------|
| Copiar línea completa | `yy` |
| Copiar N líneas | `3yy` |
| Copiar hasta fin de línea | `y$` |
| Copiar una palabra | `yw` |
| Cortar línea | `dd` |
| Cortar N líneas | `3dd` |
| Cortar hasta fin de línea | `d$` |
| Pegar DESPUÉS del cursor | `p` |
| Pegar ANTES del cursor | `P` |
| Deshacer | `u` |
| Rehacer | `Ctrl+r` |

### Con selección Visual

```
1. Entra en modo Visual con v o V
2. Selecciona con hjkl
3. y → copia la selección
4. d → corta la selección
5. Esc → sale de Visual
6. p → pega donde esté el cursor
```

---

## Buscar texto

### Búsqueda básica

```
/palabra       → busca hacia adelante
?palabra       → busca hacia atrás
n              → siguiente resultado
N              → resultado anterior
*              → busca la palabra bajo el cursor (adelante)
#              → busca la palabra bajo el cursor (atrás)
```

### Buscar y reemplazar

```
:%s/viejo/nuevo/g       → reemplaza en todo el archivo
:%s/viejo/nuevo/gc      → reemplaza con confirmación una por una
:5,10s/viejo/nuevo/g    → reemplaza solo entre líneas 5 y 10
```

---

## Comandos esenciales de archivo

Modo Command (`:`)

| Comando | Acción |
|---------|--------|
| `:w` | guardar |
| `:q` | cerrar (si no hay cambios) |
| `:wq` o `:x` | guardar y cerrar |
| `:q!` | cerrar sin guardar |
| `:e archivo.txt` | abrir otro archivo |
| `:vs archivo.txt` | abrir en split vertical |
| `:sp archivo.txt` | abrir en split horizontal |

---

## Buscar archivos y texto en el proyecto

Esto depende de los plugins de tu config en `~/.config/nvim/`.
La mayoría de configs modernas incluyen **Telescope** o **fzf-lua**.

### Con Telescope (lo más común)

```
<leader>ff    → buscar archivos por nombre (usa fzf internamente)
<leader>fg    → buscar texto en todos los archivos (grep)
<leader>fb    → ver buffers abiertos
<leader>fh    → buscar en el historial
```

> `<leader>` es generalmente la tecla `Space` en configs modernas.
> Revisa tu `~/.config/nvim/` para confirmarlo.

### Verificar tu leader key

```bash
grep -r "leader" ~/.config/nvim/ | grep "mapleader"
```

---

## Splits y navegación entre paneles

```
Ctrl+w h    → panel izquierdo
Ctrl+w l    → panel derecho
Ctrl+w j    → panel de abajo
Ctrl+w k    → panel de arriba
Ctrl+w v    → nuevo split vertical
Ctrl+w s    → nuevo split horizontal
Ctrl+w q    → cerrar panel actual
```

---

## Flujos de trabajo para practicar

### Flujo 1 — Editar un archivo

```
1. nvim archivo.txt          → abrir archivo
2. /función                  → buscar "función" en el archivo
3. n / N                     → navegar entre resultados
4. i                         → entrar en Insert
5. (editar)
6. Esc                       → volver a Normal
7. :w                        → guardar
8. :q                        → cerrar
```

### Flujo 2 — Mover un bloque de código

```
1. nvim main.go
2. Navega con j/k hasta la función que quieres mover
3. V                         → Visual line mode
4. j (varias veces)          → selecciona las líneas
5. d                         → corta el bloque
6. Navega al destino
7. p                         → pega
8. :w                        → guarda
```

### Flujo 3 — Buscar y reemplazar en un proyecto

```
1. Abrir Neovim en el proyecto: nvim .
2. <leader>fg                → abre búsqueda de texto global
3. Escribes el término
4. Enter en el resultado     → te lleva al archivo y línea exacta
5. (editas)
6. :%s/viejo/nuevo/gc        → si quieres reemplazar en ese archivo
```

### Flujo 4 — Refactor rápido de variable

```
1. Pones el cursor SOBRE la variable
2. *                         → busca todas las ocurrencias del término
3. n / N                     → navegas entre ellas
4. ciw                       → borra la palabra y entra en Insert (change inner word)
5. Escribes el nuevo nombre
6. Esc
7. :%s/viejoNombre/nuevoNombre/g   → si quieres reemplazar todas de golpe
```

### Flujo 5 — Navegar el proyecto sin mouse

```
1. nvim .                    → abre el file explorer (si tu config lo tiene)
2. <leader>ff                → busca archivo por nombre con fzf
3. Ctrl+w v                  → abre split para comparar dos archivos
4. Ctrl+w hjkl               → te mueves entre splits
5. :q                        → cierras el que no necesitas
```

---

## Cheatsheet de emergencia

```
Esc         → vuelve a Normal (siempre)
:w          → guarda
:q!         → sal sin guardar
u           → deshacer
Ctrl+r      → rehacer
/texto      → buscar
n           → siguiente resultado
yy / dd / p → copiar / cortar / pegar línea
gg / G      → inicio / fin del archivo
```
