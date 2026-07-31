# scripts/docs/generate_nav.py
"""
Generate client documentation navigation dynamically.

Run this script before mkdocs build to generate:
docs/SUMMARY.md - Navigation file for literate-nav plugin
"""

import logging
import sys

from pathlib import Path


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(name)s - %(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("generate_nav")


def generate_nav(repo_root: Path) -> bool:
    """
    Generate navigation structure for clients using literate-nav SUMMARY.md format.

    Args:
        repo_root: Path to the repository root.

    Returns:
        True if navigation was generated successfully, False otherwise.
    """
    logger.info("⏳ Generating navigation structure...")

    clients_dir = repo_root / "clients"
    if not clients_dir.exists():
        logger.error(f"Clients directory not found: {clients_dir}")
        return False

    # Build the SUMMARY.md content for literate-nav
    lines = [
        "* [Overview](index.md)",
        "* [Contributing](contributing.md)",
        "* [Available Clients](clients/index.md)",
    ]

    # Discover clients and add each as a nested item under Available Clients
    client_count = 0
    for client_path in sorted(clients_dir.iterdir()):
        if not (client_path / "scripts" / "docs" / "generate_doc_stubs.py").exists():
            continue

        # Extract service name and path from package name
        # (e.g., "aws-sdk-bedrock-runtime" -> "Bedrock Runtime" / "bedrock-runtime")
        path_name = client_path.name.replace("aws-sdk-", "")
        display_name = path_name.replace("-", " ").title()

        lines.append(f"    * [{display_name}](clients/{path_name}/index.md)")
        logger.info(f"Discovered client: {display_name}")
        client_count += 1

    logger.info(f"Found {client_count} total clients")

    # Write the SUMMARY.md file to the docs directory
    summary_path = repo_root / "docs" / "SUMMARY.md"
    try:
        summary_path.write_text("\n".join(lines) + "\n")
    except OSError as e:
        logger.error(f"Failed to write SUMMARY.md: {e}")
        return False

    logger.info(f"✅ Generated SUMMARY.md navigation for {client_count} clients")
    return True


def main() -> int:
    """Main entry point to generate navigation."""
    repo_root = Path(__file__).parent.parent.parent

    try:
        if not generate_nav(repo_root):
            return 1
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
