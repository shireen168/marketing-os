---
name: marketing-os-analytics-dashboard
description: Build weekly marketing analytics dashboards tracking reach, engagement, ROI, and optimization opportunities
type: marketing
---

# Marketing-OS: Analytics Dashboard Skill

Transform raw platform metrics into actionable weekly dashboards. Track what's working, what's not, and where to focus next week's effort and budget.

## Use When

- Week complete, need to review performance
- Monthly budget check (ROI analysis)
- Identifying top-performing content (what to repeat)
- Spotting underperforming content (what to kill)
- Planning next week's strategy based on data

## How to Use

**Input:** Platform metrics (Facebook, Instagram, TikTok, LinkedIn, email, etc.), weekly performance data, budget spent, goals from the week

**Output:** Executive summary dashboard with performance by format, product, platform; ROI analysis; optimization recommendations

## Templates

### Template 1: Weekly Marketing Dashboard

```
PROMPT:
Build a weekly marketing performance dashboard.

Date range: [START DATE] to [END DATE]
Platforms: [Facebook, Instagram, TikTok, LinkedIn, Email, Other]
Budget spent this week: $[AMOUNT]
Team size: [solo / 2 people / team of X]
Content posted: [NUMBER OF POSTS] posts/week

Metrics available: [list what you track from each platform]

Provide a dashboard with sections:

1. Executive Summary (one paragraph)
   - Total reach
   - Total engagement
   - Top performer (post/product)
   - Key insight (what's the biggest learning?)

2. Performance by Platform (table + analysis)
   - Facebook: Reach, Engagement Rate, Shares, Saves
   - Instagram: Reach, Engagement Rate, Shares, Saves
   - TikTok: Views, Engagement Rate, Comments
   - [Other platforms used]
   - Total: combined metrics

3. Performance by Content Format (table)
   - Reels/Short-form video: [metrics]
   - Carousel: [metrics]
   - Single image: [metrics]
   - Static text: [metrics]
   - Best format for next week: [recommendation]

4. Performance by Product (table)
   - Product 1: [reach, engagement, saves, intent-to-buy signals]
   - Product 2: [metrics]
   - Best performer: [which product moved the needle]
   - Underperformer: [which product got minimal traction]

5. ROI Analysis (if applicable)
   - Budget spent: $[AMOUNT]
   - Reach generated: [TOTAL IMPRESSIONS]
   - Cost per impression: $[AMOUNT]
   - Engagement generated: [TOTAL INTERACTIONS]
   - Cost per engagement: $[AMOUNT]
   - Estimated value (if revenue tied to content): $[if known]

6. Top 3 Insights
   - What worked: [specific finding with numbers]
   - What didn't work: [specific finding with numbers]
   - Opportunity: [where to focus next]

7. Actionable Recommendations
   - Double down on: [format/product/angle]
   - Reduce or eliminate: [what underperformed]
   - Test next week: [new angle/format/time]
   - Fix: [what's broken or needs iteration]

Return as formatted markdown or JSON dashboard.
```

### Template 2: Sunny Homemade Weekly Analytics

```
PROMPT:
Analyze Sunny Homemade's weekly performance (Facebook + Instagram).

Week of: [DATE]
Posts published: [NUMBER and which products/formats]
Budget spent: $[AMOUNT] (ads + tools)
Goals for week: [what was the objective?]

Metrics data available:
- Facebook: [views, engagement, shares, saves for each post]
- Instagram: [views, engagement, shares, saves for each post]
- Organic reach only (0 ad spend at moment)
- Email list: [if tracking opens/clicks]

Provide:
1. One-page executive summary
   - Reach (total impressions both platforms)
   - Engagement (total interactions)
   - Best post (which one? views + engagement)
   - Worst post (which one? why did it underperform?)
   - Product insights (which product resonated most)

2. Format performance breakdown
   - Reels: [avg reach, avg engagement rate, best performer]
   - Carousels: [metrics]
   - Single images: [metrics]
   - Best format recommendation (reel vs. carousel vs. static)

3. Product performance breakdown
   - Collagen: [reach, engagement, saves, intent signals]
   - Bak Zang: [metrics]
   - Ginger Paste: [metrics]
   - Chilli Paste: [metrics]
   - Winning product: [which one got most saves/engagement]

4. Content angle analysis
   - Before-after angles: [performance]
   - Recipe/how-to angles: [performance]
   - Emotional/story angles: [performance]
   - Educational/benefit angles: [performance]
   - Best angle for next week: [recommendation]

5. Time-based insights
   - Posts by day of week (did certain days outperform?)
   - Posts by time of day (early morning vs. evening better?)
   - Week over week trend (growing or declining engagement?)

6. Recommendations for next week
   - Content format: 80% [WHAT], 20% [WHAT] (based on data)
   - Product focus: Feature [PRODUCT] more (highest performer)
   - Angle to test: [NEW ANGLE based on gaps in performance]
   - Timing optimization: Post at [TIME] (algorithm sweet spot)
   - Content to reduce: [ANGLE/FORMAT that underperformed]

Return as one-page executive dashboard.
```

