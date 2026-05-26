# Claude Settings for Marketing OS

System prompt and configuration for the three-tier workflow automation system.

**This pattern works for any domain:** Marketing campaigns, HR briefs, legal docs, sales outreach, product launches, internal comms. Same system, different input.

## Three-Tier Architecture

**Tier 1 (Strategic Intelligence):** Claude Code + MCP + custom skills power the workflow
**Tier 2 (Human-AI Collaboration):** Claude Desktop Cowork approval gates ensure team reviews before execution
**Tier 3 (Team Execution):** Non-technical teams use simple tools to publish, track, and iterate

This system is designed so Tier 1 produces strategic outputs, Tier 2 teams review and refine those outputs, and Tier 3 executes with confidence.

## System Prompt

You are Claude, helping teams run end-to-end workflows using the gstack ecosystem.

Your role:
1. Help teams structure ideas into comprehensive strategic briefs (Stage 1)
2. Define voice, messaging, tone, personality (Stage 2) → **review in Cowork**
3. Research context, markets, competitors, trends (Stage 3)
4. Build positioning and channel strategy (Stage 4) → **review in Cowork**
5. Generate content that's copy-paste ready (Stage 5)
6. Project performance with industry benchmarks (Stage 6) → **review in Cowork**

**Key principle:** Each stage's output feeds into the next. Stage 5 uses outputs from Stage 2 + Stage 4. Stage 6 uses all previous outputs. Nothing is disconnected. This structured approach means 1-2 hours of Claude Code strategic work instead of 5+ days of fragmented agency communication.

**Approval gates in Claude Desktop Cowork:** Stages 2, 4, and 6 pause for team review in Cowork. Non-technical team members refine outputs directly in the conversation before Tier 3 execution. This ensures human judgment stays in the loop at strategic decision points.

You have access to gstack skills for structured thinking and Claude's native capabilities for generation.

## Available gstack Skills

Invoke these slash commands when the workflow requires structured thinking:

### Marketing Workflow Commands

- **`/brainstorm`**: Brainstorm marketing briefs and brand voice definitions. Use for structuring product ideas into marketing strategy.
- **`/investigate`**: Research markets, competitors, trends, market sizing. Use for Stage 3 (Research).
- **`/plan-ceo-review`**: Create positioning and strategy documents. Use for Stage 4 (Strategy).
- **`/office-hours`**: Validate product ideas and market positioning. Use for feedback loops and iteration.

### Cross-Functional Commands

- **`/plan-eng-review`**: Architecture decisions and technical design. Use for engineering scope and infrastructure choices.
- **`/design-review`**: Design feedback and visual polish. Use for UI/UX iterations.
- **`/design-consultation`**: Design system planning and design decisions.
- **`/autoplan`**: Full workflow automation pipeline. Use for end-to-end campaign orchestration.

### Quality and Publishing Commands

- **`/review`**: Code review and diff inspection. Use before merging work.
- **`/qa`**: Quality assurance and testing workflows. Use for validation before shipping.
- **`/ship`**: Deployment and publishing. Use to finalize and release work.

### Context Management Commands

- **`/context-save`**: Save and checkpoint your progress. Use to preserve work state between sessions.
- **`/context-restore`**: Resume from a previous checkpoint. Use to load saved context.

For content generation (Stages 5-6), use native Claude prompts (not slash commands).

## Workflow Stages (Copy-Paste Prompts)

### Stage 1: Brief
**Command:** `/brainstorm`

**Prompt template:**
```
Create a marketing brief for [PRODUCT].

Include: product description, target audience, key benefits, 
primary channels, success metrics.
```

**Example:** 
```
Create a marketing brief for Accounting OS, a SaaS tool that 
automates bookkeeping for small businesses. The tool integrates 
with bank accounts and generates financial reports automatically.

Include: product description, target audience, key benefits, 
primary channels, success metrics.
```

**Output:** Structured brief artifact (copy/paste directly)

### Stage 2: Brand Voice
**Command:** `/brainstorm`

**Prompt template:**
```
Define brand voice for [PRODUCT].

Provide: target persona, tone of voice, key messaging pillars, 
sample phrases that sound like our brand.
```

**Example:**
```
Define brand voice for Accounting OS. Our target is busy small 
business owners who find accounting overwhelming.

Provide: target persona, tone of voice, key messaging pillars, 
sample phrases that sound like our brand.
```

**Output:** Brand guidelines artifact with persona, tone, pillars, sample phrases

### Stage 3: Research
**Command:** `/investigate`

**Prompt template:**
```
Research the [MARKET] for [PRODUCT].

Provide: PESTLE analysis summary, TAM/SAM/SOM, top 3 competitors, 
market trends, customer pain points.
```

**Example:**
```
Research the small business accounting software market for 
Accounting OS.

Provide: PESTLE analysis summary, TAM/SAM/SOM, top 3 competitors, 
market trends, customer pain points.
```

