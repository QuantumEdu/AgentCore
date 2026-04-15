#!/usr/bin/env python3
"""
AgentCore v2.0 - Project Initialization Script
Inicializa un nuevo proyecto con la estructura de AgentCore
"""

import os
import sys
import shutil
from pathlib import Path


def init_project(project_path: str):
    """Inicializa un nuevo proyecto con AgentCore"""

    # Validar que la ruta no exista
    project_path = Path(project_path).resolve()
    if project_path.exists():
        print(f"❌ El directorio ya existe: {project_path}")
        return False

    # Crear estructura base
    print(f"📁 Creando proyecto en: {project_path}")
    project_path.mkdir(parents=True, exist_ok=True)

    # Copiar .claude/ al nuevo proyecto
    claude_source = Path(__file__).parent.parent
    claude_dest = project_path / ".claude"

    print("📋 Copiando estructura .claude/...")
    shutil.copytree(
        claude_source,
        claude_dest,
        ignore=shutil.ignore_patterns("__pycache__", "*.pyc", ".git"),
    )

    # Crear directorios básicos del proyecto
    dirs_to_create = [
        "app",
        "app/domain",
        "app/application",
        "app/infrastructure",
        "app/adapters",
        "tests",
        "docs",
    ]

    for dir_path in dirs_to_create:
        (project_path / dir_path).mkdir(parents=True, exist_ok=True)

    # Crear archivos básicos
    (project_path / "README.md").write_text(
        "# Project Name\n\nInitialized with AgentCore v2.0\n"
    )
    (project_path / ".gitignore").write_text("""
# Python
__pycache__/
*.pyc
.venv/
.ENV

# AgentCore
.claude/stack_config.yml
.claude/outputs/
""")

    # Preguntar stack preferido
    print("\n🤖 ¿Qué stack deseas usar?")
    print("  [1] FastAPI Stack A (SSR: Jinja2 + HTMX)")
    print("  [2] FastAPI Stack B (SPA: React + MUI)")
    print("  [3] FastAPI Stack C (Desktop: PyWebview)")
    print("  [4] Next.js 15")
    print("  [5] Go + Wails")

    choice = input("\nTu elección (1-5): ").strip()

    stack_map = {
        "1": "fastapi_ssr",
        "2": "fastapi_spa",
        "3": "fastapi_desktop",
        "4": "nextjs15",
        "5": "go-wails",
    }

    stack = stack_map.get(choice)
    if not stack:
        print("⚠️  Elección inválida. Se usará fastapi_ssr por defecto.")
        stack = "fastapi_ssr"

    print(f"\n✅ Stack seleccionado: {stack}")
    print(
        f"ℹ️  Ejecuta 'python .claude/scripts/stack_selector.py' para cambiar el stack más tarde"
    )

    # Los templates de 35 secciones ya fueron copiados por shutil.copytree arriba:
    #   .claude/templates/PROJECT-BRIEF-FULL-Quantum.yaml  (YAML, parsing automático)
    #   .claude/templates/PROJECT-BRIEF-FULL.md            (Markdown, llenado manual)
    # Solo actualizamos el stack_principal en el YAML canónico
    quantum_path = project_path / ".claude" / "templates" / "PROJECT-BRIEF-FULL-Quantum.yaml"
    if quantum_path.exists():
        content = quantum_path.read_text(encoding="utf-8")
        content = content.replace('stack_principal: ""', f'stack_principal: "{stack}"')
        quantum_path.write_text(content, encoding="utf-8")

    print("\n✅ Proyecto inicializado exitosamente!")
    print(f"\n📝 Siguientes pasos:")
    print(f"   1. cd {project_path}")
    print(f"   2. Llená el brief (elegí el formato que preferís):")
    print(f"      - YAML (parsing automático): .claude/templates/PROJECT-BRIEF-FULL-Quantum.yaml")
    print(f"      - Markdown (llenado manual): .claude/templates/PROJECT-BRIEF-FULL.md")
    print(f"   3. Ejecuta: python .claude/scripts/stack_selector.py")
    print(f"   4. Usa el skill 'brief-to-prd' para generar PRD + config")

    return True


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python init_project.py <path/to/new/project>")
        sys.exit(1)

    project_path = sys.argv[1]
    success = init_project(project_path)
    sys.exit(0 if success else 1)
