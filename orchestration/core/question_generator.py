"""Question Generator for adaptive clarifying questions."""

from typing import Literal
from dataclasses import dataclass, field


@dataclass
class Question:
    """A single clarifying question."""

    text: str
    phase: str
    answered: bool = False
    answer: str = ""
    priority: int = 1  # Higher = more important


PHASE_QUESTIONS = {
    "research": [
        Question(
            text="What specific research topics or themes are most important to validate?",
            phase="research",
            priority=3
        ),
        Question(
            text="Who are the primary audiences for this research (buyers, decision-makers, influencers)?",
            phase="research",
            priority=3
        ),
        Question(
            text="What specific data points or metrics would validate success?",
            phase="research",
            priority=2
        ),
        Question(
            text="Are there any competitor benchmarks or market trends we should focus on?",
            phase="research",
            priority=2
        ),
        Question(
            text="What time frame should the research cover (historical, current, forward-looking)?",
            phase="research",
            priority=1
        ),
        Question(
            text="Should we prioritize quantitative data, qualitative insights, or both?",
            phase="research",
            priority=2
        ),
    ],
    "strategy": [
        Question(
            text="What's the primary positioning angle for this product/campaign?",
            phase="strategy",
            priority=3
        ),
        Question(
            text="What's your target early customer profile?",
            phase="strategy",
            priority=3
        ),
        Question(
            text="Revenue model preference (freemium, subscription, one-time purchase)?",
            phase="strategy",
            priority=3
        ),
        Question(
            text="Go-to-market timeline (when do we need to be live)?",
            phase="strategy",
            priority=3
        ),
        Question(
            text="Budget constraints for Phase 2 strategy work?",
            phase="strategy",
            priority=2
        ),
        Question(
            text="Priority: market share, profit margin, or customer acquisition?",
            phase="strategy",
            priority=2
        ),
    ],
    "planning": [
        Question(
            text="What is the planned launch or rollout timeline?",
            phase="planning",
            priority=3
        ),
        Question(
            text="Which teams or departments are involved in execution?",
            phase="planning",
            priority=3
        ),
        Question(
            text="What dependencies or prerequisites exist?",
            phase="planning",
            priority=2
        ),
        Question(
            text="How will we measure progress and iterate?",
            phase="planning",
            priority=2
        ),
        Question(
            text="What is the approval or sign-off process?",
            phase="planning",
            priority=2
        ),
        Question(
            text="Are there any technical or operational constraints?",
            phase="planning",
            priority=1
        ),
        Question(
            text="How should we handle edge cases or exceptions?",
            phase="planning",
            priority=1
        ),
    ],
    "execution": [
        Question(
            text="What content formats are needed (blog, video, email, social)?",
            phase="execution",
            priority=3
        ),
        Question(
            text="What is the approval workflow before publishing?",
            phase="execution",
            priority=3
        ),
        Question(
            text="Are there brand guidelines or messaging standards to follow?",
            phase="execution",
            priority=2
        ),
        Question(
            text="What distribution channels will be used?",
            phase="execution",
            priority=2
        ),
        Question(
            text="Who has sign-off authority?",
            phase="execution",
            priority=2
        ),
        Question(
            text="What's the publishing schedule?",
            phase="execution",
            priority=1
        ),
        Question(
            text="How should we track performance and engagement?",
            phase="execution",
            priority=1
        ),
    ],
    "design": [
        Question(
            text="What's the primary product form factor or delivery model?",
            phase="design",
            priority=3
        ),
        Question(
            text="Who is the primary user persona for this product?",
            phase="design",
            priority=3
        ),
        Question(
            text="What are the core user workflows or key use cases?",
            phase="design",
            priority=3
        ),
        Question(
            text="Software-first vs hardware-first approach, or hybrid?",
            phase="design",
            priority=3
        ),
        Question(
            text="Brand identity starting point (refresh existing or create new)?",
            phase="design",
            priority=2
        ),
        Question(
            text="Design budget and timeline constraints for Phase 3?",
            phase="design",
            priority=2
        ),
    ],
    "build": [
        Question(
            text="What's your preferred tech stack (frontend, backend, database)?",
            phase="build",
            priority=3
        ),
        Question(
            text="Which deployment platform (AWS, GCP, Azure, self-hosted)?",
            phase="build",
            priority=3
        ),
        Question(
            text="Development timeline: how fast do you need MVP (weeks vs months)?",
            phase="build",
            priority=3
        ),
        Question(
            text="Security requirements (HIPAA, SOC2, GDPR, PCI-DSS, or standard)?",
            phase="build",
            priority=3
        ),
        Question(
            text="Team size and development experience level?",
            phase="build",
            priority=2
        ),
        Question(
            text="Third-party integrations needed (payment, analytics, CRM, etc)?",
            phase="build",
            priority=2
        ),
    ],
    "testing": [
        Question(
            text="What are the critical user paths or core workflows to test?",
            phase="testing",
            priority=3
        ),
        Question(
            text="What are your performance requirements (latency, throughput targets)?",
            phase="testing",
            priority=3
        ),
        Question(
            text="Which browsers and devices must we test for compatibility?",
            phase="testing",
            priority=3
        ),
        Question(
            text="Load testing requirements: expected concurrent users and peak load?",
            phase="testing",
            priority=3
        ),
        Question(
            text="Security testing scope (vulnerability scanning, penetration testing)?",
            phase="testing",
            priority=2
        ),
        Question(
            text="User acceptance testing (UAT) timeline and sign-off criteria?",
            phase="testing",
            priority=2
        ),
    ],
    "launch": [
        Question(
            text="Primary launch announcement channels (press, social, ads, events)?",
            phase="launch",
            priority=3
        ),
        Question(
            text="Content pillars for launch campaign (thought leadership, demo, case studies)?",
            phase="launch",
            priority=3
        ),
        Question(
            text="Paid advertising budget allocation (Google Ads, LinkedIn, Facebook)?",
            phase="launch",
            priority=3
        ),
        Question(
            text="Social media strategy (platforms, posting frequency, engagement goals)?",
            phase="launch",
            priority=3
        ),
        Question(
            text="Email campaign strategy (list size, segmentation, messaging)?",
            phase="launch",
            priority=2
        ),
        Question(
            text="Launch event or webinar (virtual, in-person, hybrid)?",
            phase="launch",
            priority=2
        ),
    ],
    "growth": [
        Question(
            text="Primary growth lever (organic SEO, paid ads, partnerships, referrals)?",
            phase="growth",
            priority=3
        ),
        Question(
            text="Key retention metrics (target churn rate, LTV, engagement)?",
            phase="growth",
            priority=3
        ),
        Question(
            text="Expansion opportunities (upsell, cross-sell, new customer segments)?",
            phase="growth",
            priority=3
        ),
        Question(
            text="Customer feedback loop (NPS surveys, user interviews, support feedback)?",
            phase="growth",
            priority=3
        ),
        Question(
            text="Analytics requirements (dashboards, KPI tracking, reporting)?",
            phase="growth",
            priority=2
        ),
        Question(
            text="Growth team size and budget allocation for next quarter?",
            phase="growth",
            priority=2
        ),
    ],
    "operations": [
        Question(
            text="What were the biggest wins or successes during the launch?",
            phase="operations",
            priority=3
        ),
        Question(
            text="What were the biggest challenges or failures we faced?",
            phase="operations",
            priority=3
        ),
        Question(
            text="What would we do differently if starting over?",
            phase="operations",
            priority=3
        ),
        Question(
            text="What operational processes need to be documented?",
            phase="operations",
            priority=3
        ),
        Question(
            text="What skills or team capabilities need improvement?",
            phase="operations",
            priority=2
        ),
        Question(
            text="What's the vision for Phase 2 or the next product?",
            phase="operations",
            priority=2
        ),
    ],
}


