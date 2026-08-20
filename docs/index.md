# AWS SDK for Python

Async-first clients for AWS services, distributed as one lightweight package
per service.

Unlike [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html),
these clients are built from the ground up on Python's `async`/`await`. They
target select AWS services that benefit most from asynchronous I/O, such as
streaming and real-time inference APIs. Each client is generated from its
service's [Smithy](https://smithy.io/) model and is fully type-annotated, so
your editor can autocomplete operations, inputs, and response shapes without
extra stub packages.

!!! warning "Developer Preview — not for production use"

    This SDK is in Developer Preview and is intended for evaluation and testing
    in pre-production environments only. APIs and behavior may change before
    general availability. For production workloads, use
    [Boto3](https://github.com/boto/boto3) — the generally available AWS SDK
    for Python with full coverage of all AWS services.

## Highlights

- **Async first**: Every operation is a coroutine, designed for
  `asyncio`-based applications.
- **Per-service packages**: Install only the clients you need. Each package is
  versioned and released independently.
- **Fully typed**: Generated dataclass models and annotated signatures for
  every operation.
- **Streaming support**: First-class support for event streams and
  bidirectional streaming operations.

## Installation

Each service client is its own package on PyPI and requires Python 3.12 or
later. Create and activate a virtual environment and then install the clients
you need:

```bash
pip install aws-sdk-bedrock-runtime
```

See [Available Clients](clients/index.md) for the full list of service
packages.

## Quick example

Send a message to a model with the Amazon Bedrock Runtime client:

```python
import asyncio

from aws_sdk_bedrock_runtime.client import BedrockRuntimeClient, ConverseInput
from aws_sdk_bedrock_runtime.config import Config
from aws_sdk_bedrock_runtime.models import ContentBlockText, Message
from smithy_aws_core.identity import EnvironmentCredentialsResolver


async def main():
    client = BedrockRuntimeClient(
        config=Config(
            region="us-east-1",
            aws_credentials_identity_resolver=EnvironmentCredentialsResolver(),
        )
    )

    response = await client.converse(
        ConverseInput(
            model_id="global.anthropic.claude-opus-4-8",  # (1)!
            messages=[
                Message(
                    role="user",
                    content=[ContentBlockText(value="Tell me a fun fact about Python.")],
                )
            ],
        )
    )

    print(response.output.value.content[0].value)


asyncio.run(main())
```

1.  This model may not be the latest available and could be deprecated in the
    future. See [Models at a glance](https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards.html)
    in the Amazon Bedrock User Guide for the current list of models and their
    IDs.

## Explore

<div class="grid cards" markdown>

- **Available Clients**

    ---

    Browse the full API reference for every service client in the SDK.

    [:octicons-arrow-right-24: Available Clients](clients/index.md)

- **Contributing**

    ---

    Learn how to report issues, propose changes, and set up a development
    environment.

    [:octicons-arrow-right-24: Contributing](contributing.md)

- **Feedback**

    ---

    We welcome all feedback while we develop, and we use it to drive the
    direction of the SDK. Tell us what you like, dislike, or want to see next.

    [:octicons-arrow-right-24: Open a GitHub issue](https://github.com/aws/aws-sdk-python/issues/new/choose)

</div>
