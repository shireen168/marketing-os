# Marketing OS: AI-Powered Marketing Operations System

## The Gap

- **Most teams:** Know ChatGPT/Claude.com
- **Few teams:** Know Claude Code exists
- **You need:** Context-preserving workflows (Stage 1 → Stage 2 → Stage 3, not 6 separate chats)

## The Promise

- **Setup:** 15 minutes
- **First campaign:** 1-2 hours (focused work)
- **Subsequent campaigns:** 30-45 minutes (with templates)
- **Agency baseline:** 3-5 days
- **You own it.** Team ships independently.

---

## The 6-Stage Workflow

Repeat this for every campaign:

| Stage | Time | Input | Output | Unlocks |
|-------|------|-------|--------|---------|
| **1. Brief** | 5m | Product, audience, goals | 500-word brief + audience persona | Everyone knows who you're talking to |
| **2. Brand Voice + Guidelines** | 5m | Brief from Stage 1 | Tone, persona, voice rules | Consistency across platforms ($5k agency work) |
| **3. Research** | 10m | Brief | TAM/SAM/SOM, competitors, trends | Strategy grounded in data, not guesses |
| **4. Strategy** | 5m | Brief + Research + Voice | Positioning, messaging hierarchy, channel matrix | Everyone rows in the same direction |
| **5. Content** | 10m | Strategy + Voice | 6 platform-specific drafts (Facebook, Instagram, TikTok, LinkedIn, X, Threads) | Ready to publish (no reformatting) |
| **6. Reports** | 5m | All above | Reach, engagement, conversion, ROI forecasts | Board-level proof before you ship |

**Total: 40 minutes of Claude work + your thinking time (1-2 hours first campaign).**

---

## Proof: Works Across Industries

This system (Claude Code + gstack) works for **any industry**. Same workflow, different domain.

**Example: Financial Services**: [Full worked example](docs/complete-example.md)

Built with Claude + gstack, this workflow is easily adapted to:
- HR recruiting campaigns
- Legal/compliance briefs
- Sales outreach sequences
- Product launches
- Internal communications

Timeline for Financial Services campaign:
- Brief setup: 5 min
- Research + strategy: 20 min
- 6 platform content drafts: 10 min
- ROI report: 5 min
- **Total: 40 minutes** (vs. 5-7 days with agencies)

---

## How It Works: Workflow-as-Context

Like Garry Tan's gstack model, each stage's output feeds into the next. Nothing falls through the cracks because every step knows what came before it.

| Stage | Command | Input From | Output Goes To | Result |
|-------|---------|-----------|----------------|--------|
| 1. Brief | `/brainstorm` | Product + goals | Stage 2, 3, 4 | Aligned team |
| 2. Brand Voice | `/brainstorm` | Brief (Stage 1) | Stage 4, 5 | Consistent voice |
| 3. Research | `/investigate` | Brief (Stage 1) | Stage 4 | Data-driven strategy |
| 4. Strategy | `/plan-ceo-review` | All above | Stage 5 | Clear direction |
| 5. Content | Native prompt | Strategy + Voice | Stage 6, publishing | Ready copy |
| 6. Reports | Native prompt | All stages | Board, investors | Proof of impact |

**Key:** Each stage inherits context from all previous stages. Your thinking compounds.

---

## Why This Works

**Claude Code + gstack:**
  - Each stage's output becomes the next stage's input
  - One workflow, not 6 separate chats losing context
  - Expandable to **any department in your company** (Marketing today → Finance, Legal, Sales, HR tomorrow)

**Cowork gateway:**
  - ChatGPT-like interface for non-technical teams
  - Graduate to `/slash commands` when ready
  - No terminal scares. VS Code extension = GUI.

**No infrastructure:**
  - Clone repo, run setup, done
  - Runs on your laptop
  - Works offline

---

## Get Started

```bash
git clone https://github.com/shireen168/marketing-os.git
cd marketing-os
```

1. **[docs/setup.md](docs/setup.md)**: Installation (15 minutes)
2. **[docs/workflow.md](docs/workflow.md)**: How to run each stage
3. **[docs/complete-example.md](docs/complete-example.md)**: Financial Services walkthrough (all 6 stages)

---

## How This System Supports Your Team

**Day 1:** Setup complete. Your team runs first campaign end-to-end independently.

**Week 1:** 3-5 campaigns shipped. Team operates solo with full system ownership.

**Month 1:** 40+ hours saved vs. agencies. Your team ships campaigns traditional approaches would defer (too niche, too fast-moving, too many iterations).

**Ongoing:** This system can expand to:
  - Finance teams (budgeting, forecasting workflows)
  - Legal teams (compliance briefs, document workflows)
  - Sales teams (outreach sequences, proposal workflows)
  - HR teams (recruiting campaigns, onboarding workflows)
  - Product teams (launch workflows, feature communication)

**For best results:** Embrace Claude Code capabilities (beyond ChatGPT). Structure work in workflows. Iterate quickly.

---

## What You Get (Per Campaign)

Production-ready:
- Structured brief with audience + channels
- Brand voice + guidelines (tone, persona, rules)
- Market research (TAM/SAM/SOM, competitors)
- Positioning statement + messaging hierarchy
- 6 platform-specific content drafts
- ROI projections

All ready to publish. No formatting needed.

---

## Phase 2 (Deferred)

Real publishing to social platforms. Live analytics. Campaign calendar.

Why defer? Prove Phase 1 workflow first. Better to ship fast + iterate than over-build.

---

## FAQ

**Q: Why not just use ChatGPT?**

A: You lose context between conversations. Each stage would be a separate chat. This system preserves context across all 6 stages, so Stage 5 knows what Stage 2 decided.

---

**Q: Why not hire an agency?**

A: 3-5 days per campaign vs. 1-2 hours with this system. Plus your team owns the process and can iterate independently without waiting.

---

**Q: Why not build custom tools?**

A: Months of development work. This system works today with tools you already have (Claude Code + VS Code).

---

See [docs/faq.md](docs/faq.md) for more.

---

## License

MIT