### Template 3: ROI & Cost Analysis

```
PROMPT:
Calculate marketing ROI and cost efficiency.

Time period: [WEEK / MONTH]
Content published: [NUMBER of posts/emails/campaigns]
Total budget: $[for ads/tools/content production]
Revenue generated: $[if trackable; or "not tracking" if not]
Audience growth: [NEW FOLLOWERS/SUBSCRIBERS this period]

Metrics:
- Total reach: [IMPRESSIONS]
- Total engagement: [INTERACTIONS]
- Conversions: [SALES or SIGNUPS if known]

Provide:
1. Cost Breakdown
   - Ad spend: $[AMOUNT]
   - Tools (scheduling, analytics, design): $[AMOUNT]
   - Content production time: [HOURS] = $[calculated at $50/hr rate]
   - Total cost: $[SUM]

2. Efficiency Metrics
   - Cost per impression: $[TOTAL BUDGET / TOTAL REACH]
   - Cost per engagement: $[TOTAL BUDGET / TOTAL ENGAGEMENT]
   - Cost per follower: $[if follower growth tracked]

3. ROI (if revenue tracked)
   - Revenue generated: $[AMOUNT]
   - Cost: $[AMOUNT]
   - Net: $[REVENUE - COST]
   - ROI %: [REVENUE / COST * 100]%
   - Return per dollar: $[REVENUE / COST]

4. Benchmarks
   - Industry average cost per engagement: [show what's typical]
   - Your rate: [show where you stand]
   - Is this efficient? [analysis]

5. Optimization recommendation
   - Keep doing: [what's cost-efficient]
   - Stop doing: [what's expensive relative to results]
   - Invest more in: [high-ROI activities]

Return as structured ROI report.
```

## Real Examples

### Sunny Homemade Weekly Dashboard (Apr 28 - May 4)

```json
{
  "week": "Apr 28 - May 4, 2026",
  "executive_summary": "Strong week with 4.9K total reach across platforms and 114 total interactions. Reels continue to dominate (80% of reach, 85% of engagement). Collagen and chilli paste reels each hit 390+ views. Strategic insight: Short-form video (reels) is the core driver; single images should be eliminated in favor of carousels or reels. Recommendation: Shift to 80% reels + 20% carousel format.",
  "performance_by_platform": {
    "facebook": {
      "posts_published": 3,
      "total_reach": 2100,
      "total_engagement": 52,
      "engagement_rate": "2.5%",
      "top_post": "Collagen before-after reel (397 views)",
      "performance": "Baseline platform, organic reach only"
    },
    "instagram": {
      "posts_published": 4,
      "total_reach": 2800,
      "total_engagement": 62,
      "engagement_rate": "2.2%",
      "top_post": "Chilli paste cold dish reel (390 views)",
      "performance": "Higher absolute reach than Facebook, younger audience"
    }
  },
  "performance_by_format": {
    "reels": {
      "posts": 4,
      "avg_reach": 350,
      "avg_engagement": 28,
      "engagement_rate": "8%",
      "recommendation": "Core format. Increase to 80% of output."
    },
    "carousel": {
      "posts": 2,
      "avg_reach": 180,
      "avg_engagement": 12,
      "engagement_rate": "6.7%",
      "recommendation": "Secondary format. Keep at 15-20% of output."
    },
    "single_image": {
      "posts": 1,
      "avg_reach": 110,
      "avg_engagement": 4,
      "engagement_rate": "3.6%",
      "recommendation": "Eliminate unless paired with high-emotion hook."
    }
  },
  "performance_by_product": {
    "collagen": {
      "posts": 2,
      "total_reach": 1200,
      "engagement_rate": "7%",
      "top_performer": "Before-after reel (397 views, 5 saves)"
    },
    "chilli_paste": {
      "posts": 2,
      "total_reach": 980,
      "engagement_rate": "7.8%",
      "top_performer": "Cold dish reel (390 views, 5 saves)"
    },
    "ginger_paste": {
      "posts": 2,
      "total_reach": 640,
      "engagement_rate": "4.2%",
      "finding": "Underperformer this week"
    }
  },
  "top_3_insights": [
    {
      "insight": "Reels drive 6x watch time vs. static posts",
      "data": "Reel avg watch time 28 minutes total per post. Static post avg 4 minutes total.",
      "action": "Make reels 80% of output."
    },
    {
      "insight": "Before-after and reveal formats outperform recipes by 2-3x",
      "data": "Before-after collagen reel: 397 views. Recipe carousel: 120 views.",
      "action": "Increase narrative/emotional hooks. Test more before-after content."
    },
    {
      "insight": "3-second watch rate is the engagement lever",
      "data": "Posts with 0-3s hooks: 380-397 views. Posts with longer intros: 120-200 views.",
      "action": "Optimize first 3 seconds of every reel. Test faster cuts, stronger hooks."
    }
  ],
  "recommendations": {
    "format_split": "80% reels, 15% carousel, 5% single image (if high-emotion hook)",
    "content_angles": "Increase before-after and reveal formats. Decrease recipe-focused content (lower engagement).",
    "product_focus": "Feature collagen and chilli paste more. Investigate ginger paste underperformance (angle/timing issue?).",
    "posting_schedule": "Reels: Wed/Thu/Fri/Sat (peak times 6-8pm). Carousel: Tue/Thu (3-5pm). Single: Avoid unless special case.",
    "next_week_test": [
      "Test 60-second reel format (current avg 30s)",
      "Test trending audio (current: mostly no music/original)",
      "Test user-generated angle (if customers can submit transformations)"
    ]
  }
}
```

