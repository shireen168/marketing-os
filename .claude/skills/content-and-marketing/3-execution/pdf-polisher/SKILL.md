# PDF Polisher

## Trigger

Use when a project has "Download as PDF" or "Export as PDF" buttons and the PDF output needs visual polish, styling, or layout fixes.

## Scope
- A project has a print-based PDF export feature (like Sprint Machine's `/download` button)
- The PDF output shows wrong fonts, colors, margins, or blank pages
- `@media print` CSS rules conflict between `globals.css` and the print page
- Browser cache is preventing CSS updates from appearing in the PDF
- You need to diagnose and fix print stylesheet conflicts in Next.js

**Key trigger phrases:**
- "Fix the PDF download"
- "The PDF export looks wrong"
- "Print CSS is broken"
- "PDF fonts/colors/margins are wrong"

---

## Diagnosis: Audit All Print-Related CSS

**Step 1: Find all `@media print` blocks**

Grep the entire project for `@media print`:
```bash
grep -r "@media print" --include="*.css" --include="*.ts" --include="*.tsx" .
```

For each file found, note:
- Filename and path
- Line numbers
- What it does (sets `@page` rules, overrides fonts, hides elements, sets colors)
- Whether it uses `!important`

**Step 2: Find all `@page` rules**

```bash
grep -r "@page" --include="*.css" --include="*.ts" --include="*.tsx" .
```

Note: Line numbers, margin/size values, any `:first` pseudoclass rules. Conflicts occur when multiple `@page { margin: ... }` rules exist with different values.

**Step 3: Classify the print CSS**

Organize your findings into:
- **Global print CSS** (in `globals.css` or shared layouts) — applies to every page including print
- **Isolated print CSS** (in a print-only page, inline `<style>`, or a dedicated stylesheet) — applies only to `/print` route
- **Conflicting rules** — multiple files defining the same selector or `@page` (last one in cascade wins)

---

## Root Cause: Cascade Conflicts

**The most common issue:** `globals.css` contains a full `@media print` block. When a completely separate print page (`/[id]/print`) renders, it ALSO loads `globals.css` (via the root layout). Both sets of rules fire, and the cascade determines which wins.

**Symptoms:**
1. `* { color: #1a1a1a !important; background: white !important; }` in globals strips all colors from the print page's carefully scoped classes (because universal selector, even with `!important`, loses specificity to class selectors in modern CSS, but `!important` on `*` can still override if the specificity chain is broken)
2. `body { font-family: Arial; font-size: 11pt; }` in globals overrides `body { font-family: 'IBM Plex Sans'; }` because `body` specificity (0,0,1) is the same for both, and last-in-wins
3. `@page { margin: 2cm; } @page :first { margin-top: 4cm; }` in globals conflicts with `@page { margin: 0.5in; }` in the print template (whichever loads last wins for `@page` rules)
4. Browser cache: CSS loaded from cache may not reflect your latest edits. The print page might cache its stylesheet on the first visit, and subsequent edits to the CSS file don't appear until cache is cleared.

**The fix:** If your app has a **completely isolated print page** (a separate `/print` route with its own layout), the print page should own all print CSS. Remove `@media print` from `globals.css` and shared layouts entirely.

---

## Systematic Fix

### Check: Is Your Print Page Truly Isolated?

**Isolated:** Has its own route (`/[id]/print`), its own layout file, renders a self-contained component, inlines all print CSS via `<style>`.
**Not isolated:** Print styling mixed into regular pages, shared layout contains print rules that apply everywhere.

If **isolated**, proceed:

### 1. Remove `@media print` from shared files

Find and DELETE these blocks from:
- `app/globals.css`
- Any shared layout files (e.g., `app/layout.tsx` if it has print rules)
- Any shared component that inlines `<style>` with `@media print`

Also delete:
- `@page` rules in shared files (they belong in the isolated print page)

Keep: everything else in `globals.css` (Tailwind imports, design tokens, base body styles).

### 2. Consolidate print CSS into ONE file

**Single source of truth:** Either:
- Inline all print CSS via `<style>` in the print template component, OR
- Separate print stylesheet that is ONLY imported by the print page

Whichever approach, verify:
- `@page { margin: ...; size: A4; }` appears exactly once (no conflicts)
- All `@media print { ... }` rules are scoped to classes (`.print-section h2 { ... }`), not universal selectors (`* { ... }`)
- Use `!important` only on properties that are being overridden by globals or browser defaults

### 3. Cache bust the print page

Add a timestamp query param to the download trigger:
```typescript
// Before
window.open(`/sprint/${id}/print`, '_blank')

// After
window.open(`/sprint/${id}/print?v=${Date.now()}`, '_blank')
```

This forces a fresh fetch of the print page and its CSS, bypassing browser cache.

### 4. Verify print output

Use Chrome DevTools:
1. Open the print page in a browser tab
2. Open DevTools (Ctrl+Shift+I)
3. Click the three dots → More tools → Rendering
4. Under "Emulate CSS media type", select "print"
5. Observe the rendered page — should show print colors/fonts, not screen colors

Manually test:
1. Click the Download button (or equivalent)
2. Browser print dialog opens
3. In "More settings", scroll through and verify margin/size is correct
4. Choose "Destination: Save as PDF"
5. Open the PDF and verify fonts, colors, and layout match the preview

---

## Gotchas

**`@media print` rule specificity:** A universal selector `* { color: black !important }` DOES override class selectors that don't have `!important`. Modern CSS specificity: `!important` universal selector (0,0,1) > regular class selector (0,1,0) IF the class rule doesn't have `!important`. Solution: Use `!important` on all your class-scoped print rules too.

**`@page` cascade:** The `@page` rule does not follow normal CSS cascade. Last one in document order wins. If `globals.css` is loaded first and then an inline `<style>` is injected, the inline version wins. Verify by checking the DevTools Styles panel under the print page — the effective margin should come from your print template, not globals.

**Print-specific fonts:** Web fonts specified in `@font-face` or imported from Google Fonts need to load in print mode. Verify the font URL is accessible (some CDNs block certain user-agents). If the printed PDF shows a fallback font instead, add an explicit fallback: `font-family: 'IBM Plex Sans', Arial, sans-serif;`

**Browser headers/footers:** The user's browser may add page headers (URL), footers (page numbers), or margins by default. Instruct users to disable these in the print dialog's "More settings" > uncheck "Headers and footers". Or, set `@page { margin: 2cm; }` generously to accommodate built-in headers.

---

## Verification Checklist

After applying fixes:

- [ ] No `@media print` rules remain in `globals.css` or shared layouts
- [ ] Print page has a self-contained `<style>` or stylesheet with all print rules
- [ ] `@page` rule appears exactly once across the entire project (in the print template only)
- [ ] All class-scoped rules in print CSS use `!important` on overrides
- [ ] Download button/trigger includes cache-bust param (`?v=timestamp`)
- [ ] Chrome DevTools print emulation shows correct fonts and colors
- [ ] Browser print dialog preview looks correct (no Arial override, correct margins)
- [ ] Saved PDF opens and renders correctly
- [ ] Non-print pages unaffected (test a few regular routes to confirm no print CSS leaked)
