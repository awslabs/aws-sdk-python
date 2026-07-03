# Installation

To use the AWS SDK for Python, you first need to install the client packages
for the services you want to call. Each service client is published to PyPI as
its own package, so you install only what your application needs.

## Prerequisites

The SDK requires a supported version of
[Python](https://www.python.org/downloads/). Every client package requires
Python 3.12 or later.

## Set up a virtual environment

Once you have a supported version of Python installed, set up your workspace
by creating a virtual environment and activating it:

```bash
python -m venv .venv
source .venv/bin/activate
```

This provides an isolated space for your installation and avoids unexpected
interactions with packages installed at the system level. Skipping this step
may result in dependency conflicts or failures with other tools installed on
your system.

## Install a client

Install each service client with `pip`. For example, to install the Amazon
Bedrock Runtime client:

```bash
pip install aws-sdk-bedrock-runtime
```

This installs the client package and its dependencies, including
[smithy-python](https://github.com/smithy-lang/smithy-python). See
[Available Clients](clients/index.md) for every service client the SDK
currently offers.

## Install a specific version

If your project requires a specific version of a client, provide constraints
when installing the package:

```bash
# Install version 0.0.1 specifically
pip install "aws-sdk-bedrock-runtime==0.0.1"

# Make sure the client is no older than version 0.0.2
pip install "aws-sdk-bedrock-runtime>=0.0.2"

# Avoid versions newer than version 0.0.3
pip install "aws-sdk-bedrock-runtime<=0.0.3"
```

!!! warning "Pin your versions"

    While the SDK is experimental, breaking changes may occur between minor
    versions. We strongly advise pinning to an exact version of each client
    package and upgrading deliberately.

## Next steps

With a client installed, follow the [Quickstart](quickstart.md) to configure
credentials and make your first request.
