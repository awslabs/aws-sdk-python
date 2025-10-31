# converse_stream

## Operation

::: aws_sdk_bedrock_runtime.client.BedrockRuntimeClient.converse_stream
    options:
        heading_level: 3

## Input

::: aws_sdk_bedrock_runtime.models.ConverseStreamInput
    options:
        heading_level: 3

## Output

This operation returns an `OutputEventStream` for server-to-client streaming.

### Event Stream Structure

#### Output Event Type

[`ConverseStreamOutput`](../unions/ConverseStreamOutput.md)

### Initial Response Structure

::: aws_sdk_bedrock_runtime.models.ConverseStreamOperationOutput
    options:
        heading_level: 4

## Errors

- [`AccessDeniedException`](../errors/AccessDeniedException.md)

- [`InternalServerException`](../errors/InternalServerException.md)

- [`ModelErrorException`](../errors/ModelErrorException.md)

- [`ModelNotReadyException`](../errors/ModelNotReadyException.md)

- [`ModelTimeoutException`](../errors/ModelTimeoutException.md)

- [`ResourceNotFoundException`](../errors/ResourceNotFoundException.md)

- [`ServiceUnavailableException`](../errors/ServiceUnavailableException.md)

- [`ThrottlingException`](../errors/ThrottlingException.md)

- [`ValidationException`](../errors/ValidationException.md)
