# Workflow Guide: Running Your First Campaign

Complete end-to-end campaign in 40-90 minutes using Claude Code + gstack.

**This pattern works for:** Marketing, HR recruiting, legal briefs, sales campaigns, product launches, internal communications. Same workflow, different domain.

**Setup first:** Follow [SETUP.md](SETUP.md) before starting.

---

## The 6-Stage Flow

```
Brief → Brand Voice → Research → Strategy → Content → Reports
```

**Key:** Each stage's output feeds into the next stage. Your thinking compounds. Nothing disconnected, nothing lost.

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

**Goal:** Show projected results.

**Run this (in Claude panel):**

```
Prompt: "Create a sample campaign report for [PRODUCT] 
showing: projected reach per platform, estimated engagement rates, 
projected conversions, ROI estimate. Use industry benchmarks."
```

**You'll get:** Mock metrics artifact

**Example output:** Facebook reach 50K, IG reach 25K, total conversions est. 150

---

## Complete Example

See [examples/complete-example.md](examples/complete-example.md) for a full walkthrough with real inputs and outputs.

---

## Tips

- **Copy-paste everything:** All outputs are artifact format. Just copy and download.
- **Reuse stages:** Create brief once, use for multiple brand voices/strategies.
- **Iterate:** Don't like the output? Run the stage again with adjusted prompt.
- **Download:** Each artifact has a download button. Use those files directly.

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

**"Output looks wrong"**
- Adjust your prompt and try again
- Use the example prompts from this guide (copy-paste)

**Still stuck?**
- Check [SETUP.md](SETUP.md) troubleshooting
- Review [examples/complete-example.md](examples/complete-example.md) for reference

---

**Next:** Download your artifacts and start executing. Each stage takes ~5 minutes.

**Total time:** 30 minutes for complete campaign (Brief → Reports)
