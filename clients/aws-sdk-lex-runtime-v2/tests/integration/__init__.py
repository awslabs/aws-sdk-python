# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

from smithy_aws_core.identity import EnvironmentCredentialsResolver

from aws_sdk_lex_runtime_v2.client import LexRuntimeV2Client
from aws_sdk_lex_runtime_v2.config import AsyncLexRuntimeV2Config

BOT_ALIAS_ID = "TSTALIASID"
LOCALE_ID = "en_US"
REGION = "us-east-1"


async def create_lex_client(region: str) -> LexRuntimeV2Client:
    return LexRuntimeV2Client(
        config=await AsyncLexRuntimeV2Config.resolve(
            endpoint_uri=f"https://runtime-v2-lex.{region}.amazonaws.com",
            region=region,
            aws_credentials_identity_resolver=EnvironmentCredentialsResolver(),
        )
    )
