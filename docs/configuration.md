# Configuration

Each service client takes a `Config` object that controls how the client
makes requests: the AWS Region to call, the credentials to sign requests
with, and other settings such as endpoints and retries. This page covers the
settings you are most likely to need.

## The Config object

Every client package includes its own `Config` class in its `config` module.
Create a `Config`, set the options you need, and pass it to the client:

```python
from aws_sdk_bedrock_runtime.client import BedrockRuntimeClient
from aws_sdk_bedrock_runtime.config import Config
from smithy_aws_core.identity import EnvironmentCredentialsResolver

client = BedrockRuntimeClient(
    config=Config(
        region="us-east-1",
        aws_credentials_identity_resolver=EnvironmentCredentialsResolver(),
    )
)
```

The SDK resolves configuration values from a series of sources, in order:

1. Any explicit setting in code takes precedence over everything else.
2. Environment variables are checked next. At this time, environment
   variables are only used to obtain credentials through
   `EnvironmentCredentialsResolver`.
3. Defaults provided by the SDK itself are used last.

Some settings, such as the Region, have no default. If the SDK cannot resolve
a required setting, requests fail at runtime.

## Setting the Region

Most AWS resources reside in a specific AWS Region, and you must supply the
correct Region for the resources you use. Set the `region` property on the
`Config` object:

```python
config = Config(
    region="us-east-1",
    aws_credentials_identity_resolver=EnvironmentCredentialsResolver(),
)
```

For more information on how Regions are used, see
[AWS Region](https://docs.aws.amazon.com/sdkref/latest/guide/feature-region.html)
in the AWS SDKs and Tools Reference Guide.

The SDK does not currently read the `AWS_REGION` environment variable
automatically. To use it, read the variable yourself:

```python
import os

config = Config(
    region=os.environ["AWS_REGION"],
    aws_credentials_identity_resolver=EnvironmentCredentialsResolver(),
)
```

## Credentials

The SDK signs requests with AWS credentials, retrieved through a credential
resolver you set on the `Config` object. The following resolvers are
available from the `smithy_aws_core.identity` module:

- **`EnvironmentCredentialsResolver`**: Resolves credentials from the
  environment variables `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and
  `AWS_SESSION_TOKEN`.
- **`ContainerCredentialsResolver`**: Obtains credentials from a container
  credential service, such as the ones provided by Amazon ECS and Amazon EKS.
- **`IMDSCredentialsResolver`**: Obtains credentials from an Amazon EC2
  instance's metadata using the Instance Metadata Service (IMDS).
- **`StaticCredentialsResolver`**: Uses the static credentials set directly
  on the `Config` object through its `aws_access_key_id`,
  `aws_secret_access_key`, and `aws_session_token` properties.

!!! note

    Not all AWS credential providers are supported yet. Only the resolvers
    listed above can be used at this time. In particular, the SDK does not
    yet read the shared AWS config and credentials files, so profiles
    configured with the AWS CLI are not picked up automatically.

Set the resolver you want on the `aws_credentials_identity_resolver`
property:

```python
from smithy_aws_core.identity import IMDSCredentialsResolver

config = Config(
    region="us-east-1",
    aws_credentials_identity_resolver=IMDSCredentialsResolver(),
)
```

For guided options on setting up AWS authentication for your project, see
[Authentication and access](https://docs.aws.amazon.com/sdkref/latest/guide/access.html)
in the AWS SDKs and Tools Reference Guide.

## Other settings

The `Config` object accepts several other options. The most commonly useful
ones are:

- **`endpoint_uri`**: A static URI to route requests to, in place of the
  endpoint the SDK derives from the Region. Useful for testing against local
  or non-standard endpoints.
- **`retry_strategy`**: The retry strategy or options for configuring retry
  behavior. See [Error handling](error-handling.md) for details.
- **`user_agent_extra`**: An additional suffix added to the `User-Agent`
  header, useful for tracking your application's requests in logs.

```python
config = Config(
    region="us-east-1",
    aws_credentials_identity_resolver=EnvironmentCredentialsResolver(),
    endpoint_uri="http://localhost:8080",
)
```

See each client's API reference in [Available Clients](clients/index.md) for
the full list of configuration options.
