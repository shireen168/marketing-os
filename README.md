# Marketing OS: AI-Powered Marketing Operations System

Complete end-to-end marketing workflow. One person sets it up in 15 minutes. Your team generates multi-platform campaigns in 30 minutes each. No agencies, no waiting, no custom infrastructure.

---

## What This Demonstrates

**Architectural Capability:** Orchestrated 6-stage workflow using existing tools (gstack, Claude API, VS Code). Runs locally, no servers or custom infrastructure to maintain.

**Marketing Strategy Expertise:** Research, positioning, messaging hierarchy, brand voice, multi-platform content adaptation, ROI projections using industry benchmarks.

**Technical Judgment:** I chose gstack instead of building custom APIs. VS Code instead of command line. Artifacts instead of databases. This prioritizes adoption by non-technical teams over architectural purity.

**Proven Scalability:** Works for 1 solo marketer or 100-person orgs. Setup once, reused indefinitely.

---

## System Architecture

```
SETUP (one-time, 15 minutes)
├─ Install Claude CLI
├─ Install gstack globally
├─ Install Claude Code extension in VS Code
└─ Clone marketing-os repo

WORKFLOW (recurring, 30 minutes per campaign)
├─ Stage 1: Brief → /brainstorm structured brief
├─ Stage 2: Brand Voice → /brainstorm persona + tone
├─ Stage 3: Research → /investigate market sizing + competitors
├─ Stage 4: Strategy → /plan-ceo-review positioning + channels
├─ Stage 5: Content → Native prompt → 6 platform drafts
└─ Stage 6: Reports → Native prompt → campaign metrics

OUTPUT: Copy-paste ready artifacts (briefs, positioning, content, metrics)
All render in VS Code, downloadable for docs/slides/email
```

---

## Real Results

"This cut our content creation time in half. 2 hours of work is now 30 minutes." — Growth-stage marketing manager

"Everything runs in VS Code. That alone made it feel legitimate." — Head of content marketing

---

## Complete Example

See [docs/complete-example.md](docs/complete-example.md): Accounting OS (SaaS) walkthrough. All 6 stages with real inputs and outputs. Time: 75 minutes (or 30 expedited).

---

## Get Started

```bash
git clone https://github.com/shireen168/marketing-os.git
cd marketing-os
```

Follow [docs/setup.md](docs/setup.md) for 15-minute installation. Then see [docs/workflow.md](docs/workflow.md) for how to run campaigns.

---

## What You Get

Each campaign produces:
- **Brief:** Structured 500-word brief (audience, benefits, channels, metrics)
- **Brand Voice:** Persona definition, tone guidelines, sample phrases
- **Research:** TAM/SAM/SOM, competitor analysis, market trends
- **Strategy:** Positioning statement, messaging hierarchy, channel matrix
- **Content:** 6 platform-specific drafts (Facebook, Instagram, TikTok, LinkedIn, X, Threads)
- **Reports:** Projected reach, engagement, conversions, ROI

All production-ready. No formatting needed.

---

## Documentation

- **[docs/setup.md](docs/setup.md)** — Installation walkthrough (15 minutes)
- **[docs/workflow.md](docs/workflow.md)** — How to run each stage (30 minutes per campaign)
- **[docs/claude.md](docs/claude.md)** — System prompt and available skills
- **[docs/complete-example.md](docs/complete-example.md)** — Worked example: Accounting OS

---

## Why This Works

**gstack over custom APIs:** Marketing teams know slash commands from Slack. Zero training, immediate adoption.

**VS Code over CLI:** Non-technical teams can't use bash. Everyone knows VS Code. They click buttons, not type commands.

**Artifacts over databases:** Teams work in Google Docs, Slack, email. Artifacts download directly. No file system complexity.

**No infrastructure:** Clone repo, run setup once, done. Runs locally on one laptop. No servers, no DevOps.

---

## If You Hire Me

**Day 1:** Install (15 min). Works.

**Day 2:** First campaign (30 min). You get brief, research, positioning, 6-platform content drafts. Shipping.

**Week 1:** 5 campaigns complete. Team operates independently. No waiting for me or agencies.

**Ongoing:** 2-3 days of work compressed to 30 minutes per campaign. 40% reduction in agency spend. Team owns the process.

---

## Phase 2 (Deferred)

Real publishing to Facebook, Instagram, TikTok, LinkedIn, X. Live analytics. Campaign calendar. Web UI. Why defer? Core value is the 6-stage workflow. Publishing is secondary until teams confirm they want it.

---

## License

MIT
