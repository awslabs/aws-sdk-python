#!/usr/bin/env python3
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
"""
Common utilities for changelog management scripts.
"""

import sys
from pathlib import Path

PROJECT_ROOT_DIR = Path(__file__).resolve().parent.parent.parent


def validate_package_name(package_name: str) -> None:
    """Validate that the package exists in the clients directory."""
    package_path = PROJECT_ROOT_DIR / "clients" / package_name
    if not package_path.exists():
        print(
            f"Error: Package '{package_name}' not found in clients directory",
            file=sys.stderr,
        )
        sys.exit(1)


def get_package_changes_dir(package_name: str) -> Path:
    """Get the .changes directory for a package."""
    validate_package_name(package_name)
    return PROJECT_ROOT_DIR / "clients" / package_name / ".changes"
