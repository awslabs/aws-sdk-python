#!/usr/bin/env python3
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
"""
Common utilities for changelog management scripts.
"""

import sys
from pathlib import Path

PROJECT_ROOT_DIR = Path(__file__).resolve().parent.parent.parent
PACKAGE_ROOT_DIRS = ("clients", "packages")


def find_package_dir(package_name: str) -> Path:
    """Find a package directory, searching each of the package roots in order."""
    for package_root in PACKAGE_ROOT_DIRS:
        package_path = PROJECT_ROOT_DIR / package_root / package_name
        if package_path.is_dir():
            return package_path

    searched = ", ".join(f"{package_root}/" for package_root in PACKAGE_ROOT_DIRS)
    print(
        f"Error: Package '{package_name}' not found in {searched}",
        file=sys.stderr,
    )
    sys.exit(1)


def get_package_changes_dir(package_name: str) -> Path:
    """Get the .changes directory for a package."""
    return find_package_dir(package_name) / ".changes"
