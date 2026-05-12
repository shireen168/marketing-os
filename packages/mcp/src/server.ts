import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { CallToolRequestSchema, ListToolsRequestSchema } from "@modelcontextprotocol/sdk/types.js";
import axios from "axios";
import * as dotenv from "dotenv";

dotenv.config();

const API_BASE_URL = process.env.API_URL || "http://localhost:3000";
const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

const server = new Server(
  {
    name: "marketing-os",
    version: "0.1.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

// List available tools
server.setRequestHandler(ListToolsRequestSchema, async () => {
  return {
    tools: [
      {
        name: "brieftodraft",
        description:
          "Submit a brief and generate optimized drafts for multiple channels",
        inputSchema: {
          type: "object" as const,
          properties: {
            title: { type: "string", description: "Campaign title" },
            description: { type: "string", description: "Campaign description" },
            brandContext: { type: "string", description: "Brand tone and values" },
            targetAudience: { type: "string", description: "Who this campaign targets" },
            goal: { type: "string", description: "Campaign objective" },
            channels: {
              type: "array",
              items: { type: "string" },
              description: 'Channels to generate drafts for: "email", "linkedin", "medium"',
            },
            keyMessages: { type: "array", items: { type: "string" }, description: "Key messages to include" },
            tone: { type: "string", description: "Tone of voice" },
            cta: { type: "string", description: "Call to action" },
            feedback: { type: "string", description: "Optional: feedback for regeneration" },
          },
          required: ["title", "description", "targetAudience", "goal", "channels", "keyMessages"],
        },
      },
      {
        name: "publish",
        description: "Publish generated drafts to specified channels",
        inputSchema: {
          type: "object" as const,
          properties: {
            briefId: { type: "string", description: "ID of the brief" },
            draftIds: { type: "array", items: { type: "string" }, description: "IDs of drafts to publish" },
            channels: {
              type: "array",
              items: { type: "string" },
              description: 'Channels to publish to: "email", "linkedin", "medium"',
            },
          },
          required: ["briefId", "draftIds", "channels"],
        },
      },
      {
        name: "report",
        description: "Get analytics for a published campaign",
        inputSchema: {
          type: "object" as const,
          properties: {
            campaignId: { type: "string", description: "Campaign ID" },
            days: { type: "number", description: "Number of days to report on (default: 7)" },
          },
          required: ["campaignId"],
        },
      },
      {
        name: "listBriefs",
        description: "List all briefs you have created",
        inputSchema: {
          type: "object" as const,
          properties: {
            limit: { type: "number", description: "Number of briefs to return (default: 10)" },
          },
        },
      },
    ],
  };
});

// Handle tool calls
server.setRequestHandler(CallToolRequestSchema, async (request: any) => {
  try {
    const { name, arguments: args } = request.params;

    if (name === "brieftodraft") {
      const response = await api.post("/briefs", args);
      return { content: [{ type: "text", text: JSON.stringify(response.data, null, 2) }] };
    }

    if (name === "publish") {
      // First approve the drafts, then create campaign
      const response = await api.post("/campaigns", {
        briefId: args.briefId,
        draftIds: args.draftIds,
      });
      return { content: [{ type: "text", text: JSON.stringify(response.data, null, 2) }] };
    }

    if (name === "report") {
      const response = await api.get(`/campaigns/${args.campaignId}/analytics`, {
        params: { days: args.days || 7 },
      });
      return { content: [{ type: "text", text: JSON.stringify(response.data, null, 2) }] };
    }

    if (name === "listBriefs") {
      const response = await api.get("/briefs", { params: { limit: args.limit || 10 } });
      return { content: [{ type: "text", text: JSON.stringify(response.data, null, 2) }] };
    }

    return { content: [{ type: "text", text: `Unknown tool: ${name}` }] };
  } catch (error: any) {
    return { content: [{ type: "text", text: `Error: ${error.message}` }] };
  }
});

async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error("Marketing OS MCP server running on stdio");
}

main().catch(console.error);
