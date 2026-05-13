# Setup Guide: Marketing OS System

Get your system ready to run marketing ops workflows in 15 minutes.

## Prerequisites

### Technical Requirements
- macOS, Windows, or Linux
- Administrator access (for global gstack installation)
- ~500MB disk space
- Active Claude account (free or paid)
- Basic terminal/command line familiarity

### Team Readiness
Before starting, your team should understand:

- **Marketing:** How to brief a product idea (target audience, channels, success metrics)
- **Non-technical teams:** Comfortable with VS Code UI or Claude Desktop chat interface
- **Cross-functional:** Willingness to iterate (outputs are drafts, not final publishing-ready copy)

This is not a "set and forget" system. It's a structured thinking tool that requires team input at each stage.

### What You'll Get After Setup
- Ability to run 6-stage marketing workflows in parallel chat sessions
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

Next: Follow [workflow.md](workflow.md) to run your first campaign.

---

**Total time:** ~15 minutes (first time only)

**Need help?** See [WORKFLOW.md](WORKFLOW.md) troubleshooting section.
