# Error handling

When a request fails, the SDK raises a typed exception. Service errors are
generated from each service's API model, so you can catch the exact error a
service returns, read its details, and decide how to respond.

## Exception hierarchy

Every exception the SDK raises derives from a small set of base classes:

- **Service-specific errors**: Each client's `models` module defines a class
  for every error its service returns, such as `ThrottlingException`,
  `ValidationException`, and `AccessDeniedException` in
  `aws_sdk_bedrock_runtime.models`. Catch these to handle a specific failure.
- **`ServiceError`**: Also defined in each client's `models` module, this is
  the base class for all of that service's errors. Catch it to handle any
  error the service returns.
- **`CallError`**: Defined in `smithy_core.exceptions`, this is the base
  class for request-level errors and carries the attributes described below.
- **`SmithyError`**: Also defined in `smithy_core.exceptions`, this is the
  root of the hierarchy. Catch it to handle anything that goes wrong inside
  the SDK, including serialization and connection failures.

## Catching errors

Catch the most specific exception first and fall back to the broader base
classes:

```python
from aws_sdk_bedrock_runtime.models import (
    ServiceError,
    ThrottlingException,
    ValidationException,
)
from smithy_core.exceptions import SmithyError

try:
    response = await client.converse(converse_input)
except ThrottlingException:
    print("Request was throttled. Slow down and try again later.")
except ValidationException as e:
    print(f"Invalid request: {e.message}")
except ServiceError as e:
    print(f"The service returned an error: {e.message}")
except SmithyError as e:
    print(f"The request failed: {e}")
```

Each client's API reference in [Available Clients](clients/index.md)
documents the errors its operations can raise.

## Error attributes

Every service error carries these attributes from `CallError`:

- **`message`**: The error message returned by the service.
- **`fault`**: Whether the `"client"` or `"server"` was at fault, or `None`
  when the SDK cannot tell.
- **`is_retry_safe`**: Whether the request is safe to retry.
- **`retry_after`**: How many seconds the service asked you to wait before
  retrying, when the service provides one.

## Retries

The SDK retries safe-to-retry errors automatically before raising them. The
default strategy makes up to 3 attempts in total, waiting between attempts
with exponential backoff and jitter, and honoring the `retry_after` hint when
the service provides one. If every attempt fails, the final error is raised
to your code.

Configure retry behavior by setting `retry_strategy` on the `Config` object:

```python
from smithy_core.retries import RetryStrategyOptions

config = Config(
    region="us-east-1",
    aws_credentials_identity_resolver=EnvironmentCredentialsResolver(),
    retry_strategy=RetryStrategyOptions(max_attempts=5),
)
```

`RetryStrategyOptions` accepts two settings:

- **`max_attempts`**: The upper limit on total attempts, including the
  initial attempt and all retries.
- **`retry_mode`**: The retry strategy to use. The default, `"standard"`,
  adds a retry quota that stops retrying when too many recent requests have
  failed. The alternative, `"simple"`, retries with exponential backoff only.

To disable retries entirely, set `max_attempts` to 1:

```python
retry_strategy=RetryStrategyOptions(max_attempts=1)
```
