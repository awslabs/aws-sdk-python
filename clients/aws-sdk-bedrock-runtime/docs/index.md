# Bedrock Runtime

## Client

::: aws_sdk_bedrock_runtime.client.BedrockRuntimeClient
    options:
        merge_init_into_class: true
        docstring_options:
            ignore_init_summary: true
        members: false
        heading_level: 3

## Available Operations

- [`apply_guardrail`](operations/apply_guardrail.md)

- [`converse`](operations/converse.md)

- [`converse_stream`](operations/converse_stream.md)

- [`count_tokens`](operations/count_tokens.md)

- [`get_async_invoke`](operations/get_async_invoke.md)

- [`invoke_model`](operations/invoke_model.md)

- [`invoke_model_with_bidirectional_stream`](operations/invoke_model_with_bidirectional_stream.md)

- [`invoke_model_with_response_stream`](operations/invoke_model_with_response_stream.md)

- [`list_async_invokes`](operations/list_async_invokes.md)

- [`start_async_invoke`](operations/start_async_invoke.md)

## Configuration

::: aws_sdk_bedrock_runtime.config.Config
    options:
        merge_init_into_class: true
        docstring_options:
            ignore_init_summary: true
        heading_level: 3

## Errors

- [`AccessDeniedException`](errors/AccessDeniedException.md)

- [`ConflictException`](errors/ConflictException.md)

- [`InternalServerException`](errors/InternalServerException.md)

- [`ModelErrorException`](errors/ModelErrorException.md)

- [`ModelNotReadyException`](errors/ModelNotReadyException.md)

- [`ModelStreamErrorException`](errors/ModelStreamErrorException.md)

- [`ModelTimeoutException`](errors/ModelTimeoutException.md)

- [`ResourceNotFoundException`](errors/ResourceNotFoundException.md)

- [`ServiceQuotaExceededException`](errors/ServiceQuotaExceededException.md)

- [`ServiceUnavailableException`](errors/ServiceUnavailableException.md)

- [`ThrottlingException`](errors/ThrottlingException.md)

- [`ValidationException`](errors/ValidationException.md)

## Structures

- [`AnyToolChoice`](structures/AnyToolChoice.md)

- [`AsyncInvokeS3OutputDataConfig`](structures/AsyncInvokeS3OutputDataConfig.md)

- [`AsyncInvokeSummary`](structures/AsyncInvokeSummary.md)

- [`AutoToolChoice`](structures/AutoToolChoice.md)

- [`BidirectionalInputPayloadPart`](structures/BidirectionalInputPayloadPart.md)

- [`BidirectionalOutputPayloadPart`](structures/BidirectionalOutputPayloadPart.md)

- [`CachePointBlock`](structures/CachePointBlock.md)

- [`Citation`](structures/Citation.md)

- [`CitationSourceContentDelta`](structures/CitationSourceContentDelta.md)

- [`CitationsConfig`](structures/CitationsConfig.md)

- [`CitationsContentBlock`](structures/CitationsContentBlock.md)

- [`CitationsDelta`](structures/CitationsDelta.md)

- [`ContentBlockDeltaEvent`](structures/ContentBlockDeltaEvent.md)

- [`ContentBlockStartEvent`](structures/ContentBlockStartEvent.md)

- [`ContentBlockStopEvent`](structures/ContentBlockStopEvent.md)

- [`ConverseMetrics`](structures/ConverseMetrics.md)

- [`ConverseStreamMetadataEvent`](structures/ConverseStreamMetadataEvent.md)

- [`ConverseStreamMetrics`](structures/ConverseStreamMetrics.md)

- [`ConverseStreamTrace`](structures/ConverseStreamTrace.md)

- [`ConverseTokensRequest`](structures/ConverseTokensRequest.md)

- [`ConverseTrace`](structures/ConverseTrace.md)

- [`DocumentBlock`](structures/DocumentBlock.md)

