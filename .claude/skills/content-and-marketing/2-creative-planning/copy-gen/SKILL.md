---
name: copy-gen
description: Use when someone asks to write ad copy, generate headlines, write email subject lines, create CTAs, write landing page copy, or generate marketing copy of any kind.
argument-hint: [copy type + product/topic]
disable-model-invocation: false
---

# Skill: copy-gen

Generate marketing copy variations across formats: ads, headlines, email subjects, CTAs, landing pages, social captions.

## How to Invoke

- "Write ad copy for [product]"
- "Generate 5 headlines for [topic]"
- "Write email subject lines for [campaign]"
- "Create CTAs for [landing page]"
- "Write landing page copy for [product]"
- "/copy-gen [brief description]"

---

## Step 0: Gather Context

Ask in one message if not already provided:

1. **What:** Copy type (pick one: ad, headline, email subject, CTA, landing page section, social caption, other)
2. **Product/topic:** What is the copy about?
3. **Audience:** Who is it for? (be specific - "30s Malaysian women interested in health", not "everyone")
4. **Goal:** What action should the reader take?
5. **Tone:** Any brand voice to match? (paste samples or name a reference brand, or leave blank for default)
6. **Constraints:** Character limits, platform restrictions, words to avoid?

---

## Step 1: Generate Variations

Produce **5 variations** for the requested copy type. For each variation, use a different approach:

| Variation | Approach |
|---|---|
| 1 | Direct benefit statement (what the reader gets) |
| 2 | Problem-first (name the pain before the solution) |
| 3 | Curiosity/intrigue (open loop, incomplete thought) |
| 4 | Social proof / authority angle |
| 5 | Emotional / aspirational angle |

---

## Output Format

### [Copy Type] for [Product]

**Audience:** [confirmed audience]
**Goal:** [confirmed goal]

---

**V1 - Benefit:**
[copy]

**V2 - Problem-first:**
[copy]

**V3 - Curiosity:**
[copy]

**V4 - Social proof:**
[copy]

**V5 - Aspirational:**
[copy]

---

*Note which 1-2 you'd test first and why.*

---

## Format-Specific Rules

**Ad copy:** Headline + body + CTA as a unit. Include character count if a limit was given.

**Headlines:** Title case. No ending punctuation unless it's a question. One idea per headline.

**Email subjects:** Under 50 characters ideal. Note preview text suggestion alongside each.

**CTAs:** Verb-first. Specific over generic ("Start your audit" not "Learn more"). 2-5 words.

**Landing page sections:** Output as Hero, Value prop, Features (3 bullets), CTA block. Label each section clearly.

**Social captions:** Match platform culture. LinkedIn: professional + insight. FB/IG Sunny Homemade: load `references/sunny-homemade/content-rules.md` first.

---

## Notes

- If Sunny Homemade: always dual-language (Mandarin first), no Malay, no em-dashes. Load brand refs before writing.
- If LinkedIn/Shireen personal brand: professional, AI specialist positioning.
- Never write generic "AI is changing everything" takes.
- If no brand voice provided, default to: confident, clear, no filler words, direct benefit.
