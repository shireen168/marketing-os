"""
Orchestration System - Automated Workflow for 8-Phase Product Launch Framework

This package provides a top-level orchestration system that automates the complete
product launch workflow while maintaining human-in-the-loop approval gates.

Phase 1 (MVP) focuses on research validation using Tavily API with Perplexity fallback.
"""

__version__ = "0.1.0"
__author__ = "Shireen"

from orchestration.core.config import Config

__all__ = ["Config"]
