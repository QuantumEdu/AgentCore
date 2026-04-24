Sí — **puedes instalar Ollama completamente desde la línea de comandos en Windows**, sin usar el instalador gráfico, y además dejarlo apuntando a tu unidad D:.

Te dejo el método limpio y funcional.


ollama list
ollama ps

setx OPENAI_MODEL "deepseek-coder:6.7b"
ollama pull deepseek-coder:6.7b
ollama serve
ollama run deepseek-coder:6.7b
ollama stop deepseek-coder:33b

setx OPENAI_BASE_URL "http://localhost:11434/v1"
setx OPENAI_API_KEY "ollama"
setx OPENAI_MODEL "deepseek-coder:33b"

setx OPENAI_MODEL "qwen2.5-coder:7b"

taskkill /IM ollama.exe /F

notepad $env:USERPROFILE\.config\opencode\config.json

{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "ollama-local": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Ollama (Local)",
      "options": {
        "baseURL": "http://localhost:11434/v1"
      },
      "models": {
        "qwen2.5-coder:7b": {
          "name": "qwen2.5-coder:7b"
        }
      }
    }
  },
  "model": "ollama-local/qwen2.5-coder:7b"
}

---

# ✅ Instalación de Ollama por línea de comandos (Windows)

## Opción 1 — Con `winget` (oficial y fácil)

Abre **PowerShell como administrador** y ejecuta:

`winget install Ollama.Ollama`

Eso instala:

- El binario en `C:\Program Files\Ollama\`
    
- El servicio `ollama` en segundo plano
    

---

## Luego configuras modelos en D:

En PowerShell:

`mkdir D:\ollama-models setx OLLAMA_MODELS "D:\ollama-models"`

Cierra y abre otra consola.

Prueba:

`ollama pull llama3`

Y verifica que se descargue en:

`D:\ollama-models`

---

# Opción 2 — 100% portable (sin instalador)

Si quieres aún más control:

1. Descarga el binario:
    

`curl -L https://ollama.com/download/ollama-windows-amd64.exe -o ollama.exe`

2. Crea carpeta:
    

`mkdir D:\ollama move ollama.exe D:\ollama\ cd D:\ollama`

3. Ejecuta directamente:
    

`.\ollama.exe serve`

4. En otra terminal:
    

`.\ollama.exe pull deepseek-coder:6.7b .\ollama.exe run deepseek-coder:6.7b`

Puedes crear también:

`setx OLLAMA_MODELS "D:\ollama-models"`

Comprobar servicio:

`ollama serve`

Ver modelos:

`ollama list`

Eliminar modelos:

`ollama rm deepseek-coder:33b`
### 2. En OpenCode configuras algo como:

En tu config (`~/.opencode/config.yaml` o similar):

`provider: openai base_url: http://localhost:11434/v1 api_key: ollama model: deepseek-coder`

O con variables de entorno:

`export OPENAI_BASE_URL=http://localhost:11434/v1 export OPENAI_API_KEY=ollama export OPENAI_MODEL=deepseek-coder`

Y luego:

`opencode`