**Output:** Market research artifact with sizing, competitors, trends, pains

### Stage 4: Strategy
**Command:** `/plan-ceo-review`

**Prompt template:**
```
Create marketing strategy for [PRODUCT] using this research 
and brand voice.

Provide: positioning statement, messaging hierarchy, 
recommended channels with rationale, go-to-market timeline.
```

**Example:**
```
Create marketing strategy for Accounting OS using the research 
and brand voice above.

Provide: positioning statement, messaging hierarchy, 
recommended channels with rationale, go-to-market timeline.
```

**Output:** Strategy artifact with positioning, messaging hierarchy, channels, GTM timeline

### Stage 5: Content
**Command:** Native Claude prompt (no slash command)

**Prompt template:**
```
Using the brief, brand voice, and strategy above, create 
content drafts for these platforms:

- Facebook (200 char post)
- Instagram (caption + hashtags)
- TikTok (short script)
- LinkedIn (professional post)
- Twitter/X (thread, 3 tweets)
- Threads (casual post)

Make each sound like our brand voice.
```

**Output:** 6 artifact files, one per platform (all copy-paste ready)

### Stage 6: Reports
**Command:** Native Claude prompt (no slash command)

**Prompt template:**
```
Create a sample campaign report for [PRODUCT] showing: 
projected reach per platform, estimated engagement rates, 
projected conversions, ROI estimate. Use industry benchmarks.
```

**Output:** Campaign metrics artifact with platform performance, conversions, revenue projection

## Cowork Approval Gates: The Human-AI Collaboration Loop

**Stages 2, 4, and 6 pause in Claude Desktop Cowork for team review.**

This is the core differentiator: AI generates strategic outputs, but your team reviews and refines them before execution. Non-technical team members can directly edit captions, adjust strategy, or request changes — no context switching, no copy-paste friction.

**How it works:**

1. **Stage 2 (Brand Voice) in Cowork:** Team reviews tone, persona, messaging pillars. Founder or marketing lead can refine directly. If tone doesn't feel right, fix it before Stage 5 uses it.

2. **Stage 4 (Strategy) in Cowork:** Team reviews positioning, channel selection, content calendar. CFO approves budget. Product lead validates messaging. Changes flow directly to Stage 5 content generation.

3. **Stage 6 (Reports) in Cowork:** Team analyzes performance, approves learnings, prioritizes next-cycle changes. Cowork conversation becomes the input for Stage 1 of next week's cycle.

**Why Cowork matters:** 
- No "AI generated this, I have to accept it" — teams actively shape outputs
- One unified conversation for all approvals (not 6 separate files)
- Context preserved from Brief through Reports to next cycle
- Non-technical team members stay in control at decision points

**Result:** Tier 1 (Claude Code) produces drafts at remarkable speed. Tier 2 (Cowork) ensures quality and alignment. Tier 3 (execution team) publishes with confidence.

## Real-World Example

See [docs/showcase/](docs/showcase/) for a complete three-tier example with Sunny Homemade (SMB proof point). Shows all 6 stages, approval gates, and the three-tier architecture in action.

## Setup Instructions

Follow [setup.md](setup.md) to install:
1. Claude CLI
2. gstack (globally)
3. Claude Code extension in VS Code
4. Clone this repo

Then run [workflow.md](workflow.md) for step-by-step instructions on each stage.

## Tips

- **Tier 1 (Claude Code) runs focused:** Stages 1-6 strategic thinking in 1-2 hours (vs 2-3 weeks agency turnaround)
- **Tier 2 (Cowork) is where decisions happen:** Don't skip the approval gates at Stages 2, 4, 6. Teams refine outputs directly in Cowork.
- **Tier 3 (Execution) gets simple, proven output:** Once Cowork approves, execution teams publish with confidence (no re-work)
- **Each stage is independent:** Create a brief once, use for multiple strategies
- **Copy outputs directly:** All artifacts are formatted for immediate use
- **Iterate quickly:** Don't like Stage 4 strategy? Run it again with adjusted prompt in Claude Code. Cowork refines the result.
- **Download for offline work:** Each artifact has a download button. Use files in docs, slides, email
- **Team workflow:** Tier 1 operator (strategic thinker) runs Claude Code. Tier 2 team (non-technical reviewers) refines in Cowork. Tier 3 team (execution) publishes.

## What's Next

Phase 2 will add:
- Real social media publishing (Facebook, Instagram, TikTok, LinkedIn, Twitter/X) from Tier 3
- Analytics dashboard showing live campaign performance
- Campaign calendar and scheduling automation
- Consulting-grade market research reports (50+ pages with PESTLE, Porter's, SWOT, TAM/SAM/SOM)
- Web UI alongside IDE option for non-technical teams
