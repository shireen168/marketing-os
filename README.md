# Marketing OS

**Reduce your content production from 3-5 days to 30 minutes. Keep 40% of your marketing budget.**

---

## The Problem

Your marketing team spends too much time on repetitive work:

- Writing a brief for a new campaign
- Creating separate versions for email, LinkedIn, Medium, Twitter
- Editing and coordinating across channels
- Managing publishing timelines
- Tracking results across platforms

Result: 3-5 days per campaign. $3-5k per campaign in agency costs. Only 3-4 campaigns per quarter instead of monthly campaigns.

---

## The Solution

**Marketing OS** compresses the entire workflow:

1. Write one brief describing your campaign
2. Claude AI generates optimized versions for each channel (email, LinkedIn, Medium, etc.) in 2 minutes
3. Review and make edits in Claude Desktop
4. Publish to all channels with one command
5. Track performance across platforms automatically

**Time saved per campaign: 3-5 days**
**Cost saved per campaign: $3-5k**
**New campaign frequency: Monthly instead of quarterly**

---

## How It Works

### Step 1: Write a Brief (5 minutes)

Your marketing manager creates a brief in Claude Desktop:

```
/brieftodraft

title: Q2 Product Launch
description: Announce our new AI analytics feature
targetAudience: Engineering leaders at mid-market SaaS
goal: Generate trial signups
channels: email, linkedin, medium
keyMessages: Real-time insights, No model training, Built for engineers
tone: Technical but approachable
cta: Start free trial
```

### Step 2: Get Channel-Optimized Drafts (2 minutes)

Claude generates three tailored versions:
- Email (optimized for open rate and clicks)
- LinkedIn post (optimized for engagement)
- Medium article (optimized for SEO and time-on-page)

### Step 3: Review and Edit (15-30 minutes)

Marketing team reviews drafts in Claude Desktop. Request changes:

```
/brieftodraft --feedback "Make it shorter, add more urgency"
```

Claude regenerates based on feedback. Approve when ready.

### Step 4: Publish (5 minutes)

One command publishes to all channels:

```
/publish --channels email,linkedin,medium
```

Email goes through SendGrid. LinkedIn and Medium posts automatically.

### Step 5: Track Results (1 minute)

After one week:

```
/report --campaign q2-launch --days 7
```

See email opens, clicks, LinkedIn engagement, Medium reads, all in one view.

---

## The Real Impact

**Before Marketing OS (Team + Agency):**
- Monday: Manager writes brief
- Tuesday-Wednesday: Wait for agency to draft email, LinkedIn, Medium
- Thursday: Receive drafts, request revisions
- Friday: Agency sends final versions
- Weekend: Manage publishing across channels
- Cost: $3-5k per campaign
- Timeline: 3-5 days

**With Marketing OS (Team In-House):**
- Monday 8am: Manager writes brief in Claude Desktop
- Monday 8:30am: Team reviews generated drafts
- Monday 9am: Team requests one round of revisions
- Monday 9:30am: Team publishes across all channels
- No agency needed
- Cost: $0 (no external vendor)
- Timeline: 30 minutes
- Result: Eliminate 40% of marketing spend, do monthly campaigns instead of quarterly

---

## What You Get

- **Ownership**: Self-hosted on your infrastructure, no vendor lock-in
- **Speed**: 3-5 days to 30 minutes per campaign
- **Cost**: 40% reduction in marketing spend ($1.5-2k saved per campaign)
- **Quality**: AI-generated, reviewed by your team, optimized per channel
- **Data**: Your data stays on your servers
- **Integration**: Works with SendGrid, LinkedIn, Medium APIs (bring your own keys)
- **Scale**: Handle monthly campaigns instead of quarterly

---

## Prerequisites

To run Marketing OS, you need:

