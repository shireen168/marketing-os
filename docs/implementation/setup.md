# Setup Guide: Marketing OS Orchestration System

Get your system ready to run the 8-phase orchestration system in 30 minutes.

## Three-Tier Architecture

| Tier | Layer | Setup |
|------|-------|-------|
| **Tier 1** | Strategic Intelligence | Python orchestration + APIs (this setup) |
| **Tier 2** | Human-AI Collaboration | Approval gates in orchestration (review + revise loops) |
| **Tier 3** | Team Execution | Simple tools (Canva, schedulers, deployment tools) |

## Prerequisites

### Technical Requirements
- macOS, Windows, or Linux
- ~500MB disk space
- Python 3.8+ installed
- Active Claude account (API key required)
- Three API keys:
  - **Anthropic API** (for Claude Opus 4.7 and Sonnet 4.6)
  - **Tavily API** (for market research)
  - **Perplexity API** (fallback research)
- Basic terminal/command line familiarity

### Team Readiness

| Role | Requirement |
|------|-------------|
| **Product owner** | Can describe product vision, target market, and business goals |
| **Tier 1 operator** | Can install Python, configure API keys, run orchestration commands |
| **Tier 2 reviewers** | Can review phase outputs and provide revision feedback (non-technical OK) |
| **Tier 3 executors** | Can implement the strategy using simple tools (design, scheduling, deployment) |
| **Cross-functional** | Willingness to iterate (each phase output is reviewed and approved, not auto-executed) |

This is not a "set and forget" system. Each phase asks 6 clarifying questions and pauses for your approval. Your input directly shapes the product direction.

### What You'll Get After Setup
- **Tier 1:** Ability to run 8-phase orchestration workflows from research to launch (1-2 weeks total vs 3-4 months manual)
- **Tier 2:** Approval gates after each phase where teams review and refine findings via revision feedback
- **Tier 3:** Fully documented strategy and implementation roadmap ready for execution
- Full orchestration of 75+ gstack skills across all 8 phases
- Context preservation across all phases via checkpoint system
- Ready to use for any product launch (SaaS, hardware, services, etc.)

## Step 1: Install Python

The orchestration system requires Python 3.8 or higher.

**macOS:**
```bash
# Using Homebrew
brew install python3
```

**Windows:**
Download from [python.org](https://www.python.org/downloads/) and run the installer.

**Linux:**
```bash
# Ubuntu/Debian
sudo apt-get install python3
```

**Verify:**
```bash
python3 --version
```

## Step 2: Get API Keys

You need 3 API keys:

### 2a: Anthropic API Key
1. Go to [console.anthropic.com](https://console.anthropic.com)
2. Sign in with your Claude account
3. Click "API keys" → "Create new key"
4. Copy and save it safely

### 2b: Tavily API Key
1. Go to [tavily.com](https://tavily.com)
2. Sign up and create account
3. Go to API dashboard
4. Copy and save your API key

### 2c: Perplexity API Key
1. Go to [perplexity.ai](https://perplexity.ai)
2. Sign up and create account
3. Go to API settings
4. Copy and save your API key

## Step 3: Configure .env File

Create a `.env` file in your project root:

```bash
cd /path/to/claude-system
```

Create the file with your keys:

```
ANTHROPIC_API_KEY=sk-ant-...
TAVILY_API_KEY=tvly-...
PERPLEXITY_API_KEY=pplx-...
```

**Save and secure:** Never commit this file to git. Add to `.gitignore`:

```bash
echo ".env" >> .gitignore
git add .gitignore && git commit -m "chore: add .env to gitignore"
```

## Step 4: Clone Repositories

```bash
# Clone parent repo
git clone https://github.com/shireen168/claude-system.git
cd claude-system

# The marketing-os submodule should already be included
# If not, initialize submodules:
git submodule update --init --recursive
```

## Step 5: Test Installation

Test that the orchestration system can access all APIs:

```bash
python orchestration/cli/run_workflow.py --help
```

You should see available commands and options. If not:
- Check Python is installed: `python3 --version`
- Check `.env` file has all 3 API keys
- Check keys are valid (test in web consoles)

## Step 6: Run Phase 1 Test

```bash
# Run Phase 1 of orchestration (non-interactive mode)
python orchestration/cli/run_workflow.py \
  --project test-product \
  --phase 1 \
  --no-approval
```

This runs a full Phase 1 (market research) without asking for approval. You should see:
- Tavily research running
- /investigate skill running
- /customer-research skill running
- /competitor-profiling skill running
- Opus synthesis running
- Final research report generated

**If it fails:**
- Verify all 3 API keys in `.env` are correct
- Check internet connection is active
- Review error message for specific API issue

## You're Ready

Your orchestration system is set up. Next:

1. **Tier 1 (Orchestration):** Run `/orchestration [product-name]` or use CLI commands from [phases/](./phases/)
2. **Tier 2 (Review):** Answer clarifying questions and review each phase output. Approve, revise, or ask for more info.
3. **Tier 3 (Execution):** Implement the approved strategy using simple tools.

---

**Total setup time:** ~30 minutes (first time only)

**See it in action:** [docs/marketing-campaigns/showcase/](../marketing-campaigns/showcase/) shows a complete sleep device product launch (Phases 1-4).

**For help:** Refer to [phases/phase-1-orchestration.md](./phases/phase-1-orchestration.md) or orchestration troubleshooting.
