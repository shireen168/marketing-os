# FAQ

## Will our team actually use this?

- Yes, because it's designed for non-technical teams to actively participate.
- **Tier 1 (Orchestration):** One person types `/orchestration [product]` and the system runs 8 phases automatically (~1-2 weeks for full product launch)
- **Tier 2 (Approvals):** Your team reviews each phase output. Team members can revise scope, request changes, approve findings. Revision loops let you refine without restarting.
- **Tier 3 (Execution):** Non-technical teams implement the approved strategy using simple tools
- Everyone sees context preserved automatically across all 8 phases
- Adoption compounds:
  - Day 1 → Complete Phase 1 (market research)
  - Week 1 → Complete Phases 1-3 (research, strategy, design)
  - 2 weeks → Full product launch orchestrated (all 8 phases)

---

## Is this just a product launch tool?

No. The 8-phase pattern works for any complex, multi-stage workflow where each phase builds on previous decisions.

- **Product Launches:** Research → Strategy → Design → Build → Testing → Launch → Growth → Operations
- **Organizational Change:** Planning → Design → Communication → Training → Rollout → Adoption → Optimization → Learning
- **Real Estate Development:** Site Analysis → Architecture → Permitting → Construction → QA → Launch → Growth → Operations

Same 8-phase pattern. Same checkpoint preservation. Different domain. Currently optimized for product launches, but expandable to any domain with similar phase structure.

---

## How does governance work? Who approves what?

This system is designed so your team stays in control at decision points:

| Tier | Who | Stage | What they do |
|------|-----|-------|--------------|
| Tier 1 (Claude Code) | Strategic thinker | Stages 1-6 | Produces drafts at speed |
| Tier 2 (Claude Code) | Brand/marketing lead, CFO, product lead | Stage 2 (Brand Voice), Stage 4 (Strategy), Stage 6 (Reports) | Reviews tone and persona, validates messaging and budget, approves learnings for next cycle |
| Tier 3 (Execution) | Execution team | Post-approval | Publishes once the team approves. No surprises, no re-work. |

Outputs are structured markdown files. All stakeholders can review them in Claude Code or any editor, discuss changes in conversation, and approve before execution.

---

## What if we already have processes?

No issue, keep them. This system doesn't replace the current workflow, it's structured so nothing falls through the cracks.

If the team already brief products, research markets, and write strategy, this system makes that work 5-10x faster by:
- Automating context switching between stages
- Making decisions visible (every stage documents its choices)
- Enabling team members to pick up campaigns mid-stream (full context preserved)

---

## How is this different from hiring an agency that uses Claude Code?

Four key differences:

| Dimension | Agency | This System |
|-----------|--------|-------------|
| Speed | 2-3 weeks (scope, draft, revisions, final) | 4-8 hours strategic work + 1-2 days team review + execution |
| Cost | $20-30K per campaign | 4-8 hours of one person's time. Setup once, run unlimited campaigns. |
| Control | Delivers final copy | Team reviews and refines at Stages 2, 4, 6 in Claude Code before anything ships |
| Learning | Delivers outputs | Teaches your team to think in workflows. After 3 campaigns, your team owns the process. |

---

## What if we want to adapt this to our specific workflow?

Build custom skills using `/skill-creator`. The system is extensible.

Examples:
- Add a "Compliance Review" stage between Strategy and Content
- Insert an "Approval Gate" before publishing
- Integrate with your CRM to auto-populate brief data
- Connect to your Slack for notifications

Customization extends the base system without breaking core workflows.

---

## Do we need Claude Pro?

No. Claude free works, Claude Pro is faster. You need:
- Claude account (free or Pro)
- VS Code (free)
- This repo (free)
- 15 minutes setup time

That's it.

---

## What's the learning curve?

| Timeframe | Milestone |
|-----------|-----------|
| Day 1 | Clone repo, run setup, watch onboarding. Ship your first campaign by end of day. |
| Week 1 | Your team runs 3-5 campaigns independently. Workflow becomes second nature. |
| Month 1 | Your team is faster than agencies, and they own the process. |

The system teaches as you use it. Each campaign reinforces the workflow.

---

## Why not just use ChatGPT/Gemini/Deepseek/other LLMs directly?

You could. You'd rebuild:
- Context management (tracking what each stage decided)
- Workflow orchestration (which stages run in which order)
- Agent coordination (40+ agents working together)
- Error handling (what happens when a stage fails)
- Team memory (making sure every team member sees the same decisions)

That's 2-3 months of engineering. We've done it. You don't have to.

---

## Is this open source?

Yes. MIT license. Free to fork, modify, extend, redistribute. Build on it.

---

## Who built this?

- A team that shipped 50+ marketing campaigns in 6 months using Claude Code + manual workflows
- Observed a repeating pattern: Brief → Voice → Research → Strategy → Content → Reports (marketing campaign execution)
- Abstracted to a universal framework: 8-phase product orchestration that works for campaigns, products, services, internal programs
- Core insight: context must flow through all stages without reset. Built automation to preserve context end-to-end.

**This is a powerful system:**
1. Universal framework (8 phases for any offering)
2. Context-preserving (no data loss between stages)
3. Application-specific workflows (campaign execution is one example)
4. Scalable-from-day-one (works for solo builders to distributed teams)
