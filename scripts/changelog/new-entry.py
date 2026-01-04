#!/usr/bin/env python3
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
"""
Create new changelog entries for a specific package.
"""

import argparse
import json
import time
import uuid
from pathlib import Path

PROJECT_ROOT_DIR = Path(__file__).resolve().parent.parent.parent


def get_package_changes_dir(package_name: str) -> Path:
    package_path = PROJECT_ROOT_DIR / "clients" / package_name
    changes_dir = package_path / ".changes"
    return changes_dir


def create_change_entry(
    change_type: str,
    description: str,
    package_name: str,
) -> str:
    # Get package .changes directory and ensure it exists
    changes_dir = get_package_changes_dir(package_name)
    changes_dir.mkdir(exist_ok=True)

    # Create next-release directory for pending changes
    next_release_dir = changes_dir / "next-release"
    next_release_dir.mkdir(exist_ok=True)

    # Generate unique filename
    timestamp = int(time.time() * 1_000_000)
    unique_id = uuid.uuid4().hex
    filename = f"{package_name}-{change_type}-{timestamp}-{unique_id}.json"

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
    # Get package .changes directory and ensure it exists
    changes_dir = get_package_changes_dir(package_name)
    changes_dir.mkdir(exist_ok=True)

    # Create next-release directory for pending changes
    next_release_dir = changes_dir / "next-release"
    next_release_dir.mkdir(exist_ok=True)

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
        # TODO: Remove the 'breaking' option once this project is stable.
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
