import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env.ANTHROPIC_API_KEY,
});

interface DraftContent {
  channel: string;
  content: string;
}

export async function generateDrafts(
  title: string,
  description: string,
  channels: string[]
): Promise<DraftContent[]> {
  if (!process.env.ANTHROPIC_API_KEY) {
    throw new Error("ANTHROPIC_API_KEY not set");
  }

  if (channels.length === 0) {
    throw new Error("At least one channel required");
  }

  const channelInstructions = channels
    .map((ch) => {
      switch (ch) {
        case "email":
          return "- Email: compelling subject line + body optimized for opens and clicks";
        case "linkedin":
          return "- LinkedIn: professional post optimized for engagement and reach";
        case "medium":
          return "- Medium: article-style post optimized for SEO and reading time";
        default:
          return `- ${ch}: suitable content for this channel`;
      }
    })
    .join("\n");

  const prompt = `You are a marketing expert creating campaign content.

Campaign Brief:
Title: ${title}
Description: ${description}

Generate content for these channels:
${channelInstructions}

Format your response as JSON with this structure:
{
  "drafts": [
    {
      "channel": "email",
      "content": "..."
    },
    {
      "channel": "linkedin",
      "content": "..."
    },
    {
      "channel": "medium",
      "content": "..."
    }
  ]
}

Only include the channels requested. Make each draft distinct and optimized for that channel's audience.`;

  try {
    const message = await client.messages.create({
      model: "claude-3-5-sonnet-20241022",
      max_tokens: 2048,
      messages: [
        {
          role: "user",
          content: prompt,
        },
      ],
    });

    // Extract text content from the response
    const responseText = message.content
      .filter((block) => block.type === "text")
      .map((block) => (block.type === "text" ? block.text : ""))
      .join("");

    // Parse JSON from response
    const jsonMatch = responseText.match(/\{[\s\S]*\}/);
    if (!jsonMatch) {
      throw new Error("Could not parse JSON from Claude response");
    }

    const parsed = JSON.parse(jsonMatch[0]);
    return parsed.drafts || [];
  } catch (error) {
    console.error("Error generating drafts:", error);
    throw new Error(
      `Failed to generate drafts: ${error instanceof Error ? error.message : "Unknown error"}`
    );
  }
}
