# Skill: brand-guidelines

## Trigger

Use when asked to "create brand guidelines", "build a brand document", "write brand standards", or "document brand identity".

## How to Invoke

```
/brand-guidelines
/brand-guidelines <company name>
```

Natural language triggers:
- "Create brand guidelines for [company]"
- "Generate a brand guide for my business"
- "Build brand guidelines for [company name]"
- "I want brand guidelines for [company]"

## Input Collection

If the user invokes the skill without full details, collect these before generating. Ask all at once in a single message -- do not prompt one field at a time.

**Required:**
- Company name
- Industry / what the company does (1-2 sentences)
- Target audience (who they serve)
- Brand personality (3-5 adjectives: e.g. "bold, approachable, modern")

**Optional (use smart defaults if not provided):**
- Existing colors (hex codes or color names)
- Existing fonts
- Logo description or style reference
- Tone of voice notes
- Competitors or brands to differentiate from

If all required fields are provided in the invocation, skip to Step 1.

---

## Process

### Step 1: Derive the design system

Before writing, derive:

**Color palette** (6 colors with hex codes and RGB values):
- Primary: dominant brand color (reflects personality + industry)
- Secondary: complementary supporting color
- Accent: high-contrast highlight for CTAs and key moments
- Dark: near-black for text and headers (e.g. #0d0d0d, #111827)
- Light: near-white for backgrounds (e.g. #fafaf8, #f5f5f0)
- Mid: muted tone for borders and secondary text

Name each color meaningfully (e.g. "Ink", "Cream", "Signal Red").

All hex values must be real, tested contrast pairs. Dark text on Light background minimum 7:1. Accent on Dark minimum 4.5:1.

**Typography** (2-3 typefaces, Google Fonts only):
- Display / Heading font: distinctive, brand-appropriate
- Body font: legible, readable at small sizes, pairs well
- Accent font (optional): for pull quotes, labels, UI elements

**Visual style direction** (1 paragraph): photography style, illustration approach, layout feel, texture/pattern usage.

---

### Step 2: Generate the brand guidelines document

Write the full brand guidelines as a Markdown file. Use the exact structure below.

**Critical:** Use the HTML component blocks defined in this skill for colors, typography specimens, and voice cards. These are styled by `brand-guidelines.css` and produce polished visual output in the PDF. Do not substitute plain tables for these sections.

The stylesheet path in the frontmatter must use the absolute Windows path below, adjusted to the correct company slug:

```markdown
---
pdf_options:
  format: A4
  margin: 35mm 22mm 28mm 22mm
  printBackground: true
  displayHeaderFooter: true
  headerTemplate: '<div style="font-size:7.5pt;color:#bbb;width:100%;text-align:right;padding-right:22mm;font-family:Arial,sans-serif;">[Company Name] Brand Guidelines</div>'
  footerTemplate: '<div style="font-size:7.5pt;color:#bbb;width:100%;text-align:center;font-family:Arial,sans-serif;"><span class="pageNumber"></span> / <span class="totalPages"></span></div>'
stylesheet: C:\Users\USER\OneDrive\Desktop\Executive Assistant\.claude\skills\brand-guidelines\brand-guidelines.css
---

# [Company Name] Brand Guidelines

<p class="meta">Version 1.0 &nbsp;·&nbsp; [YYYY-MM-DD]</p>

---

## 1. Brand Overview

### Who We Are
[2-3 sentence brand description]

### Mission
[One sentence: what we do and why it matters]

### Vision
[One sentence: the future we're building toward]

---

## 2. Brand Personality

### Personality Traits

- **[Trait 1]:** [one-line description]
- **[Trait 2]:** [one-line description]
- **[Trait 3]:** [one-line description]
- **[Trait 4]:** [one-line description]
- **[Trait 5]:** [one-line description]

### Brand Archetype
**[Archetype Name]** -- [2-sentence explanation of how this archetype shows up in the brand]

---

## 3. Target Audience

### Primary Audience
**Who:** [demographic + psychographic description]

**What they want:** [their core desire or problem]

**How we speak to them:** [tone and approach]

---

## 4. Color Palette

### Primary Colors

<div class="swatch-grid">
  <div class="swatch-card">
    <div class="swatch" style="background:[PRIMARY_HEX];"></div>
    <div class="swatch-name">[Primary Color Name]</div>
    <div class="swatch-hex">[PRIMARY_HEX]</div>
    <div class="swatch-rgb">rgb([r], [g], [b])</div>
    <div class="swatch-use">Primary brand color</div>
  </div>
  <div class="swatch-card">
    <div class="swatch" style="background:[SECONDARY_HEX];"></div>
    <div class="swatch-name">[Secondary Color Name]</div>
    <div class="swatch-hex">[SECONDARY_HEX]</div>
    <div class="swatch-rgb">rgb([r], [g], [b])</div>
    <div class="swatch-use">Supporting / secondary</div>
  </div>
  <div class="swatch-card">
    <div class="swatch" style="background:[ACCENT_HEX];"></div>
    <div class="swatch-name">[Accent Color Name]</div>
    <div class="swatch-hex">[ACCENT_HEX]</div>
    <div class="swatch-rgb">rgb([r], [g], [b])</div>
    <div class="swatch-use">CTAs and key highlights</div>
  </div>
</div>

### Neutral Colors

<div class="swatch-grid">
  <div class="swatch-card">
    <div class="swatch" style="background:[DARK_HEX];"></div>
    <div class="swatch-name">[Dark Color Name]</div>
    <div class="swatch-hex">[DARK_HEX]</div>
    <div class="swatch-rgb">rgb([r], [g], [b])</div>
    <div class="swatch-use">Text and headers</div>
  </div>
  <div class="swatch-card">
    <div class="swatch" style="background:[LIGHT_HEX]; border: 1px solid #e8e8e8;"></div>
    <div class="swatch-name">[Light Color Name]</div>
    <div class="swatch-hex">[LIGHT_HEX]</div>
    <div class="swatch-rgb">rgb([r], [g], [b])</div>
    <div class="swatch-use">Backgrounds</div>
  </div>
  <div class="swatch-card">
    <div class="swatch" style="background:[MID_HEX];"></div>
    <div class="swatch-name">[Mid Color Name]</div>
    <div class="swatch-hex">[MID_HEX]</div>
    <div class="swatch-rgb">rgb([r], [g], [b])</div>
    <div class="swatch-use">Borders and secondary text</div>
  </div>
</div>

### Color Usage Rules
- [Rule 1]
- [Rule 2]
- [Rule 3]

---

## 5. Typography

### Typefaces

| Role | Font | Weights | Google Fonts |
|------|------|---------|--------------|
| Display / Heading | [Font Name] | 700, 800 | fonts.google.com/specimen/[font-slug] |
| Body | [Font Name] | 400, 500 | fonts.google.com/specimen/[font-slug] |
| Accent / Label | [Font Name] | 400, 600 | fonts.google.com/specimen/[font-slug] |

### Type Specimens

<div class="type-specimen">
  <div class="type-label">H1 -- Display / 56px / 800</div>
  <div class="type-sample" style="font-family:'[Display Font]',serif; font-size:26pt; font-weight:800; line-height:1.1;">[Company Name] makes it simple.</div>
</div>

<div class="type-specimen">
  <div class="type-label">H2 -- Section Heading / 40px / 700</div>
  <div class="type-sample" style="font-family:'[Display Font]',serif; font-size:19pt; font-weight:700; line-height:1.2;">Built for the people who do the work.</div>
</div>

<div class="type-specimen">
  <div class="type-label">Body -- 16px / 400</div>
  <div class="type-sample" style="font-family:'[Body Font]',sans-serif; font-size:10pt; font-weight:400; line-height:1.65;">[A sample sentence written in the brand's voice that demonstrates how body copy looks at reading size. Clear, direct, and easy to scan.]</div>
</div>

<div class="type-specimen">
  <div class="type-label">Label / Accent -- 11px / 600 / uppercase</div>
  <div class="type-sample" style="font-family:'[Accent Font]',sans-serif; font-size:7pt; font-weight:600; letter-spacing:0.1em; text-transform:uppercase;">Category Label &nbsp;·&nbsp; Section Title &nbsp;·&nbsp; Tag</div>
</div>

### Type Scale

| Element | Font | Size | Weight | Line Height |
|---------|------|------|--------|-------------|
| H1 | [Display Font] | 56px / 3.5rem | 800 | 1.1 |
| H2 | [Display Font] | 40px / 2.5rem | 700 | 1.2 |
| H3 | [Display Font] | 28px / 1.75rem | 700 | 1.3 |
| Body Large | [Body Font] | 18px / 1.125rem | 400 | 1.7 |
| Body | [Body Font] | 16px / 1rem | 400 | 1.65 |
| Caption | [Body Font] | 13px / 0.8125rem | 500 | 1.5 |
| Label | [Accent Font] | 11px / 0.6875rem | 600 | 1.4 |

### Typography Rules
- [Rule 1]
- [Rule 2]
- [Rule 3: Minimum contrast ratio: 4.5:1 for body text (WCAG AA)]

---

## 6. Logo Guidelines

### Logo Versions
- **Primary:** [description of primary horizontal lockup]
- **Stacked:** [description of stacked variant]
- **Icon / Mark:** [description of standalone mark, when to use]

### Clear Space
Minimum clear space around the logo: equal to the cap-height of the wordmark on all sides.

### Usage Rules

<div class="rule-grid">
  <div class="rule-item rule-item--do">
    <div class="rule-badge">Do</div>
    <p>[Approved use 1]</p>
  </div>
  <div class="rule-item rule-item--do">
    <div class="rule-badge">Do</div>
    <p>[Approved use 2]</p>
  </div>
  <div class="rule-item rule-item--dont">
    <div class="rule-badge">Don't</div>
    <p>Stretch or distort the logo</p>
  </div>
  <div class="rule-item rule-item--dont">
    <div class="rule-badge">Don't</div>
    <p>Apply drop shadows or gradients to the logo</p>
  </div>
  <div class="rule-item rule-item--dont">
    <div class="rule-badge">Don't</div>
    <p>Place on backgrounds with insufficient contrast</p>
  </div>
  <div class="rule-item rule-item--dont">
    <div class="rule-badge">Don't</div>
    <p>[Brand-specific rule]</p>
  </div>
</div>

---

## 7. Brand Voice & Tone

### Voice
**Always:** [3-4 adjectives] -- [one sentence describing the consistent brand character]

### Tone in Context

<div class="tone-grid">
  <div class="tone-card">
    <div class="tone-label">Do say</div>
    <div class="tone-text">"[Example of on-brand copy]"</div>
  </div>
  <div class="tone-card tone-card--dont">
    <div class="tone-label">Don't say</div>
    <div class="tone-text">"[Example of off-brand copy]"</div>
  </div>
  <div class="tone-card">
    <div class="tone-label">Do say</div>
    <div class="tone-text">"[Second on-brand example]"</div>
  </div>
  <div class="tone-card tone-card--dont">
    <div class="tone-label">Don't say</div>
    <div class="tone-text">"[Second off-brand example]"</div>
  </div>
</div>

### Tone by Context

| Context | Tone | Example |
|---------|------|---------|
| Marketing copy | [tone] | "[example phrase]" |
| Social media | [tone] | "[example phrase]" |
| Customer support | [tone] | "[example phrase]" |
| Error messages / UI | [tone] | "[example phrase]" |

### Writing Rules
- [Rule 1]
- [Rule 2]
- [Rule 3]

### Words We Use / Avoid

| Use | Avoid |
|-----|-------|
| [word/phrase] | [word/phrase] |
| [word/phrase] | [word/phrase] |
| [word/phrase] | [word/phrase] |

---

## 8. Imagery & Visual Style

### Photography Style
[2-3 sentence description: lighting, subject matter, mood, composition]

### Illustration Style
[2-3 sentence description: style, line weight, color use, when to use]

### Iconography
[Style description: filled vs outline, corner radius, stroke weight]

### What to Avoid
- [Visual element or style to avoid]
- [Visual element or style to avoid]

---

## 9. Digital Application

### Web & App

| Element | Color | Notes |
|---------|-------|-------|
| Page background | [Color Name] [hex] | Primary surface |
| Body text | [Color Name] [hex] | Minimum 4.5:1 contrast |
| Primary CTA | [Color Name] [hex] bg, [Color] text | Accent color |
| Secondary CTA | [style description] | Ghost / outline style |
| Links | [Color Name] [hex] | Underline on hover |
| Border / divider | [Color Name] [hex] | 1px, subtle |
| Border radius | [value] | e.g. 6px standard, 12px cards |
| Shadow | [description] | e.g. 0 2px 8px rgba(0,0,0,0.08) |

### Social Media

| Platform | Brand colors | Cover style | Post style |
|----------|-------------|-------------|------------|
| Instagram | [colors] | [description] | [description] |
| LinkedIn | [colors] | [description] | [description] |
| Facebook | [colors] | [description] | [description] |

---

## 10. Brand Don'ts

The most important rules to protect brand integrity:

1. [Don't 1]
2. [Don't 2]
3. [Don't 3]
4. [Don't 4]
5. [Don't 5]

---

*These guidelines are a living document. Update as the brand evolves.*
```

Fill every section with real, specific content. No placeholder text in the final output. Replace all bracketed tokens with actual values.

---

### Step 3: Save the Markdown file

Save to:
```
projects/<company-slug>/brand-guidelines/brand-guidelines.md
```

Where `<company-slug>` is the company name lowercased, spaces replaced with hyphens.

Create the full path if it doesn't exist.

---

### Step 4: Convert to PDF

Run from the Executive Assistant root directory:

```bash
npx --yes md-to-pdf "projects/<company-slug>/brand-guidelines/brand-guidelines.md" --stylesheet "C:\Users\USER\OneDrive\Desktop\Executive Assistant\.claude\skills\brand-guidelines\brand-guidelines.css"
```

The `--stylesheet` flag overrides any stylesheet in the frontmatter as a safety fallback. The PDF saves alongside the `.md` file automatically as `brand-guidelines.pdf`.

If conversion fails:
- Check the `.md` file was saved and frontmatter is valid YAML
- Try without the stylesheet flag first to isolate the issue
- If still failing, report the error and deliver the Markdown file only

---

### Step 5: Confirm output

Tell the user:
- Path to the `.md` file
- Path to the `.pdf` file
- 2-3 line summary of the brand identity created

Offer:
- "Want me to generate a DESIGN.md from these guidelines for UI builds?"
- "Want to adjust any section?"
- "Want me to create social media post templates using these guidelines?"

---

## Files in This Skill

```
.claude/skills/brand-guidelines/
  SKILL.md                  ← this file
  brand-guidelines.css      ← PDF stylesheet (referenced at runtime)
```

## Stylesheet Components Reference

The CSS provides these styled HTML components for use inside the Markdown:

| Component | Class | Purpose |
|-----------|-------|---------|
| Color swatch grid | `.swatch-grid` > `.swatch-card` | Visual color palette with hex/RGB |
| Type specimen | `.type-specimen` | Font preview at size |
| Tone cards | `.tone-grid` > `.tone-card` / `.tone-card--dont` | Do/don't voice examples |
| Logo rules | `.rule-grid` > `.rule-item--do` / `.rule-item--dont` | Logo usage do/don't |
| Meta line | `.meta` | Subtitle / version line under h1 |
| Page break | `.page-break` | Force new page |

## Notes

- Google Fonts only for typography
- All hex values must pass WCAG AA contrast (4.5:1 body, 3:1 large text)
- CSS stylesheet: `.claude/skills/brand-guidelines/brand-guidelines.css`
- PDF tool: `npx md-to-pdf` (installs via npx on first use, no prior install needed)
- Output: `projects/<company-slug>/brand-guidelines/`
- Markdown is the source of truth -- PDF is a rendered export
