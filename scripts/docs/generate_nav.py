# scripts/docs/generate_nav.py
"""
Generate client documentation navigation dynamically.

Run this script before `zensical build` to regenerate the `nav` block in
zensical.toml (delimited by AUTO-NAV markers) so newly added clients show up
in the sidebar without manual edits.
"""

import logging
import sys

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


def _toml_key(value: str) -> str:
    """Quote a string for use as a TOML key, escaping as a basic string."""
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def build_nav_block(clients_dir: Path) -> str:
    """
    Build the TOML `nav` block mirroring the curated documentation structure.

    Args:
        clients_dir: Path to the clients directory.

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
    clients = discover_clients(clients_dir)
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
    if not clients_dir.exists():
        logger.error(f"Clients directory not found: {clients_dir}")
        return False

    config_path = repo_root / "zensical.toml"
    try:
        config = config_path.read_text()
    except OSError as e:
        logger.error(f"Failed to read {config_path.name}: {e}")
        return False

    if NAV_START_MARKER not in config or NAV_END_MARKER not in config:
        logger.error(
            f"AUTO-NAV markers not found in {config_path.name}. "
            f"Expected '{NAV_START_MARKER}' and '{NAV_END_MARKER}'."
        )
        return False

    nav_block = build_nav_block(clients_dir)

    before, _, rest = config.partition(NAV_START_MARKER)
    _, _, after = rest.partition(NAV_END_MARKER)
    updated = f"{before}{NAV_START_MARKER}\n{nav_block}\n{NAV_END_MARKER}{after}"

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
