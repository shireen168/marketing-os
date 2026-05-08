---
name: campaign-plan
description: Use when someone asks to plan a marketing campaign, create a campaign brief, build a launch plan, map out a go-to-market strategy, or structure a marketing initiative from brief to execution.
argument-hint: [campaign goal or product name]
disable-model-invocation: false
---

# Skill: campaign-plan

Turn a campaign goal into a structured brief with channels, timeline, content mix, and KPIs.

## How to Invoke

- "Plan a campaign for [product/goal]"
- "Create a campaign brief for [launch]"
- "Build a marketing plan for [initiative]"
- "Map out a go-to-market for [product]"
- "/campaign-plan [goal]"

---

## Step 0: Gather Inputs

Ask in one message if not already provided:

1. **Goal:** What does this campaign need to achieve? (awareness, leads, sales, followers, signups)
2. **Product/offer:** What is being promoted?
3. **Audience:** Who specifically? (demographics, platform behavior)
4. **Timeline:** When does it start? How long does it run?
5. **Channels:** Which platforms are in scope? (FB, IG, LinkedIn, email, paid ads, etc.)
6. **Budget:** Rough budget or "organic only"?
7. **Assets available:** What content/creative exists already?

---

## Step 1: Campaign Brief

Output a one-page brief:

```
## Campaign Brief: [Campaign Name]

**Goal:** [specific, measurable]
**Audience:** [specific segment]
**Timeline:** [start - end date]
**Channels:** [list]
**Budget:** [amount or "organic only"]

### Core Message
[One sentence: what we want the audience to feel or do after seeing this campaign]

### Hook Angles (top 3)
1. [angle]
2. [angle]
3. [angle]
```

---

## Step 2: Channel Plan

Build a channel breakdown table:

| Channel | Role in Campaign | Content Type | Frequency | Tone |
|---|---|---|---|---|
| [channel] | [awareness / conversion / retention] | [posts / stories / emails] | [x/week] | [adj] |

---

## Step 3: Content Calendar (Week-by-Week)

Build a phase-based calendar:

**Phase 1: Awareness (Week 1-2)**
| Day | Channel | Content | Goal |
|---|---|---|---|

**Phase 2: Consideration (Week 3-4)**
| Day | Channel | Content | Goal |
|---|---|---|---|

**Phase 3: Conversion (Week 5+)**
| Day | Channel | Content | Goal |
|---|---|---|---|

Adapt phases to the timeline given. Shorter campaigns = compress phases.

---

## Step 4: KPIs

| Metric | Baseline | Target | How to Measure |
|---|---|---|---|
| [metric] | [current] | [goal] | [tool/method] |

Include: reach, engagement rate, click-through, conversions, cost per result (if paid).

---

## Step 5: Quick-Start Checklist

Output 5-7 actionable first steps to kick off the campaign immediately:

- [ ] [action]
- [ ] [action]

---

## Notes

- If Sunny Homemade: load `references/sunny-homemade/brand-identity.md` + `content-rules.md` before building plan
- If LinkedIn/AI portfolio: professional positioning, thought leadership angle, no aggressive CTAs
- If organic only: focus on content compounding (pillars that get shared/saved, not just likes)
- Always use deep-research for competitor landscape if the category is unfamiliar
- Flag if the timeline is unrealistic for the goal (e.g., 1 week to build brand awareness)
