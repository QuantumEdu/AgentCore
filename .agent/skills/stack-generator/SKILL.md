# Stack Generator Skill

## Metadata

**name**: stack-generator  
**description**: Genera stack_config.yml de AgentCore desde PROJECT-BRIEF-FULL.yaml  
**trigger**: Cuando el usuario pide generar configuración de stack desde un brief

## Overview

Este skill transforma un `PROJECT-BRIEF-FULL.yaml` en un `stack_config.yml` completo para AgentCore v2.0. Mapea todas las decisiones del brief (backend, base de datos, autenticación, herramientas, etc.) en una configuración estructurada que los agentes de AgentCore consumen antes de escribir código.

## Workflow

1. Leer `PROJECT-BRIEF-FULL.yaml`
2. Aplicar funciones de mapeo para cada sección
3. Generar `stack_config.yml` completo
4. Validar que el YAML sea válido

---

## Mapping Functions

### 1. map_project(brief)

```python
def map_project(brief: dict) -> dict:
    """
    Extrae información del proyecto desde el brief.
    """
    project = brief.get("project", {})
    
    return {
        "name": project.get("name", "Untitled Project"),
        "type": project.get("type", "web-app"),
        "scale": calculate_scale(brief),
        "description": project.get("description", ""),
        "version": "1.0.0"
    }
```

### 2. calculate_scale(brief)

```python
def calculate_scale(brief: dict) -> str:
    """
    Determina el tamaño del proyecto basado en el brief.
    
    - small: < 10 endpoints, < 5 entidades
    - medium: 10-50 endpoints, 5-15 entidades
    - large: > 50 endpoints, > 15 entidades
    """
    tech = brief.get("tech_stack", {})
    backend = tech.get("backend", {})
    
    # Contar endpoints desde requerimientos
    requirements = brief.get("requirements", {})
    api_requirements = requirements.get("api", [])
    endpoint_count = len(api_requirements) if api_requirements else 0
    
    # Contar entidades desde domain model
    domain_model = brief.get("domain_model", {})
    entities = domain_model.get("entities", [])
    entity_count = len(entities) if entities else 0
    
    if endpoint_count < 10 and entity_count < 5:
        return "small"
    elif endpoint_count <= 50 and entity_count <= 15:
        return "medium"
    else:
        return "large"
```

### 3. map_backend(brief)

```python
def map_backend(brief: dict) -> dict:
    """
    Mapea configuración del backend.
    """
    tech = brief.get("tech_stack", {})
    backend = tech.get("backend", {})
    framework = backend.get("framework", "").lower()
    
    return {
        "framework": framework,
        "runtime": get_runtime(framework),
        "server": get_server(framework),
        "architecture": "clean_architecture",
        "api_style": "restful",
        "async": backend.get("async", False),
        "cors_enabled": True
    }

def get_runtime(framework: str) -> str:
    """Determina el runtime basado en el framework."""
    if framework in ["fastapi", "django", "flask"]:
        return "python"
    elif framework in ["nextjs", "express"]:
        return "node"
    elif framework == "go-wails":
        return "go"
    return "python"

def get_server(framework: str) -> str:
    """Determina el servidor basado en el framework."""
    if framework == "fastapi":
        return "uvicorn"
    elif framework == "django":
        return "gunicorn"
    elif framework == "flask":
        return "gunicorn"
    elif framework == "nextjs":
        return "next"
    elif framework == "express":
        return "node"
    elif framework == "go-wails":
        return "wails"
    return "uvicorn"
```

### 4. map_database(brief)

```python
def map_database(brief: dict) -> dict:
    """
    Mapea configuración de la base de datos.
    """
    tech = brief.get("tech_stack", {})
    database = tech.get("database", {})
    db_type = database.get("type", "sqlite").lower()
    orm_name = database.get("orm", "").lower()
    
    return {
        "type": db_type,
        "host": database.get("host", "localhost"),
        "port": database.get("port", 5432),
        "database": database.get("name", "app_db"),
        "user": database.get("user", ""),
        "password": database.get("password", ""),
        "orm": map_orm(orm_name),
        "migrations": get_migration_tool(orm_name),
        "soft_delete": database.get("soft_delete", True),
        "append_only_tables": get_append_only_tables(brief),
        "connection_pool": {
            "min_size": 5,
            "max_size": 20,
            "timeout": 30
        }
    }

def get_append_only_tables(brief: dict) -> list:
    """
    Identifica tablas append-only desde el domain model.
    """
    domain_model = brief.get("domain_model", {})
    entities = domain_model.get("entities", [])
    
    append_only = []
    for entity in entities:
        if entity.get("append_only", False):
            append_only.append(entity.get("name", "").lower())
    
    # Tablas estándar que suelen ser append-only
    if not append_only:
        append_only = ["event_logs", "activity_logs"]
    
    return append_only
```

