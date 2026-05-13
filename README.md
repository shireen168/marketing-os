# Marketing OS: AI-Powered Marketing Operations System

**Quick Navigation:**
1. [The Gap](#the-gap)
2. [The Promise](#the-promise)
3. [Brand Building & Consistency](#brand-building--consistency-stage-2)
4. [What We Built](#what-we-built)
5. [The 6-Stage Workflow](#the-6-stage-workflow)
6. [How It Works](#how-it-works-workflow-as-context)
7. [Why This Works](#why-this-works-context-preservation)
8. [Get Started](#get-started)
9. [Day 1 to Month 1](#day-1-to-month-1-what-ships)
10. [FAQ](#faq)

---

## The Gap

- **Most teams:** Use ChatGPT, Gemini, or DeepSeek as chatbots. Copy-paste prompts. Lose context.
- **All teams:** Either hire agencies ($3-5K per campaign) or build in-house (2-3 months dev work)
- **You need:** A system that runs in-house immediately. No agency costs. No development timeline. Your team ships independently.

## The Promise

**Speed:**
- Setup: 15 minutes
- First campaign: 1-2 hours (focused work)
- Subsequent campaigns: 30-45 minutes (with templates)
- vs. agencies: 3-5 days per campaign

**In-house & Independent:**
- Run on your laptop. No infrastructure. No vendors.
- Team ships independently from Day 1. No waiting for agencies.
- Full control over brand voice, positioning, messaging.

**Cost Savings:**
- No agency fees ($3-5K per campaign disappear)
- No dev cost (2-3 months of engineering eliminated)
- First campaign pays for itself. Subsequent campaigns: near-zero cost.

---

## Brand Building & Consistency (Stage 2)

Most agencies charge $5K for brand guidelines and voice work. This is where brand consistency lives.

In this system:
- **Stage 2 (5 minutes):** Define brand persona, tone, messaging pillars, sample phrases
- **Reusable forever:** Stage 4 (Strategy) and Stage 5 (Content) inherit your voice automatically
- **Consistency guaranteed:** All 6 platforms sound like the same brand
- **In-house:** You control evolution. No external agency gatekeeping brand decisions.
- **Teachable:** Every team member learns your brand logic. New hires onboard to a documented system, not tribal knowledge.

This system turns brand consistency from a one-time agency cost into a living, reusable system.

---

## What We Built

Most teams lose context between conversations. Copy-paste prompts into ChatGPT. Start over.

We did something different:

- **One system where 40+ agents work together** (not isolated prompts)
- **Context preserved across all stages** (Stage 5 knows Stage 2's decisions)
- **Every team member, every campaign, zero context switching** (structure once, reuse infinitely)
- **Same architecture works for marketing, HR, legal, finance** (not a marketing-only tool)

That's the difference.

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

## How It Works: Workflow-as-Context

Each stage's output feeds into the next. Nothing falls through the cracks because every step knows what came before it. Behind the scenes, 20+ specialized agents work at each stage.

| Stage | Invoked By | Agent | Input From | Output Goes To | Result |
|-------|-----------|-------|-----------|----------------|--------|
| 1. Brief | `/brainstorm` | Brainstorm agent | Product + goals | Stage 2, 3, 4 | Aligned team |
| 2. Brand Voice | `/brainstorm` | Brand guidelines agent | Brief (Stage 1) | Stage 4, 5 | Consistent voice |
| 3. Research | `/investigate` | Research + market analysis agent | Brief (Stage 1) | Stage 4 | Data-driven strategy |
| 4. Strategy | `/plan-ceo-review` | Strategy + positioning agent | All above | Stage 5 | Clear direction |
| 5. Content | Native Claude | Content generation agent | Strategy + Voice | Stage 6, publishing | Ready copy |
| 6. Reports | Native Claude | Analytics + ROI agent | All stages | Board, investors | Proof of impact |

**Key:** Each stage inherits context from all previous stages. Your thinking compounds. Each agent is one of 20+ specialized tools built into the system, plus extensibility to create your own.

**See all agents:** Full list of available agents and capabilities in [skills.md](docs/skills.md).

---

## Why This Works: Context Preservation

**The core advantage:**
  - Context preserved across all 6 stages (not 6 separate chats)
  - Stage 5 (Content) inherits Brand Voice (Stage 2) + Strategy (Stage 4)
  - Each slash command builds on previous output
  - Doesn't require manual context switching
  - That's what makes 40 minutes possible instead of 5-7 days

**Slash commands vs copy-paste prompts:**
  - Most teams: Copy-paste prompts into ChatGPT, lose context, restart
  - This system: Agents preserve context automatically
  - Each `/command` invokes specialized agent with built-in reasoning
  - Backend skill set handles complexity you'd normally repeat manually

**The 1% difference:**
  - 99% of teams repeat instructions across conversations
  - We structure work once, reuse infinitely
  - Same team member leads any campaign (system carries context)
  - New team members ship independently on Day 1 (system teaches workflow)

**Works across any department:**
  - Same workflow-as-context architecture
  - Different domain, same system
  - Finance teams: cash flow forecasts, budgeting workflows
  - Legal teams: compliance briefs, document workflows
  - Sales teams: outreach sequences, proposal workflows
  - HR teams: recruiting campaigns, onboarding workflows
  - Product teams: launch workflows, feature communication

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

## Day 1 to Month 1: What Ships

**Day 1:** Setup complete. First campaign runs end-to-end independently.

**Week 1:** 3-5 campaigns shipped. Full system ownership. No external dependencies.

**Month 1:** 40+ hours saved vs. agencies. Campaigns ship that traditional approaches would defer (too niche, too fast-moving, too many iterations).

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

## FAQ

**Quick answers to hiring/adoption questions:**

- Will our team actually use this?
- Is this just a marketing tool?
- What if we already have processes?
- How is this different from hiring an agency?
- Can we customize it?

**See:** [docs/faq.md](docs/faq.md) for full answers.

---

## License

MIT
