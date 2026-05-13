# Complete Example: Financial Services Campaign

This example shows how the Marketing OS workflow works. Built with Claude Code + gstack, this same system adapts to **any industry**: HR recruiting, legal briefs, sales campaigns, product launches, internal communications.

**Product:** Accounting OS: a SaaS tool that simplifies bookkeeping for small businesses

**Key insight:** Each stage uses a gstack slash command (/brainstorm, /investigate, /plan-ceo-review) that builds structured thinking. Stage 5+ uses native Claude for content generation. This combination of structured workflow commands + freestyle generation is what makes context preservation work and 40 minutes possible instead of 5-7 days.

---

## Stage 1: Brief

**Command:** `/brainstorm`

**Input:**
```
Create a marketing brief for Accounting OS, a SaaS tool that 
automates bookkeeping for small businesses. The tool integrates 
with bank accounts and generates financial reports automatically.

Include: product description, target audience, key benefits, 
primary channels, success metrics.
```

**Output:**

```
# Marketing Brief: Accounting OS

## Product
Accounting OS is a cloud-based bookkeeping platform that automatically 
syncs bank transactions and generates financial reports. No manual 
data entry. No spreadsheets.

## Target Audience
Small business owners (1-50 employees) who currently use spreadsheets 
or hire accountants for bookkeeping. Age 28-55, revenue $500K-$5M.

## Key Benefits
- Saves 10+ hours/month on bookkeeping
- Real-time financial visibility
- Compliance-ready reports
- No accounting background required

## Primary Channels
LinkedIn (decision-makers), Facebook (business communities), 
TikTok (younger founders), Twitter/X (founder network)

## Success Metrics
- Website traffic: 500 leads/month
- Trial signups: 50/month
- Free-to-paid conversion: 20%
- Customer acquisition cost: <$50
```

---

## Stage 2: Brand Voice

**Command:** `/brainstorm`

**Input:**
```
Define brand voice for Accounting OS. Our target is busy small 
business owners who find accounting overwhelming.

Provide: target persona, tone of voice, key messaging pillars, 
sample phrases that sound like our brand.
```

**Output:**

```
# Brand Voice: Accounting OS

## Persona
Meet Sam: 35-year-old founder who just hired 15 people. Spends 
12 hours/month wrestling with spreadsheets instead of growing 
the business. Smart but not accounting-savvy. Values simplicity 
and getting back to work.

## Tone
- Confident (we know accounting is hard)
- Friendly (not corporate-speak)
- Clear (no jargon)
- Practical (solutions, not theory)

## Messaging Pillars
1. **Get Back to Work** - Stop doing accounting, start growing
2. **Peace of Mind** - Real-time visibility into your finances
3. **Compliance Built In** - Taxes handled, rules followed, automatically

## Sample Phrases
- "Your accountant in the cloud"
- "10 hours back to your business every month"
- "Spreadsheets are so 2010"
- "Stop guessing about your numbers"
- "Accounting that doesn't feel like accounting"
```

---

## Stage 3: Research

**Command:** `/investigate`

**Input:**
```
Research the small business accounting software market for 
Accounting OS.

Provide: PESTLE analysis summary, TAM/SAM/SOM, top 3 competitors, 
market trends, customer pain points.
```

**Output:**

```
# Market Research: Accounting OS

## Market Size
- TAM (Total): $30B (all accounting/bookkeeping globally)
- SAM (Serviceable): $5B (cloud accounting in US/EU)
- SOM (Serviceable Obtainable): $200M (our focus: SMBs <50 people)

## Top Competitors
1. QuickBooks - Entrenched, expensive ($300+/mo), complicated
2. Wave - Free but outdated UI, slow customer support
3. Freshbooks - Focused on service businesses, not product companies

## Market Trends
- 65% of SMBs still use spreadsheets for accounting
- Cloud adoption growing 18%/year
- AI/automation expectations rising (auto-categorization, reporting)

## Customer Pain Points
- Manual data entry (5-10 hours/month)
- Error-prone spreadsheets
- Compliance confusion (taxes, VAT, SOX)
- Hidden costs (accountant fees: $150-300/month)
- Integration headaches (bank → tool → accountant)

## Competitive Advantage
- Simplest onboarding (10 minutes vs 2 hours for competitors)
- Automatic bank sync (competitors charge extra)
- Transparent pricing (no hidden fees)
- Vertical focus (we understand SaaS cash flow, not just general SMBs)
```

