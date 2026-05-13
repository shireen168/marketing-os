# Marketing OS: AI-Powered Marketing Operations System

**Position:** Complete end-to-end marketing operations system for teams. Use gstack + Claude to go from product idea to multi-platform content in 30 minutes.

---

## What This Demonstrates

As a hiring manager evaluates this project, you'll see:

1. **Architectural Capability**
   - Orchestrated 6-stage workflow using existing tools (gstack ecosystem, Claude API, VS Code IDE)
   - No custom infrastructure, no MCP servers to maintain
   - Self-contained on one laptop, runs locally with no deployment overhead

2. **Marketing Domain Expertise**
   - Research-backed strategy (market sizing, competitive landscape, customer pain points)
   - Brand voice and messaging hierarchy (personas, tone, pillars, sample copy)
   - Multi-platform content adapted per channel (Facebook, Instagram, TikTok, LinkedIn, Twitter/X, Threads)
   - Campaign performance projections using industry benchmarks

3. **Technical Judgment**
   - Leveraged gstack ecosystem instead of building custom infrastructure
   - Used Claude Code IDE (VS Code) for non-technical users instead of command line
   - Prioritized immediate productivity over architectural purity
   - Understood the trade-off: artifacts replace file I/O, slash commands replace custom APIs

4. **Scalability**
   - Works for a team of 1 (solo marketer) or 100 (distributed marketing org)
   - Setup once on a laptop, team runs workflows repeatedly
   - No external dependencies beyond Claude API key
   - Documented thoroughly so teams can operate independently

---

## System Architecture

```
TEAM SETUP (one-time, 15 minutes)
├─ Install Claude CLI
├─ Install gstack globally
├─ Install Claude Code extension in VS Code
└─ Clone marketing-os repo

TEAM WORKFLOW (recurring, 30 minutes per campaign)
├─ Stage 1: Brief
│  └─ /brainstorm → Structured marketing brief
├─ Stage 2: Brand Voice
│  └─ /brainstorm → Persona, tone, messaging pillars
├─ Stage 3: Research
│  └─ /investigate → Market sizing, competitors, trends
├─ Stage 4: Strategy
│  └─ /plan-ceo-review → Positioning, messaging hierarchy, channels
├─ Stage 5: Content
│  └─ Claude native prompt → 6 platform-specific artifacts
└─ Stage 6: Reports
   └─ Claude native prompt → Mock campaign metrics and ROI

OUTPUT ARTIFACTS
├─ Brief (structured, JSON-like)
├─ Brand Voice (copy-paste guidelines)
├─ Research Summary (market data, competitor analysis)
├─ Strategy Document (positioning, go-to-market plan)
├─ Content Drafts (Facebook, Instagram, TikTok, LinkedIn, X, Threads)
└─ Campaign Report (projected reach, engagement, conversions, revenue)

All outputs render as native Claude artifacts in VS Code Claude Code panel.
Team downloads and uses directly in docs, slides, email, presentations.
```

---

## How Your Team Uses It

### Setup (15 minutes, once per laptop)

Follow [SETUP.md](SETUP.md):
1. Install Claude CLI
2. Install gstack globally
3. Install Claude Code extension in VS Code
4. Clone this repo

Verify everything works by running a test `/brainstorm` command.

### Workflow (30 minutes per campaign, recurring)

Follow [WORKFLOW.md](WORKFLOW.md) for step-by-step instructions:

1. **Stage 1: Brief** (5 min) — Structure the campaign idea
2. **Stage 2: Brand Voice** (5 min) — Define persona and tone
3. **Stage 3: Research** (5 min) — Understand the market
4. **Stage 4: Strategy** (5 min) — Build positioning and channel plan
5. **Stage 5: Content** (5 min) — Generate platform-specific drafts
6. **Stage 6: Reports** (5 min) — Project campaign performance

Each stage outputs an artifact. Copy the output, paste into your campaign doc, and iterate.

### Outputs

Every stage generates a copy-paste-ready artifact:
- Stage 1: 500-word structured brief
- Stage 2: Persona definition + tone guidelines + sample phrases
- Stage 3: Market research with TAM/SAM/SOM + competitor analysis + trends
- Stage 4: Positioning statement + messaging hierarchy + channel matrix
- Stage 5: 6 platform-specific content drafts (Facebook post, Instagram caption, TikTok script, LinkedIn article, X thread, Threads post)
- Stage 6: Campaign metrics (reach, engagement, conversions, ROI projection)

