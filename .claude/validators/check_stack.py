#!/usr/bin/env python3
# .claude/validators/check_stack.py
"""
Stack Validator - Verifies that implementation follows stack_config.json

Run BEFORE implementing code:
    python .claude/validators/check_stack.py

Run AFTER implementing to verify:
    python .claude/validators/check_stack.py --verify
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


def check_python_version(config):
    """Verify Python version"""
    import platform
    current = platform.python_version()
    minimum = config["tools"]["python_version"]["minimum"]

    current_parts = tuple(map(int, current.split(".")[:2]))
    minimum_parts = tuple(map(int, minimum.split(".")[:2]))

    if current_parts < minimum_parts:
        print(f"WARNING: Python {current} < minimum required {minimum}")
        return False

    print(f"OK: Python {current} >= {minimum}")
    return True


def check_package_manager(config):
    """Verify package manager is installed"""
    pm = config["tools"]["package_manager"]["name"]

    try:
        result = subprocess.run([pm, "--version"], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"OK: {pm} installed - {result.stdout.strip()}")
            return True
    except FileNotFoundError:
        pass

    print(f"WARNING: {pm} not found. Install with: pip install {pm}")
    return False


def check_dependencies_installed(config):
    """Verify critical dependencies are installed"""
    checks = []

    # Password hashing
    hash_algo = config["auth"]["password_hash"]["algorithm"]
    hash_pkg = config["auth"]["password_hash"]["package"]

    try:
        if hash_algo == "argon2id":
            import argon2
            print(f"OK: {hash_pkg} installed for {hash_algo}")
            checks.append(True)
        elif hash_algo == "bcrypt":
            import bcrypt
            print(f"OK: bcrypt installed")
            checks.append(True)
    except ImportError:
        print(f"MISSING: {hash_pkg} not installed. Use: uv add {hash_pkg}")
        checks.append(False)

    # ORM
    orm = config["database"]["orm"]
    try:
        import sqlalchemy
        print(f"OK: SQLAlchemy {sqlalchemy.__version__} installed")
        checks.append(True)
    except ImportError:
        print("MISSING: SQLAlchemy not installed")
        checks.append(False)

    # Framework
    try:
        import fastapi
        print(f"OK: FastAPI {fastapi.__version__} installed")
        checks.append(True)
    except ImportError:
        print("MISSING: FastAPI not installed")
        checks.append(False)

    return all(checks)


def check_forbidden_packages(config):
    """Verify forbidden packages are NOT installed"""
    forbidden = config["auth"]["password_hash"].get("FORBIDDEN", [])
    issues = []

    for pkg in forbidden:
        try:
            if pkg == "bcrypt":
                import bcrypt
                # Only a problem if argon2id is specified
                if config["auth"]["password_hash"]["algorithm"] == "argon2id":
                    issues.append(f"bcrypt installed but stack requires argon2id")
        except ImportError:
            pass  # OK, not installed

    if issues:
        print("CONFLICTS DETECTED:")
        for issue in issues:
            print(f"  - {issue}")
        return False

    print("OK: No forbidden packages installed")
    return True


def verify_code_uses_correct_libs():
    """Verify that code uses the correct libraries"""
    issues = []

    # Search for bcrypt usage in code when argon2id should be used
    py_files = list(Path(".").rglob("*.py"))

    for py_file in py_files:
        if ".claude" in str(py_file) or "venv" in str(py_file):
            continue

        try:
            content = py_file.read_text()

            # Detect problematic imports
            if "from passlib" in content and "bcrypt" in content:
                issues.append(f"{py_file}: Uses passlib with bcrypt")

            if "import bcrypt" in content:
                issues.append(f"{py_file}: Imports bcrypt directly")

        except Exception:
            pass

    if issues:
        print("\nPROBLEMS IN CODE:")
        for issue in issues:
            print(f"  - {issue}")
        return False

    return True


def print_stack_summary(config):
    """Print summary of configured stack"""
    print("\n" + "="*50)
    print("CONFIGURED STACK:")
    print("="*50)
    print(f"  Project:         {config['project']['name']}")
    print(f"  Package Manager: {config['tools']['package_manager']['name']}")
    print(f"  Python Version:  >= {config['tools']['python_version']['minimum']}")
    print(f"  Framework:       {config['backend']['framework']}")
    print(f"  Database:        {config['database']['type']} + {config['database']['orm']}")
    print(f"  Password Hash:   {config['auth']['password_hash']['algorithm']}")
    print(f"  Auth Method:     {config['auth']['method']}")
    print(f"  Roles:           {', '.join(config['auth']['roles'].keys())}")
    print("="*50 + "\n")


def main():
    verify_mode = "--verify" in sys.argv

    print("\n" + "="*50)
    print("STACK VALIDATOR v2.0")
    print("="*50 + "\n")

    config = load_stack_config()
    print_stack_summary(config)

    all_ok = True

    print("VERIFICATIONS:\n")

    if not check_python_version(config):
        all_ok = False

    if not check_package_manager(config):
        all_ok = False

    if verify_mode:
        print("\n[Verify mode - checking installed dependencies]\n")

        if not check_dependencies_installed(config):
            all_ok = False

        if not check_forbidden_packages(config):
            all_ok = False

        if not verify_code_uses_correct_libs():
            all_ok = False

    print("\n" + "="*50)
    if all_ok:
        print("RESULT: OK - Stack configured correctly")
    else:
        print("RESULT: PROBLEMS DETECTED - Review above")
    print("="*50 + "\n")

    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
