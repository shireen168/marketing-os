# Marketing-OS Skills Reference

Complete inventory of all 13,14 skills organized by layer. Use this table to find the right skill for your task.

## How to Use This Reference

1. **Find your goal** in the left column
2. **Find the skill** that matches
3. **Trigger it** using the invocation syntax (e.g., `/market-research`)
4. **Reference the SKILL.md** file for templates and examples

## Skills by Layer

### Layer 1: Strategic Discovery
Understand your market, competitors, audience, and brand positioning.

| Skill | Purpose | Trigger/Invocation | Example Use Case | SKILL.md |
|-------|---------|-------------------|------------------|----------|
| Market Research | Industry landscape, trends, competitor analysis | `/market-research` | "What's the current landscape for sustainable coffee brands?" | [1-strategic-discovery/market-research/SKILL.md](../../.claude/skills/content-and-marketing/1-strategic-discovery/market-research/SKILL.md) |
| Competitive Ads Extractor | Competitor positioning, ad copy, market gaps | `/competitive-ads-extractor` | "What ads are competing SaaS companies running right now?" | [1-strategic-discovery/competitive-ads-extractor/SKILL.md](../../.claude/skills/content-and-marketing/1-strategic-discovery/competitive-ads-extractor/SKILL.md) |
| Audience Research | Buyer personas, content preferences, engagement patterns | `/audience-research` | "Who is buying eco-friendly home products? Where are they?" | [1-strategic-discovery/audience-research/SKILL.md](../../.claude/skills/content-and-marketing/1-strategic-discovery/audience-research/SKILL.md) |
| Brand Guidelines | Brand identity, voice, positioning, unique differentiators | `/brand-guidelines` | "Document what makes our brand unique vs. competitors" | [1-strategic-discovery/brand-guidelines/SKILL.md](../../.claude/skills/content-and-marketing/1-strategic-discovery/brand-guidelines/SKILL.md) |

### Layer 2: Creative Planning
Turn insights into content strategy and campaigns.

| Skill | Purpose | Trigger/Invocation | Example Use Case | SKILL.md |
|-------|---------|-------------------|------------------|----------|
| Campaign Plan | Structured campaign brief with goals, timeline, KPIs | `/campaign-plan` | "Build a 4-week campaign to launch a new product" | [2-creative-planning/campaign-plan/SKILL.md](../../.claude/skills/content-and-marketing/2-creative-planning/campaign-plan/SKILL.md) |
| Content Calendar Strategy | Plan 1,4 weeks of content by format, product, angle | `/content-calendar-strategy` | "Create a 2-week content plan for Instagram and TikTok" | [2-creative-planning/content-calendar-strategy/SKILL.md](../../.claude/skills/content-and-marketing/2-creative-planning/content-calendar-strategy/SKILL.md) |
| Brand Voice | Extract and document brand voice, apply to copy | `/brand-voice` | "Create a voice guide for our marketing team to follow" | [2-creative-planning/brand-voice/SKILL.md](../../.claude/skills/content-and-marketing/2-creative-planning/brand-voice/SKILL.md) |
| Copy Gen | Generate marketing copy for ads, email, social, landing pages | `/copy-gen` | "Write 5 ad variations for a Facebook campaign" | [2-creative-planning/copy-gen/SKILL.md](../../.claude/skills/content-and-marketing/2-creative-planning/copy-gen/SKILL.md) |

### Layer 3: Execution
Produce and distribute content at scale.

| Skill | Purpose | Trigger/Invocation | Example Use Case | SKILL.md |
|-------|---------|-------------------|------------------|----------|
| Video Gen | Generate UGC video scripts (30,60 second reels) | `/video-gen` | "Write a TikTok script for a new product demo" | [3-execution/video-gen/SKILL.md](../../.claude/skills/content-and-marketing/3-execution/video-gen/SKILL.md) |
| Video Editing | Edit, add bilingual overlays, optimize for platform | `/video-editing` | "Edit a video with Mandarin/English overlays for Instagram" | [3-execution/video-editing/SKILL.md](../../.claude/skills/content-and-marketing/3-execution/video-editing/SKILL.md) |
| Email/SMS | Build nurture sequences and promotional emails | `/email-sms` | "Create a 3-email onboarding sequence for new customers" | [3-execution/email-sms/SKILL.md](../../.claude/skills/content-and-marketing/3-execution/email-sms/SKILL.md) |
| Social Scheduling | Schedule posts across Facebook, Instagram, TikTok, LinkedIn | `/social-scheduling` | "Schedule 2 weeks of posts to Instagram and TikTok" | [3-execution/social-scheduling/SKILL.md](../../.claude/skills/content-and-marketing/3-execution/social-scheduling/SKILL.md) |
| LinkedIn Post | Platform-specific thought leadership content | `/linkedin-post` | "Write a LinkedIn article about marketing frameworks" | [3-execution/linkedin-post/SKILL.md](../../.claude/skills/content-and-marketing/3-execution/linkedin-post/SKILL.md) |
| Infographic | Create premium data visualizations and charts | `/infographic` | "Design an infographic showing before/after marketing results" | [3-execution/infographic/SKILL.md](../../.claude/skills/content-and-marketing/3-execution/infographic/SKILL.md) |
| Excalidraw Diagram | Create architecture and workflow diagrams | `/excalidraw-diagram` | "Draw a flowchart of our customer journey" | [3-execution/excalidraw-diagram/SKILL.md](../../.claude/skills/content-and-marketing/3-execution/excalidraw-diagram/SKILL.md) |
| Analytics | Track reach, engagement, ROI weekly | `/analytics` | "Generate a weekly dashboard of Instagram metrics" | [3-execution/analytics/SKILL.md](../../.claude/skills/content-and-marketing/3-execution/analytics/SKILL.md) |
| PDF Polisher | Format and brand marketing guides, pitch decks | `/pdf-polisher` | "Convert a marketing guide into a professional PDF" | [3-execution/pdf-polisher/SKILL.md](../../.claude/skills/content-and-marketing/3-execution/pdf-polisher/SKILL.md) |

