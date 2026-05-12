# Marketing OS Setup Guide

Complete setup: **10 minutes**

## Prerequisites

- Node.js 20+
- Claude API key (free trial available at https://console.anthropic.com/)
- Git

## Step 1: Clone and Install

```bash
git clone https://github.com/shireen168/marketing-os.git
cd marketing-os
npm install
```

## Step 2: Configure API Key

Set your Claude API key:

**Option A: Environment Variable (Quick)**
```bash
export ANTHROPIC_API_KEY="sk-ant-..."
```

**Option B: .env.local File (Persistent)**

In `packages/api/`, create `.env.local`:
```
DATABASE_URL="file:./dev.db"
ANTHROPIC_API_KEY=sk-ant-...
```

## Step 3: Initialize Database

```bash
cd packages/api
npm run build
export DATABASE_URL="file:./dev.db"
npx prisma migrate deploy
```

## Step 4: Start the API

```bash
npm run dev
```

Output:
```
Marketing OS API running on http://localhost:3000
Health check: http://localhost:3000/health
API ready for MCP integration
```

## Step 5: Test the API

**Create a brief:**
```bash
curl -X POST http://localhost:3000/briefs \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Q2 Launch Campaign",
    "description": "Announce our new AI analytics feature for engineering teams",
    "channels": ["email", "linkedin", "medium"]
  }'
```

Response:
```json
{
  "briefId": "cmp2k9l870000nv4qmi7flkvk",
  "title": "Q2 Launch Campaign",
  "status": "draft_generated",
  "drafts": [
    {
      "draftId": "...",
      "channel": "email",
      "content": "Generated email draft...",
      "status": "pending_review"
    },
    ...
  ]
}
```

**List briefs:**
```bash
curl http://localhost:3000/briefs
```

**Get brief with drafts:**
```bash
curl http://localhost:3000/briefs/{briefId}
```

## Step 6: Connect Claude Desktop (Optional)

See `docs/mcp.md` for configuring the MCP server in Claude Desktop.

Once configured, test in Claude:
```
/listBriefs
/brieftodraft
/publish --channels email,linkedin
```

## Troubleshooting

**"ANTHROPIC_API_KEY not set"**
- Set your API key via environment variable or .env.local
- Verify the key is valid at https://console.anthropic.com/

**"Unable to open the database file"**
- Run migrations: `npx prisma migrate deploy`
- Verify DATABASE_URL is set correctly

**"Cannot find module @anthropic-ai/sdk"**
- Run `npm install` from the project root
- Ensure you're in the correct directory

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Health check |
| POST | `/briefs` | Create brief, generate drafts |
| GET | `/briefs` | List all briefs |
| GET | `/briefs/:id` | Get brief with drafts |
| POST | `/drafts/:id/approve` | Approve draft for publishing |
| POST | `/campaigns` | Create campaign from drafts |
| GET | `/campaigns/:id/analytics` | Get campaign analytics |

## Architecture

- **API**: Express.js on Node.js 20
- **Database**: SQLite (local dev), PostgreSQL-ready (Prisma)
- **AI**: Anthropic Claude API for draft generation
- **Integration**: MCP server for Claude Desktop

## Database Schema

```
Brief
├── id (string, unique)
├── title
├── description
├── channels (JSON array: ["email", "linkedin", "medium"])
├── status (draft, draft_generated, generation_failed, etc)
├── createdAt

Draft
├── id (string, unique)
├── briefId (references Brief)
├── channel (email, linkedin, medium)
├── content (generated text)
├── status (pending_review, approved, published)

Campaign
├── id (string, unique)
├── briefId (references Brief)
├── status (draft, published)
├── publishedAt
```

## What This Demonstrates

This is a working system built to show:

1. **Full-stack capability**: Database design, API development, AI integration
2. **Business understanding**: The workflow solves a real problem (marketing brief → optimized channel content → publish)
3. **Production thinking**: Type-safe TypeScript, error handling, proper database schema, migrations
4. **Shipping mentality**: Works end-to-end in 3 days, fast to understand, easy to extend

## Next Steps

- **For hiring manager review**: Code is in `packages/api/src/`, database schema in `packages/api/prisma/schema.prisma`
- **For running locally**: Follow Steps 1-5 above
- **For extending**: Add new channels in the prompt, new integrations in the API, etc.
- **For production**: Replace SQLite with PostgreSQL, add monitoring, scale the API

## Questions?

This is a portfolio project demonstrating core capabilities. The focus is on:
- Does it work? Yes.
- Is the code clean? Yes.
- Does it solve a real problem? Yes.

That's the signal: shipping ability, code quality, and business sense.