class QuestionGenerator:
    """
    Generates and manages adaptive clarifying questions for different phases.

    Provides methods for:
    - Getting phase-specific questions
    - Filtering answered questions
    - Tracking which questions have been answered
    - Getting next unanswered question
    """

    def __init__(self):
        """Initialize the question generator."""
        self.answered_questions: set[str] = set()
        self.question_answers: dict[str, str] = {}

    def questions_for_phase(self, phase: str) -> list[Question]:
        """
        Get all questions for a specific phase.

        Args:
            phase: Phase name (research, strategy, planning, execution)

        Returns:
            List of Question objects for the phase
        """
        if phase not in PHASE_QUESTIONS:
            return []

        # Return copies with current answered state
        questions = PHASE_QUESTIONS[phase]
        result = []
        for q in questions:
            is_answered = q.text in self.answered_questions
            result.append(
                Question(
                    text=q.text,
                    phase=q.phase,
                    answered=is_answered,
                    answer=self.question_answers.get(q.text, ""),
                    priority=q.priority
                )
            )
        return result

    def filter_answered(self, questions: list[Question]) -> list[Question]:
        """
        Filter out questions that have already been answered.

        Args:
            questions: List of Question objects

        Returns:
            Filtered list of unanswered questions
        """
        return [q for q in questions if not q.answered]

    def next_question(self, phase: str) -> Question | None:
        """
        Get the next unanswered question for a phase.

        Returns highest priority unanswered question first.

        Args:
            phase: Phase name

        Returns:
            Next unanswered Question, or None if all answered
        """
        questions = self.questions_for_phase(phase)
        unanswered = self.filter_answered(questions)

        if not unanswered:
            return None

        # Sort by priority (highest first), then by original order
        unanswered.sort(key=lambda q: q.priority, reverse=True)
        return unanswered[0]

    def mark_answered(self, question_text: str, answer: str = ""):
        """
        Mark a question as answered.

        Args:
            question_text: The question text
            answer: Optional answer to store
        """
        self.answered_questions.add(question_text)
        if answer:
            self.question_answers[question_text] = answer

    def get_progress(self, phase: str) -> tuple[int, int]:
        """
        Get progress on answering questions for a phase.

        Args:
            phase: Phase name

        Returns:
            Tuple of (answered_count, total_count)
        """
        questions = self.questions_for_phase(phase)
        answered = len([q for q in questions if q.answered])
        return (answered, len(questions))

    def get_progress_percentage(self, phase: str) -> float:
        """
        Get percentage of questions answered for a phase.

        Args:
            phase: Phase name

        Returns:
            Percentage (0-100) of questions answered
        """
        answered, total = self.get_progress(phase)
        if total == 0:
            return 0.0
        return (answered / total) * 100

    def get_unanswered_summary(self, phase: str) -> str:
        """
        Get a summary of unanswered questions.

        Args:
            phase: Phase name

        Returns:
            Formatted summary string
        """
        questions = self.questions_for_phase(phase)
        unanswered = self.filter_answered(questions)

        if not unanswered:
            return f"All questions answered for {phase} phase!"

        lines = [f"{len(unanswered)} questions remaining for {phase} phase:"]
        for i, q in enumerate(unanswered, 1):
            priority_label = {1: "Low", 2: "Medium", 3: "High"}.get(q.priority, "Unknown")
            lines.append(f"  {i}. [{priority_label}] {q.text}")

        return "\n".join(lines)

    def reset(self):
        """Reset all answered questions."""
        self.answered_questions.clear()
        self.question_answers.clear()

    def reset_phase(self, phase: str):
        """Reset answered questions for a specific phase."""
        questions = PHASE_QUESTIONS.get(phase, [])
        for q in questions:
            self.answered_questions.discard(q.text)
            self.question_answers.pop(q.text, None)
