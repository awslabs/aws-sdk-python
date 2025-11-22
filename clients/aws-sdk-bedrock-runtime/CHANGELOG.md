# Changelog

## Unreleased

## v0.2.0

### API Changes
* Add support to automatically enforce safeguards across accounts within an AWS Organization.
* This release includes support for Search Results.
* Amazon Bedrock Runtime Service Tier Support Launch
* Add support for system tool and web citation response.

### Enhancements
* Add Standard Retry Mode

### Dependencies

* **Updated**: `smithy_aws_core[eventstream, json]` from `~=0.1.0` to `~=0.2.0`.
* **Updated**: `smithy_core` from `~=0.1.0` to `~=0.2.0`.
* **Updated**: `smithy_http[awscrt]~=0.3.0` from `~=0.2.0` to `~=0.3.0`.


## v0.1.1

### API Changes
* New stop reason for Converse and ConverseStream

### Enhancements
* Improvements to the underlying AWS CRT HTTP client result in a signifigant decrease in CPU usage. Addresses [aws-sdk-python#11](https://github.com/awslabs/aws-sdk-python/issues/11).

### Dependencies

* **Updated**: `smithy_http[awscrt]` from `~=0.1.0` to `~=0.2.0`.

### Breaking
- Removed unused `serialize.py` and `deserialize.py` modules.

## v0.1.0

### API Changes
* Fixed stop sequence limit for converse API.
* Launch CountTokens API to allow token counting
* This release adds support for Automated Reasoning checks output models for the Amazon Bedrock Guardrails ApplyGuardrail API.
* document update to support on demand custom model.
* Add API Key and document citations support for Bedrock Runtime APIs
* This release adds native h2 support for the bedrock runtime API, the support is only limited to SDKs that support h2 requests natively.
* You can now reference images and documents stored in Amazon S3 when using InvokeModel and Converse APIs with Amazon Nova Lite and Nova Pro. This enables direct integration of S3-stored multimedia assets in your model requests without manual downloading or base64 encoding.

### Dependencies

* Updated support for all smithy dependencies in the 0.1.x minor version.

## v0.0.2

### Dependencies

* Updated support for all smithy dependencies in the 0.0.x minor version.

## v0.0.1

### Features
* Initial Client Release with support for current Amazon Bedrock Runtime operations.
* Added support for new InvokeModelWithBidirectionalStream API
