# Marketing OS Quick Start

Complete setup from zero to sending your first campaign. Estimated time: 15 minutes.

## Prerequisites

- Claude Desktop installed (get it from https://claude.ai/download)
- Node.js 20+ (https://nodejs.org/)
- ANTHROPIC_API_KEY (your Claude API key from https://console.anthropic.com/)

**Optional (for production):**
- Docker and Docker Compose (for PostgreSQL, Redis, full production setup)

## Step 1: Clone and Install (3 minutes)

```bash
git clone https://github.com/shireen168/marketing-os.git
cd marketing-os
npm install
```

## Step 2: Configure Environment (1 minute)

```bash
cp .env.example .env.local
```

Edit `.env.local` and add your ANTHROPIC_API_KEY:
```
ANTHROPIC_API_KEY=sk-ant-...your-key-here...
NODE_ENV=development
PORT=3000
```

## Step 3: Start the API Server (1 minute)

**Option A: Simple (for Phase 1 testing)**

Run the Node.js API directly:

```bash
npm run build --workspace=@marketing-os/api
npm run --workspace=@marketing-os/api --silent -- node dist/index.js
```

The API will start on `http://localhost:3000` and respond with mock data.

**Option B: Full Production Setup (with Docker)**

If you want PostgreSQL and Redis (needed for production):

```bash
docker-compose up
```

Wait for all services to be healthy. You should see:
```
marketing-os-postgres: database system is ready to accept connections
marketing-os-redis: Ready to accept connections
marketing-os-api: listening on port 3000
```

Leave this terminal running. Open a new terminal for the next step.

## Step 4: Configure Claude Desktop (3 minutes)

Find your Claude Desktop config file:

**Mac:**
```
~/Library/Application Support/Claude/claude_desktop_config.json
```

**Windows:**
```
C:\Users\[YourUsername]\AppData\Local\Packages\Claude_pzs8sxrjxfjjc\LocalCache\Roaming\Claude\claude_desktop_config.json
```

**Linux:**
```
~/.config/Claude/claude_desktop_config.json
```

Open it in a text editor. Find the `mcpServers` section (or create it if it doesn't exist). Add this:

```json
{
  "mcpServers": {
    "marketing-os": {
      "command": "node",
      "args": [
        "/absolute/path/to/marketing-os/packages/mcp/dist/server.js"
      ],
      "env": {
        "API_URL": "http://localhost:3000"
      }
    }
  }
}
```

**Important:** Replace the path with your actual Marketing OS location:
- Mac example: `/Users/[YourUsername]/Desktop/marketing-os/packages/mcp/dist/server.js`
- Windows example: `C:/Users/[YourUsername]/Desktop/marketing-os/packages/mcp/dist/server.js`

Your config file should now look like this (full example):
```json
{
  "mcpServers": {
    "marketing-os": {
      "command": "node",
      "args": [
        "/Users/[YourUsername]/Desktop/marketing-os/packages/mcp/dist/server.js"
      ],
      "env": {
        "API_URL": "http://localhost:3000"
      }
    }
  }
}
```

## Step 5: Restart Claude Desktop (1 minute)

Close Claude Desktop completely. Open it again.

At the bottom of the window, you should see "marketing-os" with a green dot next to it, indicating it's connected.

## Step 6: Test the Connection (1 minute)

In Claude Desktop, type:

```
/listBriefs
```

You should see:
```json
{
  "briefs": []
}
```

If you get an error, see the Troubleshooting section below.

## Step 7: Create Your First Brief (2 minutes)

In Claude Desktop, type:

```
/brieftodraft

title: My First Campaign
description: Testing Marketing OS with my team
brandContext: Professional and trustworthy
targetAudience: Marketing managers
goal: Demonstrate the system
channels: email, linkedin
keyMessages: Saves time, Easy to use, Powerful AI
tone: Friendly and professional
cta: Learn more
```

Claude will submit this to Marketing OS and generate drafts for email and LinkedIn. You'll see something like:

```json
{
  "id": "brief-abc123",
  "title": "My First Campaign",
  "drafts": [
    {
      "id": "draft-email-1",
      "channel": "email",
      "content": "[Generated email draft...]"
    },
    {
      "id": "draft-linkedin-1",
      "channel": "linkedin",
      "content": "[Generated LinkedIn post...]"
    }
  ]
}
```

## Step 8: Publish Your Drafts (1 minute)

Once you see the drafts, ask Claude to publish them:

```
/publish

briefId: brief-abc123
draftIds: draft-email-1, draft-linkedin-1
channels: email, linkedin
```

Claude will publish your content. Note: Email goes to SendGrid, LinkedIn posts to LinkedIn. You'll need to configure those integrations for real sending (see Integration Setup below).

## Step 9: Check Analytics (1 minute)

After your campaign has run for a bit:

```
/report

campaignId: brief-abc123
days: 1
```

You'll see engagement metrics from each channel.

## That's It!

You now have a working Marketing OS instance. The workflow is:
1. Write a brief in Claude Desktop
2. Get optimized drafts for each channel
3. Edit/regenerate as needed
4. Publish with one command
5. Track performance

## Integration Setup (Optional, for real sending)

To actually send emails and post to LinkedIn, configure these integrations:

### SendGrid (Email)

1. Create a SendGrid account (https://sendgrid.com/)
2. Get your API key
3. Add to `.env.local`:
```
SENDGRID_API_KEY=SG.your-key-here
SENDGRID_FROM_EMAIL=noreply@yourcompany.com
```

### LinkedIn API (LinkedIn Posts)

1. Create a LinkedIn app (https://www.linkedin.com/developers/apps)
2. Get your access token
3. Add to `.env.local`:
```
LINKEDIN_ACCESS_TOKEN=your-token-here
LINKEDIN_COMPANY_ID=your-company-id
```

### Medium API (Medium Publishing)

1. Create a Medium account and get your access token
2. Add to `.env.local`:
```
MEDIUM_ACCESS_TOKEN=your-token-here
```

Restart the API server after adding credentials (kill and restart your API process).

## Troubleshooting

**MCP not connecting in Claude Desktop?**
1. Make sure the API server is running on port 3000 (see Step 3)
2. Verify the config file path is in the correct location (see Step 4 for OS-specific paths)
3. Check that the path in `claude_desktop_config.json` uses forward slashes and is absolute (e.g., `C:/Users/...` not `C:\Users\...`)
4. Make sure there are no typos in the JSON config file (use a JSON validator if unsure)
5. Close Claude Desktop completely and reopen it (don't just minimize)
6. Look for "marketing-os" in Settings → Connectors → Desktop section
7. Run the MCP server directly to see errors:
   ```bash
   node packages/mcp/dist/server.js
   ```

**Getting "Cannot POST /briefs" error?**
1. Make sure the API server is running on `http://localhost:3000`
2. Check the API logs for errors
3. Check that ANTHROPIC_API_KEY is set in `.env.local`
4. The API responds with mock data by default - no database needed

**Can't find claude_desktop_config.json?**
1. Make sure Claude Desktop is closed
2. Create the folder if it doesn't exist (especially on Windows)
3. Create the file in the location listed in Step 4
4. Make sure it's named exactly `claude_desktop_config.json`
5. On Windows, make sure it's not being saved as `.json.txt` (use a proper code editor)

**JSON config is invalid?**
Paste your config at https://jsonlint.com/ to check for syntax errors.

## Next Steps

1. Read `docs/MCP.md` for complete command reference
2. Read `docs/ARCHITECTURE.md` to understand the system design
3. Read `docs/API.md` for REST endpoint details
4. Set up integration credentials above for real sending
5. Run test campaigns with your team

## Need Help?

- Check `docs/MCP.md` for detailed command examples
- Check `docs/ARCHITECTURE.md` for system design overview
- See `docs/API.md` for complete API reference
- Open an issue on GitHub with error messages and steps to reproduce
