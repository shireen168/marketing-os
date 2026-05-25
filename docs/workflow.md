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

## Complete Example

See [docs/showcase/](docs/showcase/) for a real-world example with Sunny Homemade (SMB proof point) showing all three tiers in action.

See [docs/complete-example.md](docs/complete-example.md) for a full walkthrough with Accounting OS as the example product.

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
- Review [docs/showcase/](docs/showcase/) for a real-world example
- Review [docs/complete-example.md](docs/complete-example.md) for reference

---

## Next Steps

1. **Tier 1 (Claude Code):** Run Stages 1-6. Total time: 40-45 minutes.
2. **Tier 2 (Cowork):** Copy outputs to Claude Desktop Cowork. Invite team. Get approvals at Stages 2, 4, 6.
3. **Tier 3 (Execution):** Once Cowork approves, execution team publishes, tracks performance, feeds learnings back to next cycle's brief.

**Total time:** 40-45 min (Claude Code) + team review time (Cowork) + execution (Tier 3)
