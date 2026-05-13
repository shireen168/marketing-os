# Available Skills and Agents

Marketing OS gives you access to 40+ specialized agents built into Claude Code, gstack, and Anthropic's skills ecosystem. Use them across any workflow.

---

## gstack Workflow Agents (23 agents)

| Agent | Category | Purpose |
|-------|----------|---------|
| `/office-hours` | Planning | Product validation with forcing questions before commitment |
| `/plan-ceo-review` | Planning | Strategic scope decisions (expansion, hold, reduction modes) |
| `/plan-eng-review` | Planning | Architecture review, data flow, edge cases, test coverage |
| `/plan-design-review` | Planning | Design system auditing with 0-10 structural ratings |
| `/plan-devex-review` | Planning | Developer experience audit with friction point analysis |
| `/design-consultation` | Design | Complete design system creation from research to mockups |
| `/design-shotgun` | Design | Generate 4-6 visual mockup variants with taste learning |
| `/design-html` | Design | Convert mockups to production-ready HTML with dynamic layouts |
| `/design-review` | Design | Live design audit with automatic fixes and atomic commits |
| `/review` | Code | Production bug detection with auto-fixes for obvious issues |
| `/investigate` | Code | Systematic root-cause debugging methodology |
| `/devex-review` | Code | Live developer onboarding audit with timing metrics |
| `/qa` | Testing | Browser-based testing with bug fixes and regression detection |
| `/qa-only` | Testing | Bug reporting without code changes |
| `/ship` | Deployment | Test running, coverage audit, and PR opening |
| `/land-and-deploy` | Deployment | PR merging, CI wait, production deploy, health verification |
| `/canary` | Monitoring | Post-deploy monitoring for errors and performance regressions |
| `/benchmark` | Performance | Performance baseline comparison before/after changes |
| `/document-release` | Documentation | Automatic documentation updates matching shipped code |
| `/retro` | Collaboration | Weekly retrospective with per-person breakdown and streaks |
| `/pair-agent` | Collaboration | Cross-agent browser coordination with security scoping |
| `/cso` | Security | Security auditing: OWASP Top 10 + STRIDE threat modeling |
| `/browse` | Tools | Real Chromium browser control with screenshots and interaction |

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

- gstack workflow agents: 23
- Anthropic native skills: 17
- Marketing OS custom agents: 5
- **Total built-in: 45 agents**

Plus unlimited custom agents you build yourself.

---

## Recommendation

Start with the 6-stage marketing workflow (uses 5 agents). When ready, explore agents in `/office-hours` for product decisions, `/design-consultation` for visual work, or `/ship` for deployment automation.

**The point:** You're not choosing between tools. You're choosing a system where every agent compounds with every other agent because they all share context.
