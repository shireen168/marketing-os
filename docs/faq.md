# FAQ

## Will our team actually use this?

- Yes, because it meets teams where they are. 
- Non-technical teams start with Claude Desktop chat (familiar UI). 
- Technical teams use VS Code with slash commands. 
- Everyone sees context preserved automatically. 
- Adoption compounds:
  - Day 1 → Ship a campaign
  - Week 1 → Ship 3-5 campaign
  - Month 1 → It has become the team's SOP

---

## Is this just a marketing tool?

No. The architecture works for any workflow that involves stages building on previous stages.

- Marketing: Brief → Brand Voice → Research → Strategy → Content → Reports
- HR: Job Description → Candidate Persona → Interview Questions → Offer Strategy
- Legal: Case Brief → Regulatory Research → Risk Analysis → Compliance Strategy
- Finance: Budget → Forecasting → Scenario Analysis → Board Report

Same 6-stage pattern. Same context preservation. Different domain. I built templates for marketing first, but the system is domain-agnostic.

---

## What if we already have processes?

No issue, keep them. This system doesn't replace the current workflow, it's structured so nothing falls through the cracks.

If the team already brief products, research markets, and write strategy, this system makes that work 5-10x faster by:
- Automating context switching between stages
- Making decisions visible (every stage documents its choices)
- Enabling team members to pick up campaigns mid-stream (full context preserved)

---

## How is this different from hiring an agency that uses Claude Code?

Three differences:

1. **Speed:**
   - Agencies take 3-5 days
   - This system: 40 minutes. You control the timeline

2. **Cost:**
   - Agency: $3-5K per campaign
   - This system: setup once, run 100 campaigns. Cost per campaign approaches zero

3. **Learning:**
   - Agencies deliver outputs
   - This system teaches your team how to think in workflows. After 3 campaigns, your team becomes expert in structuring work

---

## What if we want to adapt this to our specific workflow?

Build custom skills using `/skill-creator` or `/mcp-builder`. The system is extensible.

Examples:
- Add a "Compliance Review" stage between Strategy and Content
- Insert an "Approval Gate" before publishing
- Integrate with your CRM to auto-populate brief data
- Connect to your Slack for notifications

I can built for the team anytime.

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

- **Day 1:**
  - Clone repo, run setup, watch onboarding
  - By end of day, you ship your first campaign

- **Week 1:**
  - Your team runs 3-5 campaigns independently
  - Workflow becomes second nature

- **Month 1:**
  - Your team is faster than agencies, and they own the process

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
- We saw the pattern: same 6 stages, every time
- Same context lost between conversations. Built automation to preserve that context. Works.

**This is a powerful system:**
1. Workflow-first
2. Context-preserving
3. Scalable-from-day-one
