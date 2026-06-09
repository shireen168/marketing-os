# Orchestration System: Complete Setup Guide

**For non-technical users: Follow this checklist in order. No command-line experience needed.**

---

## Step 1: Install Python & Dependencies (5 minutes)

### If you don't have Python installed:

**Windows:**
1. Go to https://www.python.org/downloads/
2. Download Python 3.11 or higher
3. Run installer
4. ✅ Check "Add Python to PATH"
5. Click Install

**Mac:**
1. Go to https://www.python.org/downloads/
2. Download Python 3.11 for macOS
3. Run installer, follow prompts

### Install orchestration dependencies:

Open Terminal/PowerShell and run:

```bash
cd C:\Users\user\Desktop\claude-system
pip install -r orchestration/requirements.txt
```

✅ When done, you should see: `Successfully installed...`

---

## Step 2: Set Up API Keys (10 minutes)

The orchestration system needs 3 API keys. Get them:

### Anthropic API Key (for Claude)
1. Go to https://console.anthropic.com
2. Sign in with your account
3. Click "API Keys" in left sidebar
4. Click "Create Key"
5. Copy the key (starts with `sk-...`)

### Tavily API Key (for research)
1. Go to https://tavily.com
2. Sign up (free)
3. Go to https://app.tavily.com/home
4. Copy your API key

### Perplexity API Key (fallback, optional)
1. Go to https://www.perplexity.ai
2. Sign in
3. Go to settings → API
4. Copy your API key

### Save the keys:

1. Open `orchestration/.env.example`
2. Copy all contents
3. Create new file: `orchestration/.env`
4. Paste the contents
5. Replace the values:
```
ANTHROPIC_API_KEY=sk-your-actual-key-here
TAVILY_API_KEY=tvly-your-actual-key-here
PERPLEXITY_API_KEY=ppl-your-actual-key-here (optional)
DEBUG=false
```
6. Save the file

✅ API keys are now configured

---

## Step 3: Test Installation (2 minutes)

Run this command to verify everything works:

```bash
python orchestration/cli/run_workflow.py --help
```

✅ If you see help text, installation is successful!

---

## Step 4: Run Your First Workflow

### Option A: Non-Technical Users (Recommended)

Use the gstack skill:

```
/orchestration sleep-device
```

Then answer 6 clarifying questions interactively. The system handles the rest!

### Option B: Command Line (Technical Users)

```bash
# Phase 1: Research
python orchestration/cli/run_workflow.py \
  --project sleep-device \
  --phase 1 \
  --verbose

# When Phase 1 is approved, Phase 2:
python orchestration/cli/run_workflow.py \
  --project sleep-device \
  --phase 2 \
  --verbose
```

---

## Step 5: Understanding the Workflow

Each phase has 3 stages:

```
1. CLARIFYING QUESTIONS
   ↓ (You answer 6 questions)
   ↓
2. ORCHESTRATION EXECUTION
   ↓ (System runs subagents, synthesizes output)
   ↓
3. APPROVAL GATE
   ↓ (You review output, approve/revise)
   ↓ (If approved, system saves checkpoint)
   ↓
4. NEXT PHASE
   ↓ (Move to Phase N+1)
```

---

## Troubleshooting

### Error: "Python not found"
- Python not installed (see Step 1)
- Python not in PATH (reinstall and check "Add Python to PATH")

### Error: "Module not found"
- Dependencies not installed (run Step 1 again)
- Wrong directory (make sure you're in `C:\Users\user\Desktop\claude-system`)

### Error: "API key invalid"
- Check `.env` file has correct keys
- Verify keys by visiting the provider websites
- Make sure no extra spaces or quotes around keys

### Slow performance
- First run is slower (system initializing)
- Subsequent phases are faster
- Tavily research takes 1-2 minutes (normal)

---

## Next Steps

1. ✅ Complete setup (you are here)
2. 📖 Read `orchestration/docs/examples/sleep-device-workflow.md`
3. 🚀 Run Phase 1 research
4. ✔️ Review and approve Phase 1
5. ➡️ Move to Phase 2

---

## Support

If something doesn't work:

1. Check troubleshooting above
2. Read error message carefully
3. Check `.env` file has all 3 API keys
4. Try running from correct directory: `C:\Users\user\Desktop\claude-system`

---

**Last Updated:** 2026-06-08
