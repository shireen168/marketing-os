"""Design Specification Synthesizer for Phase 3."""

from typing import Any
from datetime import datetime


class DesignSynthesizer:
    """
    Synthesizes design specifications from clarifying questions and subagent outputs.

    Combines:
    - Phase 2 strategy context
    - User answers to 6 design clarifying questions
    - Outputs from /design-consultation, /plan-design-review, /plan-eng-review
    - Generates comprehensive design specification document
    """

    def __init__(self):
        """Initialize the design synthesizer."""
        self.synthesized_at = None

    def synthesize(
        self,
        product_name: str,
        clarifying_answers: dict[str, str],
        strategy_context: str,
        subagent_outputs: dict[str, str]
    ) -> str:
        """
        Synthesize design specification from inputs.

        Args:
            product_name: Name of the product
            clarifying_answers: Answers to 6 design clarifying questions
            strategy_context: Phase 2 strategy document or summary
            subagent_outputs: Outputs from design consultation, design review, eng review

        Returns:
            Markdown-formatted design specification document
        """
        self.synthesized_at = datetime.now().isoformat()

        # Extract clarifying answers
        form_factor = clarifying_answers.get("form_factor", "Not specified")
        user_persona = clarifying_answers.get("user_persona", "Not specified")
        workflows = clarifying_answers.get("workflows", "Not specified")
        approach = clarifying_answers.get("approach", "Not specified")
        brand = clarifying_answers.get("brand", "Not specified")
        budget = clarifying_answers.get("budget", "Not specified")

        # Extract subagent outputs
        design_consultation = subagent_outputs.get("design_consultation", "")
        design_review = subagent_outputs.get("design_review", "")
        eng_review = subagent_outputs.get("eng_review", "")

        # Build document
        doc = self._build_design_specification(
            product_name=product_name,
            form_factor=form_factor,
            user_persona=user_persona,
            workflows=workflows,
            approach=approach,
            brand=brand,
            budget=budget,
            strategy_context=strategy_context,
            design_consultation=design_consultation,
            design_review=design_review,
            eng_review=eng_review
        )

        return doc

    def _build_design_specification(
        self,
        product_name: str,
        form_factor: str,
        user_persona: str,
        workflows: str,
        approach: str,
        brand: str,
        budget: str,
        strategy_context: str,
        design_consultation: str,
        design_review: str,
        eng_review: str
    ) -> str:
        """Build the complete design specification document."""
        lines = []

        # Title
        lines.append(f"# Design Specification: {product_name}\n")

        # Executive Summary
        lines.append("## Executive Summary\n")
        lines.append(f"**Product:** {product_name}")
        lines.append(f"**Form Factor:** {form_factor}")
        lines.append(f"**Primary User:** {user_persona}")
        lines.append(f"**Design Approach:** {approach}")
        if strategy_context:
            lines.append(f"**Strategy Context:** {strategy_context}")
        lines.append("")

        # Product Overview
        lines.append("## Product Overview\n")
        lines.append(f"**Form Factor:** {form_factor}\n")
        lines.append(f"**Primary User Persona:** {user_persona}\n")
        lines.append(f"**Core Value Proposition:** Design a {approach} solution for {user_persona}")
        lines.append("")

        # User Experience (UX)
        lines.append("## User Experience (UX)\n")
        lines.append(f"**Primary Workflows:** {workflows}\n")
        lines.append(f"**User Persona:** {user_persona}\n")
        if design_consultation:
            lines.append(f"**Design Insights:** {design_consultation}\n")
        lines.append("**Wireframes/Mockups:** To be created based on approved design specifications")
        lines.append("")

        # Technical Architecture
        lines.append("## Technical Architecture\n")
        if eng_review:
            lines.append(f"**Engineering Review:** {eng_review}\n")
        lines.append(f"**Design Approach:** {approach}-first architecture")
        lines.append("**System Components:** To be detailed based on selected tech stack")
        lines.append("**Infrastructure:** Cloud-based deployment with scalable architecture")
        lines.append("")

        # Brand & Visual Identity
        lines.append("## Brand & Visual Identity\n")
        lines.append(f"**Brand Strategy:** {brand}\n")
        if design_review:
            lines.append(f"**Design System:** {design_review}\n")
        lines.append("**Brand Guidelines:** Logo, color palette, typography to be finalized")
        lines.append("**Voice & Tone:** Professional, user-centric, clear communication")
        lines.append("")

        # Implementation Roadmap
        lines.append("## Implementation Roadmap\n")
        lines.append(f"**Timeline:** {budget}\n")
        lines.append("**MVP Scope:** Core workflows and primary features")
        lines.append("**Phase 1 (Design):** Wireframes and design system")
        lines.append("**Phase 2 (Development):** Build MVP based on approved designs")
        lines.append("**Phase 3 (Testing):** QA and user testing")
        lines.append("**Phase 4 (Launch):** Release and monitor performance")
        lines.append("")

        # Design Principles
        lines.append("## Design Principles\n")
        lines.append("1. **User-Centric:** All design decisions prioritize user needs")
        lines.append("2. **Consistency:** Follow established design patterns and systems")
        lines.append("3. **Simplicity:** Reduce complexity, maximize usability")
        lines.append("4. **Accessibility:** Ensure inclusive design for all users")
        lines.append("5. **Scalability:** Design for growth and future enhancements")
        lines.append("")

        # Next Steps
        lines.append("## Next Steps\n")
        lines.append("1. Review and approve this design specification")
        lines.append("2. Create detailed wireframes based on approved approach")
        lines.append("3. Develop design system and component library")
        lines.append("4. Plan Phase 4 (Build & Development)")
        lines.append("")

        # Metadata
        lines.append("---\n")
        lines.append(f"**Generated:** {self.synthesized_at}")
        lines.append(f"**Status:** Draft - Awaiting Approval")

        return "\n".join(lines)