### 5. map_auth(brief)

```python
def map_auth(brief: dict) -> dict:
    """
    Mapea configuración de autenticación.
    """
    tech = brief.get("tech_stack", {})
    auth = tech.get("auth", {})
    auth_method = auth.get("method", "jwt").lower()
    hash_method = auth.get("password_hash", "argon2id").lower()
    
    return {
        "method": auth_method,
        "password_hash": hash_method,
        "hash_package": get_hash_package(hash_method, tech),
        "hash_rationale": get_hash_rationale(hash_method),
        "forbidden_hashes": get_forbidden_hashes(hash_method),
        "forbidden_reason": get_forbidden_reason(hash_method),
        "roles": map_roles(auth.get("authorization", {}).get("method", "rbac")),
        "token_expiry": auth.get("token_expiry", "24h"),
        "refresh_token_expiry": auth.get("refresh_token_expiry", "7d"),
        "session": {
            "secure": True,
            "http_only": True,
            "same_site": "strict"
        }
    }
```

### 6. map_tools(brief)

```python
def map_tools(brief: dict) -> dict:
    """
    Mapea herramientas y dependencias.
    """
    tech = brief.get("tech_stack", {})
    backend = tech.get("backend", {})
    framework = backend.get("framework", "").lower()
    runtime = get_runtime(framework)
    
    return {
        "package_manager": get_package_manager(runtime),
        "python_version": "3.12" if runtime == "python" else None,
        "node_version": "20" if runtime == "node" else None,
        "go_version": "1.21" if runtime == "go" else None,
        "dependency_lock": True,
        "virtual_env": runtime == "python"
    }

def get_package_manager(runtime: str) -> str:
    """Determina el gestor de paquetes por runtime."""
    if runtime == "python":
        return "uv"
    elif runtime == "node":
        return "npm"
    elif runtime == "go":
        return "go"
    return "uv"
```

### 7. map_testing(brief)

```python
def map_testing(brief: dict) -> dict:
    """
    Mapea configuración de pruebas.
    """
    tech = brief.get("tech_stack", {})
    testing = tech.get("testing", {})
    framework = testing.get("framework", "").lower()
    
    return {
        "framework": framework,
        "coverage": testing.get("coverage", 80),
        "e2e": testing.get("e2e", False),
        "e2e_framework": testing.get("e2e_framework", "playwright") if testing.get("e2e") else None,
        "ci_integration": True,
        "aaa_pattern": True,
        "fixtures": True
    }
```

### 8. map_deployment(brief)

```python
def map_deployment(brief: dict) -> dict:
    """
    Mapea configuración de despliegue.
    """
    tech = brief.get("tech_stack", {})
    deployment = tech.get("deployment", {})
    
    return {
        "target": deployment.get("target", "docker"),
        "containerized": deployment.get("containerized", True),
        "container_registry": deployment.get("container_registry", "ghcr.io"),
        "ci_cd": deployment.get("ci_cd", "github_actions"),
        "environment": deployment.get("environment", "production"),
        "health_checks": True,
        "monitoring": deployment.get("monitoring", True)
    }
```

### 9. map_code_quality(brief)

```python
def map_code_quality(brief: dict) -> dict:
    """
    Mapea herramientas de calidad de código.
    """
    tech = brief.get("tech_stack", {})
    code_quality = tech.get("code_quality", {})
    runtime = get_runtime(tech.get("backend", {}).get("framework", "").lower())
    
    return {
        "linter": get_linter(runtime),
        "formatter": get_formatter(runtime),
        "type_checker": get_type_checker(runtime),
        "pre_commit": True,
        "lint_staged": True
    }

def get_linter(runtime: str) -> str:
    """Determina el linter por runtime."""
    if runtime == "python":
        return "ruff"
    elif runtime == "node":
        return "eslint"
    elif runtime == "go":
        return "golangci-lint"
    return "ruff"

def get_formatter(runtime: str) -> str:
    """Determina el formatter por runtime."""
    if runtime == "python":
        return "ruff"
    elif runtime == "node":
        return "prettier"
    elif runtime == "go":
        return "gofmt"
    return "ruff"

def get_type_checker(runtime: str) -> str:
    """Determina el type checker por runtime."""
    if runtime == "python":
        return "mypy"
    elif runtime == "node":
        return "typescript"
    elif runtime == "go":
        return "builtin"
    return "mypy"
```

