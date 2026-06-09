"""CLI entry point for workflow orchestration."""

import argparse
import sys
import os
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from orchestration.core.orchestrator import Orchestrator
from orchestration.core.approval_gate import ApprovalGate


def setup_arg_parser():
    """Set up command-line argument parser."""
    parser = argparse.ArgumentParser(
        description="Orchestrate workflow phases with adaptive clarifications",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python orchestration/cli/run_workflow.py --project marketing-os --phase 1
  python orchestration/cli/run_workflow.py --project marketing-os --phase 1 --checkpoint ~/checkpoints/test.md
  python orchestration/cli/run_workflow.py --project sunny-homemade --phase 2 --verbose
        """
    )

    parser.add_argument(
        "--project",
        required=True,
        help="Project name (e.g., marketing-os, sunny-homemade)"
    )

    parser.add_argument(
        "--phase",
        type=int,
        required=True,
        choices=[1, 2, 3, 4, 5, 6],
        help="Phase number to run (1-6)"
    )

    parser.add_argument(
        "--checkpoint",
        help="Path to checkpoint file to restore from"
    )

    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose output"
    )

    parser.add_argument(
        "--no-approval",
        action="store_true",
        help="Skip approval gate (auto-approve)"
    )

    parser.add_argument(
        "--save-checkpoint",
        help="Save checkpoint with this name after completion"
    )

    return parser


def print_header(text, level=1):
    """Print formatted header."""
    if level == 1:
        print("\n" + "=" * 60)
        print(f"  {text.upper()}")
        print("=" * 60)
    elif level == 2:
        print(f"\n--- {text} ---")
    else:
        print(f"\n{text}")


def run_workflow(args):
    """
    Execute the workflow orchestration.

    Args:
        args: Parsed command-line arguments

    Returns:
        Exit code (0 for success, 1 for failure)
    """
    try:
        # Initialize orchestrator
        orchestrator = Orchestrator(project=args.project)

        if args.verbose:
            print(f"Initializing orchestrator for project: {args.project}")

        # Restore from checkpoint if provided
        if args.checkpoint:
            print_header("Restoring Checkpoint", 1)
            if orchestrator.restore_checkpoint(args.checkpoint):
                print(f"✓ Checkpoint restored: {args.checkpoint}")
            else:
                print(f"✗ Failed to restore checkpoint: {args.checkpoint}")
                return 1

        # Display phase information
        print_header(f"Phase {args.phase}: {orchestrator.get_phase_name(args.phase)}", 1)
        print(f"\nDescription: {orchestrator.get_phase_description(args.phase)}")

        # Gather clarifications
        print_header("Gathering Clarifications", 2)
        clarifications = orchestrator.gather_clarifications(args.phase)

        if clarifications.get("status") == "all_answered":
            print("✓ All clarifying questions have been answered")
        else:
            questions = clarifications.get("questions", [])
            if questions:
                print(f"\nQuestions to answer ({len(questions)}):")
                for i, q in enumerate(questions, 1):
                    print(f"  {i}. {q}")
                print("\n[In full implementation, would prompt for answers]")
            else:
                print("No questions to clarify")

        # Run phase subagents
        print_header("Running Phase Subagents", 2)

        def progress_callback(msg):
            if args.verbose:
                print(f"  > {msg}")

        result = orchestrator.run_phase_subagents(
            phase=args.phase,
            callback=progress_callback
        )

        # Store result
        orchestrator.phase_results[args.phase] = result

        if result.status == "success":
            print("✓ Subagent execution completed")
        else:
            print(f"✗ Subagent execution failed: {result.error}")

        # Synthesize output
        print_header("Phase Output", 2)
        synthesis = orchestrator.synthesize_phase_output(args.phase, result)
        print(synthesis)

        # Approval gate
        if not args.no_approval:
            approval_gate = ApprovalGate()
            formatted = approval_gate.format_for_display(
                synthesis,
                title=f"Phase {args.phase} Deliverable",
                metadata={
                    "project": args.project,
                    "phase": args.phase,
                    "status": result.status
                }
            )
            print(formatted)

            # Simulate approval (in real implementation, would prompt user)
            print("\n[In full implementation, would request user approval]")
            approval_decision = "approve"
            print(f"✓ Auto-approved (--no-approval flag set)" if args.no_approval else f"Decision: {approval_decision}")
        else:
            print("✓ Approval gate skipped (--no-approval flag)")

        # Save checkpoint
        if args.save_checkpoint:
            print_header("Saving Checkpoint", 2)
            checkpoint_path = orchestrator.save_checkpoint(
                args.save_checkpoint,
                phase=args.phase
            )
            print(f"✓ Checkpoint saved: {checkpoint_path}")

        # Display final status
        print_header("Workflow Status", 1)
        status = orchestrator.get_status()
        print(f"Project: {status['project']}")
        print(f"Current Phase: {status['current_phase']}")
        print(f"Completed Phases: {status['completed_phases']}")

        print("\n✓ Workflow execution complete\n")
        return 0

    except Exception as e:
        print(f"\n✗ Error: {e}", file=sys.stderr)
        if args.verbose:
            import traceback
            traceback.print_exc()
        return 1


def main():
    """Main entry point."""
    parser = setup_arg_parser()
    args = parser.parse_args()

    return run_workflow(args)


if __name__ == "__main__":
    sys.exit(main())
