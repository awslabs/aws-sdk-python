# Installing the experimental Amazon Bedrock Runtime client for Python<a name="installing"></a>

## Prerequisites<a name="installing-prerequisites"></a>

To use the experimental Amazon Bedrock Runtime client for Python, you first
need a supported version of [Python](https://www.python.org/downloads/). The client requires Python 3.12 or later.

## Set up a virtual environment<a name="installing-virtual-env"></a>

Once you have a supported version of Python installed, you should set up your workspace by creating a virtual environment and activating it:

```
$ python -m venv .venv
...
$ source .venv/bin/activate
```

This provides an isolated space for your installation that will avoid unexpected interactions with packages installed at the system level. Skipping this step may result in unexpected dependency conflicts or failures with other tools installed on your system.

## Installing the experimental Amazon Bedrock Runtime client for Python<a name="installing-sdk"></a>

To add the SDK to your Python project, use the pip tool to install each service package into your environment. For example, to install support for the Amazon Bedrock Runtime, use the following command:

```
$ python -m pip install aws-sdk-bedrock-runtime
```

This will install into your environment the experimental Amazon Bedrock Runtime client for Python package(s) you specify, as well as their dependencies, including `[smithy-python](https://github.com/smithy-lang/smithy-python)`.

If your project requires a specific version of the Amazon Bedrock Runtime client, you may wish to provide constraints when installing the package:

```
$ # Install experimental Amazon Bedrock Runtime client for Python version 0.0.1 specifically
$ python -m pip install aws-sdk-bedrock-runtime==0.0.1

$ # Make sure the experimental Amazon Bedrock Runtime client for Python is no older than version 0.0.2
$ pip install aws-sdk-bedrock-runtime>=0.0.2
    
$ # Avoid versions of the experimental Amazon Bedrock Runtime client for Python newer than version 0.0.3
$ pip install aws-sdk-bedrock-runtime<=0.0.3
```

As long as the Amazon Bedrock Runtime client for Python is experimental, you may wish to pin to a specific version of the client, or to versions up to and including a specific version, in order to prevent updating to a version that isn't compatible with your application.