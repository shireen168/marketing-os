---
name: marketing-os-video-editing
description: Automate CapCut video editing workflows for short-form marketing reels with bilingual text overlays
type: marketing
---

# Marketing-OS: Video Editing Skill

Streamline CapCut production for short-form reels. Turn scripts from `/video-gen` into export-ready videos with bilingual overlays, transitions, and platform optimization.

## Use When

- Have video concept + script from `/video-gen`
- Need to batch-edit multiple reel takes
- Want consistent text overlay style (bilingual Mandarin/English)
- Ready to export for Meta, TikTok, YouTube Shorts

## How to Use

**Input:** Video script + concept (from `/video-gen`), raw footage/template, platform destination

**Output:** CapCut project setup guide + overlay templates + export settings

## Templates

### Template 1: CapCut Workflow Automation (Sunny Homemade)

```
PROMPT:
Help me set up a CapCut template for Sunny Homemade reels.

Product: [collagen / ginger paste / chilli paste]
Video length: [15-30 sec / 30-60 sec]
Hook: [specific text from /video-gen]
Brand colors: Mocha Earth (#4A3B32), Cream (#F5E6D3), Lighter Brown (#7B5E4A)

Provide:
1. Project settings (resolution, aspect ratio, frame rate)
2. Text overlay template (bilingual: Mandarin 18pt, English 14pt, drop shadow)
3. Transition recommendations (fade, zoom, slide)
4. Sound design (music tempo, where to place voiceover)
5. Color grading (match Sunny Homemade aesthetic)
6. Sticker/animation notes
7. Export settings (platform-specific: Meta 1080x1920, TikTok 1080x1920, 9:16 aspect)
8. Timing cues (when to show product, when to CTA)

Return as structured checklist.
```

### Template 2: Bilingual Text Overlay System

```
PROMPT:
Create bilingual text overlay specs for Sunny Homemade video.

Hook text (English): "[ENGLISH TEXT]"
Hook text (Mandarin): "[MANDARIN TEXT]"
Body text (English): "[ENGLISH TEXT]"
Body text (Mandarin): "[MANDARIN TEXT]"
CTA text (English): "[ENGLISH TEXT]"
CTA text (Mandarin): "[MANDARIN TEXT]"

Provide:
1. Font choices (Chinese + English pairing)
2. Size hierarchy (hook > body > CTA)
3. Color specifications (text color + drop shadow color)
4. Timing (when each overlay appears, duration)
5. Positioning (safe area for vertical 9:16)
6. Animation (fade in, slide up, static)
7. Background (solid color, semi-transparent, blur effect)
8. Platform adaptation (same overlay for Meta, TikTok, YT, FB)

Example:
- Hook (Mandarin 24pt, Mocha Earth, centered, 0-3s, fade in)
- Hook (English 16pt, Lighter Brown, below Mandarin, 0-3s, fade in)
- [body text overlays...]
- [CTA overlays...]
```

### Template 3: Batch Edit Multiple Takes

```
PROMPT:
I have 5 raw video takes for one reel concept. Help me batch-edit efficiently.

Concept: [from /video-gen]
Raw footage: [5 takes, 30-60 sec each]
Best take segments: [specify which seconds of which take are best]

Provide:
1. Story beat breakdown (which take covers hook, which covers narrative, which covers CTA)
2. CapCut merge workflow (combine best segments from each take)
3. Transition placement (between segments)
4. Color match process (ensure consistent look across segments)
5. Audio sync (remove original sound, add fresh music/voiceover)
6. Overlay addition (text + product shot + CTA)
7. Quality checklist before export
8. Export confirmation step

Return as step-by-step CapCut instructions.
```

## Real Examples

### Sunny Homemade Example: Collagen Reel (CapCut Setup)

**Source:** /video-gen collagen before-after concept
**Length:** 30 seconds
**Bilingual:** Yes (Mandarin first, English second)

**CapCut Workflow:**

