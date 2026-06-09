# Orchestration System: User Experience Guide

**Two paths: Non-technical (slash command) vs Technical (CLI)**

---

## Path 1: Non-Technical Users ⭐ (Recommended)

### Setup (15 minutes, follow SETUP_GUIDE.md)

1. ✅ Install Python (direct links provided)
2. ✅ Get 3 API keys (step-by-step instructions)
3. ✅ Save keys in `.env` file (copy-paste template)
4. ✅ Test installation (one command)

**That's it! You're ready.**

---

### Running Phase 1: Research

**Just type:**
```
/orchestration sleep-device
```

**System responds:**
```
════════════════════════════════════════════════════════════════
PHASE 1: RESEARCH VALIDATION

Let me gather some clarifications first (6 questions)...

1️⃣ What specific research topics or themes are most important to validate?
```

**You answer:**
```
Health tech market, sleep disorders, wearable devices, corporate wellness
```

**System asks next question:**
```
2️⃣ Who are the primary audiences for this research?
```

**Continue for all 6 questions...**

**System runs research (2-5 minutes):**
```
Running Tavily research...
Running /investigate skill...
Running /customer-research...
Running /competitor-profiling...
Synthesizing with Opus...
✅ Phase 1 complete!
```

**System presents results:**
```
════════════════════════════════════════════════════════════════
PHASE 1 RESULTS: RESEARCH REPORT
════════════════════════════════════════════════════════════════

[Full 30-50 page research report]

Market size: $2.5B
Key entry barriers: Clinical validation
Strategic windows: 18-24 months

...
```

**Approval gate:**
```
Do you approve this research for Phase 2?

A) approve           → Proceed to Phase 2 (strategy)
B) revise: [feedback] → I'll ask more questions and re-research
C) questions: [gaps]  → What's missing?
```

**You approve:**
```
A
```

**System saves and asks:**
```
✅ Checkpoint saved: 060626-1430-phase1-research-approved.md

Ready for Phase 2 (Strategy Development)?
```

---

### Running Phase 2: Strategy

**Just type:**
```
/orchestration sleep-device --phase 2
```

**System loads Phase 1 context and asks 6 new questions:**

```
1️⃣ What's the primary positioning angle?
   → Enterprise health monitoring with clinical accuracy

2️⃣ Target early customer profile?
   → Mid-size corporations (500-5000 employees)

3️⃣ Revenue model preference?
   → Subscription

4️⃣ Go-to-market timeline?
   → Q3 2026

5️⃣ Budget constraints?
   → $100K

6️⃣ Priority?
   → Market share
```

**System runs strategy orchestration:**
```
Running /product-marketing...
Running /pricing...
Running /sales-enablement...
Synthesizing strategy document...
✅ Phase 2 complete!
```

**System presents strategy document:**
```
════════════════════════════════════════════════════════════════
STRATEGY DOCUMENT: Sleep Guard Pro
════════════════════════════════════════════════════════════════

## Positioning
Enterprise-grade sleep health platform for corporate wellness

## Pricing
Subscription: $2-3 PEPM

## GTM
Launch Q3 2026, target corporate wellness

...
```

**Approval gate:**
```
Do you approve this strategy for Phase 3?

A) approve
B) revise: [feedback]
C) questions: [gaps]
```

---

## Path 2: Technical Users 👨‍💻 (CLI)

**Same results, different interface:**

```bash
# Phase 1
python orchestration/cli/run_workflow.py \
  --project sleep-device \
  --phase 1 \
  --verbose

# Phase 2
python orchestration/cli/run_workflow.py \
  --project sleep-device \
  --phase 2 \
  --verbose
```

**Pros:**
- Full control
- Scriptable
- Integrate with CI/CD

**Cons:**
- Need command line knowledge
- More flags to remember

---

## Complete Workflow: All 8 Phases

### Non-Technical: Just keep typing!

```
/orchestration sleep-device              # Phase 1: Research
[approve] → /orchestration sleep-device --phase 2   # Phase 2: Strategy
[approve] → /orchestration sleep-device --phase 3   # Phase 3: Design
[approve] → /orchestration sleep-device --phase 4   # Phase 4: Build
[approve] → /orchestration sleep-device --phase 5   # Phase 5: Testing
[approve] → /orchestration sleep-device --phase 6   # Phase 6: Launch
[approve] → /orchestration sleep-device --phase 7   # Phase 7: Growth
[approve] → /orchestration sleep-device --phase 8   # Phase 8: Operations
```

**Result:** Complete product launch from research to optimization ✨

---

## What Happens Behind the Scenes

```
Your input: /orchestration sleep-device

        ↓
    
System breaks down into 8 phases:

Phase 1: Research
  ├── Ask 6 clarifying questions
  ├── Run 4 subagents (Tavily, /investigate, /customer-research, /competitor-profiling)
  ├── Synthesize with Opus
  └── Present 30-50 page research report

Phase 2: Strategy
  ├── Ask 6 clarifying questions
  ├── Run 3 subagents (/product-marketing, /pricing, /sales-enablement)
  ├── Synthesize with Opus
  └── Present 5-8 page strategy document

[Phases 3-8 follow same pattern with different skills]

Each phase:
  ├── Saves checkpoint
  ├── Asks for approval (approve/revise/question)
  ├── If revise: loops back with diagnostic questions
  ├── If approve: saves state and moves to Phase N+1
  └── Full context preserved (can resume from any checkpoint)
```

---

## Checkpoints & Recovery

**All phases auto-save checkpoints:**

```
~/.orchestration/checkpoints/sleep-device/
├── 060626-1430-phase1-research-approved.md
├── 060626-1500-phase2-strategy-approved.md
└── ...
```

**Resume anytime:**

```
# Resume from Phase 2 checkpoint → Phase 3
/orchestration sleep-device --phase 3 --checkpoint 060626-1500-phase2-strategy-approved.md
```

**Or restart fresh:**

```
# Delete checkpoint, start Phase 1 from scratch
/orchestration sleep-device
```

---

## Getting Help

### If something doesn't work:

1. Check SETUP_GUIDE.md troubleshooting section
2. Verify `.env` file has all 3 API keys
3. Make sure Python is installed
4. Run test command: `python orchestration/cli/run_workflow.py --help`

### If you want details:

- **How to use slash commands?** → `.claude/skills/orchestration/SKILL.md`
- **Complete workflow example?** → `orchestration/docs/examples/sleep-device-workflow.md`
- **Implementation plans?** → `docs/superpowers/plans/phase-NN-*.md`
- **Setup instructions?** → `SETUP_GUIDE.md`

---

## Key Features

✅ **No manual skill invocation** - System orchestrates all 75+ skills  
✅ **Interactive questions** - System asks until it fully understands your intent  
✅ **Approval gates** - You stay in control at every phase  
✅ **Auto-saving** - Checkpoints saved after each approval  
✅ **Context preservation** - Resume from any checkpoint anytime  
✅ **Revision loops** - Refine outputs without restarting  
✅ **Confidence scoring** - System shows confidence in synthesis quality  

---

## Status

✅ **Phases 1-2:** Available now (tested, 210 tests passing)  
📋 **Phases 3-8:** Coming (high-level plans ready, implementation starting)

---

**Ready to launch your product?**

```
/orchestration [your-product-name]
```

That's it! 🚀
