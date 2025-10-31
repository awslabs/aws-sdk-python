# invoke_model_with_response_stream

## Operation

::: aws_sdk_bedrock_runtime.client.BedrockRuntimeClient.invoke_model_with_response_stream
    options:
        heading_level: 3

## Input

::: aws_sdk_bedrock_runtime.models.InvokeModelWithResponseStreamInput
    options:
        heading_level: 3

## Output

This operation returns an `OutputEventStream` for server-to-client streaming.

### Event Stream Structure

#### Output Event Type

[`ResponseStream`](../unions/ResponseStream.md)

### Initial Response Structure

::: aws_sdk_bedrock_runtime.models.InvokeModelWithResponseStreamOutput
    options:
        heading_level: 4

## Errors

- [`AccessDeniedException`](../errors/AccessDeniedException.md)

- [`InternalServerException`](../errors/InternalServerException.md)

- [`ModelErrorException`](../errors/ModelErrorException.md)

- [`ModelNotReadyException`](../errors/ModelNotReadyException.md)

- [`ModelStreamErrorException`](../errors/ModelStreamErrorException.md)

- [`ModelTimeoutException`](../errors/ModelTimeoutException.md)

- [`ResourceNotFoundException`](../errors/ResourceNotFoundException.md)

- [`ServiceQuotaExceededException`](../errors/ServiceQuotaExceededException.md)

- [`ServiceUnavailableException`](../errors/ServiceUnavailableException.md)

- [`ThrottlingException`](../errors/ThrottlingException.md)

- [`ValidationException`](../errors/ValidationException.md)
