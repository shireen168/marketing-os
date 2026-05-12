import express, { Request, Response } from "express";
import { PrismaClient } from "@prisma/client";
import { generateDrafts } from "./claude";

const app = express();
const prisma = new PrismaClient();
const PORT = process.env.PORT || 3000;

app.use(express.json());

// Health check
app.get("/health", (req: Request, res: Response) => {
  res.json({ status: "ok", timestamp: new Date().toISOString() });
});

// POST /briefs - Create brief and generate drafts via Claude
app.post("/briefs", async (req: Request, res: Response) => {
  try {
    const { title, description, channels } = req.body;

    if (!title || !description) {
      res.status(400).json({ error: "title and description required" });
      return;
    }

    if (!Array.isArray(channels) || channels.length === 0) {
      res.status(400).json({ error: "channels must be a non-empty array" });
      return;
    }

    // Create brief in database
    const brief = await prisma.brief.create({
      data: {
        title,
        description,
        channels: JSON.stringify(channels),
        status: "drafts_generating",
      },
    });

    // Generate drafts via Claude
    let generatedDrafts;
    try {
      generatedDrafts = await generateDrafts(title, description, channels);
    } catch (error) {
      // Update brief status on error
      await prisma.brief.update({
        where: { id: brief.id },
        data: { status: "generation_failed" },
      });
      res.status(500).json({
        error: `Draft generation failed: ${error instanceof Error ? error.message : "Unknown error"}`,
      });
      return;
    }

    // Store generated drafts
    const drafts = await Promise.all(
      generatedDrafts.map((draft) =>
        prisma.draft.create({
          data: {
            briefId: brief.id,
            channel: draft.channel,
            content: draft.content,
            status: "pending_review",
          },
        })
      )
    );

    // Update brief status
    await prisma.brief.update({
      where: { id: brief.id },
      data: { status: "draft_generated" },
    });

    res.status(201).json({
      briefId: brief.id,
      title: brief.title,
      description: brief.description,
      status: "draft_generated",
      drafts: drafts,
      createdAt: brief.createdAt,
    });
  } catch (error) {
    console.error("Error in POST /briefs:", error);
    res.status(500).json({
      error: `Server error: ${error instanceof Error ? error.message : "Unknown error"}`,
    });
  }
});

// GET /briefs - List all briefs
app.get("/briefs", async (req: Request, res: Response) => {
  try {
    const limitQuery = req.query.limit;
    const offsetQuery = req.query.offset;
    const limit = typeof limitQuery === "string" ? parseInt(limitQuery) : 10;
    const offset = typeof offsetQuery === "string" ? parseInt(offsetQuery) : 0;

    const briefs = await prisma.brief.findMany({
      take: limit,
      skip: offset,
      orderBy: { createdAt: "desc" },
    });

    // Fetch draft counts separately
    const briefsWithDrafts = await Promise.all(
      briefs.map(async (b) => {
        const draftCount = await prisma.draft.count({
          where: { briefId: b.id },
        });
        return { ...b, draftCount };
      })
    );

    const total = await prisma.brief.count();

    res.json({
      briefs: briefsWithDrafts.map((b) => ({
        briefId: b.id,
        title: b.title,
        description: b.description,
        status: b.status,
        draftCount: b.draftCount,
        createdAt: b.createdAt,
      })),
      total,
      limit,
      offset,
    });
  } catch (error) {
    console.error("Error in GET /briefs:", error);
    res.status(500).json({
      error: "Failed to fetch briefs",
    });
  }
});

// GET /briefs/:id - Get brief with drafts
app.get("/briefs/:id", async (req: Request, res: Response) => {
  try {
    const { id } = req.params as { id: string };

    const brief = await prisma.brief.findUnique({
      where: { id },
      include: {
        drafts: true,
      },
    });

    if (!brief) {
      res.status(404).json({ error: "Brief not found" });
      return;
    }

    res.json({
      briefId: brief.id,
      title: brief.title,
      description: brief.description,
      channels: JSON.parse(brief.channels),
      status: brief.status,
      drafts: brief.drafts,
      createdAt: brief.createdAt,
      updatedAt: brief.updatedAt,
    });
  } catch (error) {
    console.error("Error in GET /briefs/:id:", error);
    res.status(500).json({ error: "Failed to fetch brief" });
  }
});

// POST /drafts/:id/approve - Approve draft
app.post("/drafts/:id/approve", async (req: Request, res: Response) => {
  try {
    const { id } = req.params as { id: string };

    const draft = await prisma.draft.update({
      where: { id },
      data: { status: "approved" },
      include: { brief: true },
    });

    res.json({
      draftId: draft.id,
      channel: draft.channel,
      status: "approved",
      content: draft.content,
    });
  } catch (error) {
    console.error("Error in POST /drafts/:id/approve:", error);
    res.status(500).json({ error: "Failed to approve draft" });
  }
});

// POST /campaigns - Create campaign from approved drafts
app.post("/campaigns", async (req: Request, res: Response) => {
  try {
    const { briefId, draftIds } = req.body;

    if (
      !briefId ||
      typeof briefId !== "string" ||
      !Array.isArray(draftIds) ||
      draftIds.length === 0
    ) {
      res.status(400).json({
        error: "briefId (string) and draftIds (non-empty array) required",
      });
      return;
    }

    const campaign = await prisma.campaign.create({
      data: {
        briefId: briefId as string,
        status: "published",
        publishedAt: new Date(),
      },
    });

    // Mark drafts as published
    await prisma.draft.updateMany({
      where: {
        id: { in: draftIds },
      },
      data: { status: "published" },
    });

    res.status(201).json({
      campaignId: campaign.id,
      briefId: campaign.briefId,
      status: "published",
      publishedDraftCount: draftIds.length,
      publishedAt: campaign.publishedAt,
      message: `Published ${draftIds.length} drafts`,
    });
  } catch (error) {
    console.error("Error in POST /campaigns:", error);
    res.status(500).json({ error: "Failed to create campaign" });
  }
});

// GET /campaigns/:id/analytics - Get campaign analytics
app.get("/campaigns/:id/analytics", async (req: Request, res: Response) => {
  try {
    const { id } = req.params as { id: string };
    const daysQuery = req.query.days;
    const days = typeof daysQuery === "string" ? parseInt(daysQuery) : 7;

    const campaign = await prisma.campaign.findUnique({
      where: { id },
      include: { brief: true },
    });

    if (!campaign) {
      res.status(404).json({ error: "Campaign not found" });
      return;
    }

    // Return realistic mock analytics (in production, would fetch real data)
    res.json({
      campaignId: campaign.id,
      briefId: campaign.briefId,
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
      publishedAt: campaign.publishedAt,
    });
  } catch (error) {
    console.error("Error in GET /campaigns/:id/analytics:", error);
    res.status(500).json({ error: "Failed to fetch analytics" });
  }
});

// Start server
app.listen(PORT, () => {
  console.log(`Marketing OS API running on http://localhost:${PORT}`);
  console.log(`Health check: http://localhost:${PORT}/health`);
  console.log(`API ready for MCP integration`);
});

// Graceful shutdown
process.on("SIGINT", async () => {
  await prisma.$disconnect();
  process.exit(0);
});
