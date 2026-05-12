# Marketing OS MCP Server

Claude Desktop integration for Marketing OS via Model Context Protocol.

## What This Does

This package implements an MCP server that bridges Claude Desktop and the Marketing OS API. Once configured, marketing teams can interact with Marketing OS directly in Claude Desktop using slash commands.

## How It Works

1. MCP server runs locally (started via `npm run mcp-server`)
2. Claude Desktop connects to it (configured in `claude_desktop_config.json`)
3. Users type slash commands in Claude Desktop (e.g., `/brieftodraft`)
4. Commands are translated to API calls to the Marketing OS backend
5. Results are returned to Claude Desktop

## Setup

See the main README and `docs/MCP.md` for configuration instructions.

## Available Commands

- `/brieftodraft` - Generate drafts from a brief
- `/publish` - Publish drafts to channels
- `/report` - Get campaign analytics
- `/listBriefs` - List all briefs

## Development

```bash
npm install
npm run dev      # Watch mode with tsx
npm run build    # TypeScript compilation
npm run start    # Run compiled version
```

## Architecture

- `src/server.ts` - Main MCP server implementation
- `tools/` - Individual tool definitions (for future expansion)
- `dist/` - Compiled JavaScript output

The server uses the MCP SDK to define tools that Claude Desktop can call. Each tool maps to a corresponding Marketing OS API endpoint.

## Dependencies

- `@modelcontextprotocol/sdk` - MCP protocol implementation
- `axios` - HTTP client for API calls
- `typescript` - Type safety

## See Also

- `docs/MCP.md` - Complete MCP integration guide
- `docs/API.md` - Marketing OS REST API reference
- `packages/api` - The backend API this server connects to
