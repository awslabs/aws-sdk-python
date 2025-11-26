# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0


from pathlib import Path

from smithy_aws_core.identity import EnvironmentCredentialsResolver

from aws_sdk_bedrock_runtime.client import BedrockRuntimeClient
from aws_sdk_bedrock_runtime.config import Config

MODEL_ID = "amazon.titan-text-express-v1"
BIDIRECTIONAL_MODEL_ID = "amazon.nova-sonic-v1:0"
MESSAGE = "Who created the Python programming language?"
AUDIO_FILE = Path(__file__).parent / "assets" / "test.pcm"


def create_bedrock_client(region: str) -> BedrockRuntimeClient:
    """Helper to create a BedrockRuntimeClient for a given region."""
    return BedrockRuntimeClient(
        config=Config(
            endpoint_uri=f"https://bedrock-runtime.{region}.amazonaws.com",
            region=region,
            aws_credentials_identity_resolver=EnvironmentCredentialsResolver(),
        )
    )
