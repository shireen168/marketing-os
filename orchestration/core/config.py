"""Configuration constants for the orchestration system."""

import os
from datetime import datetime
from typing import Literal


class Config:
    """Central configuration for the orchestration system."""

    # ============================================================================
    # API Configuration
    # ============================================================================

    # Anthropic API
    ANTHROPIC_API_KEY: str = os.getenv("ANTHROPIC_API_KEY", "")

    # Research APIs
    TAVILY_API_KEY: str = os.getenv("TAVILY_API_KEY", "")
    PERPLEXITY_API_KEY: str = os.getenv("PERPLEXITY_API_KEY", "")

    # ============================================================================
    # Model Configuration
    # ============================================================================

    # Phases 1-3: Complex reasoning (research, strategy, planning)
    MODEL_RESEARCH: Literal["claude-opus-4-7-20250219", "claude-sonnet-4-6-20250225"] = "claude-opus-4-7-20250219"

    # Phases 4-8: Execution (content creation, deployment, monitoring)
    MODEL_EXECUTION: Literal["claude-sonnet-4-6-20250225", "claude-opus-4-7-20250219"] = "claude-sonnet-4-6-20250225"

    # ============================================================================
    # Timeouts and Rate Limiting
    # ============================================================================

    # API call timeout (seconds)
    API_TIMEOUT: int = 60

    # Research phase timeout (seconds)
    RESEARCH_TIMEOUT: int = 300

    # Tavily API timeout (seconds)
    TAVILY_TIMEOUT: int = 30

    # Perplexity fallback timeout (seconds)
    PERPLEXITY_TIMEOUT: int = 45

    # ============================================================================
    # Checkpoint Configuration
    # ============================================================================

    # Checkpoint naming format: ddmmyy-hhmm-short-descriptive-name.md
    # Example: 060626-1645-research-phase-validation.md
    CHECKPOINT_FORMAT: str = "%d%m%y-%H%M-"
    CHECKPOINT_EXTENSION: str = ".md"

    # Checkpoint base directory
    CHECKPOINT_BASE_DIR: str = os.path.expanduser("~/.gstack/projects/claude-system/checkpoints")

    # ============================================================================
    # System Configuration
    # ============================================================================

    # Minimum confidence score for research validation (0.0 - 1.0)
    MIN_RESEARCH_CONFIDENCE: float = 0.75

    # Maximum retries for API calls
    MAX_RETRIES: int = 3

    # Retry backoff multiplier (exponential backoff)
    RETRY_BACKOFF: float = 2.0

    # Enable debug logging
    DEBUG: bool = os.getenv("DEBUG", "").lower() in ("true", "1", "yes")

    # ============================================================================
    # Helper Methods
    # ============================================================================

    @classmethod
    def get_checkpoint_filename(cls, name: str) -> str:
        """
        Generate a checkpoint filename with timestamp.

        Args:
            name: Descriptive name for the checkpoint (e.g., "research-phase-validation")

        Returns:
            Formatted checkpoint filename (e.g., "060626-1645-research-phase-validation.md")
        """
        timestamp = datetime.now().strftime(cls.CHECKPOINT_FORMAT)
        # Ensure name is lowercase and uses hyphens
        clean_name = name.lower().replace("_", "-")
        return f"{timestamp}{clean_name}{cls.CHECKPOINT_EXTENSION}"

    @classmethod
    def get_checkpoint_path(cls, name: str) -> str:
        """
        Get the full path for a checkpoint file.

        Args:
            name: Descriptive name for the checkpoint

        Returns:
            Full path to checkpoint file
        """
        filename = cls.get_checkpoint_filename(name)
        return os.path.join(cls.CHECKPOINT_BASE_DIR, filename)

    @classmethod
    def validate_api_keys(cls) -> bool:
        """
        Validate that required API keys are configured.

        Returns:
            True if all required keys are present, False otherwise
        """
        required_keys = {
            "ANTHROPIC_API_KEY": cls.ANTHROPIC_API_KEY,
            "TAVILY_API_KEY": cls.TAVILY_API_KEY,
        }

        missing = [key for key, value in required_keys.items() if not value]

        if missing:
            raise ValueError(
                f"Missing required API keys: {', '.join(missing)}. "
                f"Set them as environment variables."
            )

        return True
