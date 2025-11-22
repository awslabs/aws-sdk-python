# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

"""Test output streaming event stream handling."""

from aws_sdk_bedrock_runtime.client import BedrockRuntimeClient
from aws_sdk_bedrock_runtime.models import (
    ContentBlockDeltaText,
    ContentBlockText,
    ConverseStreamInput,
    ConverseStreamOperationOutput,
    ConverseStreamOutputContentBlockDelta,
    ConverseStreamOutputMetadata,
    Message,
)


async def test_converse_stream(
    bedrock_client: BedrockRuntimeClient, model_id: str, message: str
) -> None:
    input_message = Message(role="user", content=[ContentBlockText(value=message)])
    response = await bedrock_client.converse_stream(
        ConverseStreamInput(model_id=model_id, messages=[input_message])
    )

    received_text: list[str] = []
    metadata_received = False

    async with response as stream:
        async for event in stream.output_stream:
            if isinstance(event, ConverseStreamOutputContentBlockDelta):
                delta = event.value.delta
                if isinstance(delta, ContentBlockDeltaText):
                    received_text.append(delta.value)
            elif isinstance(event, ConverseStreamOutputMetadata):
                metadata_received = True
                assert event.value.usage.input_tokens > 0
                assert event.value.usage.output_tokens > 0

        full_response = "".join(received_text)
        assert full_response

        response_text = full_response.lower()
        assert "guido" in response_text, (
            f"Expected response to mention 'Guido' (van Rossum). Got: {full_response}"
        )

        assert metadata_received
        assert isinstance(stream.output, ConverseStreamOperationOutput)
