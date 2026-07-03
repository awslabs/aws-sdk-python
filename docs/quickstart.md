# Quickstart

This guide walks you through installing a client, configuring credentials,
and making your first request with the AWS SDK for Python. The example uses
the Amazon Bedrock Runtime client to send a message to a model, but the same
steps apply to every client in the SDK.

!!! note "Amazon Bedrock access"

    To run this example, your AWS account needs access to Amazon Bedrock and
    permission to use the model you call. See
    [Getting started with Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/getting-started.html)
    for details.

## Installation

Create and activate a virtual environment and then install the client:

```bash
python -m venv .venv
source .venv/bin/activate
pip install aws-sdk-bedrock-runtime
```

See [Installation](installation.md) for prerequisites and version pinning
guidance.

## Configuration

The SDK signs each request with AWS credentials. This example reads them from
the standard AWS environment variables, so set those before running it:

```bash
export AWS_ACCESS_KEY_ID="your-access-key-id"
export AWS_SECRET_ACCESS_KEY="your-secret-access-key"
export AWS_SESSION_TOKEN="your-session-token"  # (1)!
```

1.  Only required when you use temporary security credentials, such as those
    from an assumed IAM role.

The SDK supports other credential sources as well, such as container and EC2
instance metadata credentials. See [Configuration](configuration.md) for the
full list.

## Using the SDK

Create a file named `quickstart.py` with the following code:

```python
import asyncio

from aws_sdk_bedrock_runtime.client import BedrockRuntimeClient, ConverseInput
from aws_sdk_bedrock_runtime.config import Config
from aws_sdk_bedrock_runtime.models import ContentBlockText, Message
from smithy_aws_core.identity import EnvironmentCredentialsResolver


async def main():
    # Create a client, providing the Region and a credential resolver.
    client = BedrockRuntimeClient(
        config=Config(
            region="us-east-1",
            aws_credentials_identity_resolver=EnvironmentCredentialsResolver(),
        )
    )

    # Every operation is a coroutine, so await the call.
    response = await client.converse(
        ConverseInput(
            model_id="global.anthropic.claude-opus-4-8",  # (1)!
            messages=[
                Message(
                    role="user",
                    content=[
                        ContentBlockText(value="What is the AWS SDK for Python?")
                    ],
                )
            ],
        )
    )

    # The response contains a list of content blocks. Print the text ones.
    for block in response.output.value.content:
        if isinstance(block, ContentBlockText):
            print(block.value)


asyncio.run(main())
```

1.  This model may not be the latest available and could be deprecated in the
    future. See [Models at a glance](https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards.html)
    in the Amazon Bedrock User Guide for the current list of models and their
    IDs.

The program does three things:

- **Creates a client**: Each client takes a `Config` object that provides the
  AWS Region and a credential resolver. `EnvironmentCredentialsResolver` reads
  the environment variables you set above.
- **Calls an operation**: Operations are async and take a typed input object,
  in this case a `ConverseInput` with the model ID and messages to send.
- **Reads the response**: The response is a typed object as well. Here the
  model's reply is a list of content blocks, and the text blocks are printed.

Run the program:

```bash
python quickstart.py
```

The model's reply prints to your terminal:

```text
The AWS SDK for Python provides async, per-service clients for calling AWS
services from Python applications.
```

## Next steps

- Learn how to set the Region, choose a credential resolver, and adjust other
  client settings in [Configuration](configuration.md).
- Stream responses and build real-time applications with
  [Streaming](streaming.md).
- Browse the API reference for every client in
  [Available Clients](clients/index.md).
