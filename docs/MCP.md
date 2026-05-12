# Marketing OS MCP Integration

Model Context Protocol (MCP) allows Claude Desktop to interact with Marketing OS through slash commands.

## What is MCP?

MCP is a standard protocol that lets Claude Desktop connect to tools and services. Once configured, you can use Marketing OS directly in Claude Desktop as if it were a native feature.

## Setup

### Prerequisites

- Claude Desktop installed (Mac or Windows)
- Marketing OS API running locally (via `docker-compose up`)
- Node.js 20+

### Step 1: Update claude_desktop_config.json

Find your Claude Desktop config file:

**Mac:**
```
~/Library/Application Support/Claude/claude_desktop_config.json
```

**Windows:**
```
%APPDATA%\Claude\claude_desktop_config.json
```

Open it and add this to the `mcpServers` section (create the section if it doesn't exist):

```json
{
  "mcpServers": {
    "marketing-os": {
      "command": "npm",
      "args": ["run", "mcp-server"],
      "cwd": "/full/path/to/marketing-os"
    }
  }
}
```

Replace `/full/path/to/marketing-os` with your actual path:
- Mac example: `/Users/shireen/Desktop/claude-system/marketing-os`
- Windows example: `C:\\Users\\user\\Desktop\\claude-system\\marketing-os`

### Step 2: Restart Claude Desktop

Close Claude Desktop completely and open it again. You should see "marketing-os" connected at the bottom of the window.

### Step 3: Test the Connection

In Claude Desktop, type:

```
/listBriefs
```

If it works, you should see an empty list (no briefs yet). If it fails, check the MCP setup above.

## Available Commands

### brieftodraft

Generate optimized drafts from a brief.

**Usage:**
```
/brieftodraft

title: Q2 Product Launch
description: Announce our new AI analytics feature
brandContext: Developer-friendly, technical, approachable
targetAudience: Engineering leaders at mid-market SaaS
goal: Awareness and trial signups
channels: email, linkedin, medium
keyMessages: Real-time AI insights, No model training, Built for engineers
tone: Technical but approachable
cta: Start free trial
```

**Optional: Regenerate with feedback:**
```
/brieftodraft

feedback: Make it shorter and more casual
```

**Result:**
```json
{
  "id": "brief-123",
  "title": "Q2 Product Launch",
  "drafts": [
    {
      "id": "draft-email-1",
      "channel": "email",
      "content": "[email draft...]"
    },
    {
      "id": "draft-linkedin-1",
      "channel": "linkedin",
      "content": "[LinkedIn post...]"
    },
    {
      "id": "draft-medium-1",
      "channel": "medium",
      "content": "[Medium article...]"
    }
  ]
}
```

### publish

Publish approved drafts to channels.

**Usage:**
```
/publish

briefId: brief-123
draftIds: draft-email-1, draft-linkedin-1
channels: email, linkedin
```

This publishes the email draft to SendGrid and the LinkedIn draft to LinkedIn API.

**Result:**
```json
{
  "published": [
    {
      "draftId": "draft-email-1",
      "channel": "email",
      "status": "sent",
      "timestamp": "2026-05-12T10:30:00Z"
    }
  ]
}
```

### report

Get analytics for a campaign.

**Usage:**
```
/report

campaignId: brief-123
days: 7
```

**Result:**
```json
{
  "campaign": "brief-123",
  "analytics": {
    "email": {
      "sent": 2400,
      "opened": 768,
      "openRate": "32%",
      "clicked": 96,
      "ctr": "4%"
    },
    "linkedin": {
      "impressions": 5200,
      "engaged": 450,
      "engagementRate": "8.6%",
      "likes": 120,
      "comments": 30,
      "shares": 10
    }
  },
  "summary": "Solid engagement across channels"
}
```

### listBriefs

List all briefs you have created.

**Usage:**
```
/listBriefs
```

Or with a limit:

```
/listBriefs

limit: 5
```

**Result:**
```json
{
  "briefs": [
    {
      "id": "brief-123",
      "title": "Q2 Product Launch",
      "createdAt": "2026-05-12T09:00:00Z",
      "status": "published"
    }
  ]
}
```

## Complete Workflow in Claude Desktop

1. Start with a brief:

```
/brieftodraft

title: Summer Campaign
description: Drive signups for our new feature
targetAudience: Startup founders
goal: Increase trial signups by 25%
channels: email, linkedin
keyMessages: Save 10 hours per month, Simple setup
tone: Friendly and helpful
cta: Try free for 14 days
```

2. Review the drafts Claude shows you. Ask Claude to regenerate if needed:

```
/brieftodraft

feedback: The email is too long, make it 3 sentences max. Add urgency to the CTA
```

3. Once happy with drafts, publish:

```
/publish

briefId: brief-456
draftIds: draft-email-2, draft-linkedin-2
channels: email, linkedin
```

4. After a week, check results:

```
/report

campaignId: brief-456
days: 7
```

5. Ask Claude to help interpret the results and plan next steps.

## Troubleshooting

**MCP not connecting?**
1. Check that `docker-compose up` is running and API is at localhost:3000
2. Verify the path in claude_desktop_config.json is absolute (not relative)
3. Check for typos in the config file (JSON must be valid)
4. Try running `npm run mcp-server` manually in the marketing-os folder to see errors

**Command not working?**
1. Make sure the API is running (`docker-compose up`)
2. Check that you have ANTHROPIC_API_KEY set in .env.local
3. Verify the command syntax matches the examples above
4. Try `/listBriefs` first to test the connection

**Permission issues on Mac?**
If you get "permission denied", try:
```bash
chmod +x ~/path/to/marketing-os/packages/mcp/src/server.ts
```

## Architecture

The MCP server acts as a bridge between Claude Desktop and the Marketing OS API:

```
Claude Desktop
     ↓ (slash commands)
  MCP Server
     ↓ (HTTP requests)
  Marketing OS API (localhost:3000)
     ↓
  PostgreSQL + Redis
```

Each command maps directly to an API endpoint. See `API.md` for the full REST specification.

## Next Steps

Once you have MCP working:
1. Test with example briefs
2. Connect your actual marketing channels (SendGrid, LinkedIn API, Medium)
3. Run a real campaign through the system
4. Evaluate Phase 2 (web UI with more advanced features)
