# Setting the AWS Region for the experimental Amazon Bedrock Runtime client for Python<a name="region"></a>

You can access AWS services that operate in a specific geographic area by using AWS Regions. This can be useful both for redundancy and to keep your data and applications running close to where you and your users access them. For more information on how Regions are used, see [AWS Region](https://docs.aws.amazon.com/sdkref/latest/guide/feature-region.html) in the *AWS SDKs and Tools Reference Guide*.

**Important**  
Most resources reside in a specific AWS Region and you must supply the correct Region for the resource when using the SDK.

## Specifying the region inline<a name="region-setting"></a>

The Region is specified by setting the `region` property of the `Config` object to a string giving the name of the Region. For example, to specify the region `us-east-1` when creating an Amazon Bedrock Runtime client:

```
    service_client = BedrockRuntimeClient(
        config=Config(
            aws_credentials_identity_resolver=EnvironmentCredentialsResolver(),
            region = "us-east-1",
        )
    )
```

**Note**  
Not all Amazon Bedrock foundation models are available in all Regions. See [Model support by AWS Region in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/models-regions.html) for model compatibility information.

## Getting the region from the environment<a name="region-getting-from-environment"></a>

The experimental Amazon Bedrock Runtime client for Python does not currently support automatically retrieving the value of the `AWS_REGION` environment variable. To make your application use this variable to specify the Region in which to operate, you can add code similar to the following to your project:

```
import os
    
...
region = os.getenv('AWS_REGION', default="us-east-1")
    
service_client = BedrockRuntimeClient(
    config=Config(
        aws_credentials_identity_resolver=EnvironmentCredentialsResolver(),
        region = region,
    )
)
```

This uses the value of `AWS_REGION`, falling back to `us-east-1` if the variable isn't found in the environment.
