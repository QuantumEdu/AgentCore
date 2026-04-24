# Changelog

**Note:** Historical log for the previous AgentCore layout. The `.agent/` and `.claude/` folders have been removed from this repo; the active system now lives in `/ai`.

All notable changes to AgentCore will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2026-04-12

### Added
- Multi-stack support (FastAPI, Next.js 15, Go+Wails)
- PROJECT-BRIEF-FULL.yaml with validation schema (brief-schema.json)
- Interactive skill `brief-to-prd` that generates PRD + stack_config.yml in ONE command
- Skill `stack-generator` that converts Brief to stack_config.yml
- `.agent/skills/` directory with generic skills
- `.claude/stacks/` directory with stack-specific configurations
  - `template.yaml` - Base template for new stacks
  - `registry.yaml` - Registry of all available stacks
  - `nextjs15/` - Next.js 15 stack configuration
  - `go-wails/` - Go + Wails stack configuration
  - `fastapi/` - FastAPI stack configuration (principal)
    - `config.yaml` - Complete configuration
    - `decisions.yaml` - Architecture decisions (ADR format)
    - `patterns.md` - Code patterns with examples
    - `modules/` - Reusable modules (auth, database, testing, frontend, hardware)
    - `substacks/` - 3 sub-stacks (SSR, SPA, Desktop)
  - `laravel/` - Laravel stack (extensibility example)
- `.claude/rules/patterns/` directory with reusable patterns
  - `hexagonal.md` - Hexagonal Architecture pattern
  - `solid.md` - SOLID principles with examples
  - `design-patterns.md` - 10 design patterns (Factory, Builder, Adapter, etc.)
  - `testing-patterns.md` - 12 testing patterns (AAA, Test Pyramid, etc.)
- `.claude/scripts/` directory with utility scripts
  - `init_project.py` - Initialize new project with AgentCore
  - `stack_selector.py` - Interactive stack selector
  - `project_brief_parser.py` - Parse and validate Brief
  - `decision_adr_converter.py` - Convert JSON decisions to ADR Markdown
- `.claude/templates/` directory with reusable templates
  - `PROJECT-BRIEF.md` - Brief template (simplified)
  - `decision_adr_template.md` - ADR template
  - `roadmap_template.md` - Roadmap template
- `improve01/outputs/` directory for generated PRDs
- `ARCHITECTURE.md` - Architecture documentation
- Complexity score calculation (1-10) based on project factors
- Optional sections dynamically applied based on complexity score
- Stack auto-detection from PROJECT-BRIEF-FULL.yaml

### Changed
- `stack_config.json` → `stack_config.yml` (dynamic, multi-stack)
- `decision_log.json` → `decision_log.md` (ADR Markdown format)
- Updated all agents for stack-aware validation (architect, backend-developer, security-expert)
- Updated all rules to reference patterns in `.claude/rules/patterns/`
- Updated `AGENT_GUIDE.md` with Skills Directory, Multi-Stack Support, Stack-Aware Validation
- Updated `MANDATORY_CHECKS.md` with stack verification
- Updated `PORTABILITY.md` with new files and stack configuration section
- Improved prd-fastapi_skill.md with 7 new sections (Domain Modeling, Modelo de Errores, etc.)
- Improved prd-nextjs15_skill.md with domain-specific enhancements
- Improved prd-go-wails_skill.md with domain-specific enhancements

### Fixed
- Multi-stack support now works correctly with dynamic stack_config.yml
- Brief validation with JSON schema (brief-schema.json)
- Stack consistency checks between config and brief
- All stacks now have consistent configuration structure

### Removed
- Temporary Qwen files from improve01/ (Qwen__*.txt, Qwen_markdown_*.md)
- Single-stack limitation (now supports 3+ stacks)

### Migration Guide

### From v1.3 to v2.0

1. **Backup your current version**:
   ```bash
   git tag v1.3-backup
   ```

2. **Update your repository**:
   ```bash
   git pull origin main
   ```

3. **Update your PROJECT-BRIEF**:
   - Convert your existing Brief to YAML format (use `PROJECT-BRIEF-FULL.yaml` as template)
   - Fill in the required fields

4. **Select your stack**:
   ```bash
   python .claude/scripts/stack_selector.py
   ```

5. **Generate PRD + config**:
   - Use the `brief-to-prd` skill
   - Or manually generate from your Brief

6. **Update your code**:
   - Review stack_config.yml for your selected stack
   - Update code to match new patterns and decisions
   - Run validators: `python .claude/validators/check_stack.py`

### Breaking Changes

- `stack_config.json` format changed to YAML (use `decision_adr_converter.py` to migrate)
- Decision log format changed from JSON to ADR Markdown (manual or use converter)
- Some directory structures have changed (review `.claude/stacks/{stack}/`)

### Upgrade Path

If you're using v1.3 with FastAPI (FlowTask):

1. Your existing stack_config.json is still valid as reference
2. Create a new PROJECT-BRIEF-FULL.yaml based on your project
3. Select the FastAPI stack that matches your setup (A, B, or C)
4. Generate new PRD and config
5. Gradually migrate your code to match new patterns

## [1.3.0] - 2026-04-05

### Added
- Stack configuration for FlowTask Inc. (FastAPI)
- Decision log with 6 architectural decisions
- Agent validation with stack verification
- Swarms for discovery, module creation, endpoint addition, testing

### Fixed
- Agent validation now checks for bcrypt vs argon2id
- Agent validation now checks for pip vs uv

## [1.2.0] - 2026-04-01

### Added
- Initial AgentCore structure
- FastAPI stack with SQLAlchemy 2.0
- Clean Architecture rules
- Testing rules with pytest
