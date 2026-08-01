"""Utilities for reading service metadata from Smithy models."""

import json
from pathlib import Path
from typing import Any


_AWS_SERVICE_TRAIT = "aws.api#service"


def get_sdk_id(model_path: Path) -> str:
    """Return the SDK ID from the service shape in a Smithy model."""
    model: dict[str, Any] = json.loads(model_path.read_text())
    service_shapes = [
        shape
        for shape in model.get("shapes", {}).values()
        if shape.get("type") == "service"
    ]

    if len(service_shapes) != 1:
        raise ValueError(
            f"Expected exactly one service shape in {model_path}, "
            f"found {len(service_shapes)}"
        )

    sdk_id = (
        service_shapes[0].get("traits", {}).get(_AWS_SERVICE_TRAIT, {}).get("sdkId")
    )
    if not isinstance(sdk_id, str) or not sdk_id:
        raise ValueError(f"Missing {_AWS_SERVICE_TRAIT}.sdkId in {model_path}")

    return sdk_id