### Layer 4: Optimization
Test, measure, and iterate on strategy.

| Skill | Purpose | Trigger/Invocation | Example Use Case | SKILL.md |
|-------|---------|-------------------|------------------|----------|
| A/B Testing | Plan and analyze multivariate tests for conversion | `/a-b-testing` | "Design an A/B test for email subject lines" | [4-optimization/a-b-testing/SKILL.md](../../.claude/skills/content-and-marketing/4-optimization/a-b-testing/SKILL.md) |

### Router & Orchestration

| Skill | Purpose | Trigger/Invocation | Example Use Case | SKILL.md |
|-------|---------|-------------------|------------------|----------|
| Market Router | Intelligent router that finds the right skill for your request | `/market` | "I want to understand my audience and their content preferences" | [router/SKILL.md](../../.claude/skills/content-and-marketing/router/SKILL.md) |

## Quick Lookup by Goal

### I want to understand my market
1. `/market-research` (Layer 1) - Understand landscape and trends
2. `/competitive-ads-extractor` (Layer 1) - See what competitors are doing
3. `/audience-research` (Layer 1) - Understand your buyers

### I want to plan content
1. `/campaign-plan` (Layer 2) - Create campaign brief
2. `/content-calendar-strategy` (Layer 2) - Plan specific weeks of content
3. `/copy-gen` (Layer 2) - Write the actual copy

### I want to execute and publish
1. `/video-gen` (Layer 3) - Write video scripts
2. `/social-scheduling` (Layer 3) - Schedule across platforms
3. `/email-sms` (Layer 3) - Build email sequences
4. `/analytics` (Layer 3) - Track performance

### I want to optimize and improve
1. `/analytics` (Layer 3) - Measure what's working
2. `/a-b-testing` (Layer 4) - Test variations
3. `/campaign-plan` (Layer 2) - Adjust strategy based on results

### I'm not sure which skill
Use `/market` (Router) to describe your goal and get routed to the right skill.

## Skill Dependencies

The 4 layers build on each other. For best results, follow this sequence:

```
1. Start with Layer 1 (Strategic Discovery)
   Use: market-research, competitive-ads-extractor, audience-research, brand-guidelines

2. Then Layer 2 (Creative Planning)
   Use: campaign-plan, content-calendar-strategy, brand-voice, copy-gen

3. Then Layer 3 (Execution)
   Use: video-gen, social-scheduling, email-sms, analytics, etc.

4. Then Layer 4 (Optimization)
   Use: a-b-testing, analytics again to measure improvements
```

You CAN skip layers or jump in mid-framework, but you'll get better results if you follow the sequence.

## Integration Patterns

### For Claude Code Users (Local Execution)
Each skill is a SKILL.md file in `.claude/skills/content-and-marketing/`

Trigger format: `/skill-name` (e.g., `/market-research`)

### For API/Custom Integration
Each SKILL.md contains:
- Input schema (what the skill accepts)
- Output schema (what the skill returns)
- Example invocations
- Integration patterns

## Extending the Framework

Want to add a new skill? Follow this pattern:

1. Determine which layer it belongs to (Strategic Discovery, Creative Planning, Execution, Optimization)
2. Create a new folder: `.claude/skills/content-and-marketing/[layer]/[skill-name]/`
3. Create SKILL.md with templates, examples, integration patterns
4. Update this reference with the new skill

## Questions?

- **How do I run a skill?** See [WORKFLOWS.md](WORKFLOWS.md)
- **How do I set up the framework?** See [CONFIGURATION.md](CONFIGURATION.md)
- **Where is the folder structure?** See [FOLDER-STRUCTURE.md](FOLDER-STRUCTURE.md)
- **What are real results?** See [../projects/sunny-homemade/CASE-STUDY.md](../../projects/sunny-homemade/CASE-STUDY.md)
