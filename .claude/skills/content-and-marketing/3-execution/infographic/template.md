# Infographic Template Reference

Use this as the structural blueprint for every new infographic. Copy and adapt - do not modify this file.

---

## Canvas

- Size: 1080 x 1350px (LinkedIn portrait)
- Background: #0D0D0D
- Font: Space Grotesk (Google Fonts, all weights)
- Padding: 36px 60px 28px

---

## Brand Colors

| Token | Hex | Use |
|---|---|---|
| Gold | #C9A84C | Accent, headers, bullets, badges, pills |
| Gold dark bg | #1C1600 | Payoff box bg, code bg |
| White | #FFFFFF | Primary headlines |
| Light grey | #C8C8C8 | Body copy, list items |
| Mid grey | #999999 | Secondary copy, hook text, dim labels |
| Dark grey | #666666 | Metric labels, separators |
| Phase bg | #111111 | Phase card background |
| Metric bg | #181818 | Metric/wrap item background |
| Red | #E05252 | Consequence / warning text |

---

## Layout Structure (top to bottom)

```
[HEADER ROW]
  Left: eyebrow + headline + hook
  Right: sign-off URLs (top-right, subtle, 9px, #383838)

[DIVIDER] 1px #1C1C1C, margin 11px 0

[PHASES FLEX COLUMN] gap: 8px, flex: 1
  Phase card (flex: 1 each)
    - phase-header: gold bg, phase-number + phase-title + phase-cmd badge
    - phase-body: content + payoff strip

[COMPOUND CALLOUT] flex: 0 0 auto, #141000 bg, gold border

[AUTHOR BLOCK] margin-top: 8px
  - 48px avatar (gold border) + FOLLOW label + name + pill links
```

---

## Phase Card Template

```html
<div class="phase">
  <div class="phase-header">
    <span class="phase-number">Phase 0X</span>
    <span class="phase-title">Title Here</span>
    <span class="phase-cmd">command</span>
  </div>
  <div class="phase-body">
    <!-- content goes here -->
    <div class="payoff">Payoff line here.</div>
  </div>
</div>
```

---

## Common Content Layouts Inside phase-body

### 2-column grid (without/with, before/after)
```html
<div class="p1-grid">
  <div>
    <div class="col-label">Without it</div>
    <div class="list-item"><div class="bullet"></div><div>Point one</div></div>
  </div>
  <div>
    <div class="col-label">With [command]</div>
    <div class="list-item"><div class="bullet"></div><div>Point one</div></div>
  </div>
</div>
```

### 3-column metrics (live stats)
```html
<div class="metrics-row">
  <div class="metric">
    <div class="metric-label">Live</div>
    <div class="metric-value">67%</div>
    <div class="metric-name">Metric Name</div>
    <div class="metric-consequence">Consequence at limit</div>
  </div>
</div>
```

### 2-column wrap grid (feature list)
```html
<div class="wrap-grid">
  <div class="wrap-item">
    <strong>Feature title</strong>
    Short description of what it does
  </div>
</div>
```

### Token comparison (2-stat side by side)
```html
<div class="plan-row">
  <div class="plan-stat">
    <div class="plan-num">2k</div>
    <div class="plan-label">
      <strong>Label</strong>
      Description
    </div>
  </div>
</div>
```

---

## Author Block Template

```html
<div class="author-block">
  <img class="author-avatar" src="../../assets/headshot.png" alt="Shireen Low">
  <div class="author-info">
    <div class="author-follow">Follow</div>
    <div class="author-name">Shireen Low</div>
    <div class="author-pills">
      <a href="https://aiwithshireen.com" class="pill">aiwithshireen.com</a>
      <a href="https://github.com/shireen168/[repo]" class="pill">github.com/shireen168/[repo]</a>
    </div>
  </div>
</div>
```

---

## Locked Header (copy exactly - do not alter structure)

```html
<div>
  <div class="eyebrow">EYEBROW TEXT HERE</div>
  <div class="headline">Headline <span class="accent">Accent Words</span> Rest of Title</div>
  <div class="hook">
    Hook sentence. <strong>Key pain 1.</strong> More context. <strong>Key pain 2.</strong>
  </div>
</div>
```

CSS rules (locked):
- `.headline`: `font-size: 44px; white-space: nowrap;` - always single line, never break
- `.hook`: `font-size: 13px; color: #999;` - pain-led, max 2 lines

## Locked Sign-off Bar (copy exactly - single line, centered)

```html
<div class="signoff-bar">
  <img class="signoff-avatar" src="../../assets/headshot.png" alt="Shireen Low">
  <span class="signoff-follow">Follow</span>
  <span class="signoff-name">Shireen Low</span>
  <span class="signoff-dot">·</span>
  <a href="https://aiwithshireen.com" class="signoff-link">aiwithshireen.com</a>
  <span class="signoff-dot">·</span>
  <a href="https://github.com/shireen168/[repo]" class="signoff-link">github.com/shireen168/[repo]</a>
</div>
```

CSS (locked):
```css
.signoff-bar {
  display: flex; align-items: center; justify-content: center;
  gap: 10px; margin-top: 10px; padding: 11px 18px;
  background: #111; border-radius: 8px; flex-shrink: 0;
}
.signoff-avatar { width: 32px; height: 32px; border-radius: 50%; border: 2px solid #C9A84C; object-fit: cover; }
.signoff-follow { font-size: 10px; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; color: #C9A84C; }
.signoff-name   { font-size: 14px; font-weight: 700; color: #FFF; }
.signoff-dot    { color: #383838; font-size: 14px; }
.signoff-link   { font-size: 12px; font-weight: 500; color: #666; text-decoration: none; }
```

---

## Export Command

```bash
node scripts/export-png.js outputs/[slug]/[filename].html outputs/[slug]/[filename].png
```

---

## Statusline Settings (for GitHub repo reference)

The statusline requires two things:

**1. `~/.claude/settings.json`**
```json
{
  "statusLine": {
    "type": "command",
    "command": "powershell -NoProfile -ExecutionPolicy Bypass -File C:/Users/[username]/.claude/statusline.ps1"
  }
}
```

**2. `~/.claude/statusline.ps1`**
Full PowerShell script that reads Claude Code's JSON data and outputs:
- Line 1: `[Model] $cost duration | ctx used/total (%) cache N`
- Line 2: `5hr [bar] % resets Xh Xm | 7day [bar] % resets Xd Xh`

Color coding: green under 70%, yellow 70-90%, red over 90%.

Full script available at: `github.com/shireen168/claude-session-system`
