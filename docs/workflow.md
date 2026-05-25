# Workflow Guide: Running Your First Campaign

Complete end-to-end campaign using the three-tier architecture: Claude Code (Tier 1) for strategy, Claude Desktop Cowork (Tier 2) for approval gates, and simple tools (Tier 3) for execution.

**Timeline:** 40-45 minutes of Claude Code work + team review in Cowork + Tier 3 execution

**This pattern works for:** Marketing, HR recruiting, legal briefs, sales campaigns, product launches, internal communications. Same workflow, different domain.

**Setup first:** Follow [setup.md](setup.md) before starting.

---

## The Three-Tier System

| Tier | Layer | Tools | Who | What |
|------|-------|-------|-----|------|
| **Tier 1** | Strategic Intelligence | Claude Code + gstack skills | Strategic thinker | Stages 1-6: Brief → Voice → Research → Strategy → Content → Reports |
| **Tier 2** | Human-AI Collaboration | Claude Desktop Cowork | Team reviewers (non-technical OK) | **Approval gates at Stages 2, 4, 6** — refine outputs before execution |
| **Tier 3** | Team Execution | Simple tools (Linktree, Canva, scheduling) | Execution team | Publish, track, iterate based on Tier 2 approvals |

---

## The 6-Stage Flow

```
Brief → Brand Voice ⚠️ → Research → Strategy ⚠️ → Content → Reports ⚠️
        (Cowork review)        (Cowork review)         (Cowork review)
```

**Key:** Each stage's output feeds into the next stage. Your thinking compounds. Nothing disconnected, nothing lost.

⚠️ = Approval gate in Claude Desktop Cowork. Team reviews and refines before Tier 3 executes.

You can pause/resume between stages, but you'll keep the full context from all previous stages.

---

## Stage 1: Brief

**Goal:** Structure your product idea into a marketing brief.

**Run this:**
```
/brainstorm

Prompt: "Create a marketing brief for [YOUR PRODUCT]. 
Include: product description, target audience, key benefits, 
primary channels, success metrics."
```

**Output:** Structured brief artifact (copy to file or download)

**Example input:** "SaaS tool that automates social media posting for small businesses"

**Example output:** Brief with audience, channels (LinkedIn, Twitter, Instagram), KPIs

---

## Stage 2: Brand Voice

**Goal:** Define your brand's personality and how it speaks.

**Run this:**
```
/brainstorm

Prompt: "Define brand voice for [PRODUCT]. 
Provide: target persona, tone of voice, key messaging pillars, 
sample phrases that sound like our brand."
```

**You'll get:** Brand guidelines artifact

**Example output:** Persona (friendly expert), tone (clear + confident), pillars (simplify, educate, empower)

**⚠️ Approval Gate — Review in Claude Desktop Cowork:**
Once you have the voice guidelines, copy the output into Claude Desktop Cowork and invite your team to review. Non-technical team members can directly edit the tone, persona, or messaging pillars. Does the voice feel authentic? Does it match your brand? Make changes in Cowork before moving to Stage 3.

Why? If the voice isn't right here, every piece of content (Stage 5) will inherit the wrong tone.

---

## Stage 3: Research

**Goal:** Understand the market landscape.

**Run this:**
```
/investigate

Prompt: "Research the [MARKET] for [PRODUCT]. 
Provide: PESTLE analysis summary, TAM/SAM/SOM, top 3 competitors, 
market trends, customer pain points."
```

**You'll get:** Research summary artifact

**Example output:** Market sizing (TAM $500M), top 3 competitors, key trends

---

## Stage 4: Strategy

**Goal:** Create positioning and messaging strategy.

**Run this:**
```
/plan-ceo-review

Prompt: "Create marketing strategy for [PRODUCT] using this research 
and brand voice. Provide: positioning statement, messaging hierarchy, 
recommended channels with rationale, go-to-market timeline."
```

**You'll get:** Strategy document artifact

**Example output:** Position as "simplest social tool for busy small business owners", channels (Twitter, Instagram, LinkedIn)

