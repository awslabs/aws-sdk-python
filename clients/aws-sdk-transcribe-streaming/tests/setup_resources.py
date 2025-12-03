# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "boto3",
# ]
# ///
#
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

"""Setup script to create AWS resources for integration tests.

Creates an IAM role and S3 bucket needed for medical scribe integration tests.

Note:
    This script is intended for local testing only and should not be used for
    production setups.

Usage:
    uv run scripts/setup_resources.py
"""

import json
from typing import Any

import boto3


def create_iam_role(iam_client: Any, role_name: str, bucket_name: str) -> None:
    trust_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {
                    "Service": [
                        "transcribe.streaming.amazonaws.com"
                    ]
                },
                "Action": "sts:AssumeRole",
            }
        ]
    }

    try:
        iam_client.create_role(
            RoleName=role_name, AssumeRolePolicyDocument=json.dumps(trust_policy)
        )
    except iam_client.exceptions.EntityAlreadyExistsException:
        pass

    permissions_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Action": [
                    "s3:PutObject"
                ],
                "Resource": [
                    f"arn:aws:s3:::{bucket_name}",
                    f"arn:aws:s3:::{bucket_name}/*",
                ],
                "Effect": "Allow"
            }
        ]
    }

    iam_client.put_role_policy(
        RoleName=role_name,
        PolicyName="HealthScribeS3Access",
        PolicyDocument=json.dumps(permissions_policy),
    )


def setup_healthscribe_resources() -> tuple[str, str]:
    region = "us-east-1"
    iam = boto3.client("iam")
    s3 = boto3.client("s3", region_name=region)
    sts = boto3.client("sts")

    account_id = sts.get_caller_identity()["Account"]
    bucket_name = f"healthscribe-test-{account_id}-{region}"
    role_name = "HealthScribeIntegrationTestRole"

    s3.create_bucket(Bucket=bucket_name)
    create_iam_role(iam, role_name, bucket_name)

    role_arn = f"arn:aws:iam::{account_id}:role/{role_name}"
    return role_arn, bucket_name


if __name__ == "__main__":
    role_arn, bucket_name = setup_healthscribe_resources()

    print("Setup complete. Export these environment variables before running tests:")
    print(f"export HEALTHSCRIBE_ROLE_ARN={role_arn}")
    print(f"export HEALTHSCRIBE_S3_BUCKET={bucket_name}")