- [`DocumentCharLocation`](structures/DocumentCharLocation.md)

- [`DocumentChunkLocation`](structures/DocumentChunkLocation.md)

- [`DocumentPageLocation`](structures/DocumentPageLocation.md)

- [`GuardrailAssessment`](structures/GuardrailAssessment.md)

- [`GuardrailAutomatedReasoningImpossibleFinding`](structures/GuardrailAutomatedReasoningImpossibleFinding.md)

- [`GuardrailAutomatedReasoningInputTextReference`](structures/GuardrailAutomatedReasoningInputTextReference.md)

- [`GuardrailAutomatedReasoningInvalidFinding`](structures/GuardrailAutomatedReasoningInvalidFinding.md)

- [`GuardrailAutomatedReasoningLogicWarning`](structures/GuardrailAutomatedReasoningLogicWarning.md)

- [`GuardrailAutomatedReasoningNoTranslationsFinding`](structures/GuardrailAutomatedReasoningNoTranslationsFinding.md)

- [`GuardrailAutomatedReasoningPolicyAssessment`](structures/GuardrailAutomatedReasoningPolicyAssessment.md)

- [`GuardrailAutomatedReasoningRule`](structures/GuardrailAutomatedReasoningRule.md)

- [`GuardrailAutomatedReasoningSatisfiableFinding`](structures/GuardrailAutomatedReasoningSatisfiableFinding.md)

- [`GuardrailAutomatedReasoningScenario`](structures/GuardrailAutomatedReasoningScenario.md)

- [`GuardrailAutomatedReasoningStatement`](structures/GuardrailAutomatedReasoningStatement.md)

- [`GuardrailAutomatedReasoningTooComplexFinding`](structures/GuardrailAutomatedReasoningTooComplexFinding.md)

- [`GuardrailAutomatedReasoningTranslation`](structures/GuardrailAutomatedReasoningTranslation.md)

- [`GuardrailAutomatedReasoningTranslationAmbiguousFinding`](structures/GuardrailAutomatedReasoningTranslationAmbiguousFinding.md)

- [`GuardrailAutomatedReasoningTranslationOption`](structures/GuardrailAutomatedReasoningTranslationOption.md)

- [`GuardrailAutomatedReasoningValidFinding`](structures/GuardrailAutomatedReasoningValidFinding.md)

- [`GuardrailConfiguration`](structures/GuardrailConfiguration.md)

- [`GuardrailContentFilter`](structures/GuardrailContentFilter.md)

- [`GuardrailContentPolicyAssessment`](structures/GuardrailContentPolicyAssessment.md)

- [`GuardrailContextualGroundingFilter`](structures/GuardrailContextualGroundingFilter.md)

- [`GuardrailContextualGroundingPolicyAssessment`](structures/GuardrailContextualGroundingPolicyAssessment.md)

- [`GuardrailConverseImageBlock`](structures/GuardrailConverseImageBlock.md)

- [`GuardrailConverseTextBlock`](structures/GuardrailConverseTextBlock.md)

- [`GuardrailCoverage`](structures/GuardrailCoverage.md)

- [`GuardrailCustomWord`](structures/GuardrailCustomWord.md)

- [`GuardrailImageBlock`](structures/GuardrailImageBlock.md)

- [`GuardrailImageCoverage`](structures/GuardrailImageCoverage.md)

- [`GuardrailInvocationMetrics`](structures/GuardrailInvocationMetrics.md)

- [`GuardrailManagedWord`](structures/GuardrailManagedWord.md)

- [`GuardrailOutputContent`](structures/GuardrailOutputContent.md)

- [`GuardrailPiiEntityFilter`](structures/GuardrailPiiEntityFilter.md)

- [`GuardrailRegexFilter`](structures/GuardrailRegexFilter.md)

- [`GuardrailSensitiveInformationPolicyAssessment`](structures/GuardrailSensitiveInformationPolicyAssessment.md)

