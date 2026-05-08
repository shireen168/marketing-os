---
name: brand-voice
description: Use when someone asks to analyze brand voice, extract voice from copy samples, define tone of voice, or write copy in a specific brand's style.
argument-hint: [brand name or "paste samples"]
disable-model-invocation: false
---

# Skill: brand-voice

Extract a brand voice profile from copy samples and apply it to new copy.

## How to Invoke

- "Analyze the brand voice in these samples"
- "Extract voice from [brand]'s copy"
- "Write in the style of [brand]"
- "What is [brand]'s tone of voice?"
- "Apply [brand] voice to this copy"

---

## Step 0: Gather Inputs

Ask in one message (do not ask one at a time):

1. **Samples:** Paste 3-5 pieces of copy from the brand (captions, headlines, website copy, email subject lines). Or provide a URL and I'll fetch key copy.
2. **Purpose:** Are we (a) analyzing voice for documentation, (b) applying voice to new copy, or both?
3. If applying voice: what is the new copy for? (ad, email, landing page, caption, etc.)

---

## Step 1: Extract Voice Profile

Analyze samples across these 6 dimensions:

| Dimension | What to look for |
|---|---|
| **Tone** | Warm/cool, formal/casual, confident/humble, playful/serious |
| **Sentence rhythm** | Short punchy fragments vs long flowing sentences; average length |
| **Vocabulary level** | Simple everyday words vs technical/elevated; any signature words |
| **Personality** | 3 adjectives that describe the brand as if it were a person |
| **What it avoids** | Clichés, jargon, phrases that feel off-brand based on samples |
| **CTA style** | Direct command, question, soft invite, or no CTA |

---

## Step 2: Write the Voice Profile

Output a clean voice profile in this format:

```
## [Brand Name] Voice Profile

**Personality:** [3 adjectives]
**Tone:** [2-3 sentence description]
**Sentence style:** [description of rhythm and length]
**Vocabulary:** [what words feel right; what to avoid]
**Avoid:** [list of 5-8 phrases or patterns that feel off-brand]
**CTA style:** [how the brand closes]

### Voice in Action

| Instead of | Write |
|---|---|
| [generic phrase] | [on-brand alternative] |
| [generic phrase] | [on-brand alternative] |
| [generic phrase] | [on-brand alternative] |
```

---

## Step 3: Apply Voice (if requested)

If the user wants new copy written in this voice:
1. State the voice rules you are applying
2. Generate 3 variations of the requested copy
3. After each variation, note the 1-2 voice choices made

---

## Notes

- If samples are too few (fewer than 3 pieces) or too short (single words), say so - voice extraction needs substance
- If the brand is Shireen's own LinkedIn, reference `context/me.md` for positioning
- If the brand is Sunny Homemade, load `references/sunny-homemade/brand-identity.md` and `content-rules.md` first
- Never hallucinate brand personality - only infer from what the samples actually show
