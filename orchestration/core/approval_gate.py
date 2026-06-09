"""Approval Gate Manager for user decisions and revision feedback."""

from typing import Literal
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class ApprovalDecision:
    """Container for approval decision and associated data."""

    decision: Literal["approve", "revise", "unclear"]
    feedback: str = ""
    diagnostic_questions: list[str] = field(default_factory=list)
    timestamp: str = ""

    def __post_init__(self):
        """Initialize timestamp if not provided."""
        if not self.timestamp:
            self.timestamp = datetime.now().isoformat()


class ApprovalGate:
    """
    Manages user approval decisions and revision feedback.

    Provides methods for:
    - Getting user approval/revision decisions
    - Capturing revision feedback
    - Generating diagnostic questions based on feedback
    - Formatting deliverables for terminal display
    """

    def __init__(self):
        """Initialize the approval gate."""
        self.last_decision: ApprovalDecision | None = None

    def get_user_decision(self) -> Literal["approve", "revise", "unclear"]:
        """
        Get user decision on the current deliverable.

        Returns:
            "approve" - User accepts the deliverable
            "revise" - User wants revisions
            "unclear" - User uncertain about the decision
        """
        while True:
            print("\n" + "=" * 60)
            print("APPROVAL GATE")
            print("=" * 60)
            print("\nWhat would you like to do?")
            print("  [a] Approve - accept this deliverable")
            print("  [r] Revise - request changes")
            print("  [u] Unclear - not sure yet")
            print()

            choice = input("Enter your choice (a/r/u): ").strip().lower()

            if choice == "a":
                return "approve"
            elif choice == "r":
                return "revise"
            elif choice == "u":
                return "unclear"
            else:
                print("Invalid choice. Please enter a, r, or u.")

    def get_revision_feedback(self) -> str:
        """
        Capture structured feedback for revisions.

        Returns:
            User feedback as a string
        """
        print("\n" + "-" * 60)
        print("REVISION FEEDBACK")
        print("-" * 60)
        print("\nWhat would you like changed? Be as specific as possible.")
        print("(You can provide multiple items. Press Enter twice when done.)\n")

        lines = []
        empty_count = 0

        while True:
            line = input()
            if line == "":
                empty_count += 1
                if empty_count >= 2:
                    break
                lines.append(line)
            else:
                empty_count = 0
                lines.append(line)

        feedback = "\n".join(lines).strip()
        return feedback if feedback else "No specific feedback provided."

    def generate_diagnostic_questions(self, feedback: str) -> list[str]:
        """
        Generate proactive diagnostic questions based on feedback.

        These questions help clarify vague feedback and identify root causes
        of dissatisfaction.

        Args:
            feedback: User feedback text

        Returns:
            List of diagnostic questions
        """
        feedback_lower = feedback.lower()
        questions = []

        # Map keywords to diagnostic questions
        keyword_map = {
            "tone": [
                "What tone would work better? (e.g., more formal, more conversational, more technical)",
                "Are there specific phrases or words that feel off?",
            ],
            "length": [
                "Should this be shorter, longer, or about the same length?",
                "Which parts feel too verbose? Which parts need more detail?",
            ],
            "content": [
                "What information is missing or incorrect?",
                "What should be removed or de-emphasized?",
            ],
            "structure": [
                "Does the flow make sense? Where should sections be reordered?",
                "Are there any logical gaps or jumps?",
            ],
            "unclear": [
                "What specific part is confusing?",
                "Would examples or clearer definitions help?",
            ],
            "wrong": [
                "What's incorrect or misleading?",
                "What's the correct information or approach?",
            ],
            "need": [
                "What specifically is needed that's missing?",
                "How should this information be presented?",
            ],
            "different": [
                "What would 'different' look like?",
                "Can you provide an example of what you're envisioning?",
            ],
        }

        # Check for keywords and add relevant questions
        for keyword, qs in keyword_map.items():
            if keyword in feedback_lower:
                questions.extend(qs)

        # If no specific keywords matched, ask general clarifying questions
        if not questions:
            questions = [
                "What specifically about this doesn't meet your needs?",
                "Are there particular aspects (tone, content, structure, length) that need adjustment?",
                "Can you provide an example of what would work better?",
            ]

        # Remove duplicates while preserving order
        seen = set()
        unique_questions = []
        for q in questions:
            if q not in seen:
                seen.add(q)
                unique_questions.append(q)

        return unique_questions

    def format_for_display(
        self,
        deliverable: str,
        title: str = "Deliverable",
        metadata: dict | None = None
    ) -> str:
        """
        Format a deliverable for terminal display.

        Args:
            deliverable: The content to display
            title: Display title for the deliverable
            metadata: Optional metadata dictionary (phase, step, etc.)

        Returns:
            Formatted string ready for terminal output
        """
        output = []

        # Header with title
        output.append("\n" + "=" * 60)
        output.append(f"  {title.upper()}")
        output.append("=" * 60)

        # Metadata if provided
        if metadata:
            output.append("")
            for key, value in metadata.items():
                output.append(f"  {key}: {value}")

        # Divider and content
        output.append("\n" + "-" * 60)
        output.append("")
        output.append(deliverable)
        output.append("")
        output.append("-" * 60)

        return "\n".join(output)

    def record_decision(
        self,
        decision: Literal["approve", "revise", "unclear"],
        feedback: str = "",
        diagnostic_questions: list[str] | None = None
    ) -> ApprovalDecision:
        """
        Record an approval decision.

        Args:
            decision: The approval decision
            feedback: Optional feedback text
            diagnostic_questions: Optional diagnostic questions

        Returns:
            ApprovalDecision object
        """
        approval_decision = ApprovalDecision(
            decision=decision,
            feedback=feedback,
            diagnostic_questions=diagnostic_questions or []
        )
        self.last_decision = approval_decision
        return approval_decision

    def print_summary(self):
        """Print a summary of the last decision."""
        if not self.last_decision:
            print("No decision recorded yet.")
            return

        print("\n" + "=" * 60)
        print("DECISION SUMMARY")
        print("=" * 60)
        print(f"\nDecision: {self.last_decision.decision.upper()}")
        print(f"Timestamp: {self.last_decision.timestamp}")

        if self.last_decision.feedback:
            print(f"\nFeedback:\n{self.last_decision.feedback}")

        if self.last_decision.diagnostic_questions:
            print("\nDiagnostic Questions:")
            for i, q in enumerate(self.last_decision.diagnostic_questions, 1):
                print(f"  {i}. {q}")
