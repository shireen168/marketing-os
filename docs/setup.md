# Setup Guide: Marketing OS System

Get your system ready to run marketing ops workflows in 15 minutes.

## Prerequisites

- macOS, Windows, or Linux
- Administrator access (for global gstack installation)
- ~500MB disk space

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

Next: Follow [WORKFLOW.md](WORKFLOW.md) to run your first campaign.

---

**Total time:** ~15 minutes (first time only)

**Need help?** See [WORKFLOW.md](WORKFLOW.md) troubleshooting section.