### 10. map_frontend(brief)

```python
def map_frontend(brief: dict) -> dict:
    """
    Mapea configuración del frontend.
    """
    tech = brief.get("tech_stack", {})
    frontend = tech.get("frontend", {})
    frontend_type = frontend.get("type", "").lower()
    
    if frontend_type == "none":
        return {"type": "none"}
    
    return {
        "type": frontend_type,
        "framework": frontend.get("framework", ""),
        "css_framework": frontend.get("css_framework", ""),
        "state_management": frontend.get("state_management", ""),
        "build_tool": frontend.get("build_tool", ""),
        "ssr": frontend.get("ssr", False)
    }
```

### 11. map_security(brief)

```python
def map_security(brief: dict) -> dict:
    """
    Mapea configuración de seguridad.
    """
    tech = brief.get("tech_stack", {})
    security = tech.get("security", {})
    
    return {
        "cors": {
            "enabled": True,
            "origins": security.get("cors_origins", ["*"]),
            "methods": security.get("cors_methods", ["GET", "POST", "PUT", "DELETE", "OPTIONS"]),
            "headers": security.get("cors_headers", ["*"])
        },
        "rate_limiting": {
            "enabled": security.get("rate_limiting", True),
            "requests_per_minute": security.get("rate_limit", 60),
            "burst": security.get("rate_burst", 10)
        },
        "helmet": True,
        "csrf_protection": security.get("csrf", True),
        "input_validation": True,
        "output_sanitization": True,
        "security_headers": True
    }
```

### 12. map_optional_modules(brief)

```python
def map_optional_modules(brief: dict) -> dict:
    """
    Mapea módulos opcionales.
    """
    tech = brief.get("tech_stack", {})
    optional = tech.get("optional_modules", {})
    runtime = get_runtime(tech.get("backend", {}).get("framework", "").lower())
    
    return {
        "email": {
            "enabled": optional.get("email", False),
            "library": get_email_library(runtime) if optional.get("email") else None,
            "provider": optional.get("email_provider", "smtp")
        },
        "background_tasks": {
            "enabled": optional.get("background_tasks", False),
            "library": get_background_library(runtime) if optional.get("background_tasks") else None,
            "queue": optional.get("queue", "redis")
        },
        "file_upload": {
            "enabled": optional.get("file_upload", False),
            "max_size_mb": optional.get("file_max_size", 10),
            "allowed_types": optional.get("file_types", ["image/*", "application/pdf"]),
            "storage": optional.get("file_storage", "local")
        },
        "api_docs": {
            "enabled": True,
            "format": "openapi",
            "version": "3.0.0"
        },
        "cache": {
            "enabled": optional.get("cache", False),
            "server": optional.get("cache_server", "redis"),
            "library": get_cache_library(optional.get("cache_server", "redis"), tech) if optional.get("cache") else None
        },
        "websockets": {
            "enabled": optional.get("websockets", False)
        }
    }
```

### 13. map_business_rules(brief)

```python
def map_business_rules(brief: dict) -> dict:
    """
    Mapea reglas de negocio específicas del stack.
    """
    domain_model = brief.get("domain_model", {})
    business_rules = domain_model.get("business_rules", {})
    
    return {
        "forbidden_substitutions": generate_forbidden_substitutions(brief),
        "required_fields": business_rules.get("required_fields", {}),
        "validation_rules": business_rules.get("validation_rules", {}),
        "status_machines": business_rules.get("status_machines", {}),
        "immutable_entities": get_immutable_entities(brief),
        "file_path_headers": True,
        "transaction_safety": True
    }

def get_immutable_entities(brief: dict) -> list:
    """
    Identifica entidades inmutables desde el domain model.
    """
    domain_model = brief.get("domain_model", {})
    entities = domain_model.get("entities", [])
    
    immutable = []
    for entity in entities:
        if entity.get("immutable", False):
            immutable.append(entity.get("name", "").lower())
    
    return immutable
```

