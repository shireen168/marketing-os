# Marketing-OS for Power Users: Technical Architecture

This guide is for developers, architects, and Claude Code practitioners who want to understand how Marketing-OS is built, why it works, and how to replicate it for any domain.

## What You'll Learn

1. **SCEO Framework** (methodology, not tools)
2. **Claude Code Architecture** (how the system runs)
3. **Skill Building Patterns** (how to create reusable workflows)
4. **Project Structure** (organizing work for Claude Code)
5. **Session Discipline** (planning, verification, automation)
6. **Anti-Patterns** (what NOT to do)

---

## Core Concept: Methodology + Engine

```
SCEO Framework (Methodology)
       +
Claude Code (Engine)
       =
Systematic Operations (Reality)
```

The SCEO framework is methodology. Claude Code is the engine that operationalizes it. Together, they eliminate manual chaos while maintaining consistency and scale.

---

## The SCEO Framework

**S: Strategic Discovery** - Understand your landscape  
Market research, competitive analysis, trend identification, audience mapping

**C: Creative Planning** - Design your approach  
Brand positioning, content strategy, campaign planning, copywriting

**E: Execution** - Build and ship  
Content creation, automation, scheduling, publishing

**O: Optimization** - Measure and iterate  
Analytics, testing, conversion optimization, strategy refinement

The order matters: Discovery informs Planning informs Execution informs Optimization.

---

## Claude Code Architecture

Marketing-OS uses three Claude Code primitives:

### 1. Skills (Reusable Workflows)
22 skills organized by SCEO layer. Each skill:
- Solves one job (not everything)
- Is under 200 lines of documentation
- Includes examples for both domain-specific AND generic use cases
- Runs via slash command or scheduled agent

**Location:** `.claude/skills/content-and-marketing/` organized by S/C/E/O layer

### 2. Context Files (Persistent State)
Session state, decisions, priorities, and project structure live in files:
- `context/current-priorities.md` (weekly focus)
- `decisions/log.md` (meaningful decisions, append-only)
- `projects/<name>/tasks/todo.md` (progress tracking)
- `projects/<name>/tasks/lessons.md` (lessons learned)

**Why:** Git-based state is queryable, reviewable, and auditable. No lost context.

### 3. Session Workflows (/standup, /wrap, hooks)
Three integrated workflows keep context fresh:

**`/standup`** - Entry point
- Reads priorities, last session, recent logs
- Generates morning brief + recommendations

**`/wrap`** - Exit point
- Logs session, updates context files
- Commits meaningful work, pushes to GitHub
- Syncs knowledge base (Obsidian)

**Automation hooks** - Background context management
- `on_conversation_start`: Load context automatically
- `on_memory_update`: Keep memory fresh
- `before_tool_use`: Validate context before acting

---

## Skill Building Patterns

All 22 Marketing-OS skills follow this pattern:

```
SKILL.md (single file under 200 lines)
├── Trigger (when to use this skill)
├── Purpose (what it accomplishes)
├── How it works (step-by-step)
├── Domain example (marketing use case)
├── Generic example (applies to any domain)
├── Integration notes (how to compose with other skills)
└── Output format (what it returns)
```

### Examples

**Skill:** `/video-gen`  
Purpose: Generate video scripts and Gemini Gem prompts  
Examples: Sunny Homemade reel idea + generic product launch video

**Skill:** `/analytics-dashboard`  
Purpose: Weekly metrics summary from raw data  
Examples: Sunny Homemade engagement trends + generic SaaS metrics

---

## Project Structure for Claude Code

```
marketing-os/
├── README.md (choose your path)
├── beginner/ (marketing focus)
├── power-user/ (technical focus)
├── reference/ (shared across both)
├── .claude/
│   ├── skills/ (22 reusable workflows by SCEO)
│   └── SKILLS-BUILDING-TEMPLATE.md (how to build new skills)
└── projects/sunny-homemade/ (working example)
```

**Key principles:**
- Beginner path: marketing language, no technical depth
- Power user path: Claude Code patterns, architectural decisions
- Skills: organized by layer (S/C/E/O), not alphabetical
- Projects: real working examples with full context

---

## Session Discipline: Planning → Execution → Verification

### 1. Planning Phase
- Use `/brainstorming` skill to explore the problem
- Use `/planning` skill to design the solution
- Document assumptions and constraints
- Get alignment before coding

### 2. Execution Phase
- Build vertically: one feature end-to-end, not partial work
- Keep files under 200 lines (split when needed)
- Commit frequently with meaningful messages
- Track progress in `tasks/todo.md`

### 3. Verification Phase
- **Never claim work is done without testing in browser**
- Use `/verification` skill before completion
- Check both golden path AND edge cases
- Update lessons.md with any surprises

---

## Technical Documentation

Deep dives into:
- [CLAUDE-CODE-PATTERNS.md](CLAUDE-CODE-PATTERNS.md) - Skill architecture, composition patterns
- [PROJECT-ARCHITECTURE.md](PROJECT-ARCHITECTURE.md) - Folder structure, context files, state management
- [SESSION-DISCIPLINE.md](SESSION-DISCIPLINE.md) - Planning, execution, verification workflows
- [SKILLS-REFERENCE.md](../reference/SCEO-SKILL-REFERENCE.md) - All 22 skills by layer
- [WORKFLOWS.md](WORKFLOWS.md) - /standup, /wrap, hooks, automation
- [CONFIGURATION.md](CONFIGURATION.md) - Settings, env vars, advanced setup
- [ANTI-PATTERNS.md](ANTI-PATTERNS.md) - What NOT to do and why

---

## Replicating Marketing-OS for Another Domain

The pattern is domain-agnostic. To build an OS for Sales, HR, Finance, or Operations:

1. **Define 4 layers** (S/C/E/O applies everywhere)
   - S: Research, competitive analysis, strategy
   - C: Plan, design, positioning
   - E: Build, execute, deliver
   - O: Measure, learn, iterate

2. **Identify 5-8 core skills** per layer
   - Sales-OS might have: prospecting, pitch generation, deal tracking, email sequencing
   - HR-OS might have: job posting, candidate screening, interview prep, onboarding

3. **Structure the repo** (same folder pattern)
   - Beginner path (domain language)
   - Power user path (Claude Code patterns)
   - Reference (shared)
   - Skills (organized by layer)
   - Projects (working examples)

4. **Document with examples** (both domain + generic)
   - Every skill has Sunny Homemade example AND generic example
   - Every pattern shows how to adapt for your domain

---

## Next Steps

1. **Understand the framework:** Read [CLAUDE-CODE-PATTERNS.md](CLAUDE-CODE-PATTERNS.md)
2. **Explore skills:** Browse [SCEO-SKILL-REFERENCE.md](../reference/SCEO-SKILL-REFERENCE.md)
3. **See it in action:** Check [Sunny Homemade project](../projects/sunny-homemade/)
4. **Build your own:** Use the [SKILLS-BUILDING-TEMPLATE.md](../.claude/SKILLS-BUILDING-TEMPLATE.md)

Questions? See [FAQ](FAQ.md) or [ANTI-PATTERNS.md](ANTI-PATTERNS.md).
