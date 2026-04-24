#!/usr/bin/env python3
"""
AgentCore v2.0 - Decision Log Converter
Convierte decision_log.json a formato ADR Markdown
"""

import json
from datetime import datetime
from pathlib import Path


def convert_decision_log(json_path: str):
    """Convierte decision_log.json a decision_log.md"""
    json_path = Path(json_path)

    if not json_path.exists():
        print(f"❌ Archivo no encontrado: {json_path}")
        return False

    # Leer JSON
    with open(json_path) as f:
        data = json.load(f)

    # Generar Markdown ADR
    md_content = "# Decision Log\n\n"
    md_content += f"Última actualización: {datetime.now().strftime('%Y-%m-%d')}\n\n"
    md_content += "---\n\n"

    decisions = data.get("decisions", [])

    for i, decision in enumerate(decisions, 1):
        md_content += f"## [{i}] {decision.get('decision', 'Sin título')}\n\n"

        if decision.get("context"):
            md_content += f"**Contexto**: {decision['context']}\n\n"

        md_content += f"**Decisión**: {decision.get('decision', '')}\n\n"

        if decision.get("alternatives"):
            md_content += "**Alternativas Consideradas**:\n"
            for alt in decision["alternatives"]:
                md_content += (
                    f"- **{alt.get('name', '')}**: {alt.get('rejected', '')}\n"
                )
            md_content += "\n"

        if decision.get("rationale"):
            md_content += f"**Rationale**: {decision['rationale']}\n\n"

        if decision.get("consequences"):
            md_content += "**Consecuencias**:\n"
            for cons in decision["consequences"]:
                md_content += f"- {cons}\n"
            md_content += "\n"

        md_content += "---\n\n"

    # Guardar Markdown
    md_path = json_path.parent / "decision_log.md"
    with open(md_path, "w") as f:
        f.write(md_content)

    print(f"✅ Convertidas {len(decisions)} decisiones a formato ADR")
    print(f"📄 Archivo generado: {md_path}")

    return True


if __name__ == "__main__":
    if len(__import__("sys").argv) < 2:
        print("Uso: python decision_adr_converter.py <path/to/decision_log.json>")
        __import__("sys").exit(1)

    convert_decision_log(__import__("sys").argv[1])
