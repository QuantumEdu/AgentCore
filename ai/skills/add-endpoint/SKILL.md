---
name: add-endpoint
description: Guía la adición segura de un endpoint nuevo sin sobreasumir stack, cubriendo contrato, validación, reglas, pruebas y documentación mínima.
---

# Add Endpoint

## Goal

Agregar un endpoint sin romper consistencia, seguridad ni contratos existentes.

## When to use

- cuando hay que exponer una nueva operación por API;
- cuando ya existe un módulo y falta una capacidad nueva;
- cuando se requiere un endpoint nuevo con validación y pruebas mínimas.

## Inputs

- recurso o módulo afectado;
- objetivo del endpoint;
- método HTTP tentativo;
- input/output esperado;
- reglas de auth o permisos;
- impacto en documentación o consumers.

## Workflow

1. Confirmar si el endpoint realmente debe existir.
2. Definir contrato:
   - método
   - path
   - request
   - response
   - errores esperados
3. Validar consistencia con convenciones de API.
4. Separar:
   - contrato
   - lógica de aplicación
   - validaciones
   - permisos
5. Definir pruebas mínimas:
   - happy path
   - validation error
   - not found o conflict
   - auth/permission case
6. Actualizar documentación mínima si aplica.

## Output format

### 1. Endpoint Summary
- propósito
- recurso
- impacto

### 2. Contract
- method
- path
- request
- response
- error cases

### 3. Implementation Notes
- dónde vive la lógica
- qué dependencias necesita

### 4. Validation Plan
- pruebas mínimas
- riesgos

## Rules

- no meter lógica de negocio pesada en el handler;
- no crear endpoints duplicados por conveniencia;
- cuidar compatibilidad con consumers existentes;
- si el sistema ya está en operación, revisar si conviene feature flag, versionado o rollout gradual.
