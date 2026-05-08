# LinkedIn Daily AI Digest

## Trigger
`/linkedin-daily-digest` or scheduled at 8am MYT daily

---

## What This Skill Does

1. Spawns the existing `ai-news-digest` subagent to search last 24h AI + Claude Code news
2. Selects the 1 most LinkedIn-worthy story (impact + shareability + Shireen's positioning)
3. Generates a ready-to-post LinkedIn post (under 150 words, no em-dashes, no emojis)
4. Formats as a Telegram Markdown message
5. Sends via Telegram Bot API (curl)

---

## Step-by-Step Workflow

### Step 1: Trigger AI news digest search

Invoke the existing `ai-news-digest` agent (available at `.claude/agents/ai-news-digest.md`).

The agent automatically:
- Searches last 7-14 days for Claude Code, Anthropic, AI marketing tools, AI dev news
- Formats results with clean Markdown sections (### Claude Code / Anthropic, ### AI Marketing Tools, etc.)
- Returns structured findings

---

### Step 2: Select the top 1 LinkedIn-worthy story

From the ai-news-digest results, apply these selection criteria:

**Criteria (rank in this order):**
1. **Biggest impact** on AI practitioners or marketing professionals
2. **Highest shareability** — surprising, counterintuitive, or immediately practical
3. **Alignment with Shireen's positioning** as AI systems architect / marketing strategist

**Examples of LinkedIn-worthy stories:**
- New Claude/Anthropic capability launch (impact + credibility)
- AI industry shift (surprising + strategic)
- Marketing automation trend (practical + Shireen's wheelhouse)
- Tool integration that solves a common problem (practical + immediate value)

**Examples to skip:**
- Vague industry commentary ("AI is changing everything")
- Competitor news that doesn't involve Shireen's platforms
- Research papers without industry application
- Announcements that duplicate prior week's news

**Output:** 1 headline + 2-line summary of why it matters

---

### Step 3: Generate a ready-to-post LinkedIn post

Using patterns from the existing `linkedin-post` skill, write a post with:

**Structure:**
- Hook line (first sentence, NO question openers)
- 3-4 insight lines (why this matters to the audience)
- 1 practical takeaway (what to do with this info)
- Soft CTA (call to action, warm invitation — not aggressive)

**Style guide:**
- Length: Under 150 words
- Tone: Professional, confident, insightful
- No em-dashes (—), no dashes used as punctuation separators
- No emojis
- No humble-bragging or generic "AI is changing everything" takes
- Audience: Hiring managers, AI/tech companies, marketing teams
- Goal: Establish Shireen as an AI systems thinking specialist

**Example hook lines:**
- "Claude 4.X just shipped with native MCP support. Here's what this means for AI teams."
- "The AI tools landscape is consolidating. I'm tracking which ones actually survive."
- "Marketing teams are drowning in 14 different AI tools. One integration just solved that."

**Do NOT use:**
- Question openers ("Did you know...", "Have you considered...")
- Self-referential intro ("I just discovered...", "Thought you should know...")
- Vague positioning ("In today's AI landscape...")

---

### Step 4: Format the Telegram message

Send a clean Markdown message:

```
*LinkedIn Digest — [Date]*

*Top Story:*
[Headline]
Source: [publication/site if known]

*Why it matters:*
[2-line summary of impact/relevance]

---
*Ready to post:*

[Full LinkedIn post content]

_Copy and paste into LinkedIn_
```

---

### Step 5: Send via Telegram Bot API

Use curl to POST:

```bash
curl -s -X POST "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage" \
  -H "Content-Type: application/json" \
  -d "{\"chat_id\":\"${TELEGRAM_CHAT_ID}\",\"text\":\"${MESSAGE}\",\"parse_mode\":\"Markdown\"}"
```

Read `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID` from environment (root `.env` or shell env).

---

## Context Files to Load

Load these to ensure LinkedIn post quality:
- Shireen's profile context (smart AI specialist, not just marketer)
- Prior LinkedIn posts for tone + style consistency (if available in memory)
- LinkedIn post skill patterns from `.claude/skills/content-and-marketing/3-execution/linkedin-post/SKILL.md`

---

## Example Workflow: Thursday 8 May 2026

**Input:** Run at 8am MYT

**Step 1:** ai-news-digest agent searches last 24h, returns:
```
### Claude Code / Anthropic
- Claude 4.X now supports MCP natively
- New prompt caching improvements (20% faster)
- Anthropic introduces batch processing API

### AI Marketing Tools
- Competitor X launches AI-powered email tool
- Perplexity adds research sharing features
```

**Step 2:** Select top story
- "Claude 4.X native MCP support" — HIGH IMPACT (enables new workflows), HIGH SHAREABILITY (technical + practical), SHIREEN'S WHEELHOUSE (systems architecture)
- Decision: SELECT this story

**Step 3:** Generate LinkedIn post
```
Claude 4.X just shipped native MCP support. This changes how AI systems talk to the outside world.

For teams building AI workflows, MCP makes integration seamless. No more adapter layers. Your tools connect directly.

What this means: Teams can build more complex agent systems without fighting integration overhead. Faster iteration, more reliable systems.

If you're thinking about how AI fits into your operations, this is worth understanding. The tooling is getting smarter.
```

**Step 4:** Format Telegram message
```
*LinkedIn Digest — 8 May 2026*

*Top Story:*
Claude 4.X ships native MCP support
Source: Anthropic Releases

*Why it matters:*
Direct tool integration for AI agents means less integration overhead and faster iteration for teams building complex workflows. Changes how systems architecture works at scale.

---
*Ready to post:*

Claude 4.X just shipped native MCP support. This changes how AI systems talk to the outside world.

For teams building AI workflows, MCP makes integration seamless. No more adapter layers. Your tools connect directly.

What this means: Teams can build more complex agent systems without fighting integration overhead. Faster iteration, more reliable systems.

If you're thinking about how AI fits into your operations, this is worth understanding. The tooling is getting smarter.

_Copy and paste into LinkedIn_
```

**Step 5:** Send to Telegram → User copies and posts to LinkedIn

---

## Fallback Scenarios

- **No news found:** "No significant AI news today. Try again tomorrow or check LinkedIn trending topics for alternative angle."
- **All stories are duplicates of prior week:** "Top news is repeats from last week. Suggest: Comment on existing LinkedIn trends or publish a reflection post on a prior launch."
- **News exists but not Shireen-relevant:** "Found AI news but not aligned with positioning. Suggest: Skip today or write a meta-post about filtering signal from noise in AI."
