# How Three Tiers Scale (SMB → Enterprise)

## What Doesn't Change (The Foundation)

**The framework stays the same at any scale:**
- Six stages still flow in order (Brief → Voice → Research → Strategy → Content → Reports)
- Context still preserved end-to-end (Stage 5 references Stage 2 + 4 automatically)
- Claude Code still orchestrates (central decision-making logic)
- Approval gates still happen in Claude Desktop Cowork (human-in-the-loop at each checkpoint)

**The flow is identical.** What changes is volume, complexity, and integration depth.

---

## Tier 1: Strategic Intelligence Scaling

### SMB (Sunny Homemade)

**The system:**
- Claude Code + 2-3 MCP servers (public data: market trends, competitor pricing, audience demographics)
- Manual decision-making (Shireen reviews output, decides next step)
- Time per cycle: 5 minutes system + 10 minutes manual review = 15 minutes
- Run frequency: Weekly (once per week)

**What it produces:**
- Brief: 500-word strategic direction
- Research: Competitor analysis (3-5 competitors), audience insights from tracker data
- Strategy: Channel focus (Instagram reels), content angle (heritage + family duty)

**Constraints:**
- Data sources are public (Twitter trends, Instagram insights, Google Trends)
- Decision-making is manual (Shireen makes the calls)
- Limited to what's publicly available

**Cost:**
- Time: 15 minutes weekly
- Infrastructure: Claude Code + public MCP servers
- Expertise: Mid-level marketing strategy

---

### Enterprise (Fortune 500 Marketing Department)

**The system:**
- Claude Code + 10+ MCP servers (proprietary: sales CRM data, brand guidelines, legal review, exec reporting, customer NPS, pricing data)
- Automated workflows (approval gates, stakeholder notifications, legal review automation)
- Time per cycle: 5 minutes system + 30 minutes automated review = 35 minutes
- Run frequency: Daily or per-campaign (triggered by new product launch, quarter planning)

**What it produces:**
- Brief: 2,000-word strategic direction + appendices (regional variants, product-specific angles)
- Research: Deep competitive analysis (50+ competitors), audience segmentation by region/persona, win/loss analysis
- Strategy: Multi-channel approach (brand strategy + regional variants + channel-specific tactics)

**Advantages:**
- Data sources are proprietary (CRM, brand systems, sales pipeline, customer feedback)
- Decision-making is partially automated (approval gates, automated compliance checks)
- Can leverage internal data at scale

**Additional complexity:**
- Legal review automation (new claims need legal sign-off)
- Stakeholder notifications (CMO, product, legal, exec leadership each get relevant updates)
- Regional adaptation (same strategy, localized for EMEA, APAC, Americas)

**Cost:**
- Time: 35 minutes per cycle + integration overhead
- Infrastructure: Enterprise MCP servers, internal system integrations
- Expertise: Senior strategy + legal + product alignment

---

## Tier 2: Workflow Outputs Scaling

### SMB (Sunny Homemade)

**What gets produced at each stage:**
- **Stage 1 (Brief):** 500-word strategic brief + featured products for the week
- **Stage 2 (Voice):** 1-page voice guide (Mandarin-first tone, product-specific voice)
- **Stage 3 (Research):** 1-page competitor + audience analysis (3-5 competitors, tracker trends)
- **Stage 4 (Strategy):** 1-page channel strategy (Instagram reels + Facebook carousel, format decisions)
- **Stage 5 (Content):** 6 posts with captions, design specs (bilingual, emotion-driven hook)
- **Stage 6 (Reports):** 1-page performance report (weekly metrics, ad ROI, next week recommendations)

**Team review (Claude Desktop Cowork):**
- Shireen reviews each output before execution
- Questions Claude if something feels off ("Is this tone right for our audience?")
- Approves and passes to Tier 3

**Collaboration depth:**
- One person reviewing (Shireen)
- 15-20 minutes review per stage
- Changes are minor (tone tweaks, copy adjustments)

