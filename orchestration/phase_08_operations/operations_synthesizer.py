"""Operations & Learning Synthesizer for Phase 8 (Operations & Learning)."""

from typing import Any


class OperationsSynthesizer:
    """Synthesizes operations and learning reports from Phase 8 clarifications and subagent outputs."""

    def __init__(self):
        """Initialize the operations synthesizer."""
        self.phase = 8

    def synthesize(
        self,
        product_name: str,
        clarifying_answers: dict[str, str],
        subagent_outputs: dict[str, Any] | None = None
    ) -> str:
        """
        Synthesize a comprehensive operations and learning report.

        Args:
            product_name: Name of the product
            clarifying_answers: Answers from Phase 8 clarifying questions
            subagent_outputs: Outputs from 4 operations/learning skills

        Returns:
            Markdown-formatted operations and learning report document
        """
        if not product_name:
            return ""

        subagent_outputs = subagent_outputs or {}

        # Extract key retrospective parameters
        wins = clarifying_answers.get("wins", "")
        challenges = clarifying_answers.get("challenges", "")
        improvements = clarifying_answers.get("improvements", "")
        documentation = clarifying_answers.get("documentation", "")
        skill_gaps = clarifying_answers.get("skill_gaps", "")
        vision = clarifying_answers.get("vision", "")

        # Build comprehensive operations report
        lines = []
        lines.append("# Operations & Learning Report")
        lines.append("")
        lines.append(f"Product: {product_name}")
        lines.append("")

        # Launch Retrospective
        lines.append("## Launch Retrospective")
        lines.append("")
        if wins:
            lines.append("### What Went Well 🎉")
            lines.append(wins)
            lines.append("")

        if challenges:
            lines.append("### Challenges & Lessons Learned 📚")
            lines.append(challenges)
            lines.append("")

        if improvements:
            lines.append("### What We'd Do Differently 🔄")
            lines.append(improvements)
            lines.append("")

        lines.append("### Key Metrics vs Targets")
        lines.append("- Launch timeline: [Compare actual vs planned]")
        lines.append("- Launch day traffic: [Website visitors, signups]")
        lines.append("- Content performance: [Top performing pieces, engagement rates]")
        lines.append("- Paid advertising: [ROAS, CAC, conversion rates]")
        lines.append("- Social reach: [Impressions, engagement, follower growth]")
        lines.append("")

        # Operational Health
        lines.append("## Operational Health")
        lines.append("")
        lines.append("### System Performance")
        lines.append("- Uptime: [% uptime, incident count]")
        lines.append("- Performance: [p95 latency, throughput, error rate]")
        lines.append("- Scalability: [Max concurrent users handled, peak load]")
        lines.append("- Disaster recovery: [RTO, RPO achieved vs targets]")
        lines.append("")

        lines.append("### Customer Satisfaction")
        lines.append("- NPS score: [Current score, target, benchmark]")
        lines.append("- CSAT: [Customer satisfaction rating]")
        lines.append("- Support tickets: [Volume, resolution time, sentiment]")
        lines.append("- Churn rate: [% customers lost, main reasons]")
        lines.append("")

        lines.append("### Team Health")
        lines.append("- Team satisfaction: [Internal NPS, eNPS score]")
        lines.append("- Retention: [Team member turnover, critical roles]")
        lines.append("- Morale: [Post-launch team feedback, burnout assessment]")
        lines.append("- Collaboration: [Cross-team effectiveness, communication]")
        lines.append("")

        lines.append("### Financial Performance")
        lines.append("- Revenue generated: [MRR, ARR achieved in first 30 days]")
        lines.append("- Operating costs: [COGS, infrastructure, operations]")
        lines.append("- Profitability: [Gross margin, path to profitability]")
        lines.append("- Unit economics: [CAC, LTV, payback period]")
        lines.append("")

        # Process Documentation
        lines.append("## Process Documentation")
        lines.append("")
        if documentation:
            lines.append("### Required Documentation")
            lines.append(documentation)
            lines.append("")

        lines.append("### Launch Process Documentation")
        lines.append("- Pre-launch checklist: Exact steps and timeline")
        lines.append("- Day-of coordination: Communication channels, escalation")
        lines.append("- Monitoring: Alerts and response procedures")
        lines.append("- Rollback procedure: How to quickly revert if needed")
        lines.append("")

        lines.append("### Operational Runbooks")
        lines.append("- Daily tasks: Monitoring, support triage, incident response")
        lines.append("- Weekly tasks: Reporting, metrics review, optimization")
        lines.append("- Monthly tasks: Planning, retrospectives, strategy review")
        lines.append("- Quarterly tasks: Goal setting, resource planning, roadmap")
        lines.append("")

        lines.append("### Decision Log")
        lines.append("- Major technical decisions: Architecture choices, tech stack")
        lines.append("- Product decisions: Feature prioritization, positioning")
        lines.append("- Commercial decisions: Pricing, target market, go-to-market")
        lines.append("- Operational decisions: Team structure, process changes")
        lines.append("- Rationale: Why each decision was made, tradeoffs considered")
        lines.append("")

        lines.append("### Knowledge Base")
        lines.append("- System architecture: Diagrams, component descriptions")
        lines.append("- API documentation: Endpoints, authentication, error codes")
        lines.append("- Database schema: Tables, relationships, migration history")
        lines.append("- Infrastructure setup: AWS configurations, CI/CD pipeline")
        lines.append("- Third-party integrations: APIs, credentials, troubleshooting")
        lines.append("")

        # Team Development
        lines.append("## Team Development")
        lines.append("")
        if skill_gaps:
            lines.append("### Skills Developed & Gaps")
            lines.append(skill_gaps)
            lines.append("")

        lines.append("### Team Capabilities Assessment")
        lines.append("- Frontend development: [Proficiency level, gaps]")
        lines.append("- Backend development: [Proficiency level, gaps]")
        lines.append("- DevOps/Infrastructure: [Proficiency level, gaps]")
        lines.append("- Product management: [Proficiency level, gaps]")
        lines.append("- Marketing/Growth: [Proficiency level, gaps]")
        lines.append("")

        lines.append("### Training & Upskilling Plan")
        lines.append("- Critical skills: Areas requiring immediate training")
        lines.append("- Courses/certifications: Recommended programs")
        lines.append("- Mentorship: Pairing junior with senior engineers")
        lines.append("- Knowledge sharing: Regular tech talks and documentation")
        lines.append("")

        lines.append("### Hiring Plan for Phase 2")
        lines.append("- Immediate hires: Roles needed to unblock growth")
        lines.append("- 3-month plan: Team composition for 2x user growth")
        lines.append("- 12-month plan: Full team structure for sustainable growth")
        lines.append("- Hiring budget: [Budget allocation for recruiting]")
        lines.append("")

        # Financial Summary
        lines.append("## Financial Summary")
        lines.append("")
        lines.append("### Total Cost Analysis")
        lines.append("- Development costs: [Engineering salary, contractors, tools]")
        lines.append("- Infrastructure: [Cloud services, hosting, databases]")
        lines.append("- Marketing: [Ads, content creation, PR]")
        lines.append("- Operations: [Support, tools, overhead]")
        lines.append("- Total burn: [Total cost to launch]")
        lines.append("")

        lines.append("### Revenue Generation")
        lines.append("- MRR at launch: [Baseline recurring revenue]")
        lines.append("- ARR projection: [Annualized recurring revenue]")
        lines.append("- Total customers: [Number of paying customers]")
        lines.append("- ARPU: [Average revenue per user]")
        lines.append("")

        lines.append("### Path to Profitability")
        lines.append("- Current burn rate: [Monthly cash burn]")
        lines.append("- Runway: [Months until profitability/next funding]")
        lines.append("- Break-even analysis: [Customer count/MRR needed]")
        lines.append("- Unit economics: [LTV/CAC ratio, payback period]")
        lines.append("- Profitability timeline: [Months to profitability]")
        lines.append("")

        # Next Phase Planning
        lines.append("## Next Phase Planning")
        lines.append("")
        if vision:
            lines.append("### Vision for Phase 2 or Next Product")
            lines.append(vision)
            lines.append("")

        lines.append("### Strategic Roadmap (6-12 months)")
        lines.append("- Q1 goals: [Key initiatives and metrics]")
        lines.append("- Q2 goals: [Key initiatives and metrics]")
        lines.append("- Q3 goals: [Key initiatives and metrics]")
        lines.append("- Q4 goals: [Key initiatives and metrics]")
        lines.append("")

        lines.append("### Product Roadmap")
        lines.append("- New features: [Top feature requests from customers]")
        lines.append("- Improvements: [Optimization opportunities identified]")
        lines.append("- New markets: [Geographic expansion, new use cases]")
        lines.append("- Integrations: [Third-party platforms to integrate]")
        lines.append("")

        lines.append("### Team Expansion")
        lines.append("- Current team: [Size and composition]")
        lines.append("- Target team: [Size and roles for Q2/Q3]")
        lines.append("- Hiring priorities: [Most critical roles to fill]")
        lines.append("- Organizational structure: [New departments or teams]")
        lines.append("")

        lines.append("### Investment Needs")
        lines.append("- Runway estimate: [Months of cash remaining]")
        lines.append("- Next funding round: [Seed? Series A? Amount needed?]")
        lines.append("- Use of capital: [Breakdown of spending by category]")
        lines.append("- Growth targets: [Revenue/user growth milestones]")
        lines.append("")

        # Continuous Improvement
        lines.append("## Continuous Improvement Framework")
        lines.append("")
        lines.append("### Process Improvements")
        lines.append("- Development process: [Agile, sprints, release cadence]")
        lines.append("- Deployment: [CI/CD improvements, deployment frequency]")
        lines.append("- Quality: [Testing strategy, code review process]")
        lines.append("- Communication: [Team coordination, cross-functional alignment]")
        lines.append("")

        lines.append("### Automation Opportunities")
        lines.append("- Testing: [Increase test automation coverage]")
        lines.append("- Deployment: [Automated rollout and rollback]")
        lines.append("- Monitoring: [Automated alerts and incident response]")
        lines.append("- Reporting: [Automated metrics and dashboards]")
        lines.append("")

        lines.append("### Scaling Challenges & Solutions")
        lines.append("- Database scaling: [Sharding, read replicas strategy]")
        lines.append("- Cache strategy: [Redis, CDN optimization]")
        lines.append("- Team scaling: [Org structure for 2x/10x growth]")
        lines.append("- Customer support: [Automation, knowledge base, tier support]")
        lines.append("")

        lines.append("### Risk Mitigation")
        lines.append("- Technical risks: [Vendor lock-in, architecture changes needed]")
        lines.append("- Market risks: [Competitive threats, market shifts]")
        lines.append("- Financial risks: [Runway, burn rate, fundraising]")
        lines.append("- Operational risks: [Key person dependency, turnover]")
        lines.append("")

        lines.append("## Key Takeaways")
        lines.append("")
        lines.append(f"The {product_name} launch demonstrated:")
        lines.append("- [Key strength 1]")
        lines.append("- [Key strength 2]")
        lines.append("- [Key learning 1]")
        lines.append("- [Key learning 2]")
        lines.append("")
        lines.append("For Phase 2, we will focus on:")
        lines.append("- [Priority 1]")
        lines.append("- [Priority 2]")
        lines.append("- [Priority 3]")

        return "\n".join(lines)
