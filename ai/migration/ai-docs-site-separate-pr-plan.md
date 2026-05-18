# AI Docs Site — Separate PR Plan

## Purpose

Definir cómo incorporar `ai-docs-site/` en una PR separada, sin mezclar documentación visual con la migración principal del sistema `/ai`.

## Why separate it

`ai-docs-site/` sí tiene valor real, pero representa una superficie nueva:

- agrega una experiencia visual/navegable;
- puede terminar como `docs/`, sitio estático o GitHub Pages;
- requiere validación de contenido, estructura y estrategia de publicación.

No debe entrar mezclado con una refactorización arquitectónica grande.

## What it is

Actualmente contiene:

- `index.html`
- `app.js`
- `styles.css`

Y documenta visualmente:

- qué es `/ai`;
- capas del sistema;
- governance;
- skills;
- templates;
- agents;
- contexto local;
- flujo canónico;
- relación con gentle-ai y SDD.

## Recommended PR goal

Crear una PR dedicada con objetivo claro, por ejemplo:

> `docs: add visual architecture site for /ai system`

## Recommended review checklist

- [ ] Confirmar si el sitio vivirá en `ai-docs-site/`, `docs/` o GitHub Pages
- [ ] Alinear el contenido con `README.md`, `ai/README.md`, `04-workflow-map.md` y `05-quick-start-by-scenario.md`
- [ ] Corregir referencias desactualizadas (por ejemplo, menciones de `pi` o rutas antiguas)
- [ ] Verificar que el sitio refleje la frontera correcta entre `gentle-ai`, `agent-core-v3` y `/ai`
- [ ] Decidir si será documentación interna del repo o artefacto público oficial

## Recommended technical adjustments before PR

- extraer textos canónicos desde docs fuente para evitar drift manual;
- revisar si el sitio necesita build step o puede quedar estático puro;
- agregar un README corto dentro de `ai-docs-site/` si se mantiene como carpeta independiente;
- decidir si conviene moverlo luego a `docs/`.

## Decision rule

Si el sitio se mantendrá como referencia visual oficial, debe tener:

- owner claro;
- fuente documental canónica;
- estrategia para evitar desalineación futura.

Si no se puede sostener eso, mejor dejarlo fuera del repo principal.
