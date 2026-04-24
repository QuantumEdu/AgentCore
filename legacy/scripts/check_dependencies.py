#!/usr/bin/env python3
# .claude/validators/check_dependencies.py
"""
Dependency Validator - Verifies dependency conflicts

Run after installing dependencies:
    python .claude/validators/check_dependencies.py
"""

import json
import sys
import subprocess
from pathlib import Path


def load_stack_config():
    """Load stack_config.json"""
    config_path = Path(__file__).parent.parent / "stack_config.json"
    if not config_path.exists():
        print("ERROR: stack_config.json not found")
        sys.exit(1)

    with open(config_path) as f:
        return json.load(f)


def get_installed_packages():
    """Get list of installed packages"""
    try:
        result = subprocess.run(
            ["pip", "list", "--format=json"],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            return {pkg["name"].lower(): pkg["version"]
                    for pkg in json.loads(result.stdout)}
    except Exception:
        pass

    # Try with uv
    try:
        result = subprocess.run(
            ["uv", "pip", "list", "--format=json"],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            return {pkg["name"].lower(): pkg["version"]
                    for pkg in json.loads(result.stdout)}
    except Exception:
        pass

    return {}


def check_forbidden_packages(config, installed):
    """Verify no forbidden packages are installed"""
    issues = []

    # Password hash forbidden
    forbidden_hash = config.get("auth", {}).get("password_hash", {}).get("FORBIDDEN", [])
    required_algo = config.get("auth", {}).get("password_hash", {}).get("algorithm", "")

    for pkg in forbidden_hash:
        pkg_lower = pkg.lower()
        if pkg_lower in installed:
            if required_algo and required_algo != pkg:
                issues.append(
                    f"CONFLICT: '{pkg}' installed but stack requires '{required_algo}'"
                )

    return issues


def check_required_packages(config, installed):
    """Verify required packages are installed"""
    missing = []

    # Password hash package
    hash_pkg = config.get("auth", {}).get("password_hash", {}).get("package", "")
    if hash_pkg:
        pkg_name = hash_pkg.lower().replace("-", "_").split("[")[0]
        # Search for name variants
        found = any(
            pkg_name in name or name in pkg_name
            for name in installed.keys()
        )
        if not found:
            missing.append(f"{hash_pkg} (for password hashing)")

    # Framework
    framework = config.get("backend", {}).get("framework", "").lower()
    if framework and framework not in installed:
        missing.append(f"{framework} (backend framework)")

    # ORM
    orm = config.get("database", {}).get("orm", "")
    if orm:
        orm_pkg = orm.lower().split()[0]  # "SQLAlchemy 2.0" -> "sqlalchemy"
        if orm_pkg not in installed:
            missing.append(f"{orm_pkg} (ORM)")

    return missing


def main():
    print("\n" + "="*50)
    print("DEPENDENCY VALIDATOR v2.0")
    print("="*50 + "\n")

    config = load_stack_config()
    installed = get_installed_packages()

    if not installed:
        print("WARNING: Could not get list of installed packages")
        return 1

    print(f"Installed packages: {len(installed)}\n")

    all_ok = True

    # Check forbidden
    print("Checking forbidden packages...")
    issues = check_forbidden_packages(config, installed)
    if issues:
        print("\nCONFLICTS FOUND:")
        for issue in issues:
            print(f"  [ERROR] {issue}")
        all_ok = False
    else:
        print("  [OK] No forbidden packages installed")

    # Check required
    print("\nChecking required packages...")
    missing = check_required_packages(config, installed)
    if missing:
        print("\nMISSING PACKAGES:")
        for pkg in missing:
            print(f"  [WARN] {pkg}")
        all_ok = False
    else:
        print("  [OK] All required packages installed")

    print("\n" + "="*50)
    if all_ok:
        print("RESULT: OK - Dependencies correct")
    else:
        print("RESULT: PROBLEMS - Review above")
    print("="*50 + "\n")

    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
