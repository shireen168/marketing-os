# Architecture

## Core Pipeline

Marketing OS is built on a reusable pipeline that accepts input, processes via Claude AI, versions outputs, and integrates with external publishing platforms.

```
Input (Brief) -> Validation -> Claude API -> Draft Generation -> Versioning -> Publishing -> Analytics
```

## System Components

### 1. API Backend (packages/api)

REST API that handles:
- Brief submission and validation
- Draft generation via Claude
- Version control for drafts
- Publishing orchestration
- Performance tracking

Key endpoints:
- `POST /api/v1/briefs` - Submit a marketing brief
- `GET /api/v1/briefs/:id/drafts` - Retrieve generated drafts
- `POST /api/v1/drafts/:id/publish` - Publish draft to channels
- `GET /api/v1/campaigns/:id/analytics` - Retrieve campaign metrics

Database:
- PostgreSQL: briefs, drafts, versions, audit logs
- Redis: job queue, caching

### 2. CLI Tools (packages/cli)

Command-line interface for team members and integrations.

Commands:
- `brief2draft` - Generate drafts from a brief file
- `publish` - Publish drafts to specified channels
- `report` - Generate campaign performance reports
- `config` - Manage API keys and integrations

### 3. Web UI (packages/web, Phase 2)

Next.js application for marketing managers.

Features (Phase 2):
- Brief editor with brand context
- Draft review and editing
- Publishing workflow
- Analytics dashboard

## Data Model

### Brief

```json
{
  "id": "brief-001",
  "title": "Q2 Product Launch",
  "description": "...",
  "brand_context": "...",
  "target_audience": "...",
  "channels": ["email", "linkedin", "blog"],
  "tone": "professional",
  "created_at": "2026-05-12T00:00:00Z",
  "updated_at": "2026-05-12T00:00:00Z"
}
```

### Draft

```json
{
  "id": "draft-001",
  "brief_id": "brief-001",
  "channel": "email",
  "content": "...",
  "status": "pending_review",
  "version": 1,
  "generated_at": "2026-05-12T00:00:00Z"
}
```

## Integration Points

### Phase 1 Integrations

- HubSpot: CRM data, field mapping
- SendGrid: Email preview, sending
- LinkedIn API: Company page publishing
- Medium: Blog publishing
- Google Analytics: Performance tracking

### Phase 2 Integrations

- Slack: Notifications
- Webhooks: Custom integrations
- More platforms based on feedback

## Deployment

### Phase 1

- Docker containers for API and CLI
- GitHub Actions for CI/CD
- Railway or Vercel for backend hosting
- NPM registry for CLI distribution

### Phase 2

- Managed SaaS environment
- Scaling considerations
- Database scaling strategy

## Extension Points

For future divisions (Sales, Ops, HR, Training):

- Core pipeline is division-agnostic
- Input handler accepts custom brief schemas
- Output formatting plugs in per-division
- Integration layer accepts new platforms
- CLI commands extend via plugin system

Example: Sales division would use same pipeline but with:
- Different brief schema (proposal, RFP response, etc.)
- Different output formats (slides, documents)
- Different integrations (Salesforce, Docusign, etc.)
