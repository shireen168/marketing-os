# Skill: sunny-homemade-content

## Trigger

Use when asked to "plan this week's Sunny Homemade content", "create a content calendar", "help me plan FB/IG posts", or "write a caption about [topic]".

## How to Invoke

- "Plan this week's Sunny Homemade content"
- "Create a content calendar for Sunny Homemade"
- "Help me plan FB/IG posts for the week"
- "Write a Sunny Homemade caption about [topic]"

## Step 0: Always Load These Files First

Before generating anything:
1. Read `projects/sunny-homemade/reference/brand-identity.md`
2. Read `projects/sunny-homemade/reference/content-rules.md`
3. **Glob for ALL product files** in `projects/sunny-homemade/reference/` using pattern `product-*.md` (do not hardcode product list)
4. Read all product files returned by glob
5. **Validate each product file** (see Validation Checklist below)

This ensures new product launches are automatically picked up without skill updates.

## Validation Checklist (Required Before Content Planning)

For each product file loaded, verify it contains ALL of these sections:

- [ ] **Hook Angles table:** At least 3 numbered hooks with Angle, Trigger, and Example Line columns
- [ ] **Content Mode Rotation:** Defines Mode A, Mode B, Mode C with specific hook numbers and goals
- [ ] **Messaging Notes:** Key audience angles, any health claims to avoid, price justification if applicable
- [ ] **Conversion Belief Map:** Funnel stages (Awareness, Consideration, Conversion, Retention)
- [ ] **Messaging Architecture:** Four-stage framework (Awareness, Consideration, Conversion, Retention)

**If any section is missing:**
- STOP content planning
- Report which product file is incomplete and which sections are missing
- Ask user to fill template before proceeding
- Do not invent hooks or modes for incomplete products

**Exception:** `product-template.md` is skipped (not a real product)

## Product File Sync Mechanism

**How it works:**
- All product references live in `projects/sunny-homemade/reference/product-*.md`
- This skill uses Glob to auto-detect all product files at runtime (no manual skill updates needed)
- When a new product launches: create `product-newproduct.md` in that folder with Hook Angles table, modes, and messaging notes (use `product-template.md` as reference)
- The skill immediately picks it up on next content planning session

**If sync breaks:**
- Skill will still function (glob returns all available products)
- But calendar proposals might miss the new product if not explicitly requested
- Always check the glob results at top of planning session

## Inputs to Gather

Only ask these AFTER validation passes. If validation fails, stop and report the issue.

Ask only if not already stated:
1. What week is this for? (default: current week)
2. Which product(s) to feature this week? (default: all available products from validation)
3. Any promotion, theme, or campaign to work around?
4. How many posts? (default: 5, Mon-Fri)

## Content Calendar Output Format

Produce a markdown table:

| Day | Platform | Product | Angle / Hook | Mode | Format | Sign-off |
|-----|----------|---------|--------------|------|--------|---------|

**Mode** = A (Education/Utility) / B (Emotional/Lifestyle) / C (Reach/Reel) -- from product file rotation rules
**Format** = Single image / Carousel / Reel / Story

Rule: Never repeat the same Mode two days in a row. Never repeat the same format two days in a row.

## Full Caption Output Format

When writing full captions (or when asked to expand a calendar row):

```
[Mandarin caption]
[Hook line]
[Body -- 2-4 lines]
[Sign-off block from content-rules.md -- exact text, no changes]

[English caption]
[Hook line]
[Body -- 2-4 lines]
[Sign-off block from content-rules.md -- exact text, no changes]

Hashtags: [English and Chinese only. No Malay hashtags.]
```

## Writing Rules (from content-rules.md -- enforced here)

- Mandarin first, English second. Always.
- No em dashes. No clinical jargon. No aggressive CTAs.
- CTA style: warm and inviting. "欢迎私信了解更多" / "feel free to message us."
- Cold audience first: lead with education, story, or curiosity. Not product push.
- Health claims (collagen only): use "research-backed" or "studies show" framing. Never state as absolute fact. Pastes have no health claims -- stick to ingredients and usage.
- Use hook angles and content mode rotation from the product file. Don't invent angles that aren't in the product strategy.

## Hook Selection

Pull hook angles from the product file's Hook Angles table. Match the mode:
- Mode A posts: use utility/education hooks
- Mode B posts: use emotional/lifestyle hooks
- Mode C posts: use curiosity/reach hooks

Do not use the same hook number twice in the same week.

## Reel Posts (CapCut + Gemini Gem Workflow)

**Decided 2026-04-17:** Switch from CapCut text-to-video to Gemini Gem 9:16 images + CapCut Animate. CapCut text-to-video letterboxes 16:9 into 9:16 causing black bars. Gemini Gem at native 9:16 eliminates this.

### Format Specs
- Screens: 1080x1920px each (9:16, max 4 screens)
- Reel cover: 1080x1080px (separate Gemini Gem prompt)

### Workflow
- Gemini Gem generates each screen image -- NO text inside the image
- CapCut adds all text overlays after import
- CapCut Animate handles motion -- no filming directions in prompts

### Screen Structure
- Screen 1: Hook -- attention-grabbing visual, no product
- Screen 2: Contrast or tension
- Screen 3: Resolution, proof, or education
- Screen 4: Product CTA -- always flag `*** PRODUCT PHOTO NEEDED ***` (actual jar, never AI-generated)

### CapCut Text Overlay Spec (every screen)
- CN: large, Mocha Earth (#4A3B32)
- EN: directly below, smaller, Lighter Brown (#7B5E4A)

### Reel Cover
- Always include a reel cover section after the last screen prompt
- Flag `*** PRODUCT PHOTO NEEDED ***` when cover includes the product jar

### Output Order for Reel Posts
1. Format header (4 screens, 1080x1920px, CapCut)
2. Screens 1-4: Gemini Gem image prompt + CapCut text instruction per screen
3. Reel cover: Gemini Gem prompt (1080x1080px)
4. CN full caption (hook + body + sign-off)
5. EN full caption (hook + body + sign-off)
6. Hashtags

## Image Prompts (Gemini Gem)

Refer to:
- `projects/sunny-homemade/reference/gemini-gem-instructions.md` -- brand style guide
- `projects/sunny-homemade/reference/workflow-image-production.md` -- format specs and CapCut workflow

**Single images and carousel slides:** include text overlay instructions inside the Gemini Gem prompt (CN Mocha Earth, EN Lighter Brown, size specified at end e.g. 1080x1350px or 1080x1080px).

**Reel screens:** NO text in Gemini Gem prompt -- text added in CapCut separately.

## After Generating

- Ask: "Want full captions for any of these posts?"
- Ask: "Want me to generate Gemini image prompts for any slides?"
- Offer to adjust hooks, mode rotation, or language
