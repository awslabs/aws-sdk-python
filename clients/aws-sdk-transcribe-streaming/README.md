## Amazon Transcribe Streaming Service Client

The `aws_sdk_transcribe_streaming` client is still under active developement.
Changes may result in breaking changes prior to the release of version
1.0.0.

### Documentation

Documentation is available in the `/docs` directory of this package.
Pages can be built into portable HTML files for the time being. You can
follow the instructions in the docs [README.md](https://github.com/awslabs/aws-sdk-python/blob/main/clients/aws-sdk-transcribe-streaming/docs/README.md).

For high-level documentation, you can view the [`dev-guide`](https://github.com/awslabs/aws-sdk-python/tree/main/dev-guide) at the top level of this repo.

### Examples

The `examples` directory contains the following scripts to help you get started.
You can run each one by calling `uv run <file_name>`. This will set up an
environment for you with a supported Python version and required dependencies.
- `simple_mic.py` - Stream audio from your microphone in real-time and receive transcription results as you speak.
- `simple_file.py` - Transcribe a pre-recorded audio file with simulated real-time streaming and rate limiting.