**⚠️ Approval Gate — Review in Claude Desktop Cowork:**
Copy the strategy output to Claude Desktop Cowork. Your team reviews: Does the positioning feel right? Are the recommended channels correct for our audience? Does the content calendar make sense? CFO can review budget allocation. Product lead can validate messaging against product roadmap.

Once Cowork approves the strategy, Stage 5 uses this exact strategy to generate content. Get alignment here — it saves re-work in Stage 5.

---

## Stage 5: Content

**Goal:** Generate platform-specific content drafts.

**Run this (in Claude panel, not /slash command):**

```
Prompt: "Using this brief, brand voice, and strategy, 
create content drafts for these platforms:
- Facebook (200 char post)
- Instagram (caption + hashtags)
- TikTok (short script)
- LinkedIn (professional post)
- Twitter/X (thread, 3 tweets)
- Threads (casual post)

Make each sound like our brand voice."
```

**You'll get:** 6 artifact files, one per platform

**Example output:** Facebook post, Instagram caption, TikTok script (all copy-paste ready)

---

## Stage 6: Reports

**Goal:** Show projected results and learnings for next cycle.

**Run this (in Claude panel):**

```
Prompt: "Create a sample campaign report for [PRODUCT] 
showing: projected reach per platform, estimated engagement rates, 
projected conversions, ROI estimate. Use industry benchmarks."
```

**You'll get:** Mock metrics artifact

**Example output:** Facebook reach 50K, IG reach 25K, total conversions est. 150

**⚠️ Approval Gate — Review in Claude Desktop Cowork:**
Real campaigns: copy actual performance data into Cowork. Team analyzes results, identifies what worked, what didn't, and priorities for next cycle. These learnings become the input for Stage 1 of next week's brief.

Test/sample campaigns: review projected metrics in Cowork. Are the estimates reasonable? Does the ROI projection align with business goals?

---

## Complete Example: Smart Sleep Device Product Launch

This walkthrough shows the **under-the-hood orchestration** — how Claude Code skills structure thinking, how context flows between stages, and how research findings reshape downstream decisions.

### The Product

A smart sleep tracking device targeting wellness-focused consumers. Competitors emphasize sleep *metrics* (heart rate, movement tracking). Question: What do buyers actually want?

### How the System Works: Stage-by-Stage

#### Stage 1: Brief (5 min)
**What happens:**
```
/brainstorm
Create a marketing brief for a smart sleep tracking device targeting 
wellness-conscious consumers. Include: product description, target 
audience, key benefits, primary channels, success metrics.
```

**Output:** A structured brief. Example:
- **Product:** Non-invasive sleep tracker with AI insights
- **Audience:** Women 30-50, interested in wellness, sleep quality
- **Channels:** Instagram, TikTok, wellness blogs, Reddit communities
- **KPI:** Conversion from free trial to paid ($200 device)

---

#### Stage 2: Brand Voice (5 min)
**What happens:**
```
/brainstorm
Define brand voice for our sleep tracking device. Our audience is 
wellness-focused; they're tired of data overload and want actionable 
rest recommendations. Provide: target persona, tone of voice, 
key messaging pillars, sample phrases.
```

**Output:** Brand guidelines
- **Tone:** Warm, supportive, non-clinical
- **Persona:** "Sleep coach friend" (not "sleep scientist")
- **Pillars:** Sleep quality > metrics, personalized insights, wellness lifestyle
- **Sample phrase:** "Better rest. Better you."

**⚠️ Cowork Review:** Team confirms this voice feels right before Stage 5 uses it.

---

#### Stage 3: Research (10 min) — THE KEY DECISION POINT
**What happens:**
```
/investigate
Research the sleep tracking device market and wellness consumer 
preferences. Provide: competitor analysis (what are they messaging?), 
customer pain points (what do they actually want?), market trends, 
TAM/SAM/SOM.
```

**Output:** Research findings. Critical discovery:
- **Competitor messaging:** "Track REM, deep sleep, heart rate variability" (data-focused)
- **Buyer interviews:** "I don't care about numbers. I just want to sleep well and wake refreshed" (outcome-focused)
- **Market gap:** Competitors miss the outcome focus. Buyers want rest solutions, not metrics dashboards.
- **Trend:** Wellness industry moving from "biohacking" (metrics) to "holistic wellbeing" (outcomes)

