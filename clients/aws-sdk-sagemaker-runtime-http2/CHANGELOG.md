# Changelog

## Unreleased

* None yet.

## v0.3.0

This release proceeds 0.1.0. There is no 0.2.0 as the initial release was intended to be inline
with the `smithy-aws-core` version used in the client.

### Breaking
* Function signature for `resolve_retry_strategy` has been changed to prevent unnecessary code duplication in operation methods. This will affect all 0.3.0 clients.

### Dependencies
* **Updated**: `smithy_aws_core[eventstream, json]` from `~=0.2.0` to `~=0.3.0`.
* **Updated**: `smithy_core` from `~=0.2.0` to `~=0.3.0`.

## v0.1.0

### Features
* Initial client release with support for current Amazon SageMaker Runtime HTTP2 operations.
