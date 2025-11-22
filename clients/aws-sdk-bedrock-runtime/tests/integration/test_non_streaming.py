# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

"""Test non-streaming output type handling."""

from aws_sdk_bedrock_runtime.client import BedrockRuntimeClient
from aws_sdk_bedrock_runtime.models import (
    ContentBlockText,
    ConverseInput,
    ConverseOperationOutput,
    ConverseOutputMessage,
    Message,
)


async def test_converse(
    bedrock_client: BedrockRuntimeClient, model_id: str, message: str
) -> None:
    input_message = Message(role="user", content=[ContentBlockText(value=message)])
    response = await bedrock_client.converse(
        ConverseInput(model_id=model_id, messages=[input_message])
    )

    assert isinstance(response, ConverseOperationOutput)
    assert isinstance(response.output, ConverseOutputMessage)

    output_message = response.output.value
    assert output_message.role == "assistant"
    assert len(output_message.content) > 0

    content_block = output_message.content[0]
    assert isinstance(content_block, ContentBlockText)
    assert isinstance(content_block.value, str) and content_block.value

    response_text = content_block.value.lower()
    assert "guido" in response_text, (
        f"Expected response to mention 'Guido' (van Rossum). Got: {content_block.value}"
    )

    assert response.usage.input_tokens > 0
    assert response.usage.output_tokens > 0
