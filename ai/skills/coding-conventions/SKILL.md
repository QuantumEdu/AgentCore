---
name: coding-conventions
description: Resume prácticas de arquitectura, API, seguridad y testing en forma agnóstica para usarlas como base de implementación o revisión.
---

# Coding Conventions

## Purpose

Dar una base reusable de buenas prácticas sin amarrarse a un dominio específico ni a FlowTask.

## Architecture

### Layering
- separar dominio, aplicación y presentación cuando el proyecto lo justifique;
- mantener el flujo de dependencias hacia adentro;
- evitar lógica de negocio dentro de handlers, controladores o endpoints.

### Domain Rules
- modelos o entidades con timestamps consistentes cuando aplique;
- usar soft delete solo cuando tenga sentido de negocio;
- tablas append-only o registros inmutables deben declararse explícitamente.

### Application Rules
- separar comandos de escritura y modelos de lectura cuando agregue claridad;
- usar DTOs o schemas por intención: create, update, response, persistence;
- encapsular validaciones de negocio fuera de la capa de transporte.

## API Design

- usar nombres de recursos en plural y consistentes;
- versionar la API cuando sea pública o evolutiva;
- GET sin efectos colaterales;
- POST para crear;
- PATCH para actualizaciones parciales;
- usar query params para filtros, búsqueda y paginación;
- devolver códigos HTTP coherentes y errores claros.

## Security

- usar hashing moderno y explícito para contraseñas;
- nunca almacenar secretos o credenciales en texto plano;
- los tokens deben expirar;
- minimizar claims sensibles;
- modelar autorización por roles o permisos, no por lógica dispersa;
- centralizar autenticación/autorización en dependencias, middlewares o servicios dedicados.

## Testing

- tests por módulo o feature con nombres descriptivos;
- fixtures compartidas para setup repetitivo;
- preferir cambios pequeños y verificables;
- cubrir rutas felices, errores y permisos;
- validar comportamiento antes que implementación interna.

## Review Checklist

- ¿la lógica de negocio quedó fuera de la capa de transporte?
- ¿las dependencias respetan la dirección arquitectónica elegida?
- ¿los contratos de entrada y salida son claros?
- ¿la seguridad está centralizada y explícita?
- ¿hay estrategia razonable de pruebas para el cambio?
