# invoke_model_with_bidirectional_stream

## Operation

::: aws_sdk_bedrock_runtime.client.BedrockRuntimeClient.invoke_model_with_bidirectional_stream
    options:
        heading_level: 3

## Input

::: aws_sdk_bedrock_runtime.models.InvokeModelWithBidirectionalStreamOperationInput
    options:
        heading_level: 3

## Output

This operation returns a `DuplexEventStream` for bidirectional streaming.

### Event Stream Structure

#### Input Event Type

[`InvokeModelWithBidirectionalStreamInput`](../unions/InvokeModelWithBidirectionalStreamInput.md)

#### Output Event Type

[`InvokeModelWithBidirectionalStreamOutput`](../unions/InvokeModelWithBidirectionalStreamOutput.md)

### Initial Response Structure

::: aws_sdk_bedrock_runtime.models.InvokeModelWithBidirectionalStreamOperationOutput
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
