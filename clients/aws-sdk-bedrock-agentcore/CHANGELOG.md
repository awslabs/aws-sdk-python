# Changelog

## v0.11.0

### API Changes
* Increase spans count from 1k to 20k
* AgentCore Memory now supports Flexible Namespaces and Non-Conversational Payloads in CreateEvent API
* Add support for the Machine Payments Protocol (MPP) and x402 upto scheme payments protocol in Amazon Bedrock AgentCore Payments. Customers can now pay for MPP-gated resources and also pay services which requires upto scheme in x402

### Enhancements
* Re-generated with smithy-python 0.5.0

### Dependencies
* Bump `smithy-aws-core` from `~=0.10.0` to `~=0.11.0`.
* Bump `smithy-http` from `~=0.4.0` to `~=0.5.0`.

## v0.10.0

### Dependencies
* Bump `smithy-aws-core` from `~=0.9.0` to `~=0.10.0`.

## v0.9.0

### API Changes
* Adding online eval arn as input for recommendation API.
* Add support for capacity provider sessions in Amazon Bedrock AgentCore. Customers can now delete an active session running on a runtime instance launched through their capacity provider.

### Dependencies
* Bump `smithy-core` from `~=0.7.0` to `~=0.8.0`.
* Bump `smithy-aws-core` from `~=0.8.0` to `~=0.9.0`.

## v0.8.0

### Features
* Initial client release with support for current Amazon Bedrock AgentCore operations.

### Dependencies
* Bump `smithy-aws-core` from `~=0.7.0` to `~=0.8.0`.
* Bump `smithy-core` from `~=0.6.0` to `~=0.7.0`.
