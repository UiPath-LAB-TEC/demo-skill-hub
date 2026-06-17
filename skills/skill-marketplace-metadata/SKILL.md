---
name: skill-marketplace-metadata
description: "Add or refresh Enterprise AI & Automation Marketplace metadata in Codex skill SKILL.md files. Use when creating a new skill, updating an existing skill, preparing a skill for marketplace publishing, or checking frontmatter fields such as metadata.version, ownerEmail, changeSummary, dependencies, category, and platforms."
metadata:
  author: "James Dickson"
  version: "1.0.0"
  ownerEmail: "jms.dcksn88@gmail.com"
  changeSummary: "Initial marketplace metadata authoring guidance."
  isBreaking: false
  category: "Sales Engineering"
  tags:
    - skills
    - marketplace
    - metadata
  platforms:
    - OpenAI
  businessUseCases:
    - "Prepare skills for marketplace validation"
---

# Skill Marketplace Metadata

Use this skill to make a skill's `SKILL.md` frontmatter valid for the Enterprise AI & Automation Marketplace while preserving good Codex trigger metadata. Treat `skills/SKILL_MD_SCHEMA.md` as the source of truth when it exists in the repo; if it differs from this guidance, follow the schema file.

## Workflow

1. Inspect the target skill.
   - Read the current `SKILL.md`, adjacent `agents/openai.yaml` if present, and any repo publishing instructions.
   - If publishing is expected, verify the skill is in a pipeline-discovered path such as `plugins/<plugin>/skills/<skill-name>/`; metadata alone does not make an arbitrary folder publishable.

2. Preserve top-level skill identity.
   - Keep `name` concise and unique.
   - Keep `description` as the trigger surface: include what the skill does and when to use it.
   - Use `draft: true` only while intentionally excluding the skill from validation and deployment.

3. Add or update the required `metadata:` block.
   - `author`: owning person or team.
   - `version`: semver `X.Y.Z`; increment on every re-publish.
   - `ownerEmail`: notification address for validation and approval.
   - `changeSummary`: human-readable summary for this version.
   - `isBreaking`: boolean `true` or `false`, never a string.

4. Add optional fields only when they add useful marketplace context.
   - `featured`: boolean.
   - `category`: one canonical value from the list below.
   - `documentationUrl`: documentation link.
   - `tags`: search keywords.
   - `platforms`: target platforms; canonical values are preferred but additional platform names are allowed.
   - `businessUseCases`: user-facing use cases.
   - `dependencies`: required marketplace assets.

5. Update versions deliberately.
   - Increment `metadata.version` whenever republishing changed content.
   - Update `changeSummary` for the new version.
   - Set `isBreaking: true` only when consumers must change because inputs, outputs, behavior, or supported features changed incompatibly.
   - Do not reuse an already approved `name` + `version` pair.

6. Validate before finishing.
   - Parse the frontmatter as YAML.
   - Confirm required fields exist and booleans are booleans.
   - Confirm `metadata.version` matches `X.Y.Z`.
   - Confirm `metadata.category`, if present, matches a canonical value exactly.
   - Confirm every dependency has `name`, `version`, and integer `type` of `9`, `10`, `11`, or `12`.
   - Run any repo or pipeline validator available for `SKILL.md` files.

## Valid Values

`metadata.category` must be one of:

- `General`
- `Design/Brand`
- `Productivity`
- `Marketing`
- `Sales Engineering`
- `Sales`
- `Post-sales`
- `Corporate`
- `P&E`

Canonical `metadata.platforms` values:

- `UiPath Delegate`
- `Claude`
- `OpenAI`
- `Gemini`
- `UiPath Automations`

Dependency `type` values:

- `9`: AI Skills
- `10`: AI Tool Prompts
- `11`: Apps
- `12`: UiPath Automations

Asset type, icon, owner display name, source repository URL, bucket path, dates, and status are auto-derived by the pipeline. Do not set them in `SKILL.md`.

## Frontmatter Pattern

```yaml
---
name: skill-name
description: "What the skill does. Use when ..."
metadata:
  author: "Owning Team"
  version: "1.0.0"
  ownerEmail: "owner@example.com"
  changeSummary: "Initial marketplace metadata."
  isBreaking: false
  category: "General"
  tags:
    - skill
  platforms:
    - OpenAI
  businessUseCases:
    - "Prepare reusable agent behavior"
  dependencies:
    - name: "Required Asset"
      version: "1.0.0"
      type: 9
---
```

Omit optional fields when they are not known or not useful. Do not invent dependency records; use exact marketplace asset names when dependencies are real.
