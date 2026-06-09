# Phase 1: Validation - Orchestration Guide

**Goal:** Automate market research and validation using the orchestration engine.

**Timeline:** ~30 minutes (vs 4-6 hours manual)  
**Automated Skills:** 5 (Tavily research, /investigate, /customer-research, /competitor-profiling, Opus synthesis)  
**Output:** Validation report ready for approval  
**Checkpoints:** Auto-saved before and after execution

---

## Quick Start

### 1. Run Phase 1 with Orchestration

```bash
cd /path/to/claude-system

python orchestration/cli/run_workflow.py \
  --project marketing-os \
  --phase 1 \
  --save-checkpoint phase1-validation-complete
```

**What happens:**
1. System gathers clarifying questions about your market
2. Tavily research runs (market trends, competitors)
3. /investigate skill analyzes findings
4. /customer-research framework applied
5. /competitor-profiling completed
6. Opus synthesizes all findings
7. Report formatted for approval
8. Checkpoint saved for later resumption

### 2. With Verbose Output (See All Steps)

```bash
python orchestration/cli/run_workflow.py \
  --project marketing-os \
  --phase 1 \
  --verbose \
  --save-checkpoint phase1-validation-complete
```

Shows:
- Each subagent invocation
- Input parameters
- Output synthesis
- Approval gate formatting

### 3. Skip Approval Gate (Auto-Approve)

```bash
python orchestration/cli/run_workflow.py \
  --project marketing-os \
  --phase 1 \
  --no-approval \
  --save-checkpoint phase1-validation-complete
```

Useful for:
- Batch processing
- Automated CI/CD workflows
- Testing

---

## Phase 1 Clarifying Questions

The orchestrator will ask these questions to customize research:

### Topic & Product (High Priority)
- What specific research topics or themes are most important to validate?
- Who are the primary audiences for this research (buyers, decision-makers, influencers)?

### Validation Metrics (High Priority)
- What specific data points or metrics would validate success?
- Should we prioritize quantitative data, qualitative insights, or both?

### Competitive Context (Medium Priority)
- Are there any competitor benchmarks or market trends we should focus on?
- What time frame should the research cover (historical, current, forward-looking)?

**Answer in the terminal when prompted.** Answers are saved to the checkpoint.

---

## What Gets Automated

### Subagent 1: Tavily Research
**Purpose:** Surface-level market research from public sources  
**Duration:** 10-15 seconds  
**Output:** Latest trends, recent news, market discussions

**Queries executed:**
- `{topic} market trends 2024-2025`
- `{topic} competitor comparison`
- `{topic} customer reviews and feedback`

### Subagent 2: /investigate
**Purpose:** Deep-dive root cause analysis  
**Duration:** 30-45 seconds  
**Output:** Why problems exist, what existing solutions are missing

**Analysis covers:**
- Core failure points of existing solutions
- Regulatory/market barriers
- Technology constraints
- User behavior patterns

### Subagent 3: /customer-research
**Purpose:** Understand actual customer needs  
**Duration:** 20-30 seconds  
**Output:** Customer personas, pain points, willingness to pay

**Frameworks applied:**
- Jobs to be done
- User persona mapping
- Price sensitivity analysis
- Feature prioritization

### Subagent 4: /competitor-profiling
**Purpose:** Competitive landscape mapping  
**Duration:** 20-30 seconds  
**Output:** Competitor matrix, market gaps, positioning opportunities

**Analysis includes:**
- Feature comparison
- Pricing strategies
- Go-to-market approaches
- Retention/churn metrics
- Brand positioning

### Subagent 5: Opus Synthesis
**Purpose:** Synthesize all research into actionable insights  
**Duration:** 10-20 seconds  
**Output:** Strategic recommendations, confidence assessment

**Synthesis produces:**
- Key findings summary
- Market opportunity assessment
- Recommended positioning
- MVP scope recommendation
- Risk assessment

---

## Approval Gate

### What You See

```
============================================================
  PHASE 1 DELIVERABLE
============================================================

  Project: marketing-os
  Phase: 1
  Status: success

------------------------------------------------------------

[Full research synthesis and strategic recommendations]

------------------------------------------------------------
```

### Your Options

**[a] Approve**
- Accept the findings and recommendations
- Automatically saves as "approved"
- Proceeds to Phase 2

**[r] Revise**
- Request specific changes
- System generates diagnostic questions
- Run orchestrator again with refined scope

**[u] Unclear**
- Not enough information
- System suggests additional research
- Gather more specific data before re-running

### Revision Workflow

If you choose **Revise**:

1. Provide feedback: "I need more detail on the hospitality market"
2. System generates diagnostic questions:
   - "What specific aspects of hospitality?"
   - "Which customer segments in hospitality?"
   - "What metrics matter most?"
3. Answer the questions
4. Re-run orchestrator with updated clarifications:
   ```bash
   python orchestration/cli/run_workflow.py \
     --project marketing-os \
     --phase 1 \
     --checkpoint /path/to/revision-checkpoint.md \
     --save-checkpoint phase1-revised
   ```

---

## Checkpoint Management

### Auto-Saved Checkpoints

The orchestrator saves checkpoints at 3 points:

1. **Before execution** (`phase1-start`)
2. **After execution** (`phase1-after-execution`)
3. **After approval** (`phase1-approved`)

All stored in: `~/.gstack/projects/claude-system/checkpoints/`

### Restore from Checkpoint

Resume exactly where you left off:

