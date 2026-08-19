# Changelog

## v0.10.0

### Dependencies
* Bump `smithy-aws-core` from `~=0.9.0` to `~=0.10.0`.

## v0.9.0

### API Changes
* Add support for Gateway rate limits and Runtime instances in Amazon Bedrock AgentCore. Customers can now configure rate limits scoped to control request rates, token consumption rates, and active connection rates. Customers can now create capacity providers to launch runtimes on their EC2 instances.
* Adding support for fine-grained access control for AgentCore Memory through managed AgentCore Gateway HTTP Connectors.

### Dependencies
* Bump `smithy-core` from `~=0.7.0` to `~=0.8.0`.
* Bump `smithy-aws-core` from `~=0.8.0` to `~=0.9.0`.

## v0.8.0

### Features
* Initial client release with support for current Amazon Bedrock AgentCore Control operations.

### Dependencies
* Bump `smithy-aws-core` from `~=0.7.0` to `~=0.8.0`.
* Bump `smithy-core` from `~=0.6.0` to `~=0.7.0`.
