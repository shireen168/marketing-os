# Available Skills and Agents

Marketing OS gives you access to 40+ specialized agents built into Claude Code, gstack, and Anthropic's skills ecosystem. Use them across any workflow.

---

## gstack Workflow Agents (22 agents)

Source: [garrytan/gstack](https://github.com/garrytan/gstack)

| Skill | Your Specialist | What They Do |
|-------|-----------------|--------------|
| `/office-hours` | YC Office Hours | Start here. Six forcing questions that reframe your product before you write code. |
| `/plan-ceo-review` | CEO / Founder | Rethink the problem and find hidden product opportunities. Four modes: Expansion, Selective Expansion, Hold Scope, Reduction. |
| `/plan-eng-review` | Eng Manager | Lock in architecture, data flow, diagrams, edge cases, and tests. |
| `/plan-design-review` | Senior Designer | Rates design dimensions 0-10, explains what excellence looks like, edits plans accordingly. |
| `/plan-devex-review` | Developer Experience Lead | Interactive DX review exploring personas, benchmarks, friction points. Three modes: DX EXPANSION, DX POLISH, DX TRIAGE. |
| `/design-consultation` | Design Partner | Build complete design systems from scratch with landscape research and mockups. |
| `/review` | Staff Engineer | Find production bugs that pass CI, auto-fix obvious ones, flag gaps. |
| `/investigate` | Debugger | Systematic root-cause analysis with hypothesis testing and data flow tracing. |
| `/design-review` | Designer Who Codes | Same audit as planning stage, then implements fixes with atomic commits. |
| `/devex-review` | DX Tester | Live developer experience testing: navigates docs, times setup, screenshots errors. |
| `/design-shotgun` | Design Explorer | Generates 4-6 mockup variants, opens comparison board, learns your taste preferences. |
| `/design-html` | Design Engineer | Converts mockups into production HTML with dynamic layouts and framework detection. |
| `/qa` | QA Lead | Test apps, find bugs, fix with atomic commits, generate regression tests. |
| `/qa-only` | QA Reporter | Reports bugs without code changes. |
| `/cso` | Chief Security Officer | OWASP Top 10 + STRIDE threat model. Zero-noise: 17 false positive exclusions. |
| `/ship` | Release Engineer | Sync main, run tests, audit coverage, push, open PR. |
| `/land-and-deploy` | Release Engineer | Merge PR, wait for CI, deploy, verify production health. |
| `/canary` | SRE | Post-deploy monitoring for console errors and performance regressions. |
| `/benchmark` | Performance Engineer | Baseline page load times and Core Web Vitals before/after comparisons. |
| `/document-release` | Technical Writer | Update project documentation to match shipped changes. |
| `/retro` | Eng Manager | Weekly retrospective with per-person breakdowns and shipping trends. |
| `/browse` | QA Engineer | Real Chromium browser access with clicks and screenshots (~100ms per command). |

---

## Anthropic Native Skills (17 skills)

These skills extend Claude Code with native capabilities:

| Skill | Category | Purpose |
|-------|----------|---------|
| `brand-guidelines` | Content | Brand identity, tone, messaging pillars, visual guidelines |
| `frontend-design` | Design | Frontend components, design patterns, UI libraries |
| `canvas-design` | Design | Canvas-based design and visualization tools |
| `internal-comms` | Content | Internal communications templates and workflows |
| `doc-coauthoring` | Documents | Document co-authoring and real-time collaboration |
| `docx` | Documents | Microsoft Word (.docx) file manipulation |
| `pdf` | Documents | PDF generation, parsing, and manipulation |
| `pptx` | Documents | PowerPoint (.pptx) presentation creation |
| `xlsx` | Documents | Excel (.xlsx) spreadsheet handling |
| `web-artifacts-builder` | Development | Build interactive web components and artifacts |
| `webapp-testing` | Testing | Web application testing and validation |
| `claude-api` | Integration | Claude API integration and usage patterns |
| `mcp-builder` | Development | Model Context Protocol builder for custom integrations |
| `skill-creator` | Development | Tools for creating new custom skills |
| `theme-factory` | Design | Theme generation and customization |
| `algorithmic-art` | Content | Algorithmic and generative art creation |
| `slack-gif-creator` | Integration | Create GIFs for Slack and social media |

---

## Marketing OS Custom Agents

| Agent | Purpose |
|-------|---------|
| `brainstorm` | Marketing brief and brand voice creation |
| `research` | Market sizing, competitor analysis, trend research |
| `strategy` | Positioning, messaging hierarchy, channel selection |
| `content-gen` | Platform-specific content drafts (6 channels) |
| `reporting` | Campaign metrics, ROI projections, performance analysis |

---

## How to Use These Agents

### In the Marketing Workflow

The 6-stage marketing workflow uses agents automatically:

```
Stage 1: Brief          → brainstorm agent
Stage 2: Brand Voice    → brand-guidelines agent
Stage 3: Research       → market research agent
Stage 4: Strategy       → strategy + positioning agent
Stage 5: Content        → content generation agent
Stage 6: Reports        → analytics + ROI agent
```

### Extending Beyond Marketing

Use any of the 40+ agents to build workflows for:

- **HR recruiting**: `/office-hours` for job description, `/design-html` for career page, `/content-gen` for job posts
- **Legal briefs**: `/investigate` for case research, `/document-release` for brief templates, `/cso` for compliance review
- **Sales campaigns**: `/brainstorm` for pitch decks, `/pptx` for proposals, `/content-gen` for outreach sequences
- **Product launches**: `/plan-eng-review` for tech, `/design-consultation` for launch visuals, `/content-gen` for announcement
- **Internal comms**: `/internal-comms` for tone, `/pptx` for all-hands decks, `/content-gen` for emails

---

## Build Your Own Custom Skills

The agents above are the starting point. You can build custom skills for:

- **Domain-specific workflows**: Finance forecasting, legal research, HR analytics
- **Company-specific tools**: Brand enforcement, compliance checking, product-specific templates
- **Industry templates**: Healthcare workflows, fintech compliance, SaaS customer success
- **Integration**: Slack bots, Zapier automation, Jira workflow integration

Use `/mcp-builder` or `/skill-creator` to build new agents that plug into the system.

---

## Total Agent Count

- gstack workflow agents: 22
- Anthropic native skills: 17
- Marketing OS custom agents: 5
- **Total built-in: 44 agents**

Plus unlimited custom agents you build yourself.

---

## Recommendation

Start with the 6-stage marketing workflow (uses 5 agents). When ready, explore agents in `/office-hours` for product decisions, `/design-consultation` for visual work, or `/ship` for deployment automation.

**The point:** You're not choosing between tools. You're choosing a system where every agent compounds with every other agent because they all share context.
