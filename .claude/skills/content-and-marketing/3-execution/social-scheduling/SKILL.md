---
name: marketing-os-social-scheduling
description: Automate multi-platform social media scheduling with optimal timing and content adaptation
type: marketing
---

# Marketing-OS: Social Scheduling Skill

Schedule content across Meta (Facebook, Instagram), TikTok, LinkedIn, Twitter/X at optimal posting times. Adapts single content piece to platform-specific formats and best posting windows.

## Use When

- Have finished video/image from `/video-editing` or `/video-gen`
- Weekly content calendar planned
- Need to post same content across multiple platforms
- Want to optimize posting time for maximum reach

## How to Use

**Input:** Content piece (video file, image, caption), platforms (Meta, TikTok, LinkedIn, etc.), posting strategy (immediate, scheduled, optimal time)

**Output:** Platform-specific posting schedule with timing, captions, hashtags, and metadata

## Templates

### Template 1: Multi-Platform Scheduling (Same Content, Platform-Adapted)

```
PROMPT:
I have finished [VIDEO/IMAGE] for [PRODUCT/TOPIC]. Schedule it across multiple platforms.

Content file: [filename]
Content type: [reel / carousel / single image / carousel / text post]
Caption text (English): [full caption]
Caption text (Mandarin): [bilingual if applicable]
Hashtags: [relevant hashtags]
Primary platform: [where it should post first?]
Posting date: [when to schedule]

Platforms to use: [Facebook / Instagram / TikTok / LinkedIn / Twitter / YouTube / Pinterest]

For each platform, provide:
1. Optimal posting time (based on platform + audience)
2. Platform-specific caption (character limits, hashtag strategy)
3. Content adaptation (resolution, aspect ratio, format)
4. Metadata (keywords, hashtags, description)
5. CTA adaptation (platform-specific wording)
6. Expected performance (typical engagement for this content type on this platform)

Return as JSON with platform: {...}, platform: {...}

Also include:
- Posting order (which platform first, why)
- Cross-promotion note (how to drive traffic between platforms)
- Metrics tracking setup (what to measure per platform)
```

### Template 2: Sunny Homemade Content Calendar Scheduling

```
PROMPT:
I have a [WEEKLY CONTENT CALENDAR] for Sunny Homemade. Schedule all posts across Facebook and Instagram.

Calendar:
[Paste 7-day calendar with: Day, Product, Format, Angle, Caption, Image]

Platforms: Facebook + Instagram (same content, different optimal times)
Target audience: Women 35+, health-conscious, Malaysia/SEA based
Goal: Maximize organic reach, engagement, product awareness
Language: Bilingual (Mandarin primary, English secondary)

For each post in the calendar:
1. Determine posting time (Facebook: [time], Instagram: [time] based on audience analysis)
2. Adapt caption (character limit differences)
3. Optimize hashtags (platform-specific, Mandarin + English)
4. Add pinned comment instructions (first comment = product link)
5. Suggest cross-platform link (how to drive from one to the other)
6. Estimate reach (reel vs. post expected performance)

Return as JSON calendar with posting times + platform-specific instructions.
```

### Template 3: Optimal Time Calculation

```
PROMPT:
Determine the best posting time for [CONTENT] on [PLATFORM] for [AUDIENCE].

Content type: [reel / static image / carousel / link post]
Platform: [Facebook / Instagram / TikTok / LinkedIn / Twitter]
Target audience: [demographic, location, profession, interests]
Audience timezone: [UTC+8 (Malaysia) / etc.]
Content category: [food / wellness / product / educational / entertainment]

Provide:
1. Primary posting window (best 1-2 hours)
2. Secondary windows (alternative good times)
3. Times to avoid
4. Why (audience behavior data)
5. Platform algorithm advantage (what the platform rewards at certain times)
6. A/B testing suggestion (test time 1 vs. time 2)

Return as structured analysis.
```

## Real Examples

### Sunny Homemade Example: Weekly Calendar Scheduling

**Week:** May 7-13, 2026
**Platforms:** Facebook + Instagram
**Product mix:** Collagen reel, ginger paste carousel, chilli paste single image
**Goal:** 80% reel focus, 20% carousel/static

**Schedule Output:**

