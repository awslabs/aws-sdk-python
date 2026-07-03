# Streaming

Many AWS services can stream data instead of returning a single response, and
these services are where the SDK's async design pays off most. The SDK models
streaming operations as event streams: typed events that you read with
`async for` and send with `await`, all without blocking your application.

The SDK supports two kinds of streaming operations:

- **Output streams**: The service sends a stream of events back to you, such
  as a model's reply arriving token by token from Amazon Bedrock.
- **Bidirectional streams**: You send a stream of events to the service while
  it sends events back at the same time, such as live audio going to Amazon
  Transcribe while transcripts come back.

Each client's API reference in [Available Clients](clients/index.md) lists
the streaming operations it supports and their event types.

## Output streams

A streaming operation returns an event stream instead of a complete response.
Enter it with `async with` and iterate the events with `async for`. Each
event is one member of a typed union, so check the event type with
`isinstance` and handle the ones you care about.

This example streams a model's reply from Amazon Bedrock Runtime and prints
the text as it arrives:

```python
import asyncio

from aws_sdk_bedrock_runtime.client import BedrockRuntimeClient, ConverseStreamInput
from aws_sdk_bedrock_runtime.config import Config
from aws_sdk_bedrock_runtime.models import (
    ContentBlockDeltaText,
    ContentBlockText,
    ConverseStreamOutputContentBlockDelta,
    Message,
)
from smithy_aws_core.identity import EnvironmentCredentialsResolver


async def main():
    client = BedrockRuntimeClient(
        config=Config(
            region="us-east-1",
            aws_credentials_identity_resolver=EnvironmentCredentialsResolver(),
        )
    )

    response = await client.converse_stream(
        ConverseStreamInput(
            model_id="global.anthropic.claude-opus-4-8",  # (1)!
            messages=[
                Message(
                    role="user",
                    content=[ContentBlockText(value="Tell me a short story.")],
                )
            ],
        )
    )

    async with response as stream:
        async for event in stream.output_stream:
            if isinstance(event, ConverseStreamOutputContentBlockDelta):
                delta = event.value.delta
                if isinstance(delta, ContentBlockDeltaText):
                    print(delta.value, end="", flush=True)


asyncio.run(main())
```

1.  This model may not be the latest available and could be deprecated in the
    future. See [Models at a glance](https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards.html)
    in the Amazon Bedrock User Guide for the current list of models and their
    IDs.

The stream delivers more event types than the text deltas printed here. For
example, `ConverseStreamOutputMetadata` arrives at the end of the stream and
carries token usage counts. Handle additional event types by adding
`isinstance` checks for them.

## Bidirectional streams

A bidirectional operation returns a duplex event stream as soon as the
connection is established. You send typed events on its `input_stream` and
read typed events from its `output_stream`, usually from two concurrent
tasks.

This example streams audio to Amazon Transcribe Streaming and prints
transcripts as the service produces them:

```python
import asyncio

from aws_sdk_transcribe_streaming.client import TranscribeStreamingClient
from aws_sdk_transcribe_streaming.config import Config
from aws_sdk_transcribe_streaming.models import (
    AudioEvent,
    AudioStreamAudioEvent,
    LanguageCode,
    MediaEncoding,
    StartStreamTranscriptionInput,
    TranscriptResultStreamTranscriptEvent,
)
from smithy_aws_core.identity import EnvironmentCredentialsResolver

CHUNK_SIZE = 1024 * 8


async def send_audio(stream):
    with open("audio.wav", "rb") as f:
        while chunk := f.read(CHUNK_SIZE):
            await stream.input_stream.send(
                AudioStreamAudioEvent(value=AudioEvent(audio_chunk=chunk))
            )
    # Closing the input stream tells the service you are done sending.
    await stream.input_stream.close()


async def receive_transcripts(stream):
    _, output_stream = await stream.await_output()
    async for event in output_stream:
        if isinstance(event, TranscriptResultStreamTranscriptEvent):
            if event.value.transcript and event.value.transcript.results:
                for result in event.value.transcript.results:
                    if result.alternatives:
                        print(result.alternatives[0].transcript)


async def main():
    client = TranscribeStreamingClient(
        config=Config(
            region="us-east-1",
            aws_credentials_identity_resolver=EnvironmentCredentialsResolver(),
        )
    )

    stream = await client.start_stream_transcription(
        input=StartStreamTranscriptionInput(
            language_code=LanguageCode.EN_US,
            media_sample_rate_hertz=16000,
            media_encoding=MediaEncoding.PCM,
        )
    )

    # Send audio and receive transcripts at the same time.
    await asyncio.gather(send_audio(stream), receive_transcripts(stream))


asyncio.run(main())
```

The two halves of the stream work independently:

- **Sending**: `stream.input_stream.send()` delivers one typed event to the
  service. Call `stream.input_stream.close()` when you have no more input to
  send.
- **Receiving**: `stream.await_output()` waits for the service's initial
  response and returns the output event stream, which you iterate with
  `async for` just like an output-only stream.

Running the sender and receiver with `asyncio.gather` lets input flow out
while output flows in, which is what makes real-time use cases such as live
transcription and speech-to-speech conversation work.

!!! tip "Pace real-time input"

    Real-time services expect input at the rate it naturally occurs. When
    sending recorded audio to a live transcription service, add a short
    `asyncio.sleep` between chunks to match the audio's actual duration
    instead of sending the whole file at once.