---

## Helper Functions

### map_orm(orm_name)

```python
def map_orm(orm_name: str) -> dict:
    """
    Mapea nombres de ORM a configuración estandarizada.
    """
    orm_map = {
        "sqlalchemy": {
            "name": "sqlalchemy",
            "version": "2.0",
            "async_capable": True,
            "declarative_base": True
        },
        "prisma": {
            "name": "prisma",
            "version": "5.0",
            "async_capable": True,
            "type_safe": True
        },
        "gorm": {
            "name": "gorm",
            "version": "1.25",
            "async_capable": True,
            "convention_over_configuration": True
        },
        "none": {
            "name": "raw_sql",
            "async_capable": False,
            "type_safe": False
        }
    }
    
    return orm_map.get(orm_name.lower(), orm_map["sqlalchemy"])
```

### get_hash_package(hash_method, stack)

```python
def get_hash_package(hash_method: str, tech: dict) -> str:
    """
    Determina el paquete de hasheo basado en el método y stack.
    """
    runtime = get_runtime(tech.get("backend", {}).get("framework", "").lower())
    
    hash_packages = {
        "argon2id": {
            "python": "argon2-cffi",
            "node": "argon2",
            "go": "golang.org/x/crypto/argon2"
        },
        "bcrypt": {
            "python": "bcrypt",
            "node": "bcrypt",
            "go": "golang.org/x/crypto/bcrypt"
        },
        "scrypt": {
            "python": "scrypt",
            "node": "scrypt",
            "go": "golang.org/x/crypto/scrypt"
        },
        "pbkdf2": {
            "python": "passlib",
            "node": "crypto",
            "go": "golang.org/x/crypto/pbkdf2"
        }
    }
    
    return hash_packages.get(hash_method.lower(), {}).get(runtime, "argon2-cffi")
```

### get_hash_rationale(hash_method)

```python
def get_hash_rationale(hash_method: str) -> str:
    """
    Proporciona la justificación para el método de hasheo.
    """
    rationales = {
        "argon2id": "Password Hashing Competition (PHC) winner. Resistant to GPU/ASIC attacks, memory-hard, recommended by OWASP for new systems.",
        "bcrypt": "Battle-tested since 1999, adaptive cost factor, widely supported. Good alternative if Argon2 is unavailable.",
        "scrypt": "Memory-hard like Argon2, NIST-approved. Good alternative but Argon2id is preferred.",
        "pbkdf2": "NIST-approved, widely supported, but NOT memory-hard. Use only if Argon2/bcrypt/scrypt are unavailable."
    }
    
    return rationales.get(hash_method.lower(), "")
```

### get_forbidden_hashes(hash_method)

```python
def get_forbidden_hashes(hash_method: str) -> list:
    """
    Lista de métodos de hasheo prohibidos.
    """
    forbidden = ["md5", "sha1", "sha256", "plain", "plaintext", "none"]
    
    # Si el método elegido es seguro, prohibir los demás
    if hash_method.lower() in ["argon2id", "bcrypt", "scrypt", "pbkdf2"]:
        return forbidden
    else:
        return []  # Si eligieron uno inseguro, no prohibimos nada (pero el validador lo marcará)
```

### get_forbidden_reason(hash_method)

```python
def get_forbidden_reason(hash_method: str) -> str:
    """
    Razón por la que esos métodos están prohibidos.
    """
    return "Fast hash algorithms (MD5, SHA1, SHA256) are vulnerable to rainbow table and brute force attacks. Plain text storage is NEVER acceptable. Use Argon2id, bcrypt, scrypt, or PBKDF2."
```

### map_roles(authz_method)

```python
def map_roles(authz_method: str) -> dict:
    """
    Mapea roles basado en el método de autorización.
    """
    if authz_method.lower() == "rbac":
        return {
            "method": "rbac",
            "roles": {
                "ADMIN": {
                    "description": "Full system access",
                    "permissions": ["*"]
                },
                "MEMBER": {
                    "description": "Standard user access",
                    "permissions": ["read", "write_own"]
                },
                "VIEWER": {
                    "description": "Read-only access",
                    "permissions": ["read"]
                }
            },
            "hierarchy": ["ADMIN", "MEMBER", "VIEWER"]
        }
    elif authz_method.lower() == "abac":
        return {
            "method": "abac",
            "attributes": ["role", "department", "clearance_level"],
            "policy_engine": "custom"
        }
    else:
        return {
            "method": "none",
            "description": "No authorization implemented"
        }
```

