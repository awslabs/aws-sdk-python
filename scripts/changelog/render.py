#!/usr/bin/env python3
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
"""
Render changelog entries from version JSON files using Jinja templates.
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import IO, Any

from jinja2 import Template
from utils import get_package_changes_dir

PROJECT_ROOT_DIR = Path(__file__).resolve().parent.parent.parent

TEMPLATES_DIR = PROJECT_ROOT_DIR / "scripts" / "changelog" / "templates"
DEFAULT_TEMPLATE_NAME = "PACKAGE"
VERSION_FILE_PATTERN = r"^\d+\.\d+\.\d+\.json$"


def get_sorted_versions(changes_dir: Path, reverse: bool = True) -> list[str]:
    """Get sorted list of version numbers from .changes directory."""
    version_pattern = re.compile(VERSION_FILE_PATTERN)
    versions: list[str] = []

    for file in changes_dir.iterdir():
        if file.is_file() and version_pattern.match(file.name):
            versions.append(file.stem)

    # Sort by semantic version (reverse if True)
    versions.sort(key=lambda v: [int(x) for x in v.split(".")], reverse=reverse)
    return versions


def load_package_releases(changes_dir: Path) -> dict[str, dict[str, Any]]:
    """Load all changelog entries from version JSON files."""
    releases: dict[str, dict[str, Any]] = {}

    for version_number in get_sorted_versions(changes_dir, reverse=True):
        filename = changes_dir / f"{version_number}.json"
        try:
            with open(filename) as f:
                data = json.load(f)
            # Restructure data to match PACKAGE template expectations
            changes = data.get("changes", [])
            formatted_changes = [
                {
                    "type": change.get("type", "enhancement"),
                    "description": change.get("description", ""),
                }
                for change in changes
            ]

            release_data: dict[str, Any] = {
                "changes": formatted_changes,
            }

            # Include summary if present
            if "summary" in data:
                release_data["summary"] = data["summary"]

            releases[version_number] = release_data
        except (OSError, json.JSONDecodeError) as e:
            print(f"Warning: Could not process {filename}: {e}", file=sys.stderr)
            continue

    return releases


def render_changes(
    changes: dict[str, dict[str, Any]], out: IO[str], template_contents: str
) -> None:
    """Render changelog using Jinja template."""
    # Reverse order to show newest first
    context: dict[str, Any] = {"releases": list(changes.items())}

    template = Template(template_contents)

    result = template.render(**context)
    out.write(result)


def render_package_changelog(
    package_name: str, template_name: str | None = None, output_path: Path | None = None
) -> int:
    # Get changes directory (validates package exists)
    changes_dir = get_package_changes_dir(package_name)

    if not changes_dir.exists():
        print(
            f"No .changes directory found for package: {package_name}", file=sys.stderr
        )
        return 1

    # Load changes from the directory
    changes: dict[str, dict[str, Any]] = load_package_releases(changes_dir)

    if not changes:
        print(f"No version JSON files found in {changes_dir}", file=sys.stderr)
        return 1

    # Get template contents
    template_path = TEMPLATES_DIR / (template_name or DEFAULT_TEMPLATE_NAME)

    if not template_path.exists():
        print(f"Template not found: {template_path}", file=sys.stderr)
        return 1

    try:
        with open(template_path) as f:
            template_contents = f.read()
    except OSError as e:
        print(f"Error reading template {template_path}: {e}", file=sys.stderr)
        return 1

    # Render to output
    if output_path:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w") as f:
            render_changes(changes, f, template_contents)
        print(f"Changelog written to: {output_path}")
    else:
        render_changes(changes, sys.stdout, template_contents)

    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Render package changelog from changes files"
    )
    parser.add_argument(
        "-p",
        "--package",
        required=True,
        help="Package name (looks in clients/<name>/.changes)",
    )
    parser.add_argument(
        "-t",
        "--template",
        help=f"Template name (looks in scripts/changelog/templates/, defaults to '{DEFAULT_TEMPLATE_NAME}')",
    )
    parser.add_argument(
        "-o", "--output", type=Path, help="Output file path (default: stdout)"
    )

    args = parser.parse_args()
    return render_package_changelog(
        package_name=args.package, template_name=args.template, output_path=args.output
    )


if __name__ == "__main__":
    exit(main())
