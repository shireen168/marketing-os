# Sunny Homemade Daily Content Generator

## Trigger
`/sunny-homemade-daily` or scheduled at 8am MYT daily

---

## What This Skill Does

1. Gets today's date in MYT (Asia/Kuala_Lumpur)
2. Finds the current week file (glob `projects/sunny-homemade/weeks/2026-W##-*.md`)
3. Extracts today's content block from the week file (product, format, captions CN+EN, hashtags, Gemini prompt, CapCut notes, platform target)
4. Formats as a Telegram Markdown message
5. Sends via Telegram Bot API (curl)
6. Updates `projects/sunny-homemade/tracker.md` status to "Sent to Telegram"

---

## Step-by-Step Workflow

### Step 1: Calculate today's date and find the week number

1. Get today's date (MYT timezone: Asia/Kuala_Lumpur)
2. Calculate ISO week number
3. Format: `2026-W##` (e.g., `2026-W04`)
4. Glob to find matching week file: `projects/sunny-homemade/weeks/2026-W##-*.md`

Example: If today is Wed 6 May 2026, find `2026-W04-*.md`

### Step 2: Read the week file and find today's entry

1. Read the week file
2. Find the CALENDAR OVERVIEW table (labeled "| Day | Date | Product | Mode |...")
3. Match today's day of week and date
4. Extract: Day, Date, Product, Mode, Format, Hook #, Angle
5. Find the corresponding FULL CAPTIONS section (e.g., "### MON 4 MAY | Product | Format")

Example: If today is Wed 6 May, extract the Wed row and find the "### WED 6 MAY" section.

### Step 3: Extract content from today's section

From the section header and FULL CAPTIONS, extract:
- **Product**: e.g., "Collagen", "Ginger Paste"
- **Format**: e.g., "Reel", "Single Image", "Carousel"
- **Mandarin caption**: Full bilingual caption text (CN first)
- **English caption**: Full bilingual caption text (EN second)
- **Hashtags**: Full hashtag string
- **Gemini Gem Prompt**: Entire prompt block (between triple backticks)
- **CapCut Notes**: Storyboard timing + text placement (if reel)
- **Platform**: Target (Facebook / Instagram) — infer from week file notes or default to Facebook

### Step 4: Format the Telegram message

Send a clean Markdown message:

```
*Sunny Homemade — [Day, Date]*
*Platform:* [Facebook / Instagram]
*Format:* [Reel / Carousel / Single Image]

*Caption (中文):*
[Mandarin caption text]

*Caption (English):*
[English caption text]

*Hashtags:*
[hashtags]

*Gemini Prompt:*
[Full Gemini Gem prompt block]

*CapCut / Production Notes:*
[CapCut storyboard notes if reel, else "Single image — no CapCut needed"]

_Approve and copy to Meta Business Suite_
```

### Step 5: Send via Telegram Bot API

Use curl to POST to the Telegram Bot API:

```bash
curl -s -X POST "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage" \
  -H "Content-Type: application/json" \
  -d "{\"chat_id\":\"${TELEGRAM_CHAT_ID}\",\"text\":\"${MESSAGE}\",\"parse_mode\":\"Markdown\"}"
```

Read `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID` from environment (root `.env` file or shell env).

### Step 6: Update tracker.md

1. Open `projects/sunny-homemade/tracker.md`
2. Find the current week section (e.g., "## 2026 — May" → planning table)
3. Find today's row (match by Date and Day)
4. Update Status column: `Planned` → `Sent to Telegram`

---

## Context Files to Load Before Starting

Load these files into context to ensure accuracy:
- `projects/sunny-homemade/reference/content-rules.md` (verify no dashes, no em-dashes in output)
- `projects/sunny-homemade/reference/brand-identity.md` (verify brand consistency)
- Relevant `projects/sunny-homemade/reference/product-[name].md` (for today's product context)

---

## Example: Wednesday 6 May 2026

**Input:** Today is Wed 6 May 2026

**Workflow:**
1. Find `projects/sunny-homemade/weeks/2026-W04-may04-10.md`
2. In CALENDAR OVERVIEW, find Wed row: "Wed | 6 May | Bak Zang + Chilli | C | Reel | #6"
3. Find section "### WED 6 MAY | Bak Zang + Sambal Chilli Bundle | Reel"
4. Extract captions (CN + EN), hashtags, Gemini prompt (all 4 screens), CapCut timing notes
5. Format as Telegram message
6. Send to personal Telegram chat
7. Update tracker.md: find "2026 — May" section, row "6 May | Wed", set Status to "Sent to Telegram"

**Output:** User receives formatted content in Telegram, sees "Approve and copy to Meta Business Suite"

---

## Notes

- If today's date doesn't fall within any week file's range, notify user: "No week file found for [date]"
- If today's status in tracker is already "Posted" or "Skip", still send (for reference/approval), but note in message
- Timezone: Always use Asia/Kuala_Lumpur (MYT) for date calculations
- Platform allocation: Defaults to Facebook unless week file specifies otherwise
- Preserve all formatting from the week file (colors, symbols, spacing in captions)