### get_cache_library(cache_server, tech)

```python
def get_cache_library(cache_server: str, tech: dict) -> str:
    """
    Determina la librería de cache basada en el servidor y stack.
    """
    runtime = get_runtime(tech.get("backend", {}).get("framework", "").lower())
    
    cache_libraries = {
        "redis": {
            "python": "redis",
            "node": "redis",
            "go": "github.com/redis/go-redis/v9"
        },
        "memcached": {
            "python": "pymemcache",
            "node": "memcached",
            "go": "github.com/bradfitz/gomemcache"
        }
    }
    
    return cache_libraries.get(cache_server.lower(), {}).get(runtime, "redis")
```

### get_migration_tool(orm_name)

```python
def get_migration_tool(orm_name: str) -> dict:
    """
    Determina la herramienta de migraciones basada en el ORM.
    """
    migration_tools = {
        "sqlalchemy": {
            "name": "alembic",
            "version": "1.13",
            "auto_generate": True
        },
        "prisma": {
            "name": "prisma migrate",
            "version": "5.0",
            "auto_generate": True
        },
        "gorm": {
            "name": "gormigrate",
            "version": "1.7",
            "auto_generate": False
        },
        "none": {
            "name": "manual",
            "auto_generate": False
        }
    }
    
    return migration_tools.get(orm_name.lower(), migration_tools["sqlalchemy"])
```

### get_email_library(stack)

```python
def get_email_library(runtime: str) -> str:
    """
    Determina la librería de email basada en el runtime.
    """
    email_libraries = {
        "python": "fastapi-mail",
        "node": "nodemailer",
        "go": "github.com/go-gomail/gomail"
    }
    
    return email_libraries.get(runtime, "fastapi-mail")
```

### get_background_library(stack)

```python
def get_background_library(runtime: str) -> str:
    """
    Determina la librería de background tasks basada en el runtime.
    """
    bg_libraries = {
        "python": "celery",
        "node": "bull",
        "go": "github.com/hibiken/asynq"
    }
    
    return bg_libraries.get(runtime, "celery")
```

### generate_forbidden_substitutions(brief)

```python
def generate_forbidden_substitutions(brief: dict) -> dict:
    """
    Genera lista de sustituciones prohibidas basada en el stack.
    """
    tech = brief.get("tech_stack", {})
    runtime = get_runtime(tech.get("backend", {}).get("framework", "").lower())
    
    # Sustituciones comunes que deben prohibirse
    forbidden = {
        "python": {
            "package_manager": ["pip", "pipenv", "poetry"],
            "reason": "Use 'uv' instead - faster, better lock files"
        },
        "node": {
            "linter": ["standard", "jshint"],
            "reason": "Use 'eslint' instead - more powerful, widely adopted"
        },
        "go": {
            "orm": ["gorm"],
            "reason": "Use raw SQL or sqlx for better control (unless explicitly requested)"
        }
    }
    
    return forbidden.get(runtime, {})
```

---

## Full Config Generation

### generate_stack_config(brief)