**This research finding is crucial. It doesn't just inform Stage 4 — it reshapes it.**

---

#### Stage 4: Strategy (10 min) — DECISION LOOP
**What happens:**
```
/plan-ceo-review
Create marketing strategy for our sleep device using this research 
and brand voice. Provide: positioning statement, messaging hierarchy, 
recommended channels with rationale.
```

**What Claude Code does (orchestration):**
1. Reads Stage 3 research: "Competitors miss outcome focus"
2. Reads Stage 2 voice: "Sleep coach friend, not scientist"
3. Synthesizes: Competitors position as data tools → **We position as rest solution**
4. Decides: Messaging hierarchy flips from metrics (REM, deep sleep) to outcomes (wake refreshed, better energy)
5. Channels shift: Away from fitness/biohacking communities → Toward wellness/lifestyle communities

**Output:** Strategy document
- **Positioning:** "Sleep solution for wellness-first living, not metrics-obsessed tracking"
- **Channels:** Wellness blogs, TikTok, Reddit r/wellness (not r/Quantified Self)
- **Messaging hierarchy:**
  1. "Wake up refreshed, not exhausted"
  2. "Personalized sleep recommendations, not raw data"
  3. "Sleep better in one week"

**The cause-and-effect is visible:** Research finding (competitors miss outcome focus) → Strategy choice (position as solution, not tracker) → Channels change (wellness, not fitness)

**⚠️ Cowork Review:** Team validates this strategy against the research. Does the positioning align with the market gap we found?

---

#### Stage 5: Content (12 min) — CONTEXT INHERITANCE
**What happens:**
```
Using this brief, brand voice, and strategy, create content for 
Instagram, TikTok, LinkedIn, and email. Each piece should emphasize 
outcomes (better sleep, more energy), not metrics.
```

**What Claude Code does (automatic context flow):**
1. Reads Stage 2 (voice): "Sleep coach friend"
2. Reads Stage 4 (strategy): "Position as solution, emphasize outcomes"
3. Reads Stage 3 research: "Competitors focus on metrics — we focus on rest"
4. **Combines all three:** Writes content that sounds like a sleep coach, emphasizes outcomes, differentiates from metrics-focused competitors

**Output:** 6 content artifacts
- **Instagram caption:** "Better sleep starts here. 💤 No more sleep anxiety. No data overload. Just personalized insights that help you rest."
- **TikTok script:** "POV: You wake up energized for the first time in months"
- **Email subject:** "Your sleep just got smarter (without the numbers)"

**Notice:** No content mentions "heart rate variability" or "REM cycles." That's the research-informed decision from Stage 4 flowing through Stage 5.

**Why this matters:** Content didn't start from scratch. It inherited:
- Voice from Stage 2 (coach, warm tone)
- Strategy from Stage 4 (outcomes, not metrics)
- Research from Stage 3 (market gap identified)

If you tried to write this without Stages 2-4, you'd either sound clinical or unfocused. The system chains these together automatically.

---

#### Stage 6: Reports (8 min) — LEARNING LOOP
**What happens:**
```
Create a sample campaign report showing: projected reach per platform, 
engagement rates, estimated conversions, ROI. Use wellness market benchmarks.
```

**Output:** Metrics and projections
- **Instagram:** 50K reach, 3-5% engagement, ~150 conversions
- **TikTok:** 200K reach, 6-8% engagement, ~480 conversions
- **Wellness blogs:** 25K reach (paid sponsorship), 2% conversion, $5K spend, $40K revenue
- **Total estimated revenue:** $95K from $15K spend (6.3x ROI)

**⚠️ Cowork Review:** Real campaign → show actual performance data. Sample campaign → validate projections with team.

---

### The Under-the-Hood Architecture

**How context flows across stages:**

```
Stage 1 (Brief)
    ↓
Stage 2 (Voice) ← Brief context
    ↓
Stage 3 (Research) ← Brief + Voice context
    ↓
Stage 4 (Strategy) ← Brief + Voice + Research context [DECISION LOOP HERE]
    ↓
Stage 5 (Content) ← All previous context [AUTOMATIC INHERITANCE]
    ↓
Stage 6 (Reports) ← All context flows to projections
```

