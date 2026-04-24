# v2.0 Design Documentation

This directory contains historical design documents from AgentCore v2.0 development.

## Purpose

These files are **reference documentation** of the PRD generation process. They show how the PRD skills were structured before being integrated into the multi-stack system.

## Files

- `prd-fastapi_skill.md` - Historical PRD generator for FastAPI stack (605 lines)
- `prd-go-wails_skill.md` - Historical PRD generator for Go+Wails stack
- `prd-nextjs15_skill.md` - Historical PRD generator for Next.js 15 stack

## Current Implementation

The current AgentCore v2.0 uses a **unified approach**:

1. **Single skill**: `brief-to-prd` (`.agent/skills/brief-to-prd/SKILL.md`)
2. **Stack-specific templates**: `.claude/stacks/{stack}/prd_skill.md`
3. **Interactive generation**: Detects stack from Brief automatically
4. **Output**: `.claude/outputs/PRD_{name}_{stack}.md`

## Why Keep These Files?

These files are kept for:
- Historical reference of the design process
- Understanding the evolution from single-stack to multi-stack
- Potential reuse of specific sections if needed

## Do NOT Use These Files

- **Do not** use these files directly in production
- **Do not** copy these patterns to new stacks
- **Use** the `brief-to-prd` skill instead
- **Use** the stack-specific templates in `.claude/stacks/`

---

*AgentCore v2.0 - 2026-04-12*
