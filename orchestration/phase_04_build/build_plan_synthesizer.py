"""Build Plan Synthesizer for Phase 4."""

from typing import Any
from datetime import datetime


class BuildPlanSynthesizer:
    """
    Synthesizes development and security plans from clarifying questions and subagent outputs.

    Combines:
    - Phase 3 design context
    - User answers to 6 build clarifying questions
    - Outputs from /cso, /guard, /setup-deploy skills
    - Generates comprehensive development roadmap with security considerations
    """

    def __init__(self):
        """Initialize the build plan synthesizer."""
        self.synthesized_at = None

    def synthesize(
        self,
        product_name: str,
        clarifying_answers: dict[str, str],
        design_context: str,
        subagent_outputs: dict[str, str]
    ) -> str:
        """
        Synthesize build plan from inputs.

        Args:
            product_name: Name of the product
            clarifying_answers: Answers to 6 build clarifying questions
            design_context: Phase 3 design document or summary
            subagent_outputs: Outputs from CSO, Guard, Setup-Deploy skills

        Returns:
            Markdown-formatted development and security plan
        """
        self.synthesized_at = datetime.now().isoformat()

        # Extract clarifying answers
        tech_stack = clarifying_answers.get("tech_stack", "Not specified")
        deployment_platform = clarifying_answers.get("deployment_platform", "Not specified")
        timeline = clarifying_answers.get("timeline", "Not specified")
        security_requirements = clarifying_answers.get("security_requirements", "Standard")
        team_size = clarifying_answers.get("team_size", "Not specified")
        integrations = clarifying_answers.get("integrations", "Standard")

        # Extract subagent outputs
        cso_advice = subagent_outputs.get("cso", "")
        guard_review = subagent_outputs.get("guard", "")
        setup_deploy = subagent_outputs.get("setup_deploy", "")

        # Build document
        doc = self._build_development_plan(
            product_name=product_name,
            tech_stack=tech_stack,
            deployment_platform=deployment_platform,
            timeline=timeline,
            security_requirements=security_requirements,
            team_size=team_size,
            integrations=integrations,
            design_context=design_context,
            cso_advice=cso_advice,
            guard_review=guard_review,
            setup_deploy=setup_deploy
        )

        return doc

    def _build_development_plan(
        self,
        product_name: str,
        tech_stack: str,
        deployment_platform: str,
        timeline: str,
        security_requirements: str,
        team_size: str,
        integrations: str,
        design_context: str,
        cso_advice: str,
        guard_review: str,
        setup_deploy: str
    ) -> str:
        """Build the complete development and security plan document."""
        lines = []

        # Title
        lines.append(f"# Development & Security Plan: {product_name}\n")

        # Executive Summary
        lines.append("## Executive Summary\n")
        lines.append(f"**Product:** {product_name}")
        lines.append(f"**Tech Stack:** {tech_stack}")
        lines.append(f"**Deployment:** {deployment_platform}")
        lines.append(f"**Development Timeline:** {timeline}")
        lines.append(f"**Security Level:** {security_requirements}")
        if design_context:
            lines.append(f"**Design Foundation:** {design_context}")
        lines.append("")

        # Technical Architecture
        lines.append("## Technical Architecture\n")
        lines.append(f"**Tech Stack:** {tech_stack}\n")
        lines.append(f"**Deployment Platform:** {deployment_platform}\n")
        lines.append(f"**System Approach:** Cloud-native, scalable architecture")
        if setup_deploy:
            lines.append(f"**Infrastructure Setup:** {setup_deploy}\n")
        lines.append("**Performance Targets:** Sub-100ms response times, 99.9% uptime")
        lines.append("**Scalability:** Auto-scaling based on demand")
        lines.append("")

        # Development Roadmap
        lines.append("## Development Roadmap\n")
        lines.append(f"**Total Timeline:** {timeline}\n")
        lines.append("**MVP Scope:** Core functionality for production launch")
        lines.append("**Phase 1 (Weeks 1-4):** Foundation and core features")
        lines.append("**Phase 2 (Weeks 5-8):** Integration and testing")
        lines.append("**Phase 3 (Weeks 9-12):** Security hardening and optimization")
        lines.append("**Phase 4 (Weeks 13+):** Launch and post-launch improvements")
        lines.append("")

        # Team & Resources
        lines.append("## Team & Resources\n")
        lines.append(f"**Team Composition:** {team_size}\n")
        lines.append("**Development Process:** Agile/Scrum with 2-week sprints")
        lines.append("**Code Quality:** Unit tests (80%+ coverage), code review required")
        lines.append("**Documentation:** API docs, deployment guides, runbooks")
        lines.append("")

        # Security & Compliance
        lines.append("## Security & Compliance\n")
        lines.append(f"**Requirements:** {security_requirements}\n")
        if cso_advice:
            lines.append(f"**Security Strategy:** {cso_advice}\n")
        if guard_review:
            lines.append(f"**Security Review:** {guard_review}\n")
        lines.append("**Data Protection:** Encryption at rest and in transit")
        lines.append("**Access Control:** Role-based access control (RBAC)")
        lines.append("**Audit Logging:** Comprehensive audit trails for compliance")
        lines.append("**Incident Response:** Documented incident response procedures")
        lines.append("")

        # Infrastructure Setup
        lines.append("## Infrastructure Setup\n")
        lines.append(f"**Cloud Platform:** {deployment_platform}\n")
        lines.append("**Containerization:** Docker for consistent environments")
        lines.append("**Orchestration:** Kubernetes for production deployments")
        lines.append("**CI/CD Pipeline:** Automated testing and deployment")
        lines.append("**Monitoring:** Real-time alerting and log aggregation")
        lines.append("**Backup & Recovery:** Automated daily backups, disaster recovery plan")
        lines.append("")

        # Third-Party Integrations
        lines.append("## Third-Party Integrations\n")
        lines.append(f"**Planned Integrations:** {integrations}\n")
        lines.append("**Integration Testing:** Mandatory for all third-party services")
        lines.append("**API Rate Limiting:** Implement retry logic and circuit breakers")
        lines.append("**Service Dependencies:** Document and monitor all external dependencies")
        lines.append("")

        # Deployment Strategy
        lines.append("## Deployment Strategy\n")
        lines.append("**Deployment Approach:** Blue-green deployment for zero-downtime updates")
        lines.append("**Feature Flags:** Use feature flags for gradual rollout")
        lines.append("**Canary Releases:** 5% → 25% → 100% traffic rollout")
        lines.append("**Rollback Plan:** Automated rollback on health check failures")
        lines.append("")

        # Success Criteria
        lines.append("## Success Criteria\n")
        lines.append("1. All unit tests passing (80%+ coverage)")
        lines.append("2. Security review approved")
        lines.append("3. Performance targets met (sub-100ms response)")
        lines.append("4. Compliance checklist completed")
        lines.append("5. Documentation complete and reviewed")
        lines.append("6. Team trained on deployment and runbooks")
        lines.append("")

        # Next Steps
        lines.append("## Next Steps\n")
        lines.append("1. Set up development environment and CI/CD pipeline")
        lines.append("2. Create detailed technical specifications for each component")
        lines.append("3. Begin development following Agile methodology")
        lines.append("4. Conduct security reviews at key milestones")
        lines.append("5. Prepare launch and monitoring procedures")
        lines.append("")

        # Metadata
        lines.append("---\n")
        lines.append(f"**Generated:** {self.synthesized_at}")
        lines.append(f"**Status:** Plan - Ready for Development")

        return "\n".join(lines)