---

## Stage 4: Strategy

**Command:** `/plan-ceo-review`

**Input:**
```
Create marketing strategy for Accounting OS using the research 
and brand voice above.

Provide: positioning statement, messaging hierarchy, 
recommended channels with rationale, go-to-market timeline.
```

**Output:**

```
# Marketing Strategy: Accounting OS

## Positioning
"The simplest bookkeeping platform for founders who'd rather 
focus on building. Accounting that doesn't feel like accounting."

## Messaging Hierarchy
### Primary Message
"10 hours back to your business every month"
(appeals to: efficiency, ROI, time back)

### Supporting Messages
1. "Bank connections that just work" (appeals to: simplicity)
2. "Compliance built in, you sleep at night" (appeals to: peace of mind)
3. "No accountant fees, no learning curve" (appeals to: cost savings)

## Channel Strategy

| Channel | Why | Content Type | Cadence |
|---------|-----|--------------|---------|
| LinkedIn | Reach decision-makers, founders, CFOs | Case studies, founder stories, financial tips | 3x/week |
| TikTok | Reach younger founders, viral potential | Quick wins, "watch me do accounting in 2 min", founder fails | 2x/week |
| Twitter/X | Founder community, industry discourse | Accounting hot takes, thread about founder struggles | Daily |
| Facebook | Reach SMB owners in business groups | Case studies, ROI calculator, comparison guides | 2x/week |

## Go-to-Market Timeline
- Month 1: Case study content + founder interviews (LinkedIn, Twitter)
- Month 2: Viral TikTok series launches
- Month 3: Paid ads on LinkedIn, Facebook (case studies)
- Month 4: Review sites, integrations marketing (Zapier, Slack)

## Success Metrics
- Month 1: 1,000 website visits, 50 trial signups
- Month 3: 3,000 visits, 150 trials, 20% free-to-paid conversion
- Month 6: 500 paying customers, $50K MRR
```

---

## Stage 5: Content

**Context:** Paste Brief (Stage 1), Brand Voice (Stage 2), and Strategy (Stage 4) into Claude panel. Then send native prompt below.

**Prompt (Native Claude):**
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

**Output:**

### Facebook
```
Your accountant costs $200/month and takes 2 weeks to get you 
answers. Accounting OS costs $29/mo and gives you answers in 
2 seconds. Not even close.

Try free: [link]

#AccountingOS #SmallBusiness #Startup
```

### Instagram
```
Plot twist: doing your own accounting doesn't have to suck.

@accounting_os does the boring stuff so you can do the important stuff.

3 days free. No credit card.

#SmallBizTips #FounderLife #Accounting #AccountingOS
#SaaS #StartupLife #Productivity
```

### TikTok
```
[Scene: Founder at desk, surrounded by spreadsheets, looking stressed]
VOICEOVER: "Every founder spends 10 hours a month doing this."

[Cut to: Same founder in Accounting OS, 2 clicks, big smile]
VOICEOVER: "What if you could do this instead?"

[Text on screen: "Accounting OS. 10 hours back to your business."]

[CTA: Download free link]
```

### LinkedIn
```
The Hidden Cost of QuickBooks for Founders

A founder sent me this spreadsheet last week. It was their 
"QuickBooks": 47 tabs, 200+ manual entries, 12 hours a month 
of their time.

They're not alone. 65% of SMBs still do this.

Here's what they switched to:

1. Connected their bank once. Done.
2. Transactions categorize automatically.
3. They have 10 hours back.

It's called Accounting OS. Founder-built for founder problems.

The best part? $29/month instead of $300 + accountant fees.

[Try free, no credit card]

#Startups #Founder #Accounting #SmallBusiness #SaaS
```