```json
{
  "project_settings": {
    "resolution": "1080x1920",
    "aspect_ratio": "9:16",
    "frame_rate": 24,
    "duration_target": "30 seconds"
  },
  "timeline_beats": [
    {
      "beat": "Hook (0-3s)",
      "action": "Close-up knee pain, woman wincing",
      "overlay_mandarin": "35歲，每步都疼",
      "overlay_english": "35. Every step hurt.",
      "overlay_timing": "0-3s",
      "overlay_style": "Mandarin 24pt Mocha Earth, English 16pt Lighter Brown, drop shadow"
    },
    {
      "beat": "Product reveal (3-8s)",
      "action": "Jar appears (Gemini Gem image or screenshot)",
      "overlay_mandarin": "骨膠原 by Sunny Homemade",
      "overlay_english": "Collagen by Sunny Homemade",
      "overlay_timing": "3-8s",
      "transition": "Zoom in on jar, slight pulse animation"
    },
    {
      "beat": "Transformation montage (8-25s)",
      "action": "Time-lapse of daily usage + activity progression",
      "overlay_mandarin": "持續4週",
      "overlay_english": "4 weeks in",
      "overlay_timing": "12-15s",
      "music": "Uplifting, 120+ BPM, no lyrics"
    },
    {
      "beat": "CTA (25-30s)",
      "action": "Woman climbing stairs, playing with kids, moving freely",
      "overlay_mandarin": "無需手術，只需堅持",
      "overlay_english": "No surgery. Just consistency.",
      "overlay_timing": "25-30s",
      "style": "Bold, large text, centered, 2s duration, white text with dark drop shadow"
    }
  ],
  "text_overlay_colors": {
    "hook": "#4A3B32",
    "body": "#7B5E4A",
    "cta": "#FFFFFF",
    "drop_shadow": "#000000-30-opacity"
  },
  "export_settings": {
    "facebook": "1080x1920, 30fps, H.264, AAC audio",
    "instagram_reels": "1080x1920, 30fps, H.264, AAC audio",
    "tiktok": "1080x1920, 30fps, H.264, AAC audio",
    "youtube_shorts": "1080x1920, 30fps, H.264, AAC audio"
  },
  "quality_checklist": [
    "All text overlays bilingual (Mandarin first, English second)",
    "No audio bleed from original footage (music/voiceover only)",
    "Colors consistent across all clips",
    "Product visible and recognizable",
    "CTA clear and easy to read",
    "Duration exactly 30 seconds (or 15/60 if variant)"
  ],
  "export_filename": "sunny-homemade-collagen-before-after-30s.mp4",
  "next_step": "Upload to CapCut cloud, prepare for /social-scheduling"
}
```

### Generic Example: SaaS Product Reel (Editing Checklist)

**Product:** Project management tool
**Duration:** 30 seconds
**Bilingual:** No (English only)

**CapCut Checklist:**
```
1. Import raw take (30-60 sec footage)
2. Trim to best segment (0-30s)
3. Add text overlay at 0-3s: "Your Monday morning (before)"
4. Add product screenshot at 3-10s (auto-zoom transition)
5. Add text at 3-10s: "Meet [Product]"
6. B-roll of interface (10-20s, fade between screens)
7. Add user reaction shot (20-28s)
8. Add CTA overlay (28-30s): "Free 14-day trial"
9. Add trending audio (full 30s, mix with voiceover)
10. Color grade (match brand aesthetic)
11. Export (1080x1920, H.264, AAC)
12. Review for text legibility, audio sync, product clarity
13. Rename: "[product]-reel-[date]-[angle].mp4"
14. Upload to cloud, link in /social-scheduling
```

## Workflow Integration

1. **Input:** Video concept + script from `/video-gen`
2. **CapCut setup:** Create project from template
3. **Gather footage:** Raw video, product images, B-roll
4. **Build timeline:** Follow beat-by-beat breakdown
5. **Add overlays:** Bilingual text (Mandarin first, English second)
6. **Color grade:** Match brand aesthetic (Sunny Homemade: warm earth tones)
7. **Sound design:** Remove original audio, add music + voiceover
8. **Quality check:** Run through checklist
9. **Export:** Platform-specific formats
10. **Hand off:** Pass filename to `/social-scheduling`

## Pro Tips

**Bilingual overlay best practices:**
- Mandarin 20-24pt (primary, larger)
- English 14-16pt (secondary, smaller, directly below)
- Same color for both languages (bilingual text acts as one unit)
- Drop shadow essential (readability on any background)
- 1-2 second duration for overlays (readable, not overwhelming)

**Sunny Homemade specific:**
- Brand colors: Mocha Earth (#4A3B32) for primary text, Cream (#F5E6D3) background if needed
- Always show product jar (must be recognizable)
- Bilingual every time (no exceptions)
- Emotional hook (not feature-focused)
- Transition speed: slow fades > fast cuts (premium aesthetic)

**CapCut efficiency:**
- Save templates (reuse for future reels)
- Batch import similar footage
- Pre-color-grade before timeline (faster iteration)
- Export at highest quality first, compress later if needed
- Track fonts used (ensures consistency across videos)

**Platform optimization:**
- Meta: Metadata caption (Mandarin subtitle text for algorithm)
- TikTok: Captions + trending audio = higher reach
- YouTube Shorts: Longer CTAs work better (users tolerate 5s CTA)
- All platforms: 9:16 aspect, 30fps, no black bars

## Output Format

Handoff to `/social-scheduling` should include:
- Exported video file (platform-specific)
- Original project file (CapCut .capcut for future edits)
- Thumbnail screenshot
- Overlay specifications (in case future edits needed)
- Platform destination (Meta, TikTok, YouTube, LinkedIn, etc.)
- Recommended posting time (from `/social-scheduling`)
