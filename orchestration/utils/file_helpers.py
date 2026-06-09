"""File helper utilities for checkpoint management."""

import os
from datetime import datetime
from pathlib import Path


def generate_checkpoint_filename(description: str) -> str:
    """
    Generate a checkpoint filename with timestamp.

    Format: ddmmyy-hhmm-description.md
    Example: 060626-1645-research-phase-validation.md

    Args:
        description: Human-readable description of the checkpoint

    Returns:
        Formatted filename with timestamp
    """
    timestamp = datetime.now().strftime("%d%m%y-%H%M-")
    # Ensure description is lowercase and uses hyphens
    clean_description = description.lower().replace("_", "-").replace(" ", "-")
    # Remove any trailing hyphens
    clean_description = clean_description.rstrip("-")
    return f"{timestamp}{clean_description}.md"


def get_checkpoint_dir() -> str:
    """
    Get the checkpoint directory path, creating it if needed.

    Returns:
        Absolute path to checkpoint directory
    """
    checkpoint_dir = os.path.expanduser("~/.gstack/projects/claude-system/checkpoints")
    Path(checkpoint_dir).mkdir(parents=True, exist_ok=True)
    return checkpoint_dir


def get_checkpoint_path(description: str) -> str:
    """
    Get the full path for a checkpoint file.

    Args:
        description: Checkpoint description

    Returns:
        Absolute path to checkpoint file
    """
    filename = generate_checkpoint_filename(description)
    return os.path.join(get_checkpoint_dir(), filename)


def ensure_checkpoint_dir() -> str:
    """
    Ensure checkpoint directory exists and return its path.

    Returns:
        Absolute path to checkpoint directory
    """
    return get_checkpoint_dir()


def get_user_readable_path(filepath: str) -> str:
    """
    Convert absolute path to user-readable format.

    Replaces home directory with ~ for readability.

    Args:
        filepath: Absolute file path

    Returns:
        User-readable path
    """
    home = os.path.expanduser("~")
    if filepath.startswith(home):
        return "~" + filepath[len(home):]
    return filepath
