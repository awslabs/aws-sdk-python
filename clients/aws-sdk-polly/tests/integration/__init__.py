# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

from smithy_aws_core.identity import EnvironmentCredentialsResolver

from aws_sdk_polly.client import PollyClient
from aws_sdk_polly.config import Config

REGION = "us-east-1"
VOICE_ID = "Matthew"
ENGINE = "generative"
OUTPUT_FORMAT = "mp3"
SAMPLE_RATE = "24000"
TEST_TEXT = "Hello from the AWS SDK for Python Polly integration tests."


def create_polly_client(region: str) -> PollyClient:
    """Helper to create a PollyClient for a given region."""
    return PollyClient(
        config=Config(
            endpoint_uri=f"https://polly.{region}.amazonaws.com",
            region=region,
            aws_credentials_identity_resolver=EnvironmentCredentialsResolver(),
        )
    )