```json
{
  "calendar_week": "May 7-13 (W02 May)",
  "platforms": ["Facebook", "Instagram"],
  "posts": [
    {
      "date": "2026-05-07",
      "day": "Wednesday",
      "product": "Bak Zang",
      "format": "reel",
      "angle": "4-screen reel with chilli paste pairing",
      "content_file": "sunny-homemade-bak-zang-reel-30s.mp4",
      "facebook": {
        "posting_time": "19:00 MYT",
        "reasoning": "Wed evening peak engagement for wellness content, families at dinner time planning next meals",
        "caption_mandarin": "[caption optimized for Facebook, 63 chars max]",
        "caption_english": "[English translation]",
        "hashtags": "#BakZang #SunnyHomemade #HealthyEating #TraditionalFlavors",
        "pinned_comment": "Product link + early adopter discount code",
        "expected_reach": "1200-1500 impressions (reels average for this audience)",
        "expected_engagement": "60-80 interactions (save rate typically 15-20%)"
      },
      "instagram": {
        "posting_time": "18:30 MYT",
        "reasoning": "Instagram peak time earlier than Facebook (early evening when people browse reels)",
        "caption_mandarin": "[same as Facebook, optimized for IG character limits (2200 max)]",
        "caption_english": "[English]",
        "hashtags": "#BakZang #SunnyHomemade #HealthyBreakfast #AsianFlavors #FoodStories",
        "first_comment_strategy": "Caption mentions limited batch, story link in bio",
        "expected_reach": "2000-2500 impressions",
        "expected_engagement": "100-150 interactions (IG higher engagement baseline)"
      },
      "cross_promotion": "Post FB reel at 19:00. If engagement strong by 19:30, share IG Reels link in FB comments. This drives traffic between platforms.",
      "metrics_to_track": [
        "Views (both platforms)",
        "Engagement rate (both)",
        "Save count (Reels perform higher on saves)",
        "Share count",
        "Bio link clicks (if using link in caption)"
      ]
    }
  ],
  "weekly_summary": {
    "total_posts": 5,
    "format_split": "80% reels (4), 20% carousel (1)",
    "total_expected_reach": "10000-12000 impressions",
    "total_expected_engagement": "400-500 interactions",
    "posting_order": "FB first (15-30 min before IG), then IG, to test timing and allow cross-promo",
    "hashtag_strategy": "Mandarin + English hashtags, 8-12 per post (IG-specific to maximize discoverability)"
  },
  "automation_setup": {
    "tool_recommended": "Meta Business Suite (Facebook + Instagram together) + Buffer or Later for cross-platform oversight",
    "scheduling_method": "Schedule all posts in Meta Business Suite at optimal times above",
    "monitoring": "Check engagement 1 hour post + monitor for trending comments/questions"
  }
}
```

### Generic Example: SaaS Product Multi-Platform Schedule

**Product:** Project management tool
**Platforms:** LinkedIn + Twitter
**Content:** Educational reel about time-saving features
**Audience:** Managers, solopreneurs, 9am-5pm timezone (US Eastern)

**Schedule:**

```json
{
  "linkedin": {
    "posting_time": "08:00 ET (Tuesday/Wednesday)",
    "caption_strategy": "Professional tone, 1-2 paragraphs, 1-2 data points, soft CTA",
    "hashtags": "#ProductManagement #TimeManagement #SMB #Startup",
    "expected_reach": "500-800 impressions (for 500 followers)"
  },
  "twitter": {
    "posting_time": "09:30 ET (same day, post LinkedIn first)",
    "caption_strategy": "Conversational, emoji optional, thread format (2-3 tweets)",
    "hashtags": "#BuildInPublic #ProductivityHacks",
    "expected_reach": "200-400 impressions"
  }
}
```

## Workflow Integration

**Timeline:**
1. **Content ready:** Video from `/video-editing` or image ready
2. **Caption written:** English + Mandarin (if bilingual)
3. **Run this skill:** Generate platform-specific schedule
4. **Adapt captions:** Customize for platform character limits + tone
5. **Schedule posts:** Input into Meta Business Suite / Buffer / Later
6. **Monitor:** Check engagement 1-2 hours post, respond to comments
7. **Track metrics:** Weekly performance analysis (reach, engagement, saves, shares)

## Pro Tips

**Platform-specific strengths:**
- **Facebook:** Reach older audience, carousel/single images strong, direct sharing
- **Instagram:** Reels algorithm favors high engagement, younger audience, aesthetic focus
- **TikTok:** Short-form video first (15-60s), trending audio critical, high engagement rate
- **LinkedIn:** Professional audience, thought leadership content, Monday-Thursday best
- **Twitter:** Real-time trending, conversational thread, breaking news/hot takes

**Sunny Homemade specific timing:**
- **Morning (8-10am):** Breakfast prep, health-conscious audience active
- **Afternoon (3-5pm):** Snack time, work break, casual scrolling
- **Evening (6-8pm):** Dinner prep planning, leisure browsing
- **Weekends:** Different patterns (higher morning engagement)

**Optimal posting frequency:**
- Small business (like Sunny Homemade): 5-7 posts/week (daily or 6x weekly)
- B2B SaaS: 3-5 posts/week (platform-specific)
- Agency/consultants: 2-3 posts/week (quality over quantity)

**Engagement maximization:**
- Post reel first (algorithm favorite), static post second (drives to profile)
- Respond to comments within 1 hour (engagement signals algorithm)
- Use carousel strategically (lower reach, but higher click-through)
- Bilingual captions (if applicable): Mandarin primary, English secondary
- Include CTA (link in bio, product tag, swipe up if available)

## Output Format

Handoff to scheduling tool (Meta Business Suite / Buffer / Later / automation platform):
- Scheduled posts (date, time, platform)
- Captions (platform-specific formatting)
- Hashtags (platform-specific)
- Images/videos (proper format per platform)
- Metrics tracking setup (which metrics matter per platform)
- Cross-promotion links (how to drive between platforms)
- Response plan (who handles comments, what's the response time SLA)
