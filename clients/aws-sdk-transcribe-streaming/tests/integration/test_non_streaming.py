# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

"""Test non-streaming output type handling.

This test requires AWS resources (an IAM role and an S3 bucket).
To set them up locally, run:

    uv run scripts/setup_resources.py

Then export the environment variables shown in the output.
"""

import asyncio
import os
import time
import uuid

import pytest

from aws_sdk_transcribe_streaming.models import (
    ClinicalNoteGenerationSettings,
    GetMedicalScribeStreamInput,
    GetMedicalScribeStreamOutput,
    LanguageCode,
    MedicalScribeAudioEvent,
    MedicalScribeConfigurationEvent,
    MedicalScribeInputStreamAudioEvent,
    MedicalScribeInputStreamConfigurationEvent,
    MedicalScribeInputStreamSessionControlEvent,
    MedicalScribePostStreamAnalyticsSettings,
    MedicalScribeSessionControlEvent,
    MedicalScribeSessionControlEventType,
    MediaEncoding,
    StartMedicalScribeStreamInput,
)

from . import AUDIO_FILE, create_transcribe_client

SAMPLE_RATE = 16000
BYTES_PER_SAMPLE = 2
CHANNEL_NUMS = 1
CHUNK_SIZE = 1024 * 8


async def test_get_medical_scribe_stream() -> None:
    role_arn = os.environ.get("HEALTHSCRIBE_ROLE_ARN")
    s3_bucket = os.environ.get("HEALTHSCRIBE_S3_BUCKET")

    if not role_arn or not s3_bucket:
        pytest.fail("HEALTHSCRIBE_ROLE_ARN or HEALTHSCRIBE_S3_BUCKET not set")

    transcribe_client = create_transcribe_client("us-east-1")
    session_id = str(uuid.uuid4())

    stream = await transcribe_client.start_medical_scribe_stream(
        input=StartMedicalScribeStreamInput(
            language_code=LanguageCode.EN_US,
            media_sample_rate_hertz=SAMPLE_RATE,
            media_encoding=MediaEncoding.PCM,
            session_id=session_id,
        )
    )

    await stream.input_stream.send(
        MedicalScribeInputStreamConfigurationEvent(
            value=MedicalScribeConfigurationEvent(
                resource_access_role_arn=role_arn,
                post_stream_analytics_settings=MedicalScribePostStreamAnalyticsSettings(
                    clinical_note_generation_settings=ClinicalNoteGenerationSettings(
                        output_bucket_name=s3_bucket
                    )
                ),
            )
        )
    )

    start_time = time.time()
    elapsed_audio_time = 0.0

    with AUDIO_FILE.open("rb") as f:
        while chunk := f.read(CHUNK_SIZE):
            await stream.input_stream.send(
                MedicalScribeInputStreamAudioEvent(
                    value=MedicalScribeAudioEvent(audio_chunk=chunk)
                )
            )
            elapsed_audio_time += len(chunk) / (
                BYTES_PER_SAMPLE * SAMPLE_RATE * CHANNEL_NUMS
            )
            wait_time = start_time + elapsed_audio_time - time.time()
            if wait_time > 0:
                await asyncio.sleep(wait_time)

    await stream.input_stream.send(
        MedicalScribeInputStreamSessionControlEvent(
            value=MedicalScribeSessionControlEvent(
                type=MedicalScribeSessionControlEventType.END_OF_SESSION
            )
        )
    )
    await stream.input_stream.close()

    await stream.await_output()

    # Consume output stream events to properly close the connection
    if stream.output_stream:
        async for _ in stream.output_stream:
            pass

    response = await transcribe_client.get_medical_scribe_stream(
        input=GetMedicalScribeStreamInput(session_id=session_id)
    )

    assert isinstance(response, GetMedicalScribeStreamOutput)
    assert response.medical_scribe_stream_details is not None

    details = response.medical_scribe_stream_details
    assert details.session_id == session_id
    assert details.stream_status == "COMPLETED"
    assert details.language_code == "en-US"
    assert details.media_encoding == "pcm"
    assert details.media_sample_rate_hertz == SAMPLE_RATE
