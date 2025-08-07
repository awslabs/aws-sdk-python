# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
import importlib.metadata

__version__: str = importlib.metadata.version(__name__)

# TODO: Consider adding relative imports for services from the top level namespace?
