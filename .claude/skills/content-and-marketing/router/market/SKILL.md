---
name: market
description: Use when someone says "/market" or asks for marketing help without knowing which specific skill to use. Routes intent to the right marketing skill or executes directly for brand voice, copy, and campaign planning tasks.
argument-hint: [what you need: "content calendar", "ad copy", "campaign brief", "competitor research", etc.]
---

# Skill: market

Marketing suite orchestrator. Routes your request to the right skill or executes directly.

## How to Invoke

```
/market [what you need]
```

Or just describe what you want -- this skill maps your intent to the right workflow.

---

## Routing Table

Read the user's request and route immediately. Don't ask for clarification unless the intent is genuinely ambiguous.

| If the user wants... | Route to |
|---|---|
| Sunny Homemade FB/IG content calendar or captions | Follow `sunny-homemade-content` skill |
| LinkedIn post for Shireen | Follow `linkedin-post` skill |
| Competitor ad/content research | Follow `competitive-ads-extractor` skill |
| Research on any topic (deep, sourced) | Follow `deep-research` skill |
| AI or Claude Code news | Follow `ai-news-digest` skill |
| Brand guidelines for a client or company | Follow `brand-guidelines` skill |
| Design system / DESIGN.md for a brand | Follow `design-md-fetcher` skill |
| Infographic generation | Follow `infographic` skill |
| Image generation | Follow `imagen` skill |
| Next portfolio project ideas | Follow `portfolio-brainstorm` skill |
| Brand voice analysis or writing in a specific voice | Follow `brand-voice` skill (inline below) |
| Ad copy, headlines, email subjects, CTAs, landing page copy | Follow `copy-gen` skill (inline below) |
| Campaign brief, launch plan, go-to-market | Follow `campaign-plan` skill (inline below) |

---

## How to Follow a Routed Skill

When routing to an existing skill:

1. State: "Routing to [skill-name]."
2. Read that skill's SKILL.md from `.claude/skills/[skill-name]/SKILL.md`
3. Follow it exactly from Step 0

When executing a new skill (brand-voice, copy-gen, campaign-plan):

1. State: "Running [skill-name] workflow."
2. Follow the steps in that skill's SKILL.md from `.claude/skills/[skill-name]/SKILL.md`

---

## If Intent Is Ambiguous

Ask one clarifying question only:

> "Are you working on Sunny Homemade content, LinkedIn/personal brand, a client campaign, or something else?"

Then route based on the answer.

---

## Notes

- Never execute multiple skills in one call without checking with the user first
- If the user's request spans two skills (e.g., "competitor research + write ad copy based on it"), confirm the order before starting
- Build skills are out of scope for /market: web-builder, mvp-builder handle code projects
