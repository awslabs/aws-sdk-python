# Polly Bidirectional Streaming Examples

Each script is a self-contained [uv](https://docs.astral.sh/uv/getting-started/installation/) script that demonstrates one way to use Polly's bidirectional streaming API (`start_speech_synthesis_stream`).

| Script | What it shows | Extra dependencies |
| --- | --- | --- |
| [`stream_speech_to_file.py`](stream_speech_to_file.py) | Stream synthesized audio and save it to an MP3 file. | None |
| [`stream_speech_to_speakers.py`](stream_speech_to_speakers.py) | Real-time MP3 playback through your speakers as audio arrives. The MP3 decoder handles buffering. | `miniaudio` |

## Prerequisites

- AWS credentials available via environment variables (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, optionally `AWS_SESSION_TOKEN`).
- Python 3.12+.
- `uv` installed.
- For `stream_speech_to_speakers.py`: a working audio output device.

## Running

All examples accept text as a positional argument, from stdin via `-`, or fall back to a built-in default:

```sh
# Default text
uv run stream_speech_to_file.py

# Inline text
uv run stream_speech_to_file.py "Hello from Polly."

# From stdin
cat story.txt | uv run stream_speech_to_file.py -
```

Common flags:

- `--voice` — Polly voice ID (default `Matthew`)
- `--region` — AWS region (default `us-east-1`)
- `--output` (`stream_speech_to_file.py` only) — MP3 output path

The bidi API only supports the `generative` engine, so engine selection is not exposed.
