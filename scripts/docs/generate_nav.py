# scripts/docs/generate_nav.py
"""
Generate client documentation navigation dynamically.

Run this script before `zensical build` to regenerate the `nav` block in
zensical.toml (delimited by AUTO-NAV markers) so newly added clients show up
in the sidebar without manual edits.
"""

import logging
import sys

from datetime import datetime, timezone
from pathlib import Path

from generate_all_doc_stubs import discover_clients


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(name)s - %(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("generate_nav")

# Markers in zensical.toml that bound the generated `nav` block.
NAV_START_MARKER = "# >>> AUTO-NAV >>>"
NAV_END_MARKER = "# <<< AUTO-NAV <<<"

# Markers in zensical.toml that bound the generated `copyright` line.
COPYRIGHT_START_MARKER = "# >>> AUTO-COPYRIGHT >>>"
COPYRIGHT_END_MARKER = "# <<< AUTO-COPYRIGHT <<<"


def _replace_block(config: str, start: str, end: str, body: str) -> str:
    """Replace the content between two markers (inclusive of newlines)."""
    if start not in config or end not in config:
        raise ValueError(f"Markers not found. Expected '{start}' and '{end}'.")
    before, _, rest = config.partition(start)
    _, _, after = rest.partition(end)
    return f"{before}{start}\n{body}\n{end}{after}"


def _toml_key(value: str) -> str:
    """Quote a string for use as a TOML key, escaping as a basic string."""
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def build_nav_block(clients_dir: Path, models_dir: Path) -> str:
    """
    Build the TOML `nav` block mirroring the curated documentation structure.

    Args:
        clients_dir: Path to the clients directory.
        models_dir: Path to the Smithy models directory.

    Returns:
        The `nav = [...]` TOML snippet (without the surrounding markers).
    """
    lines = [
        "nav = [",
        '  { Overview = "index.md" },',
        '  { Contributing = "contributing.md" },',
        '  { "Available Clients" = [',
        '    "clients/index.md",',
    ]

    # Discover clients and add each as a nested item under Available Clients
    clients = discover_clients(clients_dir, models_dir)
    for client in clients:
        lines.append(
            f"    {{ {_toml_key(client.service_name)} = "
            f'"clients/{client.path_name}/index.md" }},'
        )
        logger.info(f"Discovered client: {client.service_name}")

    lines.append("  ] },")
    lines.append("]")

    logger.info(f"Found {len(clients)} total clients")
    return "\n".join(lines)


def generate_nav(repo_root: Path) -> bool:
    """
    Regenerate the AUTO-NAV block in zensical.toml for all clients.

    Args:
        repo_root: Path to the repository root.

    Returns:
        True if navigation was generated successfully, False otherwise.
    """
    logger.info("⏳ Generating navigation structure...")

    clients_dir = repo_root / "clients"
    models_dir = repo_root / "codegen" / "aws-models"
    if not clients_dir.exists():
        logger.error(f"Clients directory not found: {clients_dir}")
        return False

    config_path = repo_root / "zensical.toml"
    try:
        config = config_path.read_text()
    except OSError as e:
        logger.error(f"Failed to read {config_path.name}: {e}")
        return False

    year = datetime.now(timezone.utc).year
    copyright_line = (
        f'copyright = "&copy; {year}, Amazon Web Services, Inc. '
        f'or its affiliates. All rights reserved."'
    )
    try:
        updated = _replace_block(
            config,
            NAV_START_MARKER,
            NAV_END_MARKER,
            build_nav_block(clients_dir, models_dir),
        )
        updated = _replace_block(
            updated, COPYRIGHT_START_MARKER, COPYRIGHT_END_MARKER, copyright_line
        )
    except ValueError as e:
        logger.error(f"Failed to update {config_path.name}: {e}")
        return False
    logger.info(f"Set copyright year to {year}")

    try:
        config_path.write_text(updated)
    except OSError as e:
        logger.error(f"Failed to write {config_path.name}: {e}")
        return False

    logger.info(f"✅ Regenerated navigation in {config_path.name}")
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
