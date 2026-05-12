# Development Guide

Complete guide for developers working on Marketing OS.

## Project Structure

```
packages/api/        REST API backend (Express/Fastify)
packages/mcp/        Claude Desktop MCP server
packages/cli/        CLI tools (future)
packages/web/        Web UI (future)
docs/               Documentation
.github/workflows/   CI/CD pipelines
```

## Setup for Development

### 1. Clone and Install

```bash
git clone https://github.com/shireen168/marketing-os.git
cd marketing-os
npm install
```

This installs dependencies for all packages (monorepo with Turbo).

### 2. Environment Setup

```bash
cp .env.example .env.local
```

Add your ANTHROPIC_API_KEY and other credentials.

### 3. Start Services

```bash
# Terminal 1: Start backend services (PostgreSQL, Redis, API)
docker-compose up

# Terminal 2: Watch for code changes
npm run dev

# Terminal 3 (optional): Start MCP server for testing in Claude Desktop
cd packages/mcp
npm run dev
```

## Development Workflow

### Making Changes to API

1. Edit code in `packages/api/src/`
2. TypeScript compilation is automatic with `npm run dev`
3. API hot-reloads on file changes
4. Test endpoints in Claude Desktop or via curl

### Making Changes to MCP Server

1. Edit code in `packages/mcp/src/server.ts`
2. Run `npm run dev` in the mcp folder
3. Restart Claude Desktop to reconnect to the MCP server
4. Test slash commands in Claude Desktop

### Running Tests

```bash
# Run all tests
npm test

# Run tests in watch mode
npm run test:watch

# Test specific package
npm test -- packages/api
npm test -- packages/mcp
```

### Type Checking

```bash
# Check all packages
npm run type-check

# Check specific package
npm run type-check -- packages/api
```

### Linting

```bash
# Lint all packages
npm run lint

# Format code (if prettier is set up)
npm run format
```

### Building

```bash
# Build all packages
npm run build

# Build specific package
npm run build -- packages/api
```

## Adding New Tools to MCP

To add a new slash command (tool) to Marketing OS:

1. Add the tool definition in `packages/mcp/src/server.ts` under the `ListToolsRequest` handler:

```typescript
{
  name: "newcommand",
  description: "What this command does",
  inputSchema: {
    type: "object",
    properties: {
      param1: {
        type: "string",
        description: "Description of param1"
      }
    },
    required: ["param1"]
  }
}
```

2. Add the handler in the `CallToolRequest` handler:

```typescript
if (name === "newcommand") {
  const response = await api.post("/endpoint", args);
  return {
    content: [{
      type: "text",
      text: JSON.stringify(response.data, null, 2)
    }]
  };
}
```

3. The new command will automatically be available in Claude Desktop.

## Adding New API Endpoints

1. Create a new route in `packages/api/src/routes/`
2. Add TypeScript types in `packages/api/src/types/`
3. Implement business logic in `packages/api/src/services/`
4. Add tests in `packages/api/src/__tests__/`
5. Document in `docs/API.md`

## Git Workflow

```bash
# Create feature branch
git checkout -b feature/your-feature-name

# Make changes and commit
git add .
git commit -m "feat: add your feature"

# Push and create PR
git push origin feature/your-feature-name
```

## Commit Message Convention

Use semantic commit messages:
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation
- `refactor:` Code refactoring
- `test:` Tests
- `chore:` Build, dependencies

Example: `feat: add brief regeneration endpoint`

## CI/CD

GitHub Actions automatically:
- Runs type checks on push/PR
- Runs linter on push/PR
- Runs tests on push/PR
- Builds all packages on push/PR
- Publishes to npm and creates releases on version tags

### Triggering a Release

1. Create a version tag: `git tag v0.2.0`
2. Push the tag: `git push origin v0.2.0`
3. GitHub Actions will automatically publish to npm and create a GitHub release

## Debugging

### Debug API Locally

Set `DEBUG=*` before running:

```bash
DEBUG=* npm run dev
```

### Debug MCP Server

Run the MCP server directly to see console output:

```bash
cd packages/mcp
npm run dev
```

You'll see all calls to the API and any errors.

### Database Debugging

Connect to PostgreSQL directly:

```bash
psql -h localhost -U marketing -d marketing_os
```

Common queries:
```sql
SELECT * FROM briefs;
SELECT * FROM drafts;
SELECT * FROM publications;
```

### Check API Health

```bash
curl http://localhost:3000/health
```

## Performance Considerations

- Database queries should use indexes (created in migrations)
- Cache frequently accessed data in Redis
- Use pagination for large result sets (see api.md)
- Batch requests from MCP server where possible

## Security Notes

- Never commit `.env.local` or credentials
- Store API keys as environment variables
- Use HTTPS in production
- Validate all user inputs at API boundaries
- Sanitize database queries (use parameterized queries)

## Common Issues

**API not starting?**
- Check that PostgreSQL is running: `docker-compose ps`
- Check that ANTHROPIC_API_KEY is set
- Check port 3000 is available

**MCP not connecting in Claude Desktop?**
- Make sure MCP server is running: `npm run dev` in packages/mcp
- Check the path in claude_desktop_config.json is correct
- Restart Claude Desktop

**Database migrations failing?**
- Check that PostgreSQL is running and accessible
- Check DATABASE_URL in .env.local
- Drop and recreate the database if needed

## Documentation

- `docs/ARCHITECTURE.md` - System architecture and design
- `docs/API.md` - REST API specification
- `docs/MCP.md` - Claude Desktop integration
- `docs/QUICKSTART.md` - Setup for non-developers
- `docs/SETUP.md` - Detailed setup instructions

## Code Style

- Use TypeScript for type safety
- Use descriptive variable and function names
- Add comments for complex logic
- Keep functions small and focused
- Use async/await instead of callbacks

## Testing Strategy

- Unit tests for business logic
- Integration tests for API endpoints
- End-to-end tests for complete workflows
- Test coverage target: 80%+

## Performance Profiling

To profile API performance:

```bash
# Using Node's built-in profiler
node --prof packages/api/dist/index.js
```

## Staying Updated

- Read release notes when pulling main
- Check GitHub issues for known issues
- Check GitHub discussions for architecture decisions
- Keep dependencies updated: `npm update`

## Need Help?

- Check existing issues on GitHub
- Ask in GitHub discussions
- Review similar code in the codebase
- Consult the documentation files
