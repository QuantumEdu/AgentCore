#!/usr/bin/env python3
"""
AgentCore v2.0 - PROJECT-BRIEF Parser
Parsea y valida PROJECT-BRIEF-FULL.yaml
"""

import yaml
import json
from pathlib import Path


def validate_brief(brief_path: str):
    """Valida PROJECT-BRIEF-FULL.yaml"""
    brief_path = Path(brief_path)

    if not brief_path.exists():
        print(f"❌ Archivo no encontrado: {brief_path}")
        return False

    # Leer YAML
    with open(brief_path) as f:
        brief = yaml.safe_load(f)

    # Validar schema
    schema_path = brief_path.parent / "brief-schema.json"
    with open(schema_path) as f:
        schema = json.load(f)

    # Verificar campos obligatorios
    required = schema.get("required", [])
    for field in required:
        if field not in brief or not brief[field]:
            print(f"❌ Campo obligatorio faltante: {field}")
            return False

    print("✅ Brief validado exitosamente")
    return True


def calculate_complexity_score(brief):
    """Calcula complexity score (1-10)"""
    score = 0

    # Criticalidad
    if brief.get("criticalidad") == "critical":
        score += 3
    elif brief.get("criticalidad") == "high":
        score += 2
    elif brief.get("criticalidad") == "medium":
        score += 1

    # Team Size
    if brief.get("team_size") == "15+":
        score += 3
    elif brief.get("team_size") == "6-15":
        score += 2
    elif brief.get("team_size") == "2-5":
        score += 1

    # Timeframe
    if brief.get("timeframe") == "long-6mes+":
        score += 2
    elif brief.get("timeframe") == "medium-3mes":
        score += 1

    # Tipo de Ejecución
    if brief.get("arquitectura", {}).get("tipo_ejecucion") in [
        "async",
        "event-driven",
        "hybrid",
    ]:
        score += 2

    # Bounded Contexts
    bc = brief.get("arquitectura", {}).get("bounded_contexts", {})
    active_contexts = [k for k, v in bc.items() if v]
    if len(active_contexts) > 3:
        score += 2

    return min(score, 10)


def detect_stack(brief):
    """Detecta el stack desde el Brief"""
    stack = brief.get("stack_principal", "")

    if not stack:
        # Inferir desde campos del Brief
        frontend = brief.get("frontend", {}).get("renderizado", "")
        if "jinja2" in frontend:
            return "fastapi_ssr"
        elif "react" in frontend:
            return "fastapi_spa"
        elif "pywebview" in frontend:
            return "fastapi_desktop"
        else:
            return "fastapi_ssr"  # Default

    return stack


def analyze_brief(brief_path: str):
    """Analiza el Brief y genera reporte"""
    brief_path = Path(brief_path)

    with open(brief_path) as f:
        brief = yaml.safe_load(f)

    # Validar
    if not validate_brief(brief_path):
        return

    # Calcular complexity score
    score = calculate_complexity_score(brief)
    print(f"📊 Complexity Score: {score}/10")

    # Detectar stack
    stack = detect_stack(brief)
    print(f"🔧 Stack detectado: {stack}")

    # Identificar secciones faltantes
    missing = []
    if not brief.get("nombre"):
        missing.append("nombre")
    if not brief.get("arquitectura", {}).get("patron"):
        missing.append("arquitectura.patron")
    # ... más validaciones

    if missing:
        print(f"\n⚠️  Secciones faltantes: {', '.join(missing)}")
    else:
        print("\n✅ Todas las secciones críticas están completas")


if __name__ == "__main__":
    if len(__import__("sys").argv) < 2:
        print("Uso: python project_brief_parser.py <path/to/PROJECT-BRIEF-FULL.yaml")
        __import__("sys").exit(1)

    analyze_brief(__import__("sys").argv[1])
