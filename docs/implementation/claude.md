# Claude Settings for Marketing OS

8-phase orchestration system for full product launches from research to operations.

**What this is:** Automated workflow that turns a product idea into a launched, optimized product in 1-2 weeks instead of 3-4 months.

**How it works:** Multi-phase orchestration (Python CLI) + human approval gates + skill coordination. Each phase asks clarifying questions, runs subagents, synthesizes findings, and pauses for your approval.

## Three-Tier Architecture

**Tier 1 (Strategic Intelligence):** Python orchestration + Tavily/Perplexity APIs + gstack skills coordinate all 8 phases
**Tier 2 (Human-AI Collaboration):** Approval gates after each phase let you review and refine before proceeding
**Tier 3 (Team Execution):** Non-technical teams execute the approved outputs using simple tools

This system is designed so Tier 1 produces strategic outputs at scale, Tier 2 teams review and refine those outputs, and Tier 3 executes with confidence.

## System Architecture

The orchestration system coordinates:
- **Tavily API:** Real-time market research and trend data
- **Perplexity API:** Fallback research if Tavily is unavailable
- **Anthropic API:** Opus 4.7 (phases 1-3) and Sonnet 4.6 (phases 4-8) for synthesis
- **gstack skills:** 75+ skills orchestrated across all 8 phases
- **Approval gates:** Human review + revision loops after each phase
- **Checkpoint system:** Save/restore state anytime, resume from any phase

## 8-Phase Workflow

**Phase 1: Research** - Market validation and opportunity assessment  
**Phase 2: Strategy** - Go-to-market positioning and pricing  
**Phase 3: Design** - Product design and architecture  
**Phase 4: Build** - Development and implementation  
**Phase 5: Testing** - QA, validation, and optimization  
**Phase 6: Launch** - Execution and go-live  
**Phase 7: Growth** - Growth loops and scaling  
**Phase 8: Operations** - Monitoring, learning, and iteration  

**Total timeline:** 1-2 weeks (vs 3-4 months manual)

## Skills by Phase

What orchestration happens under the hood at each phase:

### Phase 1: Research - Market Validation

| Subagent | What it does | Duration |
|----------|-------------|----------|
| Tavily API | Surface-level market research (trends, news, discussions) | 10-15s |
| `/investigate` | Deep-dive root cause analysis (why problems exist, missing solutions) | 30-45s |
| `/customer-research` | Understand customer needs (personas, pain points, willingness to pay) | 20-30s |
| `/competitor-profiling` | Competitive landscape mapping (feature matrix, gaps, positioning) | 20-30s |
| Opus 4.7 | Synthesize findings into strategic recommendations + confidence scoring | 10-20s |

**Output:** 30-50 page research report with market sizing, competitor analysis, customer validation, risk assessment

### Phase 2: Strategy - Go-to-Market

| Subagent | What it does | Duration |
|----------|-------------|----------|
| `/product-marketing` | Positioning statement and messaging hierarchy | 20-30s |
| `/pricing` | Revenue model, pricing strategy, unit economics | 20-30s |
| `/sales-enablement` | Sales collateral, pitch deck, buyer journey | 20-30s |
| Opus 4.7 | Synthesize strategy into executable GTM plan | 10-20s |

**Output:** 5-8 page strategy document with positioning, pricing, GTM timeline, sales strategy

### Phase 3: Design - Architecture & UX

| Subagent | What it does |
|----------|-------------|
| `/design-consultation` | UX philosophy and interaction patterns |
| `/plan-eng-review` | Technical architecture and data pipeline |
| `/plan-design-review` | Design system and visual tokens |

**Output:** Design system, architecture blueprint, wireframes, component library

### Phase 4: Build - Development

| Subagent | What it does |
|----------|-------------|
| `/skill-creator` | Custom skill development for product-specific workflows |
| `/plan-eng-review` | API design, database schema, deployment architecture |

**Output:** Feature-complete codebase, API documentation, deployment guide

### Phase 5: Testing - QA & Validation

| Subagent | What it does |
|----------|-------------|
| `/qa` | Quality assurance, test coverage, edge case validation |
| `/investigate` | Root cause analysis for bugs and issues |

**Output:** QA report, test coverage, performance benchmarks, optimization recommendations

### Phase 6: Launch - Execution

| Subagent | What it does |
|----------|-------------|
| `/ship` | Deployment, monitoring setup, go-live checklist |
| `/context-save` | Checkpoint creation for post-launch reference |

**Output:** Go-live report, monitoring dashboard, launch metrics

### Phase 7: Growth - Optimization

| Subagent | What it does |
|----------|-------------|
| `/autoplan` | Growth loop design and optimization strategy |
| `/investigate` | Performance analysis and bottleneck identification |

**Output:** Growth roadmap, KPI targets, optimization priorities

