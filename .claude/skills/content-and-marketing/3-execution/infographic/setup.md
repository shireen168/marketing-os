# Mode A: Infographic System Setup

Run this when the user says "build the infographic system" or "set up infographics" for a project.
This is a one-time scaffold. After setup, use Mode B in SKILL.md to generate infographics.

---

## Folder Structure to Scaffold

Create inside the target project (default: `projects/infographic-system/`):

```
projects/infographic-system/
  CLAUDE.md                     <- brand rules, canvas size, QA rules
  assets/
    headshot.png                <- placeholder (user adds their own)
    logos/                      <- tool logos the user references often
  references/
    inspiration/                <- 3-5 example infographics user admires
    design-guidelines.md        <- typography, spacing, colour palette
    templates/
      single-topic.html         <- single topic, 5-7 key points
      comparison.html           <- 2-column A vs B layout
      listicle.html             <- numbered list format
      cheatsheet.html           <- dense reference sheet
  agents/
    qa-scorer.md                <- QA agent definition
  outputs/                      <- generated PNGs land here
    .gitkeep
  scripts/
    export-png.js               <- Puppeteer export script
```

---

## CLAUDE.md to Generate

```markdown
# Infographic System

## Brand Rules
- Canvas: 1080 x 1350px (portrait, LinkedIn-optimised)
- Font: Space Grotesk (Google Fonts) -- all weights
- Body text: 15px minimum. Never smaller.
- Background: [USER_BG_COLOR] (e.g. #0A0A0A dark or #FFFFFF light)
- Primary accent: [USER_ACCENT_COLOR] (e.g. Shireen's gold #C9A84C)
- Secondary text: [USER_SECONDARY_COLOR]
- No box-shadow on content cards
- No emojis in infographic text
- Author block: always mid-section, headshot + name + follow CTA + link pills

## Layout Rules
- Max 7 key points per infographic -- fewer is better
- Every section needs breathing room: min 16px padding
- Headers: bold, large (24-32px), accent colour
- Body: regular weight, neutral colour, 15-17px
- No walls of text -- break everything into scannable chunks

## QA Gate
- Score must reach 95/100 before output is shown
- Auto-fix any violation and re-render
- Never show a draft -- only show scored and passing output

## Asset Paths
- Headshot: assets/headshot.png
- Logos: assets/logos/[tool-name].png
- Output: outputs/[topic-slug]/v[N]_[date].html + .png

## Inspiration Reference
- See references/inspiration/ for density and style targets
- Match visual weight of approved examples
```

---

## QA Agent to Generate (agents/qa-scorer.md)

```markdown
# QA Scorer Agent

You are a design QA agent. Score every infographic HTML file before it is shown to the user.

## Scoring Criteria (100 points)

### Typography (25 pts)
- Body text >= 15px (5 pts)
- Headers are large and bold (5 pts)
- Font is Space Grotesk throughout (5 pts)
- No more than 3 font sizes per infographic (5 pts)
- Line height >= 1.4 (5 pts)

### Brand (25 pts)
- Correct background colour (5 pts)
- Correct accent colour used for headers/highlights (5 pts)
- Author block present mid-section with headshot + name + follow CTA (5 pts)
- No box-shadow on content cards (5 pts)
- No emojis (5 pts)

### Layout (25 pts)
- Canvas exactly 1080 x 1350px (10 pts)
- All content visible, nothing clipped (5 pts)
- Min 16px padding inside all sections (5 pts)
- Visual hierarchy is clear at a glance (5 pts)

### Content (25 pts)
- 7 key points max (5 pts)
- No walls of text (5 pts)
- Headline is clear and punchy (5 pts)
- Information is scannable (5 pts)
- Bottom sign-off URLs present (5 pts)

## Behaviour
- Score every output before showing the user
- If score < 95: list all violations, auto-fix each one, re-render, re-score
- Repeat until score >= 95
- Only then output the final file path
```

---

## Puppeteer Export Script (scripts/export-png.js)

```javascript
const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

const htmlFile = process.argv[2];
const outputPath = process.argv[3];

if (!htmlFile || !outputPath) {
  console.error('Usage: node export-png.js <input.html> <output.png>');
  process.exit(1);
}

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.setViewport({ width: 1080, height: 1350, deviceScaleFactor: 2 });
  await page.goto(`file://${path.resolve(htmlFile)}`);
  await page.waitForNetworkIdle();

  fs.mkdirSync(path.dirname(outputPath), { recursive: true });
  await page.screenshot({ path: outputPath, fullPage: false });
  await browser.close();
  console.log(`Exported: ${outputPath}`);
})();
```

---

## After Scaffolding -- Tell the User

1. Add your headshot to `assets/headshot.png`
2. Drop 3-5 infographics you admire into `references/inspiration/` (any format)
3. Fill in your brand colours in `CLAUDE.md` (background, accent, secondary)
4. Run `npm install puppeteer` in the project root (one-time)
5. You're ready -- run `/infographic [topic]` to generate
