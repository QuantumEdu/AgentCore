# Quick Start by Scenario

## Purpose

Guía rápida para saber qué usar según la situación real del proyecto.

Si necesitas la vista estructural por tipo de cambio y skills obligatorias/opcionales, ver `04-workflow-map.md`.

---

## 1. Quiero arrancar un proyecto desde cero

Si el proyecto es pequeño o exploratorio, puedes empezar con `PROJECT-BRIEF-LITE.yaml`.
Si es más serio, sensible o complejo, usa `PROJECT-BRIEF-FULL.yaml`.

Usa este orden:

1. `brief-inception`
2. `project-stack-decider` *(si el stack no está claro)*
3. `brief-to-prd`
4. `prd-to-spec`
5. `spec-to-tasks`

Si quieres un agente:
- `project-inception-architect`

Resultado esperado:
- brief claro
- PRD corto
- spec
- tareas ejecutables

---

## 2. Tengo una idea, pero está difusa

Empieza con:

1. `brief-inception`
2. `geek-tech-tone` *(si quieres una respuesta más afilada y estratégica)*
3. `brief-to-prd`

Si además falta dirección técnica:
- `project-stack-decider`

---

## 3. Ya tengo un PRD y quiero pasar a implementación

Usa:

1. `prd-to-spec`
2. `spec-to-tasks`

Si el cambio es sensible:
3. `change-review`

Resultado esperado:
- spec verificable
- tareas pequeñas y ordenadas

---

## 4. Quiero agregar un endpoint nuevo

Usa:

1. `add-endpoint`
2. `change-review`

Si el endpoint cambia contrato o comportamiento en producción:
3. `rule-migration-plan`

Si quieres un agente:
- `endpoint-designer`

---

## 5. Tengo un sistema existente y quiero cambiar una regla sin romper producción

Usa:

1. `rule-migration-plan`
2. `change-review`

Después del cambio:
3. `local-retrospective`

Si quieres un agente:
- `migration-guardian`

Resultado esperado:
- blast radius claro
- rollout seguro
- rollback definido
- criterio para retirar la regla vieja

---

## 6. Algo está fallando repetidamente

Usa:

1. `improvement-loop`
2. `local-retrospective`

Si no hay Engram:
3. `project-memory-fallback`

Resultado esperado:
- causa raíz más clara
- mejora concreta
- regla o checklist nueva si aplica

---

## 7. No tengo Engram o necesito continuidad local

Usa:

1. `project-memory-fallback`

Archivos clave:
- `/ai/context/decisions.md`
- `/ai/context/pitfalls.md`
- `/ai/context/working-memory.md`

---

## 8. Quiero revisar un cambio antes de integrarlo

Usa:

1. `change-review`

Si quieres un agente:
- `change-reviewer`

Útil para:
- cambios riesgosos
- cambios de reglas
- cambios de contratos
- cambios en sistemas en operación

---

## 9. Quiero aprender de un cambio ya terminado

Usa:

1. `local-retrospective`
2. `improvement-loop` *(si detectas fricción repetida)*

Resultado esperado:
- lección práctica
- ajuste pequeño pero útil al flujo

---

## 10. Quiero mejorar un prompt

Usa:

1. `prompt-improver`

Si quieres tono más técnico/geek:
2. `geek-tech-tone`

---

## Fast routing

- idea difusa → `brief-inception`
- stack incierto → `project-stack-decider`
- brief a PRD → `brief-to-prd`
- PRD a spec → `prd-to-spec`
- spec a tareas → `spec-to-tasks`
- endpoint nuevo → `add-endpoint`
- cambio riesgoso → `change-review`
- migración de regla en producción → `rule-migration-plan`
- error repetido → `improvement-loop`
- continuidad sin Engram → `project-memory-fallback`
- retrospectiva → `local-retrospective`

## Rule of thumb

Si el problema es pequeño, usa una o dos skills.
Si el cambio es grande o riesgoso, sigue la cadena completa.
