#!/usr/bin/env python3
"""
Sync orchestration outputs to marketing-os documentation.

This script copies the latest phase outputs from orchestration/outputs/
to projects/marketing-os/docs/product-launch/outputs/ so they're visible
in the product launch documentation.

Usage:
    python sync-outputs.py
"""

import os
import shutil
from pathlib import Path


def sync_outputs():
    """Sync outputs from orchestration to marketing-os."""

    # Paths
    repo_root = Path(__file__).parent.parent.parent.parent.parent  # 5 levels up
    orchestration_outputs = repo_root / "orchestration" / "outputs"
    marketing_os_outputs = Path(__file__).parent / "outputs"

    print(f"Syncing orchestration outputs...")
    print(f"  Source: {orchestration_outputs}")
    print(f"  Target: {marketing_os_outputs}")

    if not orchestration_outputs.exists():
        print(f"[ERROR] Source directory not found: {orchestration_outputs}")
        return False

    # Create target directory if it doesn't exist
    marketing_os_outputs.mkdir(parents=True, exist_ok=True)

    # Copy each phase directory
    phase_count = 0
    for phase_dir in sorted(orchestration_outputs.iterdir()):
        if phase_dir.is_dir() and phase_dir.name.startswith("phase_"):
            target_phase = marketing_os_outputs / phase_dir.name

            # Remove existing if present
            if target_phase.exists():
                shutil.rmtree(target_phase)

            # Copy entire phase directory
            shutil.copytree(phase_dir, target_phase)
            print(f"  [OK] Synced {phase_dir.name}")
            phase_count += 1

    if phase_count == 0:
        print("  [WARN] No phase outputs found to sync")
        return False

    print(f"\n[SUCCESS] Synced {phase_count} phase outputs")
    print(f"\nOutputs are now available at:")
    print(f"  {marketing_os_outputs}")
    return True


if __name__ == "__main__":
    success = sync_outputs()
    exit(0 if success else 1)
