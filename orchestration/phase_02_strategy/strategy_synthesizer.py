"""Strategy Synthesizer: Combine strategy subagent outputs into comprehensive document."""

from typing import Dict, Any


class StrategySynthesizer:
    """
    Synthesizes strategy phase subagent outputs into a comprehensive strategy document.

    Combines outputs from:
    - /product-marketing (positioning, messaging)
    - /pricing (revenue model, pricing strategy)
    - /sales-enablement (sales messaging, objections)

    Produces:
    - Markdown strategy document with positioning, GTM, pricing, messaging hierarchy
    """

    def __init__(self):
        """Initialize the Strategy Synthesizer."""
        pass

    def synthesize(
        self,
        product_marketing: Dict[str, Any],
        pricing: Dict[str, Any],
        sales_enablement: Dict[str, Any],
        clarifying_answers: Dict[str, str] | None = None
    ) -> str:
        """
        Synthesize strategy outputs into comprehensive document.

        Args:
            product_marketing: Output from /product-marketing skill
            pricing: Output from /pricing skill
            sales_enablement: Output from /sales-enablement skill
            clarifying_answers: User answers to clarifying questions

        Returns:
            Markdown strategy document string
        """
        answers = clarifying_answers or {}

        # Extract positioning
        positioning = answers.get("positioning_angle", "")
        early_customer = answers.get("early_customer_profile", "")
        gtm_timeline = answers.get("gtm_timeline", "")
        revenue_model = answers.get("revenue_model", "")

        # Build document sections
        sections = []

        # Title
        sections.append(self._build_title(answers.get("product_name", "Product")))

        # Positioning
        positioning_section = self._build_positioning_section(
            positioning,
            product_marketing.get("positioning", {}),
            product_marketing.get("differentiators", [])
        )
        sections.append(positioning_section)

        # Go-to-Market
        gtm_section = self._build_gtm_section(
            gtm_timeline,
            early_customer,
            product_marketing.get("gtm_channels", [])
        )
        sections.append(gtm_section)

        # Pricing Model
        pricing_section = self._build_pricing_section(
            revenue_model,
            pricing.get("model", ""),
            pricing.get("price_points", []),
            pricing.get("revenue_projection", {})
        )
        sections.append(pricing_section)

        # Sales Enablement
        sales_section = self._build_sales_section(
            sales_enablement.get("messaging", []),
            sales_enablement.get("objections", []),
            sales_enablement.get("tools", [])
        )
        sections.append(sales_section)

        # Success Metrics
        metrics_section = self._build_metrics_section(
            answers.get("priority", ""),
            product_marketing.get("kpis", [])
        )
        sections.append(metrics_section)

        return "\n\n".join(sections)

    def _build_title(self, product_name: str) -> str:
        """Build document title."""
        return f"# Strategy Document: {product_name}"

    def _build_positioning_section(
        self,
        positioning_angle: str,
        product_marketing: Dict[str, Any],
        differentiators: list
    ) -> str:
        """Build Positioning section."""
        lines = ["## Positioning"]

        if positioning_angle:
            lines.append(f"**Primary Positioning:** {positioning_angle}")

        if differentiators:
            lines.append("\n**Key Differentiators:**")
            for diff in differentiators:
                lines.append(f"- {diff}")

        if product_marketing and isinstance(product_marketing, dict):
            for key, value in product_marketing.items():
                if key not in ["kpis"] and value:
                    formatted_key = key.replace("_", " ").title()
                    lines.append(f"- **{formatted_key}:** {value}")

        return "\n".join(lines)

    def _build_gtm_section(
        self,
        timeline: str,
        early_customer: str,
        channels: list
    ) -> str:
        """Build Go-to-Market section."""
        lines = ["## Go-to-Market (GTM)"]

        if timeline:
            lines.append(f"**Launch Timeline:** {timeline}")

        if early_customer:
            lines.append(f"**Early Customer Profile:** {early_customer}")

        if channels:
            lines.append("\n**GTM Channels:**")
            for channel in channels:
                lines.append(f"- {channel}")

        return "\n".join(lines)

    def _build_pricing_section(
        self,
        revenue_model: str,
        model_details: str,
        price_points: list,
        revenue_projection: Dict[str, Any]
    ) -> str:
        """Build Pricing Model section."""
        lines = ["## Pricing Model"]

        if revenue_model:
            lines.append(f"**Model:** {revenue_model}")

        if model_details:
            lines.append(f"**Details:** {model_details}")

        if price_points:
            lines.append("\n**Price Points:**")
            for point in price_points:
                lines.append(f"- {point}")

        if revenue_projection:
            lines.append("\n**Revenue Projection:**")
            for year, amount in revenue_projection.items():
                lines.append(f"- {year}: {amount}")

        return "\n".join(lines)

    def _build_sales_section(
        self,
        messaging: list,
        objections: list,
        tools: list
    ) -> str:
        """Build Sales Enablement section."""
        lines = ["## Sales Enablement"]

        if messaging:
            lines.append("**Sales Messaging:**")
            for msg in messaging:
                lines.append(f"- {msg}")

        if objections:
            lines.append("\n**Objection Handling:**")
            for obj in objections:
                lines.append(f"- {obj}")

        if tools:
            lines.append("\n**Sales Tools Needed:**")
            for tool in tools:
                lines.append(f"- {tool}")

        return "\n".join(lines)

    def _build_metrics_section(
        self,
        priority: str,
        kpis: list
    ) -> str:
        """Build Success Metrics section."""
        lines = ["## Success Metrics"]

        if priority:
            lines.append(f"**Primary Priority:** {priority}")

        if kpis:
            lines.append("\n**Key Performance Indicators (KPIs):**")
            for kpi in kpis:
                lines.append(f"- {kpi}")

        return "\n".join(lines)
