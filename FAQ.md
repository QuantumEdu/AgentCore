# FAQ - AgentCore

Preguntas frecuentes sobre instalación, migración y uso de AgentCore.

---

## Table of Contents

- [Installation](#installation)
- [Migration from v1.3](#migration-from-v13)
- [Project Setup](#project-setup)
- [OpenCode Integration](#opencode-configuration)
- [Common Scenarios](#common-scenarios)

---

## Installation

### How do I download AgentCore v2.0?

#### Option A: GitHub Template (Recommended)

1. Go to the repository and click "Use this template": https://github.com/QuantumEdu/AgentCore
2. Create a new repository from the template
3. Clone your new repository:

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPO.git
cd YOUR-REPO
```

#### Option B: Direct Clone (For Testing)

```bash
git clone https://github.com/QuantumEdu/AgentCore.git
cd AgentCore
```

#### Option C: Copy Only .claude/ to Existing Project

```bash
# In your existing project
cd YOUR-PROJECT

# Copy .claude/ structure
cp -r /path/to/AgentCore/.claude .
```

---

## Migration from v1.3

### I have v1.3, how do I migrate to v2.0?

#### Case A: Want to Migrate to v2.0

```bash
# 1. Backup your current version
git tag v1.3-backup
git push origin v1.3-backup

# 2. Pull v2.0
git pull origin main

# 3. Migrate stack_config.json to stack_config.yml
# - Format changed from JSON to YAML
# - Now supports multiple stacks
# - Review CHANGELOG.md for details

# 4. Create your PROJECT-BRIEF-FULL.yaml
cp .claude/templates/PROJECT-BRIEF-FULL.yaml .claude/PROJECT-BRIEF-FULL.yaml
# Edit it with your configuration

# 5. Select your stack
python .claude/scripts/stack_selector.py

# 6. Generate PRD + config
# Use the brief-to-prd skill
```

#### Important Changes v1.3 → v2.0

| Aspect | v1.3 | v2.0 | Action |
|--------|------|------|--------|
| `stack_config.json` | JSON (FastAPI only) | `stack_config.yml` (multi-stack) | Migrate to YAML |
| `decision_log.json` | JSON | `decision_log.md` (ADR) | Convert or recreate |
| Brief Files | None | `PROJECT-BRIEF-FULL.yaml` | Create new |
| Skills | None | `.agent/skills/` | New system |
| Outputs | None | `.claude/outputs/` | New directory |

#### Case B: Want to Keep v1.3

```bash
# Do nothing
# Your version continues to work as before
# v1.3-final tag is preserved on GitHub
```

---

## Project Setup

### Scenario A: New Project (From Scratch)

```bash
# 1. Create project with AgentCore structure
python .claude/scripts/init_project.py /path/to/new-project

# 2. The script creates:
# - .claude/ (complete structure)
# - app/, tests/, docs/ (base directories)
# - PROJECT-BRIEF-FULL.yaml (initial)
# - .gitignore (configured)

# 3. Configure and start
cd new-project
# Edit .claude/templates/PROJECT-BRIEF-FULL.yaml
# Run stack_selector.py
# Use brief-to-prd skill
```

### Scenario B: Existing Project (Integrate AgentCore)

```bash
# 1. Copy .claude/ to your project
cd YOUR-EXISTING-PROJECT
cp -r /path/to/AgentCore/.claude .

# 2. Copy .agent/skills/ (optional, for OpenCode)
cp -r /path/to/AgentCore/.agent/skills .

# 3. Configure for your project
# a) Edit .claude/stack_config.yml with your actual stack
# b) Create PROJECT-BRIEF-FULL.yaml with your context
# c) Adjust .claude/rules/ if you need specific rules

# 4. Agents will automatically read:
# - .claude/stack_config.yml
# - .claude/rules/
# - .claude/stacks/{your-stack}/
```

### Scenario C: Only Use Skills with OpenCode

```bash
# 1. Install skills globally
cp -r /path/to/AgentCore/.agent/skills/* ~/.config/opencode/skills/

# 2. Configure opencode.json
cat > opencode.json << EOF
{
  "permission": {
    "skill": {
      "*": "allow"
    }
  }
}
EOF

# 3. Use in any project
cd ANY-PROJECT
opencode
# Inside opencode, use /skill brief-to-prd
```

---

## OpenCode Configuration

### How do I use AgentCore with OpenCode?

AgentCore is already compatible with OpenCode. The `.agent/skills/` structure follows OpenCode's skill format.

#### Step 1: Install Skills Globally

```bash
# From AgentCore directory
cp -r .agent/skills/* ~/.config/opencode/skills/
```

#### Step 2: Configure Permissions

Create or edit `opencode.json` in your project root:

```json
{
  "permission": {
    "skill": {
      "*": "allow",
      "brief-to-prd": "allow",
      "stack-generator": "allow"
    }
  }
}
```

#### Step 3: Use in OpenCode

```bash
cd YOUR-PROJECT
opencode
```

Inside OpenCode TUI, use commands like:
- `/skill brief-to-prd` - Generate PRD from Brief
- `/skill stack-generator` - Generate stack config

#### Step 4: Project-Local Skills (Alternative)

If you want skills to be project-specific, AgentCore already has them in the right location:

```bash
# No action needed
# OpenCode automatically discovers .agent/skills/
```

---

## Common Scenarios

### Impact Summary

| Situation | Impact | Recommended Action |
|-----------|--------|-------------------|
| New machine, nothing installed | None | Use GitHub Template |
| Have v1.3, want v2.0 | Medium | Migrate (see CHANGELOG.md) |
| Have v1.3, keep it | None | Do nothing |
| Existing project without AgentCore | Low | Copy .claude/ and configure |
| Only use skills | Minimal | Install globally |

### Key Questions to Decide Your Approach

1. **Does your project already have a defined structure?**
   - Yes → Scenario B (integrate)
   - No → Scenario A (initialize)

2. **Do you use OpenCode?**
   - Yes → Copy .agent/skills/ globally
   - No → Only need .claude/

3. **Do you have stack_config.json from v1.3?**
   - Yes → You must migrate to YAML
   - No → You can create from scratch

4. **Is your project SaaS, Desktop, or API-only?**
   - Determines which stack to select (fastapi_ssr, fastapi_spa, etc.)

### What if I have a project that doesn't use any of this?

You have three options:

#### Option 1: Start Fresh (Recommended for New Projects)

```bash
python .claude/scripts/init_project.py /path/to/new-project
```

This creates a complete AgentCore-ready project structure.

#### Option 2: Integrate into Existing Project

```bash
cd YOUR-EXISTING-PROJECT
cp -r /path/to/AgentCore/.claude .
# Configure stack_config.yml for your stack
# Create PROJECT-BRIEF-FULL.yaml
```

Agents will start using AgentCore's rules and configurations automatically.

#### Option 3: Use Skills Only

```bash
cp -r /path/to/AgentCore/.agent/skills/* ~/.config/opencode/skills/
```

Use skills in any project with OpenCode, without full AgentCore structure.

---

## Troubleshooting

### Skills Not Showing in OpenCode

1. Verify `SKILL.md` is spelled in ALL CAPS
2. Check that frontmatter includes `name` and `description`
3. Ensure skill names are unique across all locations
4. Check permissions—skills with `deny` are hidden from agents

### Migration Issues from v1.3

- **stack_config.json format error**: Convert to YAML using the format in CHANGELOG.md
- **Missing brief**: Copy `.claude/templates/PROJECT-BRIEF-FULL.yaml` and fill it out
- **Stack not detected**: Ensure `stack_principal` in PROJECT-BRIEF-FULL.yaml is one of: `nextjs15`, `go_wails`, `fastapi_ssr`, `fastapi_spa`, `fastapi_desktop`

### Permission Denied on Scripts

```bash
# On Linux/Mac
chmod +x .claude/scripts/*.py

# On Windows (PowerShell)
# Scripts should run without issues
```

---

## Additional Resources

- [CHANGELOG.md](./CHANGELOG.md) - Detailed migration guide and version history
- [ARCHITECTURE.md](./.claude/ARCHITECTURE.md) - Complete architecture documentation
- [README.md](./README.md) - Project overview and quick start
- [OpenCode Skills Docs](https://opencode.ai/docs/skills/) - Skills system documentation

---

## Support

- GitHub Issues: https://github.com/QuantumEdu/AgentCore/issues
- Documentation: See files in `.claude/docs/`

---

*AgentCore v2.0 - Last Updated: 2026-04-12*