### Phase 8: Operations - Learning & Iteration

| Subagent | What it does |
|----------|-------------|
| `/plan-ceo-review` | Post-launch review and next-cycle strategy |
| `/context-save` | Final checkpoint for documentation |

**Output:** Operations report, learning summary, iteration backlog

---

## Workflow: How to Run

### Non-Technical Path (Recommended)

```bash
# Phase 1: Research
/orchestration [product-name]

# Phase 2: Strategy (when Phase 1 approved)
/orchestration [product-name] --phase 2

# Continue through phases 3-8
/orchestration [product-name] --phase 3
# ... and so on
```

**Each phase:**
1. Asks 6 clarifying questions about your product/market
2. Runs subagents (Tavily, skills, Opus synthesis)
3. Presents results for approval
4. Saves checkpoint automatically
5. Proceeds to next phase when approved

### Technical Path (CLI)

```bash
python orchestration/cli/run_workflow.py \
  --project [product-name] \
  --phase 1 \
  --save-checkpoint phase1-complete

# With checkpoint restore
python orchestration/cli/run_workflow.py \
  --project [product-name] \
  --phase 2 \
  --checkpoint ~/.gstack/projects/claude-system/checkpoints/phase1-complete.md \
  --save-checkpoint phase2-complete
```

### Options

- `--checkpoint <path>` - Resume from a previous checkpoint
- `--save-checkpoint <name>` - Save state after phase completes
- `--no-approval` - Skip approval gate (auto-approve)
- `--verbose` - Show all subagent invocations and synthesis steps

## Approval Gates: The Human-AI Collaboration Loop

**After each phase, the system pauses for your approval.**

This is the core differentiator: The orchestration runs all subagents and synthesis automatically, but you decide whether to proceed to the next phase.

**Approval options:**

- **Approve** → Accept findings, proceed to next phase, checkpoint saved automatically
- **Revise** → Provide feedback, system asks diagnostic questions, re-run phase with refined scope
- **Unclear** → Not enough information, system suggests additional research, gather more data, re-run

**Why approval gates matter:**
- Team stays in control at every decision point
- Revision loops let you refine scope without restarting
- Checkpoints preserve all context between phases
- No surprises - every phase outcome is reviewed before proceeding

**Result:** Tier 1 orchestrates all phases automatically. Tier 2 (approval gates) ensures human judgment stays in the loop. Tier 3 executes with confidence.

## Checkpoint Management

The system auto-saves checkpoints in `~/.gstack/projects/claude-system/checkpoints/`:

- **Format:** `ddmmyy-hhmm-[description].md` (e.g., `090624-1430-phase1-research-approved.md`)
- **Contents:** Metadata, all answered questions, phase results, synthesis output
- **Use:** Resume from any checkpoint anytime, zero context loss

**Resume example:**
```bash
/orchestration [product-name] --phase 3 \
  --checkpoint ~/.gstack/projects/claude-system/checkpoints/060626-1500-phase2-strategy-approved.md
```

## Real-World Example

See [docs/marketing-campaigns/showcase/](../marketing-campaigns/showcase/) for a complete three-tier example: architecture overview and the sleep device case study showing Phases 1-4 in detail.

## Setup Instructions

Follow [setup.md](setup.md) to install:
1. Python 3.8+
2. Get API keys (Tavily, Perplexity, Anthropic)
3. Configure `.env` file with keys
4. Test installation
5. Run first phase

For step-by-step instructions on each phase, see [phases/](./phases/).

## Tips

- **1-2 weeks total:** ~30-60 minutes per phase (8 phases = full product launch)
- **Ask clarifying questions:** Each phase asks 6 questions - answer honestly, system uses them to customize research/strategy
- **Approval gates are not optional:** Review each phase output carefully. Tier 2 is where your team shapes the product direction.
- **Revise without restarting:** If Phase 2 strategy doesn't match your vision, use revision feedback to refine. Don't restart Phase 1.
- **Context flows through:** Phase 5 (Testing) uses findings from all prior phases. Phase 8 (Operations) feeds back to next product cycle.
- **Checkpoints are your safety net:** Crash mid-phase? Resume from last checkpoint, zero context loss.
- **Team workflow:** Tier 1 runs orchestration automatically. Tier 2 reviews each phase output. Tier 3 implements the approved strategy.

## Status

✅ **Phases 1-8:** Fully implemented and tested (305 tests passing)  
📋 **Phases 3-8:** Specification ready, implementation in progress

## Next Steps

After Phase 2, you'll have:
- Complete market research (Phase 1)
- GTM strategy with positioning and pricing (Phase 2)

Ready to proceed to:
- Phase 3: Design & architecture
- Phase 4: Build & development
- Phase 5: Testing & QA
- Phase 6: Launch execution
- Phase 7: Growth & optimization
- Phase 8: Operations & learning
