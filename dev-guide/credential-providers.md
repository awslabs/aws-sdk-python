# Using experimental Amazon Bedrock Runtime client for Python credential providers<a name="credential-providers"></a>

To make requests to AWS using the experimental Amazon Bedrock Runtime client for Python, the SDK uses cryptographically-signed credentials issued by AWS. At runtime, the SDK retrieves configuration values for credentials by checking several locations.

For guided options for getting started on AWS authentication for your project, see [Authentication and access](https://docs.aws.amazon.com/sdkref/latest/guide/access.html) in the *AWS SDKs and Tools Reference Guide*.

## Credentials identity resolvers provided by the experimental Amazon Bedrock Runtime client for Python<a name="credproviders-available-credential-providers"></a>

`ContainerCredentialsResolver`
Obtains credentials from a container credential service such as the one provided with Amazon Elastic Container Service (Amazon ECS) and Amazon Elastic Kubernetes Service (Amazon EKS).

`EnvironmentCredentialsResolver`  
Resolves credentials found in the environment variables `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `AWS_SESSION_TOKEN`.

`IMDSCredentialsResolver`  
Obtains credentials from an Amazon EC2 instance's metadata using the Instance Metadata Service (IMDS).

`StaticCredentialsResolver`  
Uses static credentials specified in the form of an IAM access key ID, secret access key, and possibly a session token.

For details on AWS credential provider configuration settings, see [Standardized credential providers](https://docs.aws.amazon.com/sdkref/latest/guide/standardized-credentials.html) in the *Settings reference* of the *AWS SDKs and Tools Reference Guide*.

**Note**  
Not all credential providers are supported yet by the experimental Amazon Bedrock Runtime client for Python. Only those listed above can be used at this time.

## Using a specific credentials identity resolver<a name="credproviders-specific-provider-resolver"></a>

To use a specific credentials identity resolver, set the `aws_credentials_identity_resolver` property on the service client's `Config` object to an instance of the credentials identity resolver class you want to use. The following example specifically uses the `EnvironmentCredentialsResolver()`, which fetches credentials from the standard environment variables `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `AWS_SESSION_TOKEN`.

```
    service_client = BedrockRuntimeClient(
        config=Config(
            aws_credentials_identity_resolver=EnvironmentCredentialsResolver(),
            region = "us-east-1",
        )
    )
```
