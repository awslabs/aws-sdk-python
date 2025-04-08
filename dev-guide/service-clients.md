# Creating service clients in the experimental Amazon Bedrock Runtime client for Python<a name="service-clients"></a>

To make a request to an AWS service, you first instantiate a client for that service. You can configure common settings for service clients such as timeouts, the HTTP client, and retry configuration. To create a client for Amazon Bedrock Runtime:

```
    service_client = BedrockRuntimeClient(
        config=Config(
            aws_credentials_identity_resolver=EnvironmentCredentialsResolver(),
            region = "us-east-1",
        )
    )
```

Each service client requires an AWS Region and a credential provider. The SDK uses these values to send requests to the correct Region for your resources and to sign requests with the correct credentials. You can specify these values programmatically in code or have them automatically loaded from the environment.

The SDK has a series of places (or sources) that it checks in order to find a value for configuration settings.

1. Any explicit setting set in the code or on a service client itself takes precedence over anything else.

1. Environment variables
   + **Note: **At this time, environment variables are only used to obtain credentials using the `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `AWS_SESSION_TOKEN` variables.
   + For details on setting environment variables, see [environment variables](https://docs.aws.amazon.com/sdkref/latest/guide/environment-variables.html) in the *AWS SDKs and Tools Reference Guide*.

1. Any default value provided by the SDK source code itself is used last.
   + Some properties, such as Region, don't have a default. You must specify them either explicitly in code or in an environment setting. If the SDK can't resolve required configuration, API requests can fail at runtime.
