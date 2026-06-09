"""Context Manager for checkpoint save and restore operations."""

import os
import json
from datetime import datetime
from typing import Any
from pathlib import Path

from orchestration.utils.file_helpers import (
    generate_checkpoint_filename,
    get_checkpoint_dir,
    get_user_readable_path,
)


class CheckpointMetadata:
    """Metadata associated with a checkpoint."""

    def __init__(
        self,
        description: str,
        project: str = "",
        phase: int = 0,
        step: str = "",
        tags: list[str] | None = None,
    ):
        """
        Initialize checkpoint metadata.

        Args:
            description: Human-readable checkpoint description
            project: Project name (e.g., "marketing-os")
            phase: Phase number if applicable
            step: Step description if applicable
            tags: Optional tags for categorization
        """
        self.description = description
        self.project = project
        self.phase = phase
        self.step = step
        self.tags = tags or []
        self.timestamp = datetime.now().isoformat()

    def to_dict(self) -> dict:
        """Convert metadata to dictionary."""
        return {
            "description": self.description,
            "project": self.project,
            "phase": self.phase,
            "step": self.step,
            "tags": self.tags,
            "timestamp": self.timestamp,
        }


class ContextManager:
    """
    Manages context checkpoints for the orchestration system.

    Provides methods for:
    - Saving context snapshots with metadata
    - Restoring context from checkpoints
    - Getting user-readable paths
    """

    def __init__(self):
        """Initialize the context manager."""
        self.last_checkpoint_path: str | None = None

    def save(
        self,
        context: dict[str, Any],
        description: str,
        project: str = "",
        phase: int = 0,
        step: str = "",
        tags: list[str] | None = None,
    ) -> str:
        """
        Save context snapshot as a checkpoint.

        Args:
            context: Dictionary containing context data to save
            description: Human-readable description of checkpoint
            project: Project name (optional)
            phase: Phase number (optional)
            step: Step description (optional)
            tags: Optional tags for categorization

        Returns:
            Absolute path to saved checkpoint file
        """
        # Create metadata
        metadata = CheckpointMetadata(
            description=description,
            project=project,
            phase=phase,
            step=step,
            tags=tags,
        )

        # Generate filename and path
        filename = generate_checkpoint_filename(description)
        checkpoint_dir = get_checkpoint_dir()
        checkpoint_path = os.path.join(checkpoint_dir, filename)

        # Prepare checkpoint data
        checkpoint_data = {
            "metadata": metadata.to_dict(),
            "context": context,
        }

        # Write checkpoint file
        with open(checkpoint_path, "w", encoding="utf-8") as f:
            json.dump(checkpoint_data, f, indent=2)

        self.last_checkpoint_path = checkpoint_path
        return checkpoint_path

    def restore(self, filepath: str) -> dict[str, Any]:
        """
        Restore context from a checkpoint file.

        Args:
            filepath: Path to checkpoint file (absolute or relative)

        Returns:
            Dictionary containing the saved context

        Raises:
            FileNotFoundError: If checkpoint file doesn't exist
            json.JSONDecodeError: If checkpoint file is invalid JSON
        """
        # Convert to absolute path if needed
        if not os.path.isabs(filepath):
            filepath = os.path.join(get_checkpoint_dir(), filepath)

        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Checkpoint file not found: {filepath}")

        with open(filepath, "r", encoding="utf-8") as f:
            checkpoint_data = json.load(f)

        self.last_checkpoint_path = filepath
        return checkpoint_data.get("context", {})

    def get_display_path(self, filepath: str | None = None) -> str:
        """
        Get user-readable path for a checkpoint file.

        Args:
            filepath: Path to format (uses last checkpoint if not provided)

        Returns:
            User-readable path (with ~ for home directory)
        """
        path = filepath or self.last_checkpoint_path
        if not path:
            return ""
        return get_user_readable_path(path)

    def get_metadata(self, filepath: str) -> dict:
        """
        Get metadata from a checkpoint file.

        Args:
            filepath: Path to checkpoint file

        Returns:
            Dictionary containing checkpoint metadata

        Raises:
            FileNotFoundError: If checkpoint file doesn't exist
        """
        # Convert to absolute path if needed
        if not os.path.isabs(filepath):
            filepath = os.path.join(get_checkpoint_dir(), filepath)

        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Checkpoint file not found: {filepath}")

        with open(filepath, "r", encoding="utf-8") as f:
            checkpoint_data = json.load(f)

        return checkpoint_data.get("metadata", {})

    def list_checkpoints(self, limit: int = 10) -> list[dict]:
        """
        List available checkpoints, newest first.

        Args:
            limit: Maximum number of checkpoints to return

        Returns:
            List of checkpoint metadata dictionaries
        """
        checkpoint_dir = get_checkpoint_dir()

        if not os.path.exists(checkpoint_dir):
            return []

        # Get all .md files
        checkpoints = []
        for filename in os.listdir(checkpoint_dir):
            if filename.endswith(".md"):
                filepath = os.path.join(checkpoint_dir, filename)
                try:
                    with open(filepath, "r", encoding="utf-8") as f:
                        data = json.load(f)
                        metadata = data.get("metadata", {})
                        metadata["filename"] = filename
                        metadata["filepath"] = filepath
                        checkpoints.append(metadata)
                except (json.JSONDecodeError, IOError, UnicodeDecodeError):
                    # Skip invalid checkpoint files
                    continue

        # Sort by timestamp, newest first
        checkpoints.sort(
            key=lambda x: x.get("timestamp", ""),
            reverse=True
        )

        return checkpoints[:limit]

    def format_checkpoint_info(self, checkpoint: dict) -> str:
        """
        Format checkpoint metadata for display.

        Args:
            checkpoint: Checkpoint metadata dictionary

        Returns:
            Formatted string for terminal display
        """
        lines = []

        # Filename (user-readable)
        filename = checkpoint.get("filename", "")
        filepath = checkpoint.get("filepath", "")
        display_path = get_user_readable_path(filepath) if filepath else ""
        if display_path:
            lines.append(f"  File: {display_path}")

        # Description
        desc = checkpoint.get("description", "")
        if desc:
            lines.append(f"  Description: {desc}")

        # Project and phase
        project = checkpoint.get("project", "")
        phase = checkpoint.get("phase", 0)
        if project:
            lines.append(f"  Project: {project}")
        if phase:
            lines.append(f"  Phase: {phase}")

        # Step
        step = checkpoint.get("step", "")
        if step:
            lines.append(f"  Step: {step}")

        # Tags
        tags = checkpoint.get("tags", [])
        if tags:
            lines.append(f"  Tags: {', '.join(tags)}")

        # Timestamp
        timestamp = checkpoint.get("timestamp", "")
        if timestamp:
            lines.append(f"  Saved: {timestamp}")

        return "\n".join(lines)
