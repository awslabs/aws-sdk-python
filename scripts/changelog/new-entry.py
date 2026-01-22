#!/usr/bin/env python3
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
"""
Create new changelog entries for a specific package.
"""

import argparse
import json
import uuid
from pathlib import Path

from utils import get_package_changes_dir

PROJECT_ROOT_DIR = Path(__file__).resolve().parent.parent.parent


def setup_changes_directories(package_name: str) -> Path:
    """Set up and return the next-release directory for a package."""
    changes_dir = get_package_changes_dir(package_name)
    changes_dir.mkdir(exist_ok=True)

    next_release_dir = changes_dir / "next-release"
    next_release_dir.mkdir(exist_ok=True)

    return next_release_dir


def create_change_entry(
    change_type: str,
    description: str,
    package_name: str,
) -> str:
    next_release_dir = setup_changes_directories(package_name)

    # Generate unique filename
    unique_id = uuid.uuid4().hex
    filename = f"{package_name}-{change_type}-{unique_id}.json"

    entry_data = {
        "type": change_type,
        "description": description,
    }

    entry_file = next_release_dir / filename
    with open(entry_file, "w") as f:
        json.dump(entry_data, f, indent=2)

    print(f"Created changelog entry: {entry_file}")
    return str(entry_file)


def create_summary_entry(
    description: str,
    package_name: str,
) -> str:
    """Create or update the release summary for the next release."""
    next_release_dir = setup_changes_directories(package_name)

    # Summary is stored in a fixed file (only one summary per release)
    summary_file = next_release_dir / "SUMMARY.json"

    if summary_file.exists():
        print(f"Warning: Overwriting existing summary in {summary_file}")

    entry_data = {
        "summary": description,
    }

    with open(summary_file, "w") as f:
        json.dump(entry_data, f, indent=2)

    print(f"Created release summary: {summary_file}")
    return str(summary_file)


def main():
    parser = argparse.ArgumentParser(description="Create a new changelog entry")
    parser.add_argument(
        "-t",
        "--type",
        # TODO: Prompt the user for confirmation before allowing the 'breaking' or `feature` options.
        choices=(
            "feature",
            "enhancement",
            "bugfix",
            "breaking",
            "dependency",
            "api-change",
            "summary",
        ),
        required=True,
        help="Type of change (use 'summary' for release overview)",
    )
    parser.add_argument(
        "-d", "--description", required=True, help="Description of the change"
    )
    parser.add_argument(
        "-p",
        "--package",
        required=True,
        help="Package name",
    )
    args = parser.parse_args()

    if args.type == "summary":
        create_summary_entry(
            description=args.description,
            package_name=args.package,
        )
    else:
        create_change_entry(
            change_type=args.type,
            description=args.description,
            package_name=args.package,
        )


if __name__ == "__main__":
    main()
