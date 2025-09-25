# Changelog

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
