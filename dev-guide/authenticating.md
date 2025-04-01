# Authenticating the experimental Amazon Bedrock Runtime client for Python with AWS<a name="authenticating"></a>

You must establish how your code authenticates with AWS when developing with AWS services\. You can configure programmatic access to AWS resources in different ways depending on the environment and the AWS access available to you\. For choices on all primary methods of authentication, and guidance on configuring it for the SDK, see [Authentication and access](https://docs.aws.amazon.com/sdkref/latest/guide/access.html) in the *AWS SDKs and Tools Reference Guide*\. 

Although you should typically use AWS IAM Identity Center to create and use secure credentials for your applications, the experimental Amazon Bedrock Runtime client for Python currently provides a limited subset of the [Available credential providers](credential-providers.md#credproviders-available-credential-providers) that can be used to authenticate for experimental Amazon Bedrock Runtime client for Python access\.

To provide credentials to your application, you can either rely on the default credential resolver chain or you can specify a specific credentials identity resolver to use\. For more information about credentials identity resolvers, see [Using experimental Amazon Bedrock Runtime client for Python credential providers](credential-providers.md)\.

## More authentication information<a name="credother"></a>

Human users, also known as *human identities*, are the people, administrators, developers, operators, and consumers of your applications\. They must have an identity to access your AWS environments and applications\. Human users that are members of your organization \- that means you, the developer \- are known as *workforce identities*\. 
+ To learn about the credential resolvers available in the experimental Amazon Bedrock Runtime client for Python, see [Using experimental Amazon Bedrock Runtime client for Python credential providers](credential-providers.md)\.
+ To create short\-term AWS credentials, see [Temporary Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html) in the *IAM User Guide*\.
+ To learn about other credential providers supported by the AWS SDKs, see [Standardized credential providers](https://docs.aws.amazon.com/sdkref/latest/guide/standardized-credentials.html) in the *AWS SDKs and Tools Reference Guide*\.