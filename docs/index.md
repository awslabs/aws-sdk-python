# AWS SDK for Python

The AWS SDK for Python provides async-first clients for select AWS services.
Each client is distributed as a lightweight, per-service package.

!!! warning "Developer Preview: Not for production use"

    This SDK is intended for evaluation and testing in pre-production
    environments. APIs and behavior may change before general availability. For
    production workloads, use
    [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html).

[Browse clients](clients/index.md){ .md-button .md-button--primary }
[View source](https://github.com/aws/aws-sdk-python){ .md-button }

## What it provides

Use these clients when your application needs non-blocking access to supported
AWS services, including services with streaming and real-time APIs. The clients
are built on Python's `async`/`await` and generated from
[Smithy](https://smithy.io/) service models.

- **Async operations**: Call AWS services without blocking an `asyncio`
  application.
- **Per-service packages**: Install only the clients your application needs.
- **Type annotations**: Get editor completion and type checking for operations,
  input models, and response models without separate stub packages.
- **Streaming support**: First-class support for event streams and
  bidirectional streaming operations.

## Packages

The clients require Python 3.12 or later. Choose a per-service package or use
the `aws-sdk-python` meta-package for a compatible set of clients.

=== "One service"

    Install only the client you need. For example, install the Amazon DynamoDB
    client with:

    ```bash
    pip install aws-sdk-dynamodb
    ```

=== "Multiple services"

    Select clients as extras of the `aws-sdk-python` meta-package. The
    meta-package selects compatible client versions for you:

    ```bash
    pip install "aws-sdk-python[bedrock_runtime,sts]"
    ```

See [Available Clients](clients/index.md) for the full list of service
packages.

## Example

After you [configure AWS credentials](https://docs.aws.amazon.com/sdkref/latest/guide/standardized-credentials.html)
and grant permission to call `dynamodb:ListTables`, you can list your DynamoDB
tables:

```python
import asyncio

from aws_sdk_dynamodb.client import AsyncDynamoDBClient
from aws_sdk_dynamodb.config import AsyncDynamoDBConfig
from aws_sdk_dynamodb.models import ListTablesInput


async def main():
    config = await AsyncDynamoDBConfig.resolve(region="us-east-1")
    client = AsyncDynamoDBClient(config=config)

    response = await client.list_tables(input=ListTablesInput(limit=10))
    for table in response.table_names or []:
        print(table)


asyncio.run(main())
```

The configuration resolver can load credentials and other shared settings from
the standard AWS configuration sources. Each client operation accepts a typed
input model and returns a typed response model.

## Next steps

- Browse the [available clients and API reference](clients/index.md).
- Learn how to [contribute to the SDK](contributing.md).
- [Open a GitHub issue](https://github.com/aws/aws-sdk-python/issues/new/choose)
  to report a problem or share feedback.
