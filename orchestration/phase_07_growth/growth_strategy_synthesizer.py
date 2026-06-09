"""Growth Strategy Synthesizer for Phase 7 (Growth & Optimization)."""

from typing import Any


class GrowthStrategySynthesizer:
    """Synthesizes growth and optimization strategies from Phase 7 clarifications and subagent outputs."""

    def __init__(self):
        """Initialize the growth strategy synthesizer."""
        self.phase = 7

    def synthesize(
        self,
        product_name: str,
        clarifying_answers: dict[str, str],
        subagent_outputs: dict[str, Any] | None = None
    ) -> str:
        """
        Synthesize a comprehensive growth and optimization strategy.

        Args:
            product_name: Name of the product
            clarifying_answers: Answers from Phase 7 clarifying questions
            subagent_outputs: Outputs from 6 growth/optimization skills

        Returns:
            Markdown-formatted growth strategy document
        """
        if not product_name:
            return ""

        subagent_outputs = subagent_outputs or {}

        # Extract key growth parameters
        growth_lever = clarifying_answers.get("growth_lever", "")
        retention_metrics = clarifying_answers.get("retention_metrics", "")
        expansion_ops = clarifying_answers.get("expansion_opportunities", "")
        feedback_loop = clarifying_answers.get("feedback_loop", "")
        analytics_reqs = clarifying_answers.get("analytics_requirements", "")
        team_budget = clarifying_answers.get("team_budget", "")

        # Build comprehensive growth strategy
        lines = []
        lines.append("# Growth & Optimization Strategy")
        lines.append("")
        lines.append(f"Product: {product_name}")
        lines.append("")

        # Customer Acquisition Section
        lines.append("## Customer Acquisition")
        lines.append("")
        if growth_lever:
            lines.append(f"### Primary Growth Lever")
            lines.append(f"{growth_lever}")
            lines.append("")

        lines.append("### Organic Growth Strategy")
        lines.append("- SEO optimization: Focus on high-intent keywords")
        lines.append("- Content marketing: 2-3 blog posts per week, SEO-optimized")
        lines.append("- Community building: Active participation in relevant forums/communities")
        lines.append("- Referral program: Incentivize existing customers to refer")
        lines.append("- Organic target: 30-40% of new customers from organic channels")
        lines.append("")

        lines.append("### Paid Acquisition Strategy")
        lines.append("- Google Ads: Search, Shopping, Display campaigns")
        lines.append("- LinkedIn Ads: B2B audience targeting")
        lines.append("- Facebook/Instagram: Interest-based, lookalike audiences")
        lines.append("- Target CAC: <$50 for self-serve, <$500 for enterprise")
        lines.append("- Payback period: <12 months for all segments")
        lines.append("")

        lines.append("### Partnership & Channel Strategy")
        lines.append("- Strategic partnerships: Complementary SaaS platforms")
        lines.append("- Reseller program: Commission-based distribution")
        lines.append("- Agency partnerships: Agencies recommending to clients")
        lines.append("- Partnership target: 20% of revenue within 12 months")
        lines.append("")

        # Retention Section
        lines.append("## Retention & Expansion")
        lines.append("")
        if retention_metrics:
            lines.append(f"### Key Retention Metrics")
            lines.append(f"{retention_metrics}")
            lines.append("")

        lines.append("### Customer Onboarding")
        lines.append("- Onboarding goals: 90% completion of core workflows in week 1")
        lines.append("- Structured tutorials: Step-by-step product walkthroughs")
        lines.append("- Personal support: Dedicated onboarding for enterprise customers")
        lines.append("- Activation milestones: Track progress toward 'aha moment'")
        lines.append("- NPS during onboarding: Target >50 for early adopters")
        lines.append("")

        lines.append("### Churn Prevention")
        lines.append("- Early warning system: Identify at-risk customers")
        lines.append("- Win-back campaigns: Re-engagement for inactive users")
        lines.append("- NPS-driven action: Reach out to detractors for feedback")
        lines.append("- Product improvements: Act on feature requests from churning users")
        lines.append("- Churn reduction target: 5% or less per month")
        lines.append("")

        lines.append("### Expansion Revenue")
        if expansion_ops:
            lines.append(f"### Expansion Opportunities")
            lines.append(f"{expansion_ops}")
            lines.append("")

        lines.append("- Upsell strategy: Higher-tier plans for power users")
        lines.append("- Cross-sell strategy: Complementary products/features")
        lines.append("- Enterprise upgrades: Custom features and support for large accounts")
        lines.append("- Expansion revenue target: 30-40% of total revenue by end of year")
        lines.append("")

        # Analytics Section
        lines.append("## Analytics & Measurement")
        lines.append("")
        if analytics_reqs:
            lines.append(f"### Analytics Requirements")
            lines.append(f"{analytics_reqs}")
            lines.append("")

        lines.append("### Core Metrics Dashboard")
        lines.append("- Acquisition: DAU, MAU, new signups, CAC")
        lines.append("- Activation: Onboarding completion, aha-moment rate")
        lines.append("- Retention: Monthly churn, NPS score, engagement")
        lines.append("- Revenue: MRR, ARR, ARPU, LTV")
        lines.append("- Efficiency: LTV/CAC ratio (target: >3x)")
        lines.append("")

        lines.append("### Cohort Analysis")
        lines.append("- Acquisition cohorts: Track retention by signup month/channel")
        lines.append("- Feature cohorts: Compare users with/without new features")
        lines.append("- Pricing cohorts: Analyze LTV and churn by plan tier")
        lines.append("- Geographic cohorts: Regional performance differences")
        lines.append("")

        lines.append("### A/B Testing Roadmap")
        lines.append("- Onboarding flows: Test simplified vs comprehensive")
        lines.append("- Pricing pages: Test different messaging and pricing models")
        lines.append("- Email campaigns: Subject lines, send times, messaging")
        lines.append("- Feature rollouts: Gradual rollout with canary testing")
        lines.append("- Monthly tests: Run 5-10 concurrent experiments")
        lines.append("")

        # SEO Section
        lines.append("## SEO Strategy")
        lines.append("")
        lines.append("### Keyword Research & Targeting")
        lines.append("- Primary keywords: Product category, problem statements")
        lines.append("- Long-tail keywords: Feature-specific, use-case specific")
        lines.append("- Competitive analysis: Monitor competitor rankings, content")
        lines.append("- Target keywords: Top 50 keywords with 100+ monthly volume")
        lines.append("")

        lines.append("### Content Optimization")
        lines.append("- Blog content: 2-3 posts per week, optimized for keywords")
        lines.append("- Pillar pages: Comprehensive guides for major topics")
        lines.append("- Internal linking: Strategic linking for page authority")
        lines.append("- Meta optimization: Titles, descriptions, schema markup")
        lines.append("")

        lines.append("### Technical SEO")
        lines.append("- Site speed: Target <2 second load time")
        lines.append("- Mobile optimization: 100% mobile-responsive design")
        lines.append("- Crawlability: XML sitemap, robots.txt optimization")
        lines.append("- Structured data: JSON-LD for products, FAQs, reviews")
        lines.append("")

        lines.append("### Link Building")
        lines.append("- Guest posting: 2-4 articles per month on relevant sites")
        lines.append("- Broken link building: Find and replace broken competitor links")
        lines.append("- PR-driven: Press coverage with backlinks")
        lines.append("- Link target: 20 high-quality backlinks per month")
        lines.append("")

        lines.append("### Organic Growth Targets")
        lines.append("- Organic traffic: 50% growth YoY")
        lines.append("- Search rankings: #1-3 for 10 major keywords")
        lines.append("- Organic conversion rate: 2-3% traffic to signup")
        lines.append("")

        # Customer Success Section
        lines.append("## Customer Success & Feedback")
        lines.append("")
        if feedback_loop:
            lines.append(f"### Customer Feedback Loop")
            lines.append(f"{feedback_loop}")
            lines.append("")

        lines.append("### NPS Program")
        lines.append("- Survey frequency: Monthly survey to random 10% of users")
        lines.append("- Response incentive: $5 gift card for completion")
        lines.append("- Follow-up: Personal outreach to detractors")
        lines.append("- Target NPS: >50 overall, >60 for enterprise")
        lines.append("")

        lines.append("### User Feedback Collection")
        lines.append("- Feature requests: In-app feedback form, public roadmap")
        lines.append("- User interviews: Monthly interviews with 5 power users")
        lines.append("- Support tickets: Categorize and analyze support patterns")
        lines.append("- Community forums: Active engagement and feedback gathering")
        lines.append("")

        lines.append("### Support Excellence")
        lines.append("- Response time: <4 hours for P1, <24 hours for P2/P3")
        lines.append("- Resolution rate: 95% of issues resolved in first response")
        lines.append("- CSAT score: Target >90% satisfaction")
        lines.append("- Proactive support: Identify and help struggling users")
        lines.append("")

        # 90-Day Plan
        lines.append("## 90-Day Growth Plan")
        lines.append("")
        if team_budget:
            lines.append(f"### Team & Budget")
            lines.append(f"{team_budget}")
            lines.append("")

        lines.append("### Month 1 Focus: Foundation")
        lines.append("- Analytics dashboard: Set up comprehensive tracking")
        lines.append("- SEO audit: Keyword research, content gaps analysis")
        lines.append("- Onboarding review: Identify friction points")
        lines.append("- Targets: 20% traffic increase, 15% retention improvement")
        lines.append("")

        lines.append("### Month 2 Focus: Optimization")
        lines.append("- Content: Launch 10 SEO-optimized blog posts")
        lines.append("- Referral: Launch referral program for power users")
        lines.append("- Retention: Implement 3 feature improvements from user feedback")
        lines.append("- Targets: 35% traffic increase, 25% retention improvement")
        lines.append("")

        lines.append("### Month 3 Focus: Expansion")
        lines.append("- Partnerships: Announce 2-3 strategic partnerships")
        lines.append("- Upsell: Launch higher-tier plans with new features")
        lines.append("- Enterprise: Acquire 2 enterprise customers")
        lines.append("- Targets: 50% traffic increase, 5% new expansion revenue")
        lines.append("")

        lines.append("### 90-Day Revenue Target")
        lines.append(f"- {product_name} 90-day MRR growth: 30%")
        lines.append("- New customer CAC payback: <10 months")
        lines.append("- Expansion revenue contribution: 10% of new MRR")
        lines.append("- Overall growth rate: 10% MoM or higher")

        return "\n".join(lines)
