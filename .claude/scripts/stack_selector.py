#!/usr/bin/env python3
"""
AgentCore v2.0 - Stack Selector Script
Selecciona el stack activo y genera stack_config.yml
"""

import yaml
from pathlib import Path


def load_registry():
    """Carga el registro de stacks"""
    registry_path = Path(__file__).parent.parent / "stacks" / "registry.yaml"
    with open(registry_path) as f:
        return yaml.safe_load(f)


def select_stack():
    """Interactivamente selecciona un stack"""
    registry = load_registry()

    print("\n🤖 Selección de Stack - AgentCore v2.0")
    print("=" * 50)

    for idx, stack in enumerate(registry["available_stacks"], 1):
        print(f"  [{idx}] {stack['name']}")
        print(f"      {stack['description']}")
        if stack.get("substacks"):
            for sub in stack["substacks"]:
                print(f"      - {sub['name']}")

    print()
    choice = input("Tu elección (número): ").strip()

    try:
        idx = int(choice) - 1
        selected = registry["available_stacks"][idx]
    except (ValueError, IndexError):
        print("❌ Elección inválida")
        return None

    # Si tiene substacks, preguntar cual
    if selected.get("substacks"):
        print(f"\n📦 Sub-stacks disponibles para {selected['name']}:")
        for idx, sub in enumerate(selected["substacks"], 1):
            print(f"  [{idx}] {sub['name']}")

        sub_choice = input("\nTu elección (número, Enter para principal): ").strip()

        if sub_choice:
            try:
                idx = int(sub_choice) - 1
                substack = selected["substacks"][idx]
                return substack
            except (ValueError, IndexError):
                pass

        return selected

    return selected


def generate_stack_config(stack):
    """Genera stack_config.yml desde el stack seleccionado"""
    config_path = Path(__file__).parent.parent / "stack_config.yml"

    config = {
        "_filepath": ".claude/stack_config.yml",
        "_metadata": {
            "version": "2.0",
            "selected_stack": stack["id"],
            "selected_at": "2026-04-12",
        },
        "stack": stack,
    }

    with open(config_path, "w") as f:
        yaml.dump(config, f, default_flow_style=False)

    print(f"\n✅ Stack seleccionado: {stack['name']}")
    print(f"📄 Configuración guardada en: {config_path}")

    return True


if __name__ == "__main__":
    stack = select_stack()
    if stack:
        generate_stack_config(stack)
    else:
        print("❌ No se seleccionó ningún stack")
