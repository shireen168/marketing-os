# Marketing OS Showcase: Complete System Architecture

This showcase demonstrates the Marketing OS framework through real-world examples and visual architecture guides.

## What Is Marketing OS?

A three-tier system for building marketing strategy at any scale:

1. **Tier 1:** Strategic Intelligence (Claude Code orchestration + MCP servers + custom skills)
2. **Tier 2:** Structured Outputs (6-stage workflow with human-AI collaboration in Claude Desktop Cowork)
3. **Tier 3:** Team Execution (non-technical team members using simple tools)

**Core insight:** Strategy and execution are separated. Consultants build Tier 1 (thinking), teams execute Tier 3 (doing), approval gates live in Tier 2 (Cowork).

---

## Folder Structure

```
docs/showcase/
├── README.md (this file)
│
└── architecture-overview/
    ├── 00-three-tier-stack.md ⭐ START HERE (visual + explanation)
    ├── 01-why-three-tiers.md (system design: why separate strategy, approval, execution)
    └── 02-tier-scaling.md (SMB → Enterprise growth)
```

**Complete workflow walkthrough:**
- See [docs/workflow.md](../workflow.md) for the Smart Sleep Device product launch example
- Shows all 6 stages with under-the-hood orchestration, context flow, and decision loops

---

## How to Use This Showcase

### For SMB Founders (0–50M Revenue)

**Your question:** "How does this system work? What's the under-the-hood orchestration?"

**Read this path:**
1. `architecture-overview/00-three-tier-stack.md` (5 min) — Understand the three-tier system
2. [docs/workflow.md](../workflow.md) — Smart Sleep Device walkthrough (15 min) — See how all 6 stages work with full context flow
3. `architecture-overview/02-tier-scaling.md` (10 min) — How this scales as you grow

---

### For Enterprise VP Marketing (100M+ Revenue)

**Your question:** "Can this scale? How do we govern it?"

**Read this path:**
1. `architecture-overview/00-three-tier-stack.md` (5 min) — Understand the system
2. `architecture-overview/01-why-three-tiers.md` (5 min) — System architecture: why three tiers matter
3. `architecture-overview/02-tier-scaling.md` (10 min) — SMB → Enterprise scaling comparison
4. [docs/workflow.md](../workflow.md) (15 min) — Smart Sleep Device example showing orchestration + context preservation

---

## The Six-Stage Framework Explained

The six stages form a continuous workflow where each stage's output feeds the next:

| Stage | What | Where to See It |
|-------|------|-----------------|
| **1. Brief** | Strategic direction + product focus | [docs/workflow.md](../workflow.md) — Smart Sleep Device Brief section |
| **2. Voice** | Brand tone + messaging pillars | [docs/workflow.md](../workflow.md) — Smart Sleep Device Brand Voice section |
| **3. Research** | Audience insights + market gaps | [docs/workflow.md](../workflow.md) — Shows how research reveals positioning gap |
| **4. Strategy** | Channel + format + positioning | [docs/workflow.md](../workflow.md) — Decision loop: research reshapes strategy |
| **5. Content** | Captions + design specs | [docs/workflow.md](../workflow.md) — Content inherits all previous context |
| **6. Reports** | Performance data + optimization | [docs/workflow.md](../workflow.md) — Projections based on all 5 previous stages |

**Key insight:** Each stage inherits context from all previous stages. Stage 5 content automatically knows about Stage 2 voice, Stage 3 research findings, and Stage 4 strategic decisions.

---

## The Approval Gates (Claude Desktop Cowork)

**Critical feature:** Human-AI collaboration, not AI-alone execution

Every stage 2 output (voice guide, strategy, content) gets reviewed by the team in Claude Desktop Cowork:
- ✅ Stage 1 Brief → Team reviews in Cowork → Approves or refines
- ✅ Stage 2 Outputs → Team reviews in Cowork → Approves or refines
- ✅ Stage 4 Strategy → Team reviews in Cowork → Approves or refines

Only after Tier 2 approval does Tier 3 (execution) happen.

**Why this matters:** Humans stay in control. AI assists, humans decide.

---

## Three-Tier Architecture at a Glance

```
┌──────────────────────────────────────────────────┐
│ TIER 1: STRATEGIC INTELLIGENCE (Consultant)     │
│ Claude Code + MCP + Custom Skills                │
│ Output: Briefs, strategies, guidelines           │
└─────────────────────┬──────────────────────────┘
                      ↓
┌──────────────────────────────────────────────────┐
│ TIER 2: WORKFLOW OUTPUTS + COLLABORATION        │
│ 6-Stage Framework + Claude Desktop Cowork        │
│ Team reviews & approves each stage              │
│ Output: Approved content playbook               │
└─────────────────────┬──────────────────────────┘
                      ↓
┌──────────────────────────────────────────────────┐
│ TIER 3: TEAM EXECUTION (Your Team)              │
│ Canva, CapCut, Spreadsheets, Schedulers         │
│ Output: Delivered campaigns, posts, reports     │
└──────────────────────────────────────────────────┘
```

---

## Complete Workflow Example

For a detailed walkthrough showing all 6 stages with the **under-the-hood processes**, see [docs/workflow.md](../workflow.md):

**Smart Sleep Device Product Launch example includes:**
- How `/brainstorming` skill orchestrates thinking at each stage
- How research findings reshape strategy decisions (decision loop)
- How context flows automatically from Stage 3 research → Stage 4 strategy → Stage 5 content
- Cost comparison: System (40 min + approval) vs Agency (2-3 weeks, $6-10K)
- Why this eliminates the need to hire agency consultants

---

## Key Files to Understand the System

### If you have 5 minutes:
- `architecture-overview/00-three-tier-stack.md` — Visual + explanation of the system

### If you have 15 minutes:
- `architecture-overview/00-three-tier-stack.md`
- Skim [docs/workflow.md](../workflow.md) Smart Sleep Device section

### If you have 30 minutes:
- Read everything in `architecture-overview/`
- Read [docs/workflow.md](../workflow.md) Smart Sleep Device example (complete walkthrough)

### If you have 1 hour:
- Read entire `architecture-overview/` folder
- Read entire [docs/workflow.md](../workflow.md)
- You'll understand the full system, see it applied end-to-end, and understand the under-the-hood orchestration

---

## Questions?

Start with [docs/workflow.md](../workflow.md) for the complete Smart Sleep Device walkthrough showing all 6 stages, under-the-hood orchestration, context flow, and cost comparison with agencies.

---

## Document Dates & Versions

- **Showcase redesigned:** 2026-05-25 (MYT)
- **Last updated:** [see git history]
- **Current focus:** ARCHITECTURE and PROCESSES, not just outputs
- **Example:** Smart Sleep Device product launch (shows decision loops, context inheritance, skill orchestration)

---

**This is the system. This is how it works. Read docs/workflow.md to see it in action.**
