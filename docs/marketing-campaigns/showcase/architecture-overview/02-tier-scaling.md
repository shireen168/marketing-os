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

### SMB (Product Launch Example)

**The system:**
- Claude Code + 2-3 MCP servers (public data: market trends, competitor analysis, audience demographics)
- Manual decision-making (founder/strategist reviews output, decides next step)
- Time per cycle: 1-2 hours strategic work + approval time vs 2-3 weeks agency
- Run frequency: Per campaign (product launch, seasonal campaign, etc.)

**What it produces:**
- Brief: Strategic direction + positioning options
- Research: Competitor positioning analysis, audience insights, market gaps
- Strategy: Channel recommendations, messaging hierarchy, positioning statement

**Constraints:**
- Data sources are public (market research, competitor websites, trend analysis)
- Decision-making is manual (team reviews and approves)
- Limited to what's publicly available

**Cost:**
- Time: 1-2 hours strategic work per campaign (vs 2-3 weeks agency turnaround)
- Infrastructure: Claude Code + public MCP servers
- Expertise: Mid-level marketing strategy
- ROI: $6-10K agency cost eliminated by in-house operation

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

### SMB (Product Launch)

**What gets produced at each stage:**
- **Stage 1 (Brief):** Strategic brief with audience, channels, KPIs
- **Stage 2 (Voice):** 1-page voice guide (tone, persona, messaging pillars)
- **Stage 3 (Research):** Competitor analysis, audience insights, market gaps
- **Stage 4 (Strategy):** Positioning statement, channel recommendations, messaging hierarchy
- **Stage 5 (Content):** 6+ content pieces with captions, design specs, platform-specific versions
- **Stage 6 (Reports):** Performance projections and ROI estimates

**Team review (Claude Desktop Cowork):**
- Founder/marketing lead reviews each output before execution
- Questions Claude if positioning feels off ("Does this resonate with our target audience?")
- Approves and passes to Tier 3
- See [workflow.md](../../workflow.md) for complete Smart Sleep Device example

**Collaboration depth:**
- One person reviewing (founder or marketing lead)
- 15-30 minutes review per stage
- Changes are strategic (positioning, tone, channel focus)

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

### SMB (Product Launch Campaign)

**The team:**
- 1-2 people (content coordinator, designer)
- Roles: Design, posting, tracking

**Tools used:**
- Canva: Design graphics, templates, visual consistency
- Email platform: Send newsletters, drip campaigns
- Social schedulers: Schedule posts across platforms
- Spreadsheet: Track performance, calendars
- Landing page tool: Build campaign landing pages

**Execution process:**
- Takes approved content plan + strategy from Tier 2
- Designs social assets (Canva)
- Schedules posts (native schedulers or Linktree)
- Sets up email campaigns
- Logs performance in tracker
- Iterates based on weekly reports

**Time per campaign:**
- Campaign launch: 3-5 hours (design, setup, scheduling)
- Weekly monitoring: 30 minutes
- **Total: ~5-10 hours over campaign lifecycle**

**Cost:**
- 1 person at mid-level ($2-3K/month)
- Tool subscriptions: Canva, scheduler, email (~$50-100/month)

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