```python
import yaml
from typing import Dict, Any
from datetime import datetime

def generate_stack_config(brief: Dict[str, Any]) -> str:
    """
    Función principal que genera el stack_config.yml completo.
    
    Args:
        brief: Diccionario con el contenido de PROJECT-BRIEF-FULL.yaml
    
    Returns:
        str: Contenido YAML del stack_config.yml generado
    """
    
    # Generar todas las secciones
    config = {
        "_metadata": {
            "generated_at": datetime.utcnow().isoformat(),
            "version": "2.0.0",
            "template": "AgentCore v2.0"
        },
        
        "_instructions": {
            "purpose": "Single source of truth for tech stack choices",
            "usage": "All agents MUST read this file before writing any code",
            "validation": "Run .agent/validators/check_stack.py before coding"
        },
        
        "project": map_project(brief),
        
        "tools": map_tools(brief),
        
        "backend": map_backend(brief),
        
        "database": map_database(brief),
        
        "frontend": map_frontend(brief),
        
        "auth": map_auth(brief),
        
        "security": map_security(brief),
        
        "testing": map_testing(brief),
        
        "optional_modules": map_optional_modules(brief),
        
        "deployment": map_deployment(brief),
        
        "code_quality": map_code_quality(brief),
        
        "business_rules": map_business_rules(brief),
        
        # Domain-specific mappings
        "domain": {
            "entities": map_entities(brief),
            "enums": map_enums(brief),
            "relationships": map_relationships(brief)
        }
    }
    
    # Convertir a YAML
    yaml_content = yaml.dump(config, default_flow_style=False, sort_keys=False, allow_unicode=True)
    
    return yaml_content

def map_entities(brief: Dict[str, Any]) -> list:
    """Mapea entidades desde el domain model."""
    domain_model = brief.get("domain_model", {})
    entities = domain_model.get("entities", [])
    
    mapped = []
    for entity in entities:
        mapped.append({
            "name": entity.get("name", ""),
            "table_name": entity.get("name", "").lower(),
            "soft_delete": entity.get("soft_delete", True),
            "append_only": entity.get("append_only", False),
            "immutable": entity.get("immutable", False),
            "fields": entity.get("fields", [])
        })
    
    return mapped

def map_enums(brief: Dict[str, Any]) -> dict:
    """Mapea enums desde el domain model."""
    domain_model = brief.get("domain_model", {})
    enums = domain_model.get("enums", {})
    
    return enums

def map_relationships(brief: Dict[str, Any]) -> list:
    """Mapea relaciones entre entidades."""
    domain_model = brief.get("domain_model", {})
    entities = domain_model.get("entities", [])
    
    relationships = []
    for entity in entities:
        for field in entity.get("fields", []):
            if field.get("type") in ["foreign_key", "many_to_one", "one_to_many", "many_to_many"]:
                relationships.append({
                    "from": entity.get("name", ""),
                    "to": field.get("relation_to", ""),
                    "type": field.get("type", ""),
                    "cascade": field.get("cascade", False)
                })
    
    return relationships
```

---

## Example: Generated stack_config.yml (FastAPI)