```bash
python orchestration/cli/run_workflow.py \
  --project marketing-os \
  --phase 2 \
  --checkpoint ~/.gstack/projects/claude-system/checkpoints/phase1-approved.md
```

The system will:
- Load all Phase 1 findings
- Load all answered questions
- Proceed directly to Phase 2
- **Zero context loss**

### Checkpoint Contents

Each checkpoint includes:
```json
{
  "metadata": {
    "project": "marketing-os",
    "phase": 1,
    "description": "phase1-validation-complete",
    "timestamp": "2026-06-06T16:45:00"
  },
  "context": {
    "current_phase": 1,
    "answered_questions": [
      "What specific research topics...",
      "Who are the primary audiences...",
      ...
    ],
    "phase_results": {
      "tavily": { ... },
      "investigate": { ... },
      "customer_research": { ... },
      "competitor_profiling": { ... },
      "synthesis": { ... }
    }
  }
}
```

---

## Example: Sleep Device Validation

### Command

```bash
python orchestration/cli/run_workflow.py \
  --project marketing-os \
  --phase 1 \
  --save-checkpoint sleep-device-phase1
```

### Clarifying Questions Answered

**Q: What specific research topics or themes are most important to validate?**
A: Sleep tracking accuracy, wearable device reliability, consumer adoption barriers in health tech

**Q: Who are the primary audiences for this research?**
A: Tech-savvy health enthusiasts (18-45), biohackers, quantified-self communities, sleep disorder patients

**Q: What specific data points would validate success?**
A: Market size estimates, competitor retention rates, price sensitivity, feature importance rankings

**Q: Should we prioritize quantitative or qualitative data?**
A: 70% quantitative (market data, benchmarks), 30% qualitative (customer quotes, use cases)

### Output Report

**Key Findings:**
- Sleep wearable market growing 18% YoY
- Oura Ring dominates but 40% annual churn
- Price sensitivity caps at $299 for consumer market
- Battery life is #1 abandonment reason
- Market underserved in "actionable insights" (most devices just track)

**Competitive Gaps:**
- No wearable focuses on sleep *quality* recommendations
- Existing products treat sleep as data point, not health intervention
- Opportunity in therapeutic positioning (doctors, sleep clinics)

**Recommended MVP:**
- Sleep duration + REM% tracking
- "Sleep score" actionable recommendation engine
- 7-day battery minimum
- Focus on 25-45 age group (higher willingness to pay)

**Confidence:** 87% (based on market data, competitor analysis, customer research alignment)

---

## Troubleshooting

### "No clarifying questions to answer"
**Meaning:** All Phase 1 questions were already answered in a previous session  
**Solution:** Run with `--no-approval` to re-run analysis with saved context

### "Checkpoint file not found"
**Meaning:** Path to checkpoint doesn't exist  
**Solution:** Use tab-completion or list checkpoints:
```bash
ls ~/.gstack/projects/claude-system/checkpoints/
```

### "API timeout during Tavily research"
**Meaning:** Research API slow or unreachable  
**Solution:** 
1. Check internet connection
2. Wait 30 seconds and re-run
3. Use `--no-approval` to skip research and use cached data

### "Synthesis output seems incomplete"
**Meaning:** Opus response was truncated  
**Solution:** Re-run with `--verbose` to see full process

---

## Next: Phase 2

Once Phase 1 is approved:

```bash
python orchestration/cli/run_workflow.py \
  --project marketing-os \
  --phase 2 \
  --checkpoint ~/.gstack/projects/claude-system/checkpoints/phase1-approved.md \
  --save-checkpoint phase2-strategy-complete
```

The orchestrator will:
- Load all Phase 1 findings
- Ask Phase 2 clarifying questions (strategy-specific)
- Run strategy subagents
- Synthesize strategy recommendations
- Request approval

---

## Full Workflow: All Phases

```bash
# Phase 1: Validation (market research)
python orchestration/cli/run_workflow.py --project marketing-os --phase 1 --save-checkpoint p1

# Phase 2: Strategy (positioning, GTM)
python orchestration/cli/run_workflow.py --project marketing-os --phase 2 --checkpoint p1.md --save-checkpoint p2

# Phase 3: Design & Architecture
python orchestration/cli/run_workflow.py --project marketing-os --phase 3 --checkpoint p2.md --save-checkpoint p3

# Phase 4: Build & Development
python orchestration/cli/run_workflow.py --project marketing-os --phase 4 --checkpoint p3.md --save-checkpoint p4

# Phase 5: Testing & QA
python orchestration/cli/run_workflow.py --project marketing-os --phase 5 --checkpoint p4.md --save-checkpoint p5

# Phase 6: Launch Execution
python orchestration/cli/run_workflow.py --project marketing-os --phase 6 --checkpoint p5.md --save-checkpoint p6

# Phase 7: Growth & Optimization
python orchestration/cli/run_workflow.py --project marketing-os --phase 7 --checkpoint p6.md --save-checkpoint p7

# Phase 8: Operations & Learning
python orchestration/cli/run_workflow.py --project marketing-os --phase 8 --checkpoint p7.md --save-checkpoint p8
```

Each phase takes 30-60 minutes. Full workflow: ~4-6 hours.

---

## Reference

- **Orchestrator source:** `orchestration/core/orchestrator.py`
- **CLI source:** `orchestration/cli/run_workflow.py`
- **Tests:** `tests/integration/test_phase1_e2e.py`
- **Config:** `orchestration/core/config.py`