No formatting needed. Everything is production-ready.

---

## Complete Example

See [examples/complete-example.md](examples/complete-example.md) for a full walkthrough.

**Product:** Accounting OS (SaaS bookkeeping tool for small businesses)

**Input:** Brief description of the product and target market

**Output:** All 6 stages with real content, showing:
- Marketing brief with audience, benefits, channels, metrics
- Brand voice with founder persona, tone, messaging pillars
- Market research with $30B TAM, $5B SAM, $200M SOM, top 3 competitors
- Marketing strategy with positioning, messaging hierarchy, channel breakdown
- Multi-platform content (Facebook ad, Instagram caption, TikTok video script, LinkedIn article, Twitter thread, Threads post)
- Campaign report with projected reach (295K impressions), engagement rates (3.1%), conversions (82), ROI (5,821% Year 1)

**Total time:** 75 minutes (or 30 minutes if expedited)

---

## Getting Started

Clone the repo and follow SETUP.md:

```bash
git clone https://github.com/shireen168/marketing-os.git
cd marketing-os
# Follow SETUP.md step by step
```

Then run your first campaign using WORKFLOW.md.

---

## Documentation

- **[SETUP.md](SETUP.md)** — Installation walkthrough (15 min)
- **[WORKFLOW.md](WORKFLOW.md)** — How to run each stage (30 min per campaign)
- **[CLAUDE.md](CLAUDE.md)** — System prompt, available skills, example prompts
- **[examples/complete-example.md](examples/complete-example.md)** — Worked example using Accounting OS

---

## What's Next (Phase 2)

Currently, the system generates copy-paste-ready content and metrics. Phase 2 will add:

- **Real publishing** — Actually post to Facebook, Instagram, TikTok, LinkedIn, Twitter/X from generated content
- **Analytics dashboard** — Track campaign performance live (opens, clicks, engagement)
- **Campaign calendar** — Schedule campaigns and auto-publish on dates you choose
- **Consulting-grade research** — Generate 50+ page market reports with PESTLE, Porter's, SWOT, detailed TAM/SAM/SOM analysis
- **Web UI** — Optional web interface alongside VS Code IDE option
- **Customer personas** — Deep-dive templates for profiling your target audience
- **Competitive intelligence** — Automated competitor monitoring and market updates
- **Email/SMS integration** — Send generated content via email and SMS
- **Advanced features** — A/B testing, attribution modeling, ROI tracking per channel

---

## Tech Stack

**AI Engine:**
- Claude API (content generation, strategy, research)

**Orchestration:**
- gstack ecosystem (/brainstorm, /investigate, /plan-ceo-review)
- Claude Code extension (VS Code IDE)

**CLI:**
- Claude CLI (authentication, local development)

**Output Format:**
- Native Claude artifacts (markdown, JSON, HTML)
- Copy-paste ready for immediate use

---

## Why This Architecture

**Three reasons I chose this approach:**

1. **Speed to value** — gstack commands run instantly. No API servers to spin up, no databases to manage. Your team has working outputs in 30 minutes.

2. **No maintenance overhead** — No custom MCP server to debug. No API endpoints to deploy. No database migrations. The system is as stable as Claude and gstack are.

3. **Non-technical adoption** — Marketing teams don't know bash or Docker. But they know VS Code. Clicking a slash command in VS Code is comfortable. The IDE handles all complexity.

The tradeoff: outputs are artifacts, not real published posts (Phase 2 adds actual publishing).

---

## For Hiring Managers

If you're evaluating me for a Marketing Manager or Brand Manager role:

This system demonstrates I can:
- Design end-to-end workflows that actually work
- Understand marketing strategy deeply (research, positioning, messaging, channels)
- Use AI productively (gstack, Claude API, not just "ChatGPT prompting")
- Ship systems, not demos (full documentation, working examples, testable on your laptop)
- Think like a builder (architectural decisions, trade-offs, scalability)
- Enable teams to operate independently (no gatekeeping, no agencies needed)

You hire me, I set up this system on your laptop on day one. Your team runs it from VS Code. No additional training, no waiting for agencies, no external dependencies.

---

## License

MIT
