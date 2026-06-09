# Orchestration System

Automated workflow orchestration for the 8-phase product launch framework. Orchestrates 75+ existing skills while maintaining human-in-the-loop approval gates.

## Overview

The orchestration system automates product launches through 8 phases:

1. **Research** — Market research, competitive analysis, audience validation
2. **Strategy** — Market positioning, launch strategy, timeline
3. **Design** — Product design and architecture
4. **Build** — Development and implementation
5. **Testing** — QA, validation, and optimization
6. **Launch** — Execution and go-live
7. **Growth** — Growth loops and scaling
8. **Operations** — Monitoring, learning, and iteration

**Phase 1:** Research validation using Tavily API with Perplexity fallback. ✅ Complete

**Phase 2:** Strategy development (/product-marketing, /pricing, /sales-enablement). ✅ Complete

**Phases 3-8:** Complete (design, build, testing, launch, growth, operations)

## Quick Start

### Installation

```bash
cd orchestration
pip install -r requirements.txt
```

### Configuration

Set environment variables:

```bash
export ANTHROPIC_API_KEY="your-key-here"
export TAVILY_API_KEY="your-key-here"
export PERPLEXITY_API_KEY="your-key-here"  # Optional fallback
export DEBUG="false"
```

Or use `.env` file:

```
ANTHROPIC_API_KEY=your-key-here
TAVILY_API_KEY=your-key-here
PERPLEXITY_API_KEY=your-key-here
DEBUG=false
```

### Configuration Constants

All configuration is centralized in `orchestration/core/config.py`:

- **API Keys:** Environment variables with fallback
- **Models:**
  - `MODEL_RESEARCH`: Opus 4.7 (Phases 1-3, complex reasoning)
  - `MODEL_EXECUTION`: Sonnet 4.6 (Phases 4-8, execution)
- **Timeouts:** API (60s), Research (300s), Tavily (30s), Perplexity (45s)
- **Checkpoints:** Format `ddmmyy-hhmm-short-descriptive-name.md`
- **Confidence Threshold:** 0.75 (75% minimum for research validation)

## Checkpoint Naming

Checkpoints follow a strict naming format for tracking progress:

```
ddmmyy-hhmm-short-descriptive-name.md
```

Examples:
- `060626-1645-research-phase-validation.md`
- `060626-1730-market-analysis-complete.md`

**Helper Method:**

```python
from orchestration.core.config import Config

checkpoint_path = Config.get_checkpoint_path("research-phase-validation")
# Returns: ~/.gstack/projects/claude-system/checkpoints/060626-1645-research-phase-validation.md
```

## Project Structure

```
orchestration/
├── __init__.py              # Package initialization
├── README.md                # This file
├── requirements.txt         # Python dependencies
├── core/
│   ├── __init__.py
│   └── config.py           # Configuration constants
├── phases/                  # Phase implementations (all 8 complete)
├── skills/                  # Skill orchestration layer (all 8 phases)
└── tests/                   # Test suite (305 tests passing)
```

## Development

### Running Tests

```bash
pytest orchestration/tests/ -v --cov=orchestration
```

### Code Quality

```bash
# Format code
black orchestration/

# Lint
ruff check orchestration/

# Type checking
mypy orchestration/
```

## Architecture

**Human-in-the-Loop:** Each phase includes approval gates where stakeholders review and approve before proceeding to the next phase.

**Skill Orchestration:** The system dispatches 75+ existing skills across phases:
- Research: market analysis, competitive intelligence
- Strategy: positioning, messaging, timeline
- Content: copywriting, design, video, social media
- Execution: ads, email, analytics setup
- Monitoring: KPI tracking, performance analysis

**Model Selection:**
- Complex reasoning (Phases 1-3): Claude Opus 4.7
- Execution & scaling (Phases 4-8): Claude Sonnet 4.6

**Research Validation (Phase 1):**
- Primary: Tavily API for real-time search and analysis
- Fallback: Perplexity AI if Tavily unavailable
- Confidence threshold: 75%

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `ANTHROPIC_API_KEY` | Anthropic API key | Yes |
| `TAVILY_API_KEY` | Tavily research API key | Yes |
| `PERPLEXITY_API_KEY` | Perplexity fallback API key | No |
| `DEBUG` | Enable debug logging | No (default: false) |

## License

Private. Part of claude-system monorepo.
