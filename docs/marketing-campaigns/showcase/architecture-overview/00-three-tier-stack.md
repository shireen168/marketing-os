# Three-Tier Stack: The Complete System

## Tier 1: Strategic Intelligence (THE CONSULTANT'S LAYER)

**What it does:**
- Claude Code orchestrates the entire 8-phase workflow
- Tavily API and research integrations pull real market data: competitor analysis, audience insights, industry trends (not guessing)
- Custom skills coordinate decisions across phases (not isolated prompts)
- Context preservation: Stage 5 content inherits Stage 2 voice + Stage 4 strategy automatically

**Why it matters:**
- ✅ This is where consulting expertise lives (the value delivered)
- ✅ Shows systems architecture, not just "using ChatGPT"
- ✅ Built infrastructure proves differentiation in the market
- ✅ Scales to enterprise: At larger orgs, Tier 1 complexity increases (more data sources, stakeholder workflows, approval gates)

**Tools in Tier 1:**
- Claude Code (CLI, workflows, orchestration)
- Tavily API + Perplexity fallback (market research, competitor analysis, real-time search)
- Anthropic API: Claude Opus 4.7 (Phases 1-3) / Claude Sonnet 4.6 (Phases 4-8)
- Custom AI skills (decision coordination, content planning, context management)

**What gets handed to Tier 2:**
- Structured outputs at each stage (briefs, guidelines, research, strategy, content plans, reports)
- Context flows through all stages
- Everything ready for team review in Claude Code

**Not Tier 1 (handled by Tier 2/3):**
- Actual content writing or refinement (Tier 2 + Team approval)
- Design/editing (Tier 3 execution)
- Social media posting (Tier 3 execution)

---

## Tier 2: Workflow Outputs + Team Collaboration (THE PLAYBOOK + APPROVAL LAYER)

**What it produces at each stage:**
- **Stage 1:** Marketing brief (audience, goals, tone direction)
- **Stage 2:** Brand voice guidelines (persona, messaging, tone rules)
- **Stage 3:** Research findings (market size, competitors, trends, audience insights)
- **Stage 4:** Strategy brief (positioning, messaging hierarchy, channel recommendations)
- **Stage 5:** Content plan (6 platform-specific posts with captions, angles, design direction)
- **Stage 6:** Performance projections (reach, engagement, ROI forecast + board-ready report)

**How the team works:**
- Team reviews each stage output in **Claude Code** (structured approval gates built into the workflow)
- Each stage has a **human-approval checkpoint**: team member reviews, asks Claude questions, refines if needed
- **Approval advantages:**
  - Outputs are structured markdown files, easy to review and discuss in Claude Code conversations
  - Approval gates are clear (confirm before the next phase runs)
  - Context flows forward (what's approved in earlier phases shapes all later outputs)
  - Teams can review outputs in any editor; no specialized tooling required

**Why this matters:**
- ✅ Each stage feeds the next (no context loss, full collaboration trail)
- ✅ Team is actively involved (not just executing blindly)
- ✅ Approval gates prevent misalignment before execution
- ✅ Examples show what these outputs look like across all 8 phases

**Human-AI collaboration workflow:**
- Tier 1 produces output → Team reviews in Claude Code
- Team asks: "Is this right for our audience?" "Can we make this more aggressive?"
- Claude refines in real-time (in the same interface)
- Team approves → Output locked for Tier 3 execution

**Smart Sleep Device example:**
See [../../../product-launch/sleep-device-workflow-readme.md](../../../product-launch/sleep-device-workflow-readme.md) for a complete walkthrough showing how a smart sleep tracking device product moves through all 8 phases:
- Validation research reveals market gap (competitors focus on metrics, buyers want outcomes)
- Strategy shifts positioning based on research findings
- Content inherits both the research insight and strategic positioning
- Full context flow showing how findings reshape decisions across all phases

---

## Tier 3: Post-Approval Execution (THE NO-CODE LAYER)

**Who uses it:** Non-technical team members (designers, content ops, social media managers)

**What they do:**
- **Take Tier 2 outputs** (the approved playbook)
- **Execute using simple tools:** Canva (design), spreadsheets (planning), schedulers (posting)
- **No coding, no AI prompting required**: the smarts are already locked in Tier 2
- **Fast, repeatable**: once Tier 1 + 2 are done and approved, Tier 3 is plug-and-play
- **Only starts after Tier 2 approval**: clear hand-off from strategy to execution

**Why it matters:**
- ✅ Shows team members don't need to be technical to execute
- ✅ Reduces execution cost (non-technical hires can do this)
- ✅ Clear ownership: Strategy team approves, execution team delivers
- ✅ Scales to enterprise: More team members = same Tier 3 tools, bigger org

**Tools in Tier 3:**
- Canva (visual design, templates)
- Spreadsheets/Notion (planning, tracking, calendars)
- Social schedulers (Instagram, Facebook, TikTok, LinkedIn)
- Email platforms (campaign execution)

**What's NOT in Tier 3 (handled by Tier 1/2):**
- Strategy thinking (Tier 1)
- Content research/planning (Tier 2)
- Approval workflows (Tier 2 in Claude Code)
- Context preservation (Tier 1 + Tier 2)

---

## Human-AI Collaboration: Approval Gates at Each Stage

Every phase has a human approval checkpoint. The team reviews each output in **Claude Code** (structured approval gates in conversation) before moving to execution:

- **Stage 1 approval:** Does this brief reflect our brand? Are we targeting the right audience?
- **Stage 2 approval:** Does the voice guide feel authentic? Are messaging pillars comprehensive?
- **Stage 3 approval:** Do we have the data we need? Are the insights actionable?
- **Stage 4 approval:** Does the strategy align with business goals? Are the channels right?
- **Stage 5 approval:** Are the posts on-brand? Do captions feel authentic in [language]?
- **Stage 6 approval:** Do the metrics make sense? Are recommendations clear?

**Why approval gates matter:**
- ✅ Prevents misalignment (catch issues before they're expensive)
- ✅ Team stays in control (they're not executing blindly)
- ✅ Scales to enterprise governance (approval chains, stakeholder sign-off)
- ✅ Transparent decision trail (what was approved and why)

---

## Summary: Why Three Tiers Work Together

| What | Who | Where | Output |
|------|-----|-------|--------|
| **Tier 1** | Consultant (you) | Claude Code + Research APIs + Skills | Structured briefs, strategies, guidelines |
| **Tier 2** | Team | Claude Code | Approved outputs ready for execution |
| **Tier 3** | Execution team | Canva, schedulers, simple tools | Final deliverables (posts, campaigns, reports) |

**The flow:** Consulting expertise (Tier 1) → Team collaboration & approval (Tier 2 in Claude Code) → Execution (Tier 3)

**Result:** System scales without proportional cost increases. One strategist builds the system once. Multiple approval gates keep the team in control. Many executors use simple tools. Headcount grows in Tiers 2 and 3, but Tier 1 effort stays constant.
