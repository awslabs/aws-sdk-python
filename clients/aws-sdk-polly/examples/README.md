# Polly Bidirectional Streaming Examples

Each script is a self-contained [uv](https://docs.astral.sh/uv/getting-started/installation/) script that demonstrates one way to use Polly's bidirectional streaming API (`start_speech_synthesis_stream`).

| Script | What it shows | Extra dependencies |
| --- | --- | --- |
| [`simple_file.py`](simple_file.py) | Stream synthesized audio and save it to an MP3 file. | None |
| [`simple_speaker.py`](simple_speaker.py) | Real-time MP3 playback through your speakers as audio arrives. The MP3 decoder handles buffering. | `miniaudio` |

## Prerequisites

- AWS credentials available via environment variables (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, optionally `AWS_SESSION_TOKEN`).
- Python 3.12+.
- `uv` installed.
- For `simple_speaker.py`: a working audio output device.

## Running

All examples accept text as a positional argument, from stdin via `-`, or fall back to a built-in default:

```sh
# Default text
uv run simple_file.py

# Inline text
uv run simple_file.py "Hello from Polly."

# From stdin
cat story.txt | uv run simple_file.py -
```

Common flags:

- `--voice` — Polly voice ID (default `Matthew`)
- `--region` — AWS region (default `us-east-1`)
- `--output` (`simple_file.py` only) — MP3 output path

The bidi API only supports the `generative` engine, so engine selection is not exposed.
