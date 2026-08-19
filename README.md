## AWS SDK for Python (Developer Preview)
[![Apache 2 licensed][apache-badge]][apache-url]

[apache-badge]: https://img.shields.io/badge/license-APACHE2-blue.svg
[apache-url]: https://github.com/aws/aws-sdk-python/blob/main/LICENSE

> **Developer Preview — Not for production use**
>
> This SDK is in **Developer Preview** and is intended for evaluation and testing in pre-production environments only. Do not use it for production workloads. APIs and behavior might change before general availability.
>
> **For production deployments, use [Boto3](https://github.com/boto/boto3)** — the established, generally available AWS SDK for Python with full coverage of all AWS services.

---

This repository contains the next-generation AWS SDK for Python, rebuilt from
the ground up with an async-first, modular architecture. These new clients allow
you to interact with select AWS services using Python's native `async`/`await`
functionality. Unlike Boto3, these clients are distributed per-service, leaving
you the option to install only what fits your needs.

### Key features

+ **Native asynchronous APIs** — Service clients use Python `async` and `await` for non-blocking operations and concurrent I/O.
+ **Bidirectional streaming** — Supported clients can send and receive event streams concurrently over HTTP/2.
+ **Modular packages** — Each service client is available as a separate package (e.g., `aws-sdk-dynamodb`), reducing the dependencies you install and deploy.
+ **Generated types** — Type annotations provide editor completion and static-analysis support.

### When to use this SDK vs. Boto3

| | **This SDK (Developer Preview)** | **[Boto3](https://github.com/boto/boto3) (GA — Production Ready)** |
| --- | --- | --- |
| Release status | Developer Preview | General Availability |
| Production use | Not recommended | Yes |
| Architecture | Async-first, modular per-service packages | Synchronous, monolithic package |
| Service coverage | 24 services (expanding) | All AWS services |

**Choose [Boto3](https://github.com/boto/boto3) if you** need production stability, full AWS service coverage, synchronous workloads, or features like paginators, waiters, and presigned URLs.

**Choose this SDK if you** are evaluating native async capabilities, building high-throughput async prototypes, working with streaming services in test environments, or want to provide feedback to shape the GA release.

## Installation

The SDK requires Python 3.12 or later and publishes a separate package for
each AWS service client. Install the client packages that the following
examples use:

```
python -m pip install aws-sdk-sts aws-sdk-bedrock-runtime
```

This command installs both clients as individual packages.

Alternatively, install the same clients as optional dependencies of the
`aws-sdk-python` meta-package:

```
python -m pip install "aws-sdk-python[sts,bedrock_runtime]"
```

The meta-package installs only the service clients that you select as extras;
without extras, it installs no clients. It coordinates client versions through
its MAJOR.MINOR version, so it installs compatible client versions together.

Use the meta-package when your application depends on several clients. Install
individual client packages when your application uses only one or two services
and you want the smallest dependency set.

### Bidirectional streaming transport

Some operations use bidirectional (duplex) event streams. The default aiohttp
transport doesn't support duplex streaming. To use these operations, install
the client's `awscrt` extra and set `AWSCRTHTTPClient` as the transport:

```
python -m pip install "aws-sdk-bedrock-runtime[awscrt]"
```

```python
from aws_sdk_bedrock_runtime.client import AsyncBedrockRuntimeClient
from aws_sdk_bedrock_runtime.config import AsyncBedrockRuntimeConfig
from smithy_http.aio.crt import AWSCRTHTTPClient


async def create_client() -> AsyncBedrockRuntimeClient:
    config = await AsyncBedrockRuntimeConfig.resolve(
        region="us-east-1",
        transport=AWSCRTHTTPClient(),
    )
    return AsyncBedrockRuntimeClient(config=config)
```

## Quick start

The following example calls Amazon STS `GetCallerIdentity` to verify your
setup. The example doesn't configure the AWS Region or credentials in code.
The SDK reads the Region from the `AWS_REGION` environment variable or your
shared AWS config file, and resolves credentials from default sources such
as environment variables and the shared AWS `credentials` file. For
credential setup instructions and the authentication methods the Developer
Preview supports, see
[Authenticating with AWS](https://docs.aws.amazon.com/sdk-for-python/v1/guide/getting-started-authentication.html)
in the developer guide.

```python
import asyncio

from aws_sdk_sts.client import AsyncSTSClient
from aws_sdk_sts.models import GetCallerIdentityInput


async def main():
    async with AsyncSTSClient() as client:
        response = await client.get_caller_identity(GetCallerIdentityInput())
        print(f"Account: {response.account}")
        print(f"Arn: {response.arn}")


if __name__ == "__main__":
    asyncio.run(main())
```

## Resources

+ [SDK Homepage](https://aws.amazon.com/sdk-for-python/)
+ [Developer Guide](https://docs.aws.amazon.com/sdk-for-python/v1/guide/welcome.html)
+ [API Reference](https://docs.aws.amazon.com/sdk-for-python/v1/reference/)

## Feedback

The SDK uses **GitHub Issues** to track feature requests and issues with the SDK.
You can provide feedback or report a bug by submitting an [issue](https://github.com/aws/aws-sdk-python/issues/new/choose).
This is the preferred mechanism to give feedback so that other users can engage in the conversation, +1 issues, etc.

## Security

See [CONTRIBUTING](https://github.com/aws/aws-sdk-python/blob/develop/CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This project is licensed under the Apache-2.0 License.
