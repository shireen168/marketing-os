# Setup Instructions

## Quick Start (Phase 1 - Testing)

For testing Marketing OS with mock data:

### 1. Clone and Install

```bash
git clone https://github.com/shireen168/marketing-os.git
cd marketing-os
npm install
```

### 2. Build and Start API

```bash
npm run build --workspace=@marketing-os/api
npm run build --workspace=@marketing-os/mcp
npm run --workspace=@marketing-os/api --silent -- node dist/index.js
```

The API will start on `http://localhost:3000` with mock data. No database needed.

### 3. Configure Claude Desktop

See [MCP.md](MCP.md) for full setup.

---

## Production Setup (Phase 2+)

For production use with real database and services.

### Prerequisites

- Node.js 20+ (https://nodejs.org/)
- PostgreSQL 14+ (https://www.postgresql.org/) OR Docker
- Redis 6+ (https://redis.io/) OR Docker
- ANTHROPIC_API_KEY from https://console.anthropic.com/

### Option A: Docker Setup (Recommended)

```bash
git clone https://github.com/shireen168/marketing-os.git
cd marketing-os
npm install
cp .env.example .env.local
# Edit .env.local and add ANTHROPIC_API_KEY
docker-compose up
```

### Option B: Manual Service Setup

#### 1. Clone and Install

```bash
git clone https://github.com/shireen168/marketing-os.git
cd marketing-os
npm install
```

#### 2. Environment Variables

Copy `.env.example` to `.env.local`:

```bash
cp .env.example .env.local
```

Update values with your own API keys:

```
ANTHROPIC_API_KEY=your-key-here
DATABASE_URL=postgresql://user:password@localhost:5432/marketing_os
REDIS_URL=redis://localhost:6379
NODE_ENV=production
```

#### 3. Database Setup

```bash
# Create database
createdb marketing_os

# Run migrations (when available)
npm run migrate
```

#### 4. Run Services

Start PostgreSQL and Redis:

```bash
# PostgreSQL
pg_ctl -D /usr/local/var/postgres start

# Redis
redis-server
```

#### 5. Development Mode

From the root directory:

```bash
# Run all packages in dev mode (watch for changes)
npm run dev

# Or run specific packages
cd packages/api && npm run dev
cd packages/cli && npm run dev
```

## Docker Setup

Build and run with Docker Compose:

```bash
docker-compose up
```

This starts:
- API backend on port 3000
- PostgreSQL on port 5432
- Redis on port 6379

## Claude Desktop MCP Setup

To use Marketing OS through Claude Desktop:

1. Start the backend: `docker-compose up`

2. In another terminal, install MCP dependencies:
```bash
cd packages/mcp
npm install
npm run build
```

3. Configure Claude Desktop (see `docs/MCP.md` for detailed instructions)

4. Restart Claude Desktop and test:
```
/listBriefs
```

Once set up, all commands work directly in Claude Desktop via slash commands.
For full MCP documentation, see `docs/MCP.md`.

## Testing

```bash
# Run all tests
npm test

# Run tests in watch mode
npm run test:watch

# Run specific package tests
npm test -- packages/api
```

## Building

```bash
# Build all packages
npm run build

# Build specific package
npm run build -- packages/api
```

## CLI Usage

After installation:

```bash
brief2draft --input brief.json --output drafts/
publish --drafts drafts/ --channels email,linkedin
report --campaign q2-launch --days 7
```

## Troubleshooting

### Database Connection Failed
- Ensure PostgreSQL is running
- Check DATABASE_URL in .env.local
- Run: `psql -U postgres -h localhost`

### Redis Connection Failed
- Ensure Redis is running
- Check REDIS_URL in .env.local
- Run: `redis-cli ping` (should return PONG)

### API Key Invalid
- Verify ANTHROPIC_API_KEY is set correctly
- Check key has sufficient credits
- Test: `curl -H "Authorization: Bearer $ANTHROPIC_API_KEY" https://api.anthropic.com/v1/models`

## Git Workflow

```bash
# Create feature branch
git checkout -b feature/brief-validation

# Make changes and commit
git add .
git commit -m "add brief validation schema"

# Push and create PR
git push origin feature/brief-validation
```

## Next Steps

- Read ARCHITECTURE.md for system design
- Read API.md for endpoint documentation
- Review example briefs in docs/
- Check GitHub Actions workflows for CI/CD setup