### Twitter/X (Thread)
```
🧵 Why founders still use spreadsheets for accounting (and why 
it's costing them):

1/ QuickBooks was built for accountants in 1992. 
It still feels like 1992.
- 3-hour learning curve
- $300+/month
- No bank sync
- Founders hate it but there's "nothing better"

2/ Wave is free.
But free × bad UX = expensive waste of time.
- Outdated interface
- Painfully slow sync
- Customer support is a 3-day email chain
- You save $300 but lose 10 hours/month

3/ Freshbooks is for agencies.
If you're a SaaS founder, it doesn't get your business.
- Built for service businesses
- Doesn't understand SaaS cash flow
- Integrations are expensive add-ons
- Wrong tool for the job

4/ So what do founders do?
They build their own in Excel/Sheets.
- 47 tabs, 200+ manual entries
- 12 hours/month of their life
- Error-prone, always out of sync
- One bad formula and taxes become complicated

5/ This is insane.
In 2024 we have AI for everything but... 
accounting for founders still sucks.

That's why we built Accounting OS.
- Bank sync in 5 minutes
- Auto-categorization
- Zero learning curve
- $29/month (founder pricing)

[Try free]
```

### Threads
```
hot take: most accounting software was built by people who've 
never run a startup

it shows

(Accounting OS was built by 3 founders who bootstrapped from 
$0 to $2M ARR)

come at me
```

---

## Stage 6: Reports

**Context:** Paste all previous stage outputs into Claude panel. Then send native prompt below.

**Prompt (Native Claude):**
```
Create a sample campaign report for Accounting OS showing: 
projected reach per platform, estimated engagement rates, 
projected conversions, ROI estimate. Use industry benchmarks.
```

**Output:**

```
# Campaign Report: Accounting OS (Month 1)

## Platform Performance

| Platform | Impressions | Engagement Rate | Conversions | CPA |
|----------|-------------|-----------------|-------------|-----|
| LinkedIn | 25,000 | 3.2% | 24 | $42 |
| TikTok | 150,000 | 4.1% | 36 | $28 |
| Twitter/X | 40,000 | 2.8% | 14 | $35 |
| Facebook | 80,000 | 1.9% | 8 | $75 |
| **Total** | **295,000** | **3.1%** | **82** | **$41** |

## Conversion Funnel

```
295,000 impressions
    ↓ (3.1% click-through)
9,145 website visits
    ↓ (45% try free)
4,115 trial signups
    ↓ (20% conversion to paid)
823 paying customers
```

## Revenue Projection

| Metric | Value |
|--------|-------|
| Trial Signups (Month 1) | 4,115 |
| Paid Customers (Month 1) | 823 |
| MRR (Month 1) @ $29 | $23,867 |
| CAC (blended) | $41 |
| CAC Payback Period | 1.4 months |
| Year 1 ARR (Month 1 cohort) | $199,000 |

## ROI Analysis

**Campaign Spend:** $3,362 (82 conversions × $41 CPA)
**Year 1 Revenue (Month 1 cohort):** $199,000
**Year 1 ROI:** 5,821%
**Payback Period:** 6 weeks

## Key Insights

- TikTok performs best (lowest CAC $28, highest engagement)
- LinkedIn converts best (high-intent audience)
- Facebook needs optimization (highest CAC $75)
- Overall CAC $41 is healthy (LTV $870 @ 30 months)

## Recommended Actions

1. Double down on TikTok content (highest ROI)
2. Increase LinkedIn budget (converts best)
3. Pause Facebook until creative refresh
4. A/B test Twitter copy (low engagement)
5. Focus on viral TikTok series (compound effect)
```

---

## Summary

**From idea to metrics in 6 stages:**
- Brief: 10 min (slash command: /brainstorm)
- Brand Voice: 10 min (slash command: /brainstorm)
- Research: 10 min (slash command: /investigate)
- Strategy: 15 min (slash command: /plan-ceo-review)
- Content: 20 min (native Claude prompt)
- Reports: 10 min (native Claude prompt)

**Total: 75 minutes** (or 30 min if you're fast)

### Why This Works

Stages 1-4 use gstack slash commands (/brainstorm, /investigate, /plan-ceo-review) for structured thinking. These skills preserve context automatically from previous stages. Stages 5-6 use native Claude for freestyle content generation, pasting in all prior outputs as context. This hybrid approach gives you structured workflow benefits plus creative generation flexibility.

**Next:** Copy these artifacts. Use them directly. Iterate. Ship.

---

**Questions?** See [workflow.md](../workflow.md) troubleshooting.
