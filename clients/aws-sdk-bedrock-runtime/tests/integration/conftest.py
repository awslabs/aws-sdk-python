# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0


from pathlib import Path

import pytest
from smithy_aws_core.identity.chain import create_default_chain
from smithy_http.aio.crt import AWSCRTHTTPClient

from aws_sdk_bedrock_runtime.client import BedrockRuntimeClient
from aws_sdk_bedrock_runtime.config import Config

AWS_REGION = "us-west-2"
ENDPOINT_URI = f"https://bedrock-runtime.{AWS_REGION}.amazonaws.com"
MODEL_ID = "amazon.titan-text-express-v1"
BIDIRECTIONAL_MODEL_ID = "amazon.nova-sonic-v1:0"


@pytest.fixture
async def bedrock_client():
    """Create a new BedrockRuntimeClient with default credential chain."""
    http_client = AWSCRTHTTPClient()
    client = BedrockRuntimeClient(
        config=Config(
            endpoint_uri=ENDPOINT_URI,
            region=AWS_REGION,
            aws_credentials_identity_resolver=create_default_chain(http_client),
            transport=http_client,
        )
    )
    return client


@pytest.fixture
def model_id():
    """Model ID that supports non-streaming and output streaming operations."""
    return MODEL_ID


@pytest.fixture
def bidirectional_model_id():
    """Model ID that supports bidirectional streaming operations."""
    return BIDIRECTIONAL_MODEL_ID


@pytest.fixture
def message():
    """Simple test message for Bedrock operations."""
    return "Who created the Python programming language?"


@pytest.fixture
def audio_file():
    """PCM audio file for bidirectional streaming tests.

    The audio asks: "Who created the Python programming language?"
    Expected response should mention "Guido van Rossum".
    """
    fixtures_dir = Path(__file__).parent / "fixtures"
    audio_file = fixtures_dir / "test.pcm"
    if not audio_file.exists():
        pytest.fail(f"Audio file does not exist: {audio_file}")
    return audio_file
