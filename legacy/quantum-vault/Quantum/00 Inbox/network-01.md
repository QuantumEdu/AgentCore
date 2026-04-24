# Network & Infrastructure — Commands

## Tailscale

### Levantar SSH a través de Tailscale

```bash
tailscale up --ssh
```

Habilita el servidor SSH integrado de Tailscale en la máquina local.
No requiere tener `sshd` corriendo — Tailscale maneja la autenticación via tu cuenta.

**Conectarte desde otra máquina en la tailnet:**

```bash
ssh user@hostname
# o usando el nombre de Tailscale directamente:
ssh user@nombre-en-tailscale
```

**Ver el estado y las IPs asignadas:**

```bash
tailscale status
```

**Deshabilitar SSH de Tailscale:**

```bash
tailscale up --ssh=false
```

> El flag `--ssh` solo está disponible en Tailscale v1.22+. En versiones anteriores se configura desde el admin panel en `tailscale.com/admin`.

---

### Conectarse a una máquina en la tailnet

```bash
ssh user@100.x.x.x
```

Usando la IP de Tailscale (la que empieza con `100.`). La encuentras con `tailscale status`.

```bash
ssh user@nombre-maquina
```

Usando el nombre de host registrado en Tailscale. Funciona si tienes MagicDNS habilitado en el admin panel.

**Copiar archivos via SCP:**

```bash
scp archivo.txt user@nombre-maquina:/ruta/destino/
```

**Abrir tunnel (port forwarding):**

```bash
ssh -L 8080:localhost:3000 user@nombre-maquina
```

Mapea el puerto `3000` de la máquina remota a tu `localhost:8080`.
