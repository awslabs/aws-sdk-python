# AWS SDK for Python

The AWS SDK for Python provides asynchronous clients for supported AWS services.
Each service has its own package.

!!! warning "Developer preview: Not for production use"

    Use this SDK for evaluation and pre-production testing. Interfaces and
    behavior may change before general availability. Use
    [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
    for production workloads.

[Browse clients](clients/index.md){ .md-button .md-button--primary }
[View source](https://github.com/aws/aws-sdk-python){ .md-button }

## Features

- **Async operations.** Every service operation is an `async` method that works
  with `asyncio`.
- **Per-service packages.** Install only the clients your application uses.
- **Type annotations.** Operations, input models, and response models include
  type annotations, so editors and type checkers do not need separate stub
  packages.
- **Streaming support.** Clients for streaming services support event streams
  and bidirectional streaming.

The code generator builds each client from its service's
[Smithy](https://smithy.io/) model.

## Install a client

The clients require Python 3.12 or later.

=== "One client"

    Install the Amazon DynamoDB client from its service package:

    ```bash
    pip install aws-sdk-dynamodb
    ```

=== "Several clients"

    The `aws-sdk-python` meta-package keeps its client dependencies on
    compatible versions. Select the clients you need through package extras:

    ```bash
    pip install "aws-sdk-python[bedrock_runtime,sts]"
    ```

The [available clients](clients/index.md) page lists every service package.

## List DynamoDB tables

After you [configure AWS credentials](https://docs.aws.amazon.com/sdkref/latest/guide/standardized-credentials.html)
and grant `dynamodb:ListTables` permission, use the
[Amazon DynamoDB client](clients/dynamodb/index.md) to list up to ten tables in
`us-east-1`:

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

`AsyncDynamoDBConfig.resolve()` loads credentials and other shared settings
from the standard AWS configuration sources. The `region` argument overrides
the configured region for this client.

## Documentation and support

- [Browse client API references](clients/index.md)
- [Contribute to the SDK](contributing.md)
- [Report a bug or request a feature](https://github.com/aws/aws-sdk-python/issues/new/choose)
