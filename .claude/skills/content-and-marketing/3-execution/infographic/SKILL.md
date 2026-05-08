# Skill: infographic

## Trigger

Use when asked to "create an infographic", "make an infographic about [topic]", or build branded data visualizations.

## How to Invoke

User says something like:
- "Create an infographic on [topic]"
- "Make an infographic about [topic]"
- "/infographic [topic]"
- "Build the infographic system" (first-time setup)

---

## Two Modes

### Mode A: Setup (first time only)
Scaffold the full infographic generation system for a project. Run this once before generating any infographics.
See `setup.md` in this folder for the full scaffold details, templates, QA agent, and Puppeteer script.

### Mode B: Generate (ongoing)
Create an infographic on a given topic using the existing system.

---

## Mode B: Generate

Run this when the user provides a topic.

### Step 1: Confirm the brief

Ask (one message, all at once):
1. What is the infographic about? (if not already provided)
2. Which template fits best?
   - Single topic (5-7 key points)
   - Comparison (A vs B)
   - Listicle (numbered steps or ranked items)
   - Cheatsheet (dense reference)
3. Any specific angle, audience, or message to land?
4. Where will it be posted? (LinkedIn, website, other)

### Step 2: Enter plan mode

Before writing any HTML:
- State the chosen template
- Outline the section structure (headline, sections, footer)
- List the key points to include
- Get Shireen's approval

### Step 3: Generate the HTML

Using the approved plan:
- Load CLAUDE.md brand rules
- Load the base template from `references/templates/`
- Write the full HTML/CSS file in one pass
- Save to `outputs/[topic-slug]/v1_[YYYY-MM-DD].html`
- Inline all CSS (no external stylesheets except Google Fonts CDN)
- Embed the headshot as an `<img>` tag pointing to `../../assets/headshot.png`

### Step 4: QA score it

Pass the HTML file to the QA scorer agent:
- Score against all 15+ criteria
- If < 95: auto-fix violations, re-render, re-score
- Repeat until 95+
- Overwrite the existing file -- do not create new numbered versions

### Step 5: Export to PNG

Run the Puppeteer export script:
```bash
node scripts/export-png.js outputs/[topic-slug]/v[N]_[date].html outputs/[topic-slug]/v[N]_[date].png
```

### Step 6: Self-check before showing

Before presenting any output to Shireen, run this checklist internally and fix any failures:

- [ ] Color palette matches the locked brand system above - no deviations
- [ ] Gold is present in header eyebrow, phase/category labels, and footer sign-off
- [ ] Semantic colors (rust/navy/forest) used only when layout has distinct categories - never applied randomly
- [ ] No em-dashes anywhere in copy
- [ ] All text passes contrast check against its background
- [ ] Canvas is exactly 1080px wide
- [ ] Footer sign-off bar present with avatar, FOLLOW label, name, and both links
- [ ] No horizontal overflow or clipped content
- [ ] Font loaded as Space Grotesk (not Arial/system fallback)

Only show output after all checks pass. Do not surface known issues for Shireen to catch.

### Step 7: Show the user

- Serve via local HTTP server and take a Playwright screenshot - never use file:// protocol
- State the output file path
- Show the QA score and what was fixed
- Ask: "Want any changes? Or is this ready to post?"

---

## Content Guidelines for Infographic Copy

- Headlines: punchy, direct, no em-dashes
- Key points: lead with the benefit or insight, not the mechanism
- Max 12 words per bullet point
- Numbers and data make it scannable -- use them
- Author block always: headshot + name + follow CTA + link pills

---

## Shireen's Default Brand (aiwithshireen.com)

**This palette is locked. Apply it to every infographic regardless of layout format (table, card, listicle, cheatsheet, comparison, or any other structure). Do not deviate without explicit instruction.**

### Base (always applied)
| Role | Hex | Usage |
|---|---|---|
| Background | `#0D0D0D` | Page/canvas background |
| Surface | `#111111` | Cards, cells, rows |
| Surface raised | `#181818` | Nested elements, stat blocks |
| Divider | `#1C1C1C` | Horizontal rules |
| Primary text | `#FFFFFF` | Headlines, strong labels |
| Secondary text | `#C8C8C8` | Body copy |
| Muted text | `#999999` | Captions, subtitles |
| Gold accent | `#C9A84C` | Primary brand color: eyebrow tags, phase labels, bullet dots, borders, cmd badges, sign-off |
| Gold dark bg | `#1C1600` | Tinted background behind gold text callouts |

### Semantic (for content columns or multi-category layouts)
Use these when a layout has distinct categories that benefit from visual differentiation (e.g. Pain/Fix/Result, Before/After, Problem/Solution):

| Role | Column bg | Label text | Usage |
|---|---|---|---|
| Pain / Problem / Before | `#5C1F12` | `#FF8A65` | Negative state, tension, problem |
| Fix / Solution / How | `#0F2340` | `#7AB8F5` | Structure, action, solution |
| Result / After / Outcome | `#0A2E1A` | `#5DC98A` | Success, outcome, aspiration |

The semantic colors appear in column/category **headers only**. Cell/row backgrounds stay `#111111`. The gold remains the dominant accent across phase labels, header, and footer.

### Typography
- Font: Space Grotesk (Google Fonts CDN)
- No fallback to Inter, Arial, or system fonts

### Locked elements (never modify)
- Header eyebrow tag: gold `#C9A84C` bg, black text, uppercase, letter-spacing 2.5px
- Footer sign-off bar: `#111` bg, avatar with gold border, gold FOLLOW label
- Bottom links: aiwithshireen.com | github.com/shireen168

---

## Output Naming Convention

`outputs/[topic-slug]/[slug]_[YYYY-MM-DD].html`

Example: `outputs/claude-rate-limits/session-system_2026-04-18.html`

Overwrite the file on each iteration. Do not create v1, v2, v3 variants.

---

## Tips from Charlie Hills' System

- The CLAUDE.md is the system's memory -- update it after every correction
- Inspiration images are inputs, not decoration -- Claude uses them to calibrate density
- The QA agent is non-negotiable: remove it and you spend hours iterating manually
