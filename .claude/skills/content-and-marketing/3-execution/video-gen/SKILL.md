---
name: marketing-os-video-gen
description: Generate short-form UGC video scripts and concepts using Gemini Gems workflow for marketing reels
type: marketing
---

# Marketing-OS: Video Generation Skill

Generate scroll-stopping UGC video concepts and scripts for short-form reels (TikTok, Instagram Reels, YouTube Shorts). Turns marketing angles into production-ready video briefs.

## Use When

- Planning weekly content calendar
- Need to turn blog post/product feature into video
- Want 3-5 video angle ideas for a single product
- Need script + visual notes for CapCut production

## How to Use

**Input:** Product name + core angle/hook + target audience + format preference

**Output:** 3-5 video concepts with scripts, visual notes, hooks, and CTA

## Templates

### Template 1: Sunny Homemade Reel Generator

```
PROMPT:
Generate 3 short-form reel concepts for Sunny Homemade [PRODUCT].

Product: [collagen / ginger paste / chilli paste]
Angle: [before-after / reveal / recipe / comparison / problem-solution]
Hook: [emotion / curiosity / pain point]
Target Audience: [health-conscious women 35+ / busy moms / food enthusiasts]
Format: 9:16 vertical, 15-60 seconds

For each concept, provide:
1. Hook (first 3 seconds, stop-scroll moment)
2. Main narrative (what's the story?)
3. Visual notes (what's on screen at each moment)
4. CTA (call to action, product mention)
5. Best platform (TikTok / IG Reels / YT Shorts)

Format as JSON with video_concept_1, video_concept_2, video_concept_3.
```

### Template 2: Generic Marketing Team Reel Generator

```
PROMPT:
Generate 5 short-form reel concepts for [COMPANY NAME].

Product/Service: [what you sell]
Problem you solve: [specific customer pain point]
Hook angle: [education / entertainment / inspiration / controversy / problem-solution]
Target demographic: [age range / profession / interest]
Brand tone: [professional / playful / authoritative / casual]
Video length: [15-30 seconds / 30-60 seconds]

For each concept:
1. Hook: What makes someone stop scrolling? (first 2-3 seconds)
2. Story arc: What's the narrative? (setup → conflict → resolution)
3. Visual direction: Camera angle, B-roll, text overlays
4. Sound/music note: [energetic / calming / trending audio]
5. Product placement: How does your product/service appear?
6. CTA: What do you want viewers to do?

Return as JSON: [{"concept": 1, "hook": "...", "narrative": "...", "visuals": "...", "cta": "..."}, ...]
```

### Template 3: Problem-Solution Video Concept

```
PROMPT:
I need a before-after reel concept.

Before state: [customer's pain / problem / frustration]
After state: [transformation / relief / success]
Product: [what solves the problem]
Proof: [metric / testimonial / real example]

Generate 2 reel concepts showing the transformation. Format:
- Hook (3 sec): Show the pain point
- Middle (15 sec): Show the moment of change (product usage)
- End (5 sec): Show the result + CTA

Include specific visuals, text overlays, and call-to-action.
```

## Real Examples

### Sunny Homemade Example 1: Collagen Reel

**Angle:** Before-after (joint pain relief)
**Hook:** "I was limping at 35. Now? Different story."

**Concept Output:**
```json
{
  "video_concept_1": {
    "hook": "Close-up: Woman wincing while standing up. Text: '35. Every step hurt.'",
    "narrative": "Show problem (knee pain) → Show product (collagen jar) → Show solution (woman climbing stairs easily, playing with kids)",
    "visuals": [
      "0-2s: Close-up knee, wince face (text: '35 years old')",
      "2-4s: Product shot (Sunny Homemade collagen jar, Mandarin: '骨胶原')",
      "4-12s: Time-lapse: taking collagen daily (spoon in coffee, water glass)",
      "12-15s: She's walking, playing, moving freely (text: '4 weeks in')"
    ],
    "cta": "Mandarin: '無需手術，只需堅持' | English: 'No surgery. Just consistency.'",
    "platform": "Instagram Reels (1.9K views avg for collagen reels)"
  }
}
```

### Generic Example: SaaS Product Launch

**Product:** Project management tool
**Audience:** Busy solopreneurs
**Hook:** "4 hours a day managing chaos. We built this."

**Concept Output:**
```json
{
  "video_concept_1": {
    "hook": "Overwhelmed freelancer at desk, 10 browser tabs open. Text: 'Monday morning feels'",
    "narrative": "Show the pain (disorganization) → Show the tool (clean interface) → Show the win (relaxed, focused work)",
    "visuals": [
      "0-3s: Screen recording of chaotic task list + calendar mess",
      "3-8s: Product walkthrough (drag tasks, auto-schedule, integration)",
      "8-15s: User reaction (relief, productivity, client happy feedback)"
    ],
    "cta": "Free 14-day trial. No card required.",
    "platform": "TikTok / IG Reels"
  }
}
```

## Workflow Integration

1. **Brainstorm phase:** Choose product + angle (from weekly content calendar)
2. **Run this skill:** Generate 3-5 video concepts
3. **Select best:** Choose 1-2 concepts for production
4. **Hand off to /video-editing:** Pass script + visual notes to CapCut workflow
5. **Schedule:** Use /social-scheduling to post at optimal time

## Pro Tips

- **Hooks matter:** First 2-3 seconds determine 80% of engagement
- **Short-form logic:** Vertical 9:16, loud + text, captions for sound-off viewing
- **Product placement:** Don't make it an ad. Make it the solution to a real problem
- **Sunny Homemade specific:** Bilingual hooks (Mandarin first, English second), emotional connection over product specs
- **Trending audio:** Let the script live first, add trending audio during CapCut edit
- **Consistency:** Same visual style, same color grading, same text overlay format (builds brand)

## Output Format

All video concepts should return JSON with:
- `hook` (text, 3 sec max)
- `narrative` (beat-by-beat breakdown)
- `visuals` (camera direction, B-roll notes, text overlays with timing)
- `cta` (clear call-to-action, platform-specific)
- `platform` (where this performs best)
- `estimated_production_time` (CapCut hours needed)

This feeds directly into `/video-editing` workflow.
