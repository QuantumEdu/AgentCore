# Migration Checklist

## Must Adapt

| Asset Type | What to adapt |
|------------|---------------|
| stack configuration | decisiones específicas del stack, runtime, librerías y módulos |
| decision records | decisiones técnicas reales del proyecto, no ejemplos heredados |
| roadmap and backlog | hitos, riesgos y prioridades del proyecto actual |
| guides and checks | nombres, dominio, restricciones y comandos reales |
| project brief | contexto de negocio, tipo de entrega, restricciones y alcance |

## Reusable With Review

| Asset | Review needed |
|-------|---------------|
| architecture rules | adaptar nombre de proyecto, dominio y módulos |
| database rules | adaptar tablas, relaciones y estrategia de datos |
| security rules | adaptar roles, permisos y restricciones |
| api rules | adaptar endpoints, contratos y ejemplos |
| testing rules | adaptar fixtures, módulos y ejemplos |

## Reusable As-Is

| Asset | Why |
|------|-----|
| brief schema | valida la estructura canónica del brief |
| brief template | sirve como entrada agnóstica de discovery |
| ADR template | patrón genérico de decisión |
| roadmap template | estructura reusable para fases |
| pattern references | hexagonal, SOLID, design patterns y testing patterns son portables |

## Migration Rule

Promover a `/ai` solo lo que ayude a un flujo más portable, claro y profesional.
Todo lo acoplado a un proyecto ejemplo, stack rígido o runtime legacy debe ir a respaldo externo o descartarse.
