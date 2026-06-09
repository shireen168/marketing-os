"""Test Plan Synthesizer for Phase 5 (Testing & QA)."""

from typing import Any


class TestPlanSynthesizer:
    """Synthesizes test and QA plans from Phase 5 clarifications and subagent outputs."""

    def __init__(self):
        """Initialize the test plan synthesizer."""
        self.phase = 5

    def synthesize(
        self,
        product_name: str,
        clarifying_answers: dict[str, str],
        subagent_outputs: dict[str, Any] | None = None
    ) -> str:
        """
        Synthesize a comprehensive test and QA plan.

        Args:
            product_name: Name of the product being tested
            clarifying_answers: Answers from Phase 5 clarifying questions
            subagent_outputs: Outputs from /qa, /benchmark, /careful, /canary, /browse

        Returns:
            Markdown-formatted test and QA plan document
        """
        if not product_name:
            return ""

        subagent_outputs = subagent_outputs or {}

        # Extract key testing parameters
        critical_paths = clarifying_answers.get("critical_paths", "")
        performance_reqs = clarifying_answers.get("performance_requirements", "")
        browsers_devices = clarifying_answers.get("browsers_devices", "")
        load_testing = clarifying_answers.get("load_testing", "")
        security_scope = clarifying_answers.get("security_scope", "")
        uat_timeline = clarifying_answers.get("uat_timeline", "")

        # Build comprehensive test plan
        lines = []
        lines.append("# Test & QA Plan")
        lines.append("")
        lines.append(f"Product: {product_name}")
        lines.append("")

        # Quality Assurance Section
        lines.append("## Quality Assurance")
        lines.append("")
        if critical_paths:
            lines.append(f"### Critical User Paths")
            lines.append(f"{critical_paths}")
            lines.append("")

        lines.append("### Test Coverage Strategy")
        lines.append("- Unit test coverage targets: 80%+ for business logic")
        lines.append("- Integration test scenarios: All API endpoints and workflows")
        lines.append("- End-to-end test suites: Complete user journeys")
        lines.append("- Bug severity thresholds: Critical (blocks launch), High (degrades UX), Medium (workaround exists), Low (cosmetic)")
        lines.append("")

        # Performance Testing Section
        lines.append("## Performance Testing")
        lines.append("")
        if performance_reqs:
            lines.append(f"### Performance Requirements")
            lines.append(f"{performance_reqs}")
            lines.append("")

        lines.append("### Benchmarking Standards")
        lines.append("- Latency targets: p50 <100ms, p95 <500ms, p99 <1000ms")
        lines.append("- Throughput targets: Min 100 req/sec per instance")
        lines.append("- Load testing scenarios: 1x, 5x, 10x expected peak load")
        lines.append("- Performance benchmarks: Track improvements release-over-release")
        lines.append("")

        # Compatibility Testing
        lines.append("## Compatibility Testing")
        lines.append("")
        if browsers_devices:
            lines.append(f"### Target Browsers & Devices")
            lines.append(f"{browsers_devices}")
            lines.append("")

        lines.append("### Test Matrix")
        lines.append("- Desktop browsers: Chrome, Firefox, Safari, Edge (latest 2 versions)")
        lines.append("- Mobile platforms: iOS (latest 2), Android (latest 2)")
        lines.append("- Screen resolutions: 320px, 768px, 1024px, 1440px, 2560px")
        lines.append("")

        # Load & Stress Testing
        lines.append("## Load & Stress Testing")
        lines.append("")
        if load_testing:
            lines.append(f"### Load Testing Requirements")
            lines.append(f"{load_testing}")
            lines.append("")

        lines.append("### Test Scenarios")
        lines.append("- Sustained load: Maintain expected concurrent users for 24+ hours")
        lines.append("- Spike testing: Handle 5x surge for 5 minutes")
        lines.append("- Soak testing: Monitor for memory leaks and degradation")
        lines.append("- Rollback readiness: Verify instant rollback capability")
        lines.append("")

        # Security Testing
        lines.append("## Security Testing")
        lines.append("")
        if security_scope:
            lines.append(f"### Security Testing Scope")
            lines.append(f"{security_scope}")
            lines.append("")

        lines.append("### Security Requirements")
        lines.append("- Vulnerability scanning: OWASP Top 10 coverage")
        lines.append("- Penetration testing: Third-party ethical hack")
        lines.append("- Data protection: Encryption in transit (TLS 1.2+) and at rest")
        lines.append("- Authentication: Secure token handling, session management")
        lines.append("- Authorization: Role-based access control (RBAC) validation")
        lines.append("")

        # User Acceptance Testing
        lines.append("## User Acceptance Testing (UAT)")
        lines.append("")
        if uat_timeline:
            lines.append(f"### UAT Timeline & Criteria")
            lines.append(f"{uat_timeline}")
            lines.append("")

        lines.append("### UAT Process")
        lines.append("- Test user recruitment: 10-20 external beta testers")
        lines.append("- UAT environment: Pre-production staging environment")
        lines.append("- Feedback mechanisms: In-app surveys, feedback forms, user interviews")
        lines.append("- Sign-off criteria: 95% of P1/P2 bugs fixed, positive user feedback")
        lines.append("")

        # Canary Deployment
        lines.append("## Canary Deployment Plan")
        lines.append("")
        lines.append("### Rollout Strategy")
        lines.append("- Phase 1: 5% of users (24 hours)")
        lines.append("- Phase 2: 25% of users (24 hours)")
        lines.append("- Phase 3: 100% of users (full rollout)")
        lines.append("")

        lines.append("### Monitoring During Rollout")
        lines.append("- Error rate tracking: Target <0.1%")
        lines.append("- Performance metrics: p95 latency, throughput")
        lines.append("- User feedback: Support ticket volume and sentiment")
        lines.append("- Resource utilization: CPU, memory, database connections")
        lines.append("")

        lines.append("### Rollback Criteria")
        lines.append("- Error rate > 1%: Immediate rollback")
        lines.append("- P1 bugs discovered: Evaluate and decide")
        lines.append("- Performance degradation >20%: Rollback and investigate")
        lines.append("- Data corruption or security issues: Immediate rollback")
        lines.append("")

        # Launch Readiness
        lines.append("## Launch Readiness Checklist")
        lines.append("")
        lines.append("### Quality Gates")
        lines.append("- [ ] All P1/P2 bugs resolved")
        lines.append("- [ ] 80%+ test coverage achieved")
        lines.append("- [ ] Performance benchmarks met")
        lines.append("- [ ] Security scan passing (no critical/high vulnerabilities)")
        lines.append("- [ ] UAT sign-off obtained")
        lines.append("")

        lines.append("### Operational Readiness")
        lines.append("- [ ] Runbooks and incident response plans documented")
        lines.append("- [ ] Monitoring and alerting configured")
        lines.append("- [ ] Support team trained on product")
        lines.append("- [ ] Rollback procedures tested")
        lines.append("")

        lines.append("### Go/No-Go Decision Criteria")
        lines.append("- Go if: All quality gates met, no critical security issues, UAT approved")
        lines.append("- No-go if: Critical bugs, security vulnerabilities, performance misses, insufficient UAT coverage")
        lines.append("")

        lines.append("## Success Metrics")
        lines.append("")
        lines.append("- Post-launch defect escape rate: <1 critical bug per 10K users")
        lines.append("- Performance stability: p95 latency within 10% of staging environment")
        lines.append("- User satisfaction: NPS >40 within 1 week of launch")
        lines.append("- System reliability: 99.9% uptime SLA maintained")

        return "\n".join(lines)