---

### Enterprise (Fortune 500)

**What gets produced at each stage:**
- **Stage 1 (Brief):** 5,000-word strategic brief + 10 regional variants + 20 appendices (competitive deep-dives, customer research, market sizing)
- **Stage 2 (Voice):** 50-page brand guide (global brand voice + regional tone adaptations + product-specific personas)
- **Stage 3 (Research):** 100-page research synthesis (50+ competitors analyzed, segmentation by region/persona, trend forecasting, win/loss analysis)
- **Stage 4 (Strategy):** 30-page strategy doc (brand positioning + regional strategies + channel-specific tactics + budget allocation)
- **Stage 5 (Content):** 500+ content variations (A/B tests, regional variants, channel-specific creative briefs, 50+ pieces for different segments)
- **Stage 6 (Reports):** 20-page board-ready report (real metrics, variance analysis, ROI by region/channel, forecast for next quarter)

**Team review (Claude Desktop Cowork):**
- Regional marketing managers review (EMEA, APAC, Americas each have a manager)
- Product managers review (each product line has a PM)
- Brand compliance reviews (legal, brand team)
- Executive team reviews (CMO, CFO may see highlights)
- Multiple layers of approval gates

**Collaboration depth:**
- 5-10 people reviewing at different stages
- 2-4 hours per stage for full stakeholder review
- Changes are strategic (new markets, new positioning, competitive response)
- Cowork tracks who approved what and why

---

## Tier 3: Post-Approval Execution Scaling

### SMB (Sunny Homemade)

**The team:**
- 1 person (Shireen)
- Roles: Content creation, design, posting, tracking

**Tools used:**
- Gemini/ChatGPT: Generate reel images (5 images per reel)
- Canva: Create labels, design adjustments, text overlays
- CapCut: Edit reel, add bilingual text, add transitions
- Instagram/Facebook: Post reels, add captions, track engagement
- Spreadsheet: Update performance tracker

**Execution process:**
- Takes approved content plan from Tier 2
- Generates images (Gemini)
- Designs in Canva
- Edits in CapCut
- Posts on Instagram/Facebook
- Logs performance in tracker

**Time per week:**
- 6 reels: 4 hours (40 minutes per reel)
- Posting: 30 minutes
- Tracking: 15 minutes
- **Total: 4.75 hours/week**

**Cost:**
- 1 person at junior/mid-level ($2-3K/month)
- Tool subscriptions: Canva, CapCut (~$100/month)

---

### Enterprise (Fortune 500)

**The team:**
- 10-20 people across functions
  - Content creators (3-4)
  - Designers (2-3)
  - Social media managers (2-3)
  - Content operations (1-2)
  - Approval/compliance (1)
  - Analytics (1)

**Tools used:**
- AI tools: Claude Desktop Cowork, Gemini, ChatGPT (for variations)
- Design: Canva, Adobe Creative Suite, custom brand asset management
- Video: CapCut, Adobe Premiere, DaVinci Resolve
- Social: Hootsuite, Sprout Social, native platform dashboards
- Planning: Asana, Monday.com (project management)
- Analytics: Tableau, Looker (real-time dashboards)
- Email: Marketo, Salesforce Marketing Cloud
- Approval workflows: Custom integrations (Slack notifications, email approvals)

**Execution process:**
- Tier 2 outputs arrive in the execution queue
- Content ops creates project in Asana (region-specific tasks)
- Content creators write variations (30+ versions from base copy)
- Designers create assets (multiple formats: static, video, carousel)
- Managers schedule across channels (Instagram, Facebook, TikTok, LinkedIn, email, SMS)
- Approval gate: Brand compliance reviews before posting
- Schedule posts via Hootsuite or native schedulers
- Real-time monitoring (Tableau dashboards track engagement)
- Analytics team analyzes and feeds back to next Tier 1 cycle