- [`GuardrailStreamConfiguration`](structures/GuardrailStreamConfiguration.md)

- [`GuardrailTextBlock`](structures/GuardrailTextBlock.md)

- [`GuardrailTextCharactersCoverage`](structures/GuardrailTextCharactersCoverage.md)

- [`GuardrailTopic`](structures/GuardrailTopic.md)

- [`GuardrailTopicPolicyAssessment`](structures/GuardrailTopicPolicyAssessment.md)

- [`GuardrailTraceAssessment`](structures/GuardrailTraceAssessment.md)

- [`GuardrailUsage`](structures/GuardrailUsage.md)

- [`GuardrailWordPolicyAssessment`](structures/GuardrailWordPolicyAssessment.md)

- [`ImageBlock`](structures/ImageBlock.md)

- [`InferenceConfiguration`](structures/InferenceConfiguration.md)

- [`InvokeModelTokensRequest`](structures/InvokeModelTokensRequest.md)

- [`Message`](structures/Message.md)

- [`MessageStartEvent`](structures/MessageStartEvent.md)

- [`MessageStopEvent`](structures/MessageStopEvent.md)

- [`PayloadPart`](structures/PayloadPart.md)

- [`PerformanceConfiguration`](structures/PerformanceConfiguration.md)

- [`PromptRouterTrace`](structures/PromptRouterTrace.md)

- [`ReasoningTextBlock`](structures/ReasoningTextBlock.md)

- [`S3Location`](structures/S3Location.md)

- [`SpecificToolChoice`](structures/SpecificToolChoice.md)

- [`SystemTool`](structures/SystemTool.md)

- [`Tag`](structures/Tag.md)

- [`TokenUsage`](structures/TokenUsage.md)

- [`ToolConfiguration`](structures/ToolConfiguration.md)

- [`ToolResultBlock`](structures/ToolResultBlock.md)

- [`ToolResultBlockStart`](structures/ToolResultBlockStart.md)

- [`ToolSpecification`](structures/ToolSpecification.md)

- [`ToolUseBlock`](structures/ToolUseBlock.md)

- [`ToolUseBlockDelta`](structures/ToolUseBlockDelta.md)

- [`ToolUseBlockStart`](structures/ToolUseBlockStart.md)

- [`VideoBlock`](structures/VideoBlock.md)

- [`WebLocation`](structures/WebLocation.md)

## Unions

- [`AsyncInvokeOutputDataConfig`](unions/AsyncInvokeOutputDataConfig.md)

- [`CitationGeneratedContent`](unions/CitationGeneratedContent.md)

- [`CitationLocation`](unions/CitationLocation.md)

- [`CitationSourceContent`](unions/CitationSourceContent.md)

- [`ContentBlock`](unions/ContentBlock.md)

- [`ContentBlockDelta`](unions/ContentBlockDelta.md)

- [`ContentBlockStart`](unions/ContentBlockStart.md)

- [`ConverseOutput`](unions/ConverseOutput.md)

- [`ConverseStreamOutput`](unions/ConverseStreamOutput.md)

- [`CountTokensInput`](unions/CountTokensInput.md)

- [`DocumentContentBlock`](unions/DocumentContentBlock.md)

- [`DocumentSource`](unions/DocumentSource.md)

- [`GuardrailAutomatedReasoningFinding`](unions/GuardrailAutomatedReasoningFinding.md)

- [`GuardrailContentBlock`](unions/GuardrailContentBlock.md)

- [`GuardrailConverseContentBlock`](unions/GuardrailConverseContentBlock.md)

- [`GuardrailConverseImageSource`](unions/GuardrailConverseImageSource.md)

- [`GuardrailImageSource`](unions/GuardrailImageSource.md)

- [`ImageSource`](unions/ImageSource.md)

- [`InvokeModelWithBidirectionalStreamInput`](unions/InvokeModelWithBidirectionalStreamInput.md)

