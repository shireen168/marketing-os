import express from "express";

const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());

// Mock: Create a brief and generate drafts
app.post("/briefs", (req, res) => {
  const { title, description, channels } = req.body;
  res.json({
    briefId: `brief-${Date.now()}`,
    title,
    description,
    status: "draft_generated",
    drafts: channels.map((channel: string) => ({
      draftId: `draft-${Date.now()}-${channel}`,
      channel,
      content: `Generated ${channel} draft for "${title}"`,
      status: "pending_review",
    })),
    createdAt: new Date().toISOString(),
  });
});

// Mock: Publish drafts to channels
app.post("/drafts/publish", (req, res) => {
  const { briefId, draftIds, channels } = req.body;
  res.json({
    campaignId: `campaign-${Date.now()}`,
    briefId,
    publishedDrafts: draftIds.map((id: string) => ({
      draftId: id,
      status: "published",
      publishedAt: new Date().toISOString(),
    })),
    channels,
    message: `Published ${draftIds.length} drafts to ${channels.join(", ")}`,
  });
});

// Mock: Get campaign analytics
app.get("/campaigns/:campaignId/analytics", (req, res) => {
  const { campaignId } = req.params;
  const { days = 7 } = req.query;
  res.json({
    campaignId,
    period: `Last ${days} days`,
    metrics: {
      email: {
        sent: 1500,
        opens: 450,
        clicks: 120,
        conversions: 24,
      },
      linkedin: {
        impressions: 5200,
        engagements: 340,
        clicks: 89,
      },
      medium: {
        views: 2100,
        reads: 1240,
        claps: 340,
      },
    },
    summary: {
      totalReach: 8800,
      totalEngagement: 789,
      conversionRate: 3.04,
    },
  });
});

// Mock: List briefs
app.get("/briefs", (req, res) => {
  const { limit = 10 } = req.query;
  res.json({
    briefs: [
      {
        briefId: "brief-example-1",
        title: "Q2 Product Launch",
        description: "Announce AI analytics feature",
        createdAt: new Date(Date.now() - 86400000).toISOString(),
        status: "published",
      },
    ],
    total: 1,
    limit,
  });
});

// Health check
app.get("/health", (req, res) => {
  res.json({ status: "ok", timestamp: new Date().toISOString() });
});

app.listen(PORT, () => {
  console.log(`Marketing OS API running on http://localhost:${PORT}`);
  console.log(`Health check: http://localhost:${PORT}/health`);
});
