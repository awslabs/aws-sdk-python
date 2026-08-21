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
later. Create and activate a virtual environment, then install the clients you
need:

```bash
pip install aws-sdk-dynamodb
```

If your application uses several services, you can instead install the
`aws-sdk-python` meta-package and select clients as extras. It coordinates
compatible client versions through its own `MAJOR.MINOR` version:

```bash
pip install "aws-sdk-python[bedrock_runtime,sts]"
```

See [Available Clients](clients/index.md) for the full list of service
packages.

## Quick example

List your DynamoDB tables with the Amazon DynamoDB client:

```python
import asyncio

from aws_sdk_dynamodb.client import AsyncDynamoDBClient
from aws_sdk_dynamodb.config import AsyncDynamoDBConfig
from aws_sdk_dynamodb.models import ListTablesInput


async def main():
    config = await AsyncDynamoDBConfig.resolve(region="us-east-1")

    async with AsyncDynamoDBClient(config=config) as client:
        response = await client.list_tables(input=ListTablesInput(limit=10))
        for table in response.table_names or []:
            print(table)


asyncio.run(main())
```

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
