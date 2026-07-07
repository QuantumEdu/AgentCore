# Quick Start by Scenario

## Purpose

Guía rápida para saber qué usar según la situación real del proyecto.

Si necesitas la vista estructural por tipo de cambio y skills obligatorias/opcionales, ver `04-workflow-map.md`.

---

## 1. Quiero arrancar un proyecto desde cero

Si el proyecto es pequeño o exploratorio, puedes empezar con `PROJECT-BRIEF-LITE.yaml`.
Si es más serio, sensible o complejo, usa `PROJECT-BRIEF-FULL.yaml`.

Usa este orden:

1. `sdd-govp:brief-inception`
2. `sdd-govp:project-stack-decider` *(si el stack no está claro)*
3. `sdd-govp:brief-to-prd`
4. `sdd-govp:prd-to-spec`
5. `sdd-govp:spec-to-tasks`

Si quieres un agente:
- `sdd-govp:project-inception-architect`

Resultado esperado:
- brief claro
- PRD corto
- spec
- tareas ejecutables

---

## 2. Tengo una idea, pero está difusa

Empieza con:

1. `sdd-govp:brief-inception`
2. `sdd-govp:geek-tech-tone` *(si quieres una respuesta más afilada y estratégica)*
3. `sdd-govp:brief-to-prd`

Si además falta dirección técnica:
- `sdd-govp:project-stack-decider`

---

## 3. Ya tengo un PRD y quiero pasar a implementación

Usa:

1. `sdd-govp:prd-to-spec`
2. `sdd-govp:spec-to-tasks`

Si el cambio es sensible:
3. `sdd-govp:change-review`

Resultado esperado:
- spec verificable
- tareas pequeñas y ordenadas

---

## 4. Quiero agregar un endpoint nuevo

Usa:

1. `sdd-govp:add-endpoint`
2. `sdd-govp:change-review`

Si el endpoint cambia contrato o comportamiento en producción:
3. `sdd-govp:rule-migration-plan`

Si quieres un agente:
- `sdd-govp:endpoint-designer`

---

## 5. Tengo un sistema existente y quiero cambiar una regla sin romper producción

Usa:

1. `sdd-govp:rule-migration-plan`
2. `sdd-govp:change-review`

Después del cambio:
3. `sdd-govp:local-retrospective`

Si quieres un agente:
- `sdd-govp:migration-guardian`

Resultado esperado:
- blast radius claro
- rollout seguro
- rollback definido
- criterio para retirar la regla vieja

---

## 6. Algo está fallando repetidamente

Usa:

1. `sdd-govp:improvement-loop`
2. `sdd-govp:local-retrospective`

Si no hay Engram:
3. `sdd-govp:project-memory-fallback`

Resultado esperado:
- causa raíz más clara
- mejora concreta
- regla o checklist nueva si aplica

---

## 7. No tengo Engram o necesito continuidad local

Usa:

1. `sdd-govp:project-memory-fallback`

Archivos clave:
- `/ai/context/decisions.md`
- `/ai/context/pitfalls.md`
- `/ai/context/working-memory.md`

---

## 8. Quiero revisar un cambio antes de integrarlo

Usa:

1. `sdd-govp:change-review`

Si quieres un agente:
- `sdd-govp:change-reviewer`

Útil para:
- cambios riesgosos
- cambios de reglas
- cambios de contratos
- cambios en sistemas en operación

---

## 9. Quiero aprender de un cambio ya terminado

Usa:

1. `sdd-govp:local-retrospective`
2. `sdd-govp:improvement-loop` *(si detectas fricción repetida)*

Resultado esperado:
- lección práctica
- ajuste pequeño pero útil al flujo

---

## 10. Quiero mejorar un prompt

Usa:

1. `sdd-govp:prompt-improver`

Si quieres tono más técnico/geek:
2. `sdd-govp:geek-tech-tone`

---

## Fast routing

- idea difusa → `sdd-govp:brief-inception`
- stack incierto → `sdd-govp:project-stack-decider`
- brief a PRD → `sdd-govp:brief-to-prd`
- PRD a spec → `sdd-govp:prd-to-spec`
- spec a tareas → `sdd-govp:spec-to-tasks`
- endpoint nuevo → `sdd-govp:add-endpoint`
- cambio riesgoso → `sdd-govp:change-review`
- migración de regla en producción → `sdd-govp:rule-migration-plan`
- error repetido → `sdd-govp:improvement-loop`
- continuidad sin Engram → `sdd-govp:project-memory-fallback`
- retrospectiva → `sdd-govp:local-retrospective`

## Rule of thumb

Si el problema es pequeño, usa una o dos skills.
Si el cambio es grande o riesgoso, sigue la cadena completa.