- **Claude Desktop** (free or Pro account)
- **Node.js 20+** (https://nodejs.org/)
- **Docker & Docker Compose** (https://www.docker.com/)
- **ANTHROPIC_API_KEY** (your Claude API key from https://console.anthropic.com/)

**Hardware:** Any modern laptop/server. Tested on Mac and Windows.

---

## Setup (15 minutes)

Hire a developer to do this once. After setup, your marketing team just uses Claude Desktop.

### For Your Developer:

**Step 1: Clone and install**
```bash
git clone https://github.com/shireen168/marketing-os.git
cd marketing-os
npm install
```

**Step 2: Configure**
```bash
cp .env.example .env.local
# Add your ANTHROPIC_API_KEY
```

**Step 3: Start services**
```bash
docker-compose up
```

**Step 4: Connect to Claude Desktop**

The MCP server connects Claude Desktop to Marketing OS. Create/edit your config file:

**On Windows:**
`C:\Users\[YourUsername]\AppData\Local\Packages\Claude_pzs8sxrjxfjjc\LocalCache\Roaming\Claude\claude_desktop_config.json`

**On macOS:**
`~/Library/Application Support/Claude/claude_desktop_config.json`

**On Linux:**
`~/.config/Claude/claude_desktop_config.json`

Add this JSON (replace path with your Marketing OS location):

```json
{
  "mcpServers": {
    "marketing-os": {
      "command": "node",
      "args": [
        "/full/path/to/marketing-os/packages/mcp/dist/server.js"
      ],
      "env": {
        "API_URL": "http://localhost:3000"
      }
    }
  }
}
```

**Step 5: Test**

1. Make sure the API server is running: `npm run dev --workspace=@marketing-os/api`
2. Fully restart Claude Desktop (quit and reopen)
3. Go to Settings → Connectors → look for "marketing-os" server
4. In chat, type: `/listBriefs`

If it returns an empty list, you're connected and ready to go.

Full setup guide: See [docs/QUICKSTART.md](docs/QUICKSTART.md) and [docs/MCP.md](docs/MCP.md)

---

## Available Commands

Once set up, your team uses these in Claude Desktop:

**`/brieftodraft`** - Write a campaign brief, get optimized drafts for each channel
**`/publish`** - Publish approved drafts to email, LinkedIn, Medium
**`/report`** - See campaign performance (opens, clicks, engagement)
**`/listBriefs`** - View all past campaigns

---

## Tech Stack

This is a production-ready system built with:

**Backend:**
- Node.js 20 + Express/Fastify
- PostgreSQL 15 (data storage)
- Redis 7 (caching/sessions)
- Claude API (draft generation)

**Integration:**
- MCP (Claude Desktop connection)
- SendGrid (email delivery)
- LinkedIn API (social posting)
- Medium API (article publishing)

**Deployment:**
- Docker + Docker Compose (local dev)
- GitHub Actions (CI/CD)
- TypeScript (type safety)

**Scale:**
- Handles any volume of campaigns
- Monorepo structure for future scaling
- Ready for multi-team deployment

---

## Integration Setup

To actually send emails and post to social media, configure:

**SendGrid (for email):**
- Create a SendGrid account
- Add your API key to `.env.local`

**LinkedIn API (for LinkedIn posts):**
- Register a LinkedIn app
- Add your access token to `.env.local`

**Medium API (for Medium articles):**
- Get your Medium access token
- Add to `.env.local`

All keys are stored locally. No data leaves your infrastructure.

---

## Customization

Marketing OS is built to be extended:

- Add new channels (Twitter, Slack, internal systems)
- Add new integrations (HubSpot, Marketo, Salesforce)
- Customize prompt behavior
- Build custom reporting

See [docs/DEVELOPMENT.md](docs/DEVELOPMENT.md) for extending the system.

---

## Documentation

- **[QUICKSTART.md](docs/QUICKSTART.md)** - Step-by-step setup (15 min)
- **[ARCHITECTURE.md](docs/ARCHITECTURE.md)** - System design and data models
- **[API.md](docs/API.md)** - Complete REST endpoint specifications
- **[MCP.md](docs/MCP.md)** - Claude Desktop integration details
- **[DEVELOPMENT.md](docs/DEVELOPMENT.md)** - For developers extending the system
- **[PORTFOLIO.md](PORTFOLIO.md)** - What this system demonstrates

---

## License

MIT
