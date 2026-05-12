# API Endpoints

Base URL: `http://localhost:3000/api/v1`

## Authentication

All endpoints require `X-API-Key` header or Bearer token (TBD).

```
X-API-Key: your-api-key-here
```

## Briefs

### POST /briefs

Submit a new marketing brief.

Request:
```json
{
  "title": "Q2 Product Launch",
  "description": "Launch announcement for new product",
  "brand_context": "B2B SaaS, professional tone",
  "target_audience": "CTOs and engineering leads",
  "channels": ["email", "linkedin", "blog"],
  "tone": "professional",
  "additional_context": "Include ROI metrics"
}
```

Response:
```json
{
  "id": "brief-001",
  "status": "submitted",
  "created_at": "2026-05-12T00:00:00Z"
}
```

### GET /briefs/:id

Retrieve a brief.

Response:
```json
{
  "id": "brief-001",
  "title": "Q2 Product Launch",
  "description": "...",
  "status": "processing",
  "created_at": "2026-05-12T00:00:00Z",
  "updated_at": "2026-05-12T00:05:00Z"
}
```

### GET /briefs

List all briefs with pagination.

Query params:
- `limit`: number of results (default: 10)
- `offset`: pagination offset (default: 0)
- `status`: filter by status (submitted, processing, completed)

## Drafts

### GET /briefs/:id/drafts

Retrieve all drafts for a brief.

Response:
```json
{
  "brief_id": "brief-001",
  "drafts": [
    {
      "id": "draft-001",
      "channel": "email",
      "content": "Subject: Q2 Launch...",
      "status": "pending_review",
      "version": 1,
      "generated_at": "2026-05-12T00:02:00Z"
    }
  ]
}
```

### GET /drafts/:id

Retrieve a specific draft.

Response:
```json
{
  "id": "draft-001",
  "brief_id": "brief-001",
  "channel": "email",
  "content": "...",
  "status": "pending_review",
  "version": 1,
  "generated_at": "2026-05-12T00:02:00Z"
}
```

### PUT /drafts/:id

Update a draft (e.g., after review and edit).

Request:
```json
{
  "content": "Updated content...",
  "status": "approved"
}
```

### POST /drafts/:id/regenerate

Regenerate a draft with adjusted prompt.

Request:
```json
{
  "feedback": "Make this more casual",
  "tone_adjustment": "friendly"
}
```

## Publishing

### POST /drafts/:id/publish

Publish a draft to a channel.

Request:
```json
{
  "channel": "email",
  "send_to": "marketing-list-001",
  "schedule_time": "2026-05-15T09:00:00Z"
}
```

Response:
```json
{
  "id": "publish-001",
  "draft_id": "draft-001",
  "channel": "email",
  "status": "scheduled",
  "scheduled_at": "2026-05-15T09:00:00Z"
}
```

### GET /publications

List all published content.

Query params:
- `channel`: filter by channel
- `status`: draft, scheduled, published, failed

## Analytics

### GET /campaigns/:id/analytics

Retrieve analytics for a campaign.

Response:
```json
{
  "campaign_id": "campaign-001",
  "period": "7 days",
  "metrics": {
    "email": {
      "sent": 1200,
      "opened": 360,
      "clicked": 120,
      "open_rate": "30%",
      "ctr": "10%"
    },
    "linkedin": {
      "impressions": 5000,
      "engagements": 250,
      "engagement_rate": "5%"
    }
  },
  "generated_at": "2026-05-12T00:00:00Z"
}
```

## Error Responses

All error responses follow this format:

```json
{
  "error": {
    "code": "INVALID_BRIEF",
    "message": "Brief missing required field: description",
    "details": {
      "field": "description",
      "reason": "required"
    }
  }
}
```

Common error codes:
- `INVALID_BRIEF`: Brief validation failed
- `BRIEF_NOT_FOUND`: Brief does not exist
- `API_KEY_INVALID`: API key is invalid or missing
- `RATE_LIMIT_EXCEEDED`: Too many requests
- `GENERATION_FAILED`: Claude API failed to generate draft
- `PUBLISH_FAILED`: Publishing to channel failed