**Time per campaign:**
- 500+ pieces of content: 60-80 hours total
- Multiple parallel workflows (don't wait for one region to finish)
- Continuous: New campaigns every week or bi-weekly

**Cost:**
- 10-20 people: $150-300K/month (junior to senior salaries)
- Tool subscriptions: $5-10K/month (enterprise licenses)

**Efficiency gain:**
- Each person executes 25-50 pieces per week (specialized role)
- Approval gates catch 80%+ of brand/legal issues before posting
- Real-time dashboards mean rapid optimization between campaigns

---

## What Stays the Same (Key Insight)

### The Core Architecture Doesn't Change

**At SMB level (Sunny Homemade):**
- Tier 1: Claude Code + 2-3 MCP servers = 15 minutes
- Tier 2: 6 stage outputs = 1-2 hours
- Tier 3: 1 person executes = 4-5 hours/week

**At Enterprise level (Fortune 500):**
- Tier 1: Claude Code + 10+ MCP servers = 35 minutes
- Tier 2: 6 stage outputs (bigger, more variants) = 4-6 hours
- Tier 3: 10-20 people execute in parallel = same time, higher throughput

**The ratio stays consistent:**
- Tier 1 (thinking) = 1-5% of time
- Tier 2 (collaboration) = 20-30% of time
- Tier 3 (execution) = 65-75% of time

**This means:**
- You don't need to hire more strategists to scale (Tier 1 effort stays constant)
- You hire more executors (Tier 3 scales linearly)
- The system doesn't break at scale

---

## The Scaling Pitch

### To SMB Founders

> "This framework works at your scale today (Sunny Homemade). When you're 10x bigger, the process stays the same—you just hire more people for Tier 3 (execution). Tier 1 (strategy) and Tier 2 (collaboration) don't get exponentially harder."

**What they understand:**
- No reinvention needed as they grow
- Consultant doesn't become a bottleneck
- They can scale execution team independently

### To Enterprise VPs

> "This framework scales to your 100-person team without breaking. What changes is the depth of data sources and the number of executors. The fundamentals—six stages, approval gates, context preservation—stay the same. That's why it scales."

**What they understand:**
- Architectural soundness (doesn't break at scale)
- Governance is baked in (not added later)
- No "rewrite when we get bigger" risk
- Can handle complexity (regional, product variants, stakeholder approvals)

---

## Quick Comparison Table

| Dimension | SMB | Enterprise |
|-----------|-----|-----------|
| **Tier 1 Time** | 15 min/week | 35 min/day or per-campaign |
| **Tier 1 Data** | Public (trends, insights) | Proprietary (CRM, legal, sales) |
| **Tier 1 Decisions** | Manual | Partially automated + approval gates |
| **Tier 2 Output Volume** | 6 outputs/week | 500+ variants/campaign |
| **Tier 2 Reviewers** | 1 person | 5-10 stakeholders |
| **Tier 2 Approval Time** | 20 min/stage | 2-4 hours/stage |
| **Tier 3 Team** | 1 person | 10-20 people |
| **Tier 3 Tools** | Canva, CapCut, Spreadsheet | Suite of enterprise tools |
| **Tier 3 Output** | 6 posts/week | 500+ pieces/campaign |
| **Tier 3 Time** | 4-5 hours/week | 60-80 hours/campaign (parallel) |
| **Governance** | Minimal | Full trail + approval gates |

---

## Key Insight: What Makes This Scalable

**Most consultants scale by getting busier (more projects, less depth).**

**This system scales differently:**
- **Tier 1 effort stays constant** (infrastructure, not effort-per-project)
- **Tier 2 depth increases** (more variants, more stakeholders, same process)
- **Tier 3 grows horizontally** (more executors, not harder executors)

**That's the architecture advantage.**

You can take on 10x the clients without burning out (because Tier 1 is leveraged infrastructure, not billable hours). You can serve bigger clients without reinventing (because Tier 2 and 3 scale predictably).

That's why three tiers matter at enterprise scale.