```yaml
_metadata:
  generated_at: "2024-01-15T10:30:00"
  version: "2.0.0"
  template: "AgentCore v2.0"

_instructions:
  purpose: Single source of truth for tech stack choices
  usage: All agents MUST read this file before writing any code
  validation: Run .agent/validators/check_stack.py before coding

project:
  name: "TaskFlow Pro"
  type: "web-app"
  scale: "medium"
  description: "Project and task management SaaS platform"
  version: "1.0.0"

tools:
  package_manager: "uv"
  python_version: "3.12"
  node_version: null
  go_version: null
  dependency_lock: true
  virtual_env: true

backend:
  framework: "fastapi"
  runtime: "python"
  server: "uvicorn"
  architecture: "clean_architecture"
  api_style: "restful"
  async: true
  cors_enabled: true

database:
  type: "postgresql"
  host: "localhost"
  port: 5432
  database: "taskflow_db"
  user: "taskflow_user"
  password: ""
  orm:
    name: "sqlalchemy"
    version: "2.0"
    async_capable: true
    declarative_base: true
  migrations:
    name: "alembic"
    version: "1.13"
    auto_generate: true
  soft_delete: true
  append_only_tables:
    - "event_logs"
    - "activity_logs"
  connection_pool:
    min_size: 5
    max_size: 20
    timeout: 30

frontend:
  type: "none"

auth:
  method: "jwt"
  password_hash: "argon2id"
  hash_package: "argon2-cffi"
  hash_rationale: "Password Hashing Competition (PHC) winner. Resistant to GPU/ASIC attacks, memory-hard, recommended by OWASP for new systems."
  forbidden_hashes:
    - "md5"
    - "sha1"
    - "sha256"
    - "plain"
    - "plaintext"
    - "none"
  forbidden_reason: "Fast hash algorithms (MD5, SHA1, SHA256) are vulnerable to rainbow table and brute force attacks. Plain text storage is NEVER acceptable. Use Argon2id, bcrypt, scrypt, or PBKDF2."
  roles:
    method: "rbac"
    roles:
      ADMIN:
        description: "Full system access"
        permissions:
          - "*"
      MEMBER:
        description: "Standard user access"
        permissions:
          - "read"
          - "write_own"
      VIEWER:
        description: "Read-only access"
        permissions:
          - "read"
    hierarchy:
      - "ADMIN"
      - "MEMBER"
      - "VIEWER"
  token_expiry: "24h"
  refresh_token_expiry: "7d"
  session:
    secure: true
    http_only: true
    same_site: "strict"

security:
  cors:
    enabled: true
    origins:
      - "*"
    methods:
      - "GET"
      - "POST"
      - "PUT"
      - "DELETE"
      - "OPTIONS"
    headers:
      - "*"
  rate_limiting:
    enabled: true
    requests_per_minute: 60
    burst: 10
  helmet: true
  csrf_protection: true
  input_validation: true
  output_sanitization: true
  security_headers: true

testing:
  framework: "pytest"
  coverage: 80
  e2e: true
  e2e_framework: "playwright"
  ci_integration: true
  aaa_pattern: true
  fixtures: true

optional_modules:
  email:
    enabled: true
    library: "fastapi-mail"
    provider: "smtp"
  background_tasks:
    enabled: true
    library: "celery"
    queue: "redis"
  file_upload:
    enabled: true
    max_size_mb: 10
    allowed_types:
      - "image/*"
      - "application/pdf"
    storage: "local"
  api_docs:
    enabled: true
    format: "openapi"
    version: "3.0.0"
  cache:
    enabled: true
    server: "redis"
    library: "redis"
  websockets:
    enabled: false

deployment:
  target: "docker"
  containerized: true
  container_registry: "ghcr.io"
  ci_cd: "github_actions"
  environment: "production"
  health_checks: true
  monitoring: true

code_quality:
  linter: "ruff"
  formatter: "ruff"
  type_checker: "mypy"
  pre_commit: true
  lint_staged: true

business_rules:
  forbidden_substitutions:
    package_manager:
      - "pip"
      - "pipenv"
      - "poetry"
    reason: "Use 'uv' instead - faster, better lock files"
  required_fields: {}
  validation_rules: {}
  status_machines: {}
  immutable_entities:
    - "sprints"
  file_path_headers: true
  transaction_safety: true

domain:
  entities:
    - name: "User"
      table_name: "users"
      soft_delete: true
      append_only: false
      immutable: false
      fields: []
    - name: "Project"
      table_name: "projects"
      soft_delete: true
      append_only: false
      immutable: false
      fields: []
    - name: "Task"
      table_name: "tasks"
      soft_delete: true
      append_only: false
      immutable: false
      fields: []
    - name: "ActivityLog"
      table_name: "activity_logs"
      soft_delete: false
      append_only: true
      immutable: false
      fields: []
  enums:
    TaskStatus:
      - "pending"
      - "in_progress"
      - "completed"
      - "cancelled"
    ProjectStatus:
      - "active"
      - "paused"
      - "completed"
      - "archived"
  relationships:
    - from: "Project"
      to: "User"
      type: "many_to_one"
      cascade: false
    - from: "Task"
      to: "Project"
      type: "many_to_one"
      cascade: true
    - from: "Task"
      to: "User"
      type: "many_to_one"
      cascade: false
```

---

## Usage Pattern

```python
# Ejemplo de uso del skill
import yaml

# 1. Leer el brief
with open("PROJECT-BRIEF-FULL.yaml", "r") as f:
    brief = yaml.safe_load(f)

# 2. Generar el stack config
stack_config = generate_stack_config(brief)

# 3. Escribir el archivo
with open("stack_config.yml", "w") as f:
    f.write(stack_config)

# 4. Validar
import subprocess
subprocess.run(["python", ".agent/validators/check_stack.py"])
```

---

## Validation Checklist

Antes de considerar el stack_config.yml como válido, verificar:

- [ ] Todas las secciones requeridas están presentes
- [ ] El YAML es sintácticamente válido
- [ ] Los métodos de hasheo prohibidos están listados
- [ ] Las tablas append-only están identificadas
- [ ] Los roles y permisos están definidos
- [ ] Las herramientas coinciden con el runtime seleccionado
- [ ] Los ORMs tienen herramientas de migración asociadas
- [ ] Las librerías son compatibles con el stack

---

## Edge Cases

1. **Brief incompleto**: Usar valores predeterminados razonables
2. **Framework desconocido**: Asumir FastAPI/Python como fallback
3. **ORM no soportado**: Asumir SQLAlchemy como fallback
4. **Hash inseguro seleccionado**: Generar el config pero el validador lo marcará
5. **Frontend opcional**: Si es "none", incluir sección vacía pero presente
6. **Módulos opcionales**: Si no están en el brief, asumir enabled=false
