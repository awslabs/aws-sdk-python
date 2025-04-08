## AWS SDK for Python
[![Apache 2 licensed][apache-badge]][apache-url]

[apache-badge]: https://img.shields.io/badge/license-APACHE2-blue.svg
[apache-url]: https://github.com/awslabs/aws-sdk-python/blob/main/LICENSE

This repository contains experimental async clients for the AWS SDK for Python.
These new clients will allow you to interact with select AWS services that can
best utilize Python's async functionality. Unlike Boto3, these clients are
distributed per-service, leaving you the option to pick what fits your needs.

Please note that this new project is in early development and will be seeing
rapid iteration over the coming months. This may mean instability in both
public interfaces and general behaviors. Until the project releases version
1.0.0, breaking changes may occur between minor versions of the SDK. We'd
strongly advise strict pinning to a version of the SDK for any non-experimental
use cases.

While we're developing, we welcome all feedback. Please feel free to note things
you like, dislike, or would like to see in a future release. We'll be using that
to help drive the direction of the product going forward.

## Feedback

The SDK uses **GitHub Issues** to track feature requests and issues with the SDK. In addition,
we intend to use **GitHub Projects** to provide a high level overview of our roadmap and the
features we are actively working on.

You can provide feedback or report a bug by submitting an [issue](https://github.com/awslabs/aws-sdk-python/issues/new/choose).
This is the preferred mechanism to give feedback so that other users can engage in the conversation, +1 issues, etc.

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This project is licensed under the Apache-2.0 License.