### Generic SaaS Example: Monthly ROI Analysis

```json
{
  "month": "May 2026",
  "cost_analysis": {
    "ad_spend": 0,
    "content_tools": 50,
    "production_time_hours": 40,
    "production_cost": 2000,
    "total_cost": 2050
  },
  "efficiency_metrics": {
    "total_reach": 15000,
    "total_engagement": 450,
    "cost_per_impression": 0.137,
    "cost_per_engagement": 4.56
  },
  "roa_analysis": {
    "revenue_attributed": 5000,
    "cost": 2050,
    "net_profit": 2950,
    "roi_percent": "143.9%",
    "return_per_dollar": 2.44
  },
  "benchmark_comparison": {
    "your_cost_per_engagement": 4.56,
    "industry_average": 3.50,
    "status": "Above average (less efficient)",
    "opportunity": "Reduce production time or increase engagement rate"
  }
}
```

## Workflow Integration

**Weekly rhythm:**
1. **Monday morning:** Run this skill with weekend + week data
2. **Generate dashboard:** 30-60 min (pulling data + analysis)
3. **Review findings:** 30 min (read insights, identify patterns)
4. **Plan next week:** Use insights to inform `/social-scheduling` and content strategy
5. **Archive dashboard:** Save to `projects/sunny-homemade/analytics/` for historical tracking

**Monthly rhythm:**
1. **Month-end:** Aggregate weekly dashboards
2. **ROI analysis:** Calculate month-over-month trends
3. **Budget review:** Did we hit targets? Over/under spend?
4. **Report to stakeholders:** If team/client, share findings + recommendations

## Pro Tips

**Data collection:**
- Facebook/Instagram: Use Meta Business Suite native analytics
- TikTok: Native analytics dashboard (requires 1000+ followers)
- Email: Native analytics from email provider (opens, clicks, conversions)
- Manual: Keep simple spreadsheet for platforms without built-in analytics

**Metric prioritization:**
- **Reach:** Who saw it?
- **Engagement:** Who interacted?
- **Saves:** Who found it valuable enough to save?
- **Shares:** Who amplified it?
- **Conversions:** Who took action (clicked link, made purchase)?

**Sunny Homemade specific:**
- Track by product (which product gets most saves?)
- Track by format (reels vs. carousel engagement rate)
- Track by platform (where does each product perform best?)
- Track by angle (emotional vs. educational vs. how-to)
- Watch time for reels (key metric for algorithm)

**Benchmarking:**
- Reel engagement rate: typically 4-8% (you want 6%+)
- Post engagement rate: typically 1-3% (you want 2%+)
- Save rate: 10-20% of engagements (high-quality content signal)
- Cost per engagement: $2-5 range (organic content, no ads)

## Output Format

Deliverable to leadership/team (weekly):
- One-page executive dashboard (visual format preferred)
- Performance tables (reach, engagement by platform/format/product)
- Top 3 insights (with data)
- Actionable recommendations (what to do differently next week)
- Metrics to track next week (focus areas)
- Historical trend (how are we doing month-over-month?)

Store all dashboards in: `projects/marketing-os/analytics/[YYYY-MM]-dashboard.md`
