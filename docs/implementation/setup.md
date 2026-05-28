# Setup Guide: Marketing OS System

Get your system ready to run marketing ops workflows using the three-tier architecture in 15 minutes.

## Three-Tier Architecture

| Tier | Layer | Setup |
|------|-------|-------|
| **Tier 1** | Strategic Intelligence | Claude Code in VS Code (this setup) |
| **Tier 2** | Human-AI Collaboration | Claude Desktop (separate download) for approval gates |
| **Tier 3** | Team Execution | Simple tools (Linktree, Canva, etc.) |

## Prerequisites

### Technical Requirements
- macOS, Windows, or Linux
- Administrator access (for global gstack installation)
- ~500MB disk space
- Active Claude account (free or paid)
- Basic terminal/command line familiarity
- **Tier 1:** VS Code with Claude Code extension
- **Tier 2:** Claude Desktop (for Cowork approval gates with your team)

### Team Readiness
Before starting, your team should understand:

- **Marketing:** How to brief a product idea (target audience, channels, success metrics)
- **Tier 1 operator:** Comfortable with VS Code + Claude Code + gstack commands
- **Tier 2 reviewers:** Comfortable with Claude Desktop (non-technical OK, this is where teams approve outputs)
- **Tier 3 executors:** Can use simple tools (Linktree, Canva, scheduling software)
- **Cross-functional:** Willingness to iterate (outputs are approved in Cowork, not published directly)

This is not a "set and forget" system. It's a structured thinking tool that requires team input at each stage.

### What You'll Get After Setup
- **Tier 1:** Ability to run 6-stage marketing workflows in VS Code (4-8 hours strategic work per campaign vs $20-30K + 2-3 weeks agency)
- **Tier 2:** Approval gates in Claude Desktop Cowork where teams refine outputs at Stages 2, 4, 6
- **Tier 3:** Publication-ready outputs that execution teams can publish with confidence
- All gstack skills available globally (/brainstorm, /investigate, /plan-ceo-review)
- Claude Code context preservation across stages
- Ready to adapt to HR recruiting, legal briefs, sales campaigns, or other departments

## Step 1: Install Claude CLI

Download and install Claude CLI from the official source.

**macOS:**
```bash
brew install anthropic/anthropic/claude-cli
```

**Windows:**
Download from [claude.sh](https://claude.sh) and follow installer.

**Linux:**
```bash
curl -fsSL https://claude.sh/install.sh | bash
```

**Verify:**
```bash
claude --version
```

## Step 2: Install gstack (Global)

```bash
git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/.claude/skills/gstack
cd ~/.claude/skills/gstack
./setup
```

**Verify:**
```bash
gstack --version
```

You should see version output. If not, re-run `./setup`.

## Step 3: Install Claude Code Extension

1. Open **Visual Studio Code**
2. Go to Extensions (Cmd+Shift+X / Ctrl+Shift+X)
3. Search for "Claude Code"
4. Click **Install** (published by Anthropic)
5. Sign in with your Claude account

**Verify:** You should see a Claude icon in the sidebar.

## Step 3b: Install Claude Desktop (For Tier 2 Approvals)

Claude Desktop is where your team reviews and refines outputs at approval gates (Stages 2, 4, 6).

1. Download Claude Desktop from [claude.ai](https://claude.ai/desktop)
2. Install on your machine
3. Sign in with your Claude account
4. Share workflow URLs with your team in Cowork conversations

**Verify:** You can create a new conversation in Claude Desktop.

## Step 4: Clone Marketing OS Repo

```bash
git clone https://github.com/shireen168/marketing-os.git
cd marketing-os
```

## Step 5: Verify Everything Works

1. Open marketing-os folder in VS Code
2. Open Claude Code panel (click Claude icon)
3. Type: `/brainstorm "test prompt"`
4. You should see a response with formatted output

**If it doesn't work:**
- Restart VS Code
- Check that gstack is installed: `~/.claude/skills/gstack/bin/gstack --version`
- Check Claude CLI is authenticated: `claude auth status`

## You're Ready

Your Tier 1 and Tier 2 infrastructure is set up. Next:

1. **Tier 1 (Claude Code):** Follow the [8-phase implementation guide](./phases/) to run your first campaign (4-8 hours strategic work across 6 stages)
2. **Tier 2 (Cowork):** Invite your team to Claude Desktop. Share campaign outputs. Refine at approval gates (Stages 2, 4, 6)
3. **Tier 3 (Execution):** Once Cowork approves, team publishes, tracks performance, feeds learnings back

---

**Total setup time:** ~15 minutes (first time only)

**See it in action:** [docs/marketing-campaigns/showcase/](../../marketing-campaigns/showcase/) shows the three-tier architecture in detail.

**For help:** Refer to the phase documentation or the [skills inventory](./skills-inventory.md).