- [`InvokeModelWithBidirectionalStreamOutput`](unions/InvokeModelWithBidirectionalStreamOutput.md)

- [`PromptVariableValues`](unions/PromptVariableValues.md)

- [`ReasoningContentBlock`](unions/ReasoningContentBlock.md)

- [`ReasoningContentBlockDelta`](unions/ReasoningContentBlockDelta.md)

- [`ResponseStream`](unions/ResponseStream.md)

- [`SystemContentBlock`](unions/SystemContentBlock.md)

- [`Tool`](unions/Tool.md)

- [`ToolChoice`](unions/ToolChoice.md)

- [`ToolInputSchema`](unions/ToolInputSchema.md)

- [`ToolResultBlockDelta`](unions/ToolResultBlockDelta.md)

- [`ToolResultContentBlock`](unions/ToolResultContentBlock.md)

- [`VideoSource`](unions/VideoSource.md)

## Enums

- [`AsyncInvokeStatus`](enums/AsyncInvokeStatus.md)

- [`CachePointType`](enums/CachePointType.md)

- [`ConversationRole`](enums/ConversationRole.md)

- [`DocumentFormat`](enums/DocumentFormat.md)

- [`GuardrailAction`](enums/GuardrailAction.md)

- [`GuardrailAutomatedReasoningLogicWarningType`](enums/GuardrailAutomatedReasoningLogicWarningType.md)

- [`GuardrailContentFilterConfidence`](enums/GuardrailContentFilterConfidence.md)

- [`GuardrailContentFilterStrength`](enums/GuardrailContentFilterStrength.md)

- [`GuardrailContentFilterType`](enums/GuardrailContentFilterType.md)

- [`GuardrailContentPolicyAction`](enums/GuardrailContentPolicyAction.md)

- [`GuardrailContentQualifier`](enums/GuardrailContentQualifier.md)

- [`GuardrailContentSource`](enums/GuardrailContentSource.md)

- [`GuardrailContextualGroundingFilterType`](enums/GuardrailContextualGroundingFilterType.md)

- [`GuardrailContextualGroundingPolicyAction`](enums/GuardrailContextualGroundingPolicyAction.md)

- [`GuardrailConverseContentQualifier`](enums/GuardrailConverseContentQualifier.md)

- [`GuardrailConverseImageFormat`](enums/GuardrailConverseImageFormat.md)

- [`GuardrailImageFormat`](enums/GuardrailImageFormat.md)

- [`GuardrailManagedWordType`](enums/GuardrailManagedWordType.md)

- [`GuardrailOutputScope`](enums/GuardrailOutputScope.md)

- [`GuardrailPiiEntityType`](enums/GuardrailPiiEntityType.md)

- [`GuardrailSensitiveInformationPolicyAction`](enums/GuardrailSensitiveInformationPolicyAction.md)

- [`GuardrailStreamProcessingMode`](enums/GuardrailStreamProcessingMode.md)

- [`GuardrailTopicPolicyAction`](enums/GuardrailTopicPolicyAction.md)

- [`GuardrailTopicType`](enums/GuardrailTopicType.md)

- [`GuardrailTrace`](enums/GuardrailTrace.md)

- [`GuardrailWordPolicyAction`](enums/GuardrailWordPolicyAction.md)

- [`ImageFormat`](enums/ImageFormat.md)

- [`PerformanceConfigLatency`](enums/PerformanceConfigLatency.md)

- [`SortAsyncInvocationBy`](enums/SortAsyncInvocationBy.md)

- [`SortOrder`](enums/SortOrder.md)

- [`StopReason`](enums/StopReason.md)

- [`ToolResultStatus`](enums/ToolResultStatus.md)

- [`ToolUseType`](enums/ToolUseType.md)

- [`Trace`](enums/Trace.md)

- [`VideoFormat`](enums/VideoFormat.md)
