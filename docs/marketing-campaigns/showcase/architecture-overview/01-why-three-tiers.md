# Why Three Tiers? (System Architecture)

## The Core Problem

Marketing workflows typically fail in one of three ways:

1. **Strategy-execution disconnect:** Strategy is built by experts, then handed to a team that doesn't understand it or can't execute it consistently
2. **Loss of control:** AI generates outputs, team uses them without understanding or approving them (black-box problem)
3. **No scalability:** The person who builds the process becomes the bottleneck (doesn't scale with team growth)

Three-tier architecture solves all three.

---

## Tier 1: Strategic Intelligence (Claude Code)

**Purpose:** Build the marketing strategy using AI orchestration + custom infrastructure

**What it includes:**
- Claude Code running gstack skills (brainstorming, planning, research, strategy)
- MCP servers for data integration and context preservation
- Custom skills encoding domain expertise (marketing, CRO, copywriting, etc.)
- 6-stage workflow that preserves context across all stages

**Why separate from execution:**
- Strategy requires domain expertise, systems thinking, and access to decision-making logic
- Building strategy once scales to infinite executions
- Strategy can be audited, understood, and refined without touching execution
- Strategist can be expensive; executor can be cheap

**Who owns Tier 1:** Strategic thinker or consultant who builds the system

---

## Tier 2: Human-AI Collaboration (Claude Desktop Cowork)

**Purpose:** Approval gates where teams review and refine outputs before execution

**What it includes:**
- Claude Desktop Cowork conversations where team members can see all outputs
- Structured review points at Stages 2 (Voice), 4 (Strategy), 6 (Reports)
- Ability for non-technical team members to directly edit captions, adjust strategy, request changes
- Full context preservation across all approvals

**Why this matters:**
- AI generates outputs, but humans decide what ships
- Team stays in control at decision points (not just executing blindly)
- Approval gates catch misalignment before expensive execution (e.g., if tone is wrong, fix it in Cowork, not after 100 posts)
- Creates a governance trail (who approved what, when)
- Non-technical team members can participate without understanding gstack or Claude Code

**Who owns Tier 2:** Non-technical team members, decision-makers, brand leads, CFO (whoever needs to approve)

---

## Tier 3: Team Execution (Simple Tools)

**Purpose:** Publish, track, and iterate using straightforward no-code tools

**What it includes:**
- Content scheduling tools (native platform schedulers, Linktree, etc.)
- Design tools (Canva, Adobe, etc.)
- Tracking tools (spreadsheets, analytics platforms)
- No technical knowledge required

**Why separate from strategy:**
- Execution is mechanical once strategy is approved
- Non-experts can execute using a playbook
- Execution doesn't require understanding the system, only following steps
- Scales cheaply (hire 100 executors without hiring 100 strategists)
- Turnover in Tier 3 doesn't break Tier 1 (strategy persists)

**Who owns Tier 3:** Execution team (marketing operators, social media managers, etc.)

---

## How The Three Tiers Work Together

### Problem: Traditional Single-Tier Approach

```
Expert ← does everything → Outputs → Team executes (or fails)
```

Issues:
- Expert becomes bottleneck
- Expert must do strategy AND execution AND approval
- Scales linearly (add team, expert workload increases)
- Team doesn't understand decisions (can't adapt)
- No governance trail

### Solution: Three-Tier Separation

```
Tier 1: Expert builds strategy once (Claude Code)
   ↓
Tier 2: Team reviews and approves (Cowork)
   ↓
Tier 3: Team executes at scale (Simple tools)
```

Benefits:
- Expert workload is fixed (builds system once, not per campaign)
- Team understands decisions (visible in Cowork)
- Approvals are transparent (governance trail)
- Scales: 1 strategist → 1 team of 10 executors
- Non-experts can execute
- System is resilient (strategist leaves, system stays)

---

## Scaling Examples

### SMB: One Founder (All Three Tiers)

| Tier | Owner | Time | Output |
|------|-------|------|--------|
| 1 | Founder (strategic) | 45 min | Brief, Voice, Strategy, Content briefs |
| 2 | Founder (approval) | 30 min | Reviews own outputs, refines in Cowork |
| 3 | Founder (execution) | 2-3 hrs | Designs, schedules, publishes |

**Total:** One person, 4 hours per week, complete control

---

### Growth: 3-Person Team (Tiers Separate)

| Tier | Owner | Time | Output |
|------|-------|------|--------|
| 1 | Founder (strategy) | 45 min | Brief, Voice, Strategy, Content briefs |
| 2 | Marketing lead + founder | 30 min | Reviews in Cowork, refines copy |
| 3 | 2 Content operators | 4 hrs | Design, schedule, publish, track |

**Total:** 3 people, clear roles, founder can focus on strategy

---

### Enterprise: 100-Person Team (Full Separation)

| Tier | Owner | Time | Output |
|------|-------|------|--------|
| 1 | Strategy team (5 people) | 60 min | Brief, Voice, Research, Strategy |
| 2 | Approval committee (stakeholders) | 60 min | CMO reviews positioning, CFO reviews budget, legal reviews claims |
| 3 | 50+ executors | Parallel execution | Design, schedule, publish, track, optimize |

**Total:** 55+ people, parallel execution, clear governance, founder/CMO focuses on Tier 1 only

---

## Why This Matters

**Without three tiers:** Everything is tangled. Decision-making and execution are mixed. One person must understand both. Doesn't scale.

**With three tiers:** Each layer has a clear job. Strategists think. Teams approve. Executors do. Scales from 1 person to 1,000.

**The architecture is the system.** It's not about the specific tools (Claude Code, Cowork, Canva): it's about the separation of concerns that makes growth possible.
