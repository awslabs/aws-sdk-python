# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

from pathlib import Path

from smithy_aws_core.identity import EnvironmentCredentialsResolver

from aws_sdk_transcribe_streaming.client import TranscribeStreamingClient
from aws_sdk_transcribe_streaming.config import AsyncTranscribeStreamingConfig

AUDIO_FILE = Path(__file__).parent / "assets" / "test.wav"


async def create_transcribe_client(region: str) -> TranscribeStreamingClient:
    """Helper to create a TranscribeStreamingClient for a given region."""
    return TranscribeStreamingClient(
        config=await AsyncTranscribeStreamingConfig.resolve(
            endpoint_uri=f"https://transcribestreaming.{region}.amazonaws.com",
            region=region,
            aws_credentials_identity_resolver=EnvironmentCredentialsResolver(),
        )
    )