**The critical insight:** Stage 5 (Content) doesn't need you to re-brief it. Claude Code automatically:
- Reads what Stage 2 decided (voice)
- Reads what Stage 4 decided (strategy)
- Reads what Stage 3 discovered (research gap)
- Writes content that aligns with all three

This is why a human would need to manually coordinate these decisions across an email thread. Claude Code does it in 40 minutes.

---

### Why This Eliminates Agency Costs

**Agency process:**
- Client brief → $0, 30 min (your time)
- Research/workshops → Consultant time, 5 days
- Strategy development → Consultant time, 5 days (+ client meetings)
- Content writing → Consultant time, 3 days (+ revisions)
- **Total:** 2-3 weeks, $6-10K consultant fee

**This system:**
- Stages 1-6 → Claude Code, 40 min (your time)
- Tier 2 approvals → Your team, 1-2 hours Cowork review
- Tier 3 execution → Your team, simple tools (Canva, scheduling)
- **Total:** 2 hours your time, $0 additional cost

**The difference:** An agency consultant researches (2-3 days), thinks strategically (2-3 days), writes (1-2 days), and iterates. This system compresses thinking through skill orchestration:
- `/investigate` structures research questions automatically
- `/plan-ceo-review` synthesizes research → strategy decisions automatically
- Native Claude generation writes content using all previous outputs automatically

You still review everything (Tier 2 Cowork) — you just don't have to wait 2 weeks or pay $10K.

---

### Real-World Reference

For a complete working example with real metrics, see [docs/showcase/sunny-homemade-real-example/](docs/showcase/sunny-homemade-real-example/) (SMB Tier 3 execution proof point).

---

## Tips

- **Tier 1 (Claude Code) is fast:** 40-45 minutes for Stages 1-6
- **Tier 2 (Cowork) is where decisions stick:** Don't rush the approval gates. Team refinement at Stages 2, 4, 6 prevents re-work in Tier 3.
- **Tier 3 (Execution) publishes with confidence:** Once Cowork approves, execution teams have clear, approved direction.
- **Copy-paste everything:** All outputs are artifact format. Just copy and download.
- **Reuse stages:** Create brief once, use for multiple brand voices/strategies.
- **Iterate:** Don't like Stage 4 strategy? Run it again in Claude Code. Cowork refines the result.
- **Download:** Each artifact has a download button. Use those files directly.
- **Save context between sessions:** Use `/context-save` after Stage 4 approval, `/context-restore` to resume Stage 5.

---

## Troubleshooting

**"Command not found"**
- Make sure gstack is installed: `~/.claude/skills/gstack/bin/gstack --version`
- Restart VS Code

**"Claude Code not responding"**
- Refresh the Claude panel
- Check internet connection
- Try the command again

**"Artifacts aren't rendering"**
- Restart VS Code
- Make sure Claude Code extension is enabled

**"Output looks wrong in Claude Code"**
- Adjust your prompt and try again
- Use the example prompts from this guide (copy-paste)

**"Cowork approval gate feels slow"**
- Cowork is where decisions happen — don't skip it. A 5-minute Cowork review prevents 2 hours of re-work in Tier 3.
- If feedback is slow, check: are stakeholders notified? Do they have permission to edit?

**Still stuck?**
- Check [setup.md](setup.md) troubleshooting
- Review [docs/showcase/](docs/showcase/) for a real-world example with all three tiers
- Review [README.md](README.md) for system overview

---

## Next Steps

1. **Tier 1 (Claude Code):** Run Stages 1-6. Total time: 40-45 minutes.
2. **Tier 2 (Cowork):** Copy outputs to Claude Desktop Cowork. Invite team. Get approvals at Stages 2, 4, 6.
3. **Tier 3 (Execution):** Once Cowork approves, execution team publishes, tracks performance, feeds learnings back to next cycle's brief.

**Total time:** 40-45 min (Claude Code) + team review time (Cowork) + execution (Tier 3)
