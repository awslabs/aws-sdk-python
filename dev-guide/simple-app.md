# Creating a simple application using the experimental Amazon Bedrock Runtime client for Python<a name="simple-app"></a>

This chapter features a short example that asks the Amazon Titan Text Express generative AI model a simple question, then outputs the response. For more details about using Amazon Bedrock Runtime in this way, see [Carry out a conversation with the Converse API operations](https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference.html) in the [Amazon Bedrock user guide](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html).

## Importing the SDK<a name="simple-app-imports"></a>

The first thing our program does is import the service and the types we need from it:

```
from aws_sdk_bedrock_runtime.client import BedrockRuntimeClient, ConverseInput
from aws_sdk_bedrock_runtime.models import Message, ContentBlockText, StopReason
from aws_sdk_bedrock_runtime.config import Config

from smithy_aws_core.credentials_resolvers.environment import EnvironmentCredentialsResolver

import asyncio
```

This imports the following from the Bedrock client:

1. `BedrockRuntimeClient`, which is the class representing the Amazon Bedrock Runtime client.

1. The `ConverseInput` class, which is used to specify the input values when calling the client's `converse()` function.

The following are imported from the service's models:

1. The `Message` class, which describes the contents of a single message sent between the application and Amazon Bedrock Runtime.

1. The `ContentBlockText` class, which describes a block of a message's textual content.

1. The `StopReason` type, which is an enum of values defining the reason why the Amazon Bedrock Runtime service stopped sending data back to the application.

The `Config` type is imported. This is used to specify settings when creating a Amazon Bedrock Runtime client.

From Smithy, the `EnvironmentCredentialsResolver` class is imported. This is a credential resolver that uses the standard AWS environment variables to specify [access keys in environment variables](https://docs.aws.amazon.com/sdkref/latest/guide/access-users.html).

Also imported is the `asyncio` package, which is used to manage the asynchronous I/O used by the application.

## Creating the Amazon Bedrock Runtime client<a name="simple-app-create-client"></a>

To create the Amazon Bedrock Runtime client, create a `BedrockRuntimeClient` instance using a `Config` object providing the AWS Region to use. In this example, a credentials identity resolver is provided that uses the standard AWS [access keys in environment variables](https://docs.aws.amazon.com/sdkref/latest/guide/access-users.html) are used to specify credentials.

```
def get_service_client():
    service_client = BedrockRuntimeClient(
        config=Config(
            aws_credentials_identity_resolver=EnvironmentCredentialsResolver(),
            region = "us-east-1",
        )
    )
    return service_client
```

## Creating the request messages<a name="simple-app-messages"></a>

Then construct an array of `Message` objects which describe the query you wish Amazon Bedrock Runtime to process.

```
def create_messages():
    message_1 = Message(
        role="user",
        content=[
            ContentBlockText(
                value="Create a list of 3 of the best songs from the 1980s."
            )
        ]
    )
    return [message_1]
```

## Sending the messages to Amazon Bedrock Runtime<a name="simple-app-send-messages"></a>

Then send the messages to the Amazon Bedrock Runtime service by calling the client's `converse()` function, specifying in its `ConverseInput` which model to use when processing the request.

```
async def send_messages(service_client, messages):
    try:
        response = await service_client.converse(
            ConverseInput(
                model_id='amazon.titan-text-express-v1', messages=messages
            )
        )
    except:
        print("An error occurred while conversing!")
        return

    # Get the `ConverseOutput` object from the `ConverseOperationOutput`. This
    # is a `ConverseOutputMessage` unless an unexpected response arrives.
    output = response.output

    # Check the reason why the operation ended.
    stop_reason = response.stop_reason

    match stop_reason:
        case StopReason.GUARDRAIL_INTERVENED:
            print("A guardrail intervened in the response.")
        case StopReason.CONTENT_FILTERED:
            print("The content was filtered.")
        case StopReason.MAX_TOKENS:
            print("You ran out of tokens.")
        case _:
            pass

    return output
```

Once the response is received, this code also checks the reason why the response stops where it does, and outputs an appropriate message for some specific cases of interest, such as running out of tokens. The response's `output` is returned; this is of type `ConverseOutput`, which resolves to `ConverseOutputMessage` if nothing went wrong.

## Outputting the results<a name="simple-app-output"></a>

Once the response has been received, the reply can be output to the user.

```
def output_reply(output):
    # Get the `Message` from the `ConverseOutputMessage` object.
    output_msg = output.value

    # Get the content of the message from its `content` property. This is
    # an array of `ContentBlock` objects, each representing a piece of the
    # response.
    msg_contents = output_msg.content
    
    # Output the returned text by printing the value of each
    # `ContentBlockText` object found in the `msg_contents` array.
    for msg_block in msg_contents:
        if isinstance(msg_block, ContentBlockText):
            print(msg_block.value)
        else:
            print("Unexpected type of response.")
```

In this example, all of the returned blocks of type `ContentBlockText` are output, in order to display the text portion of the response. Any other type of block results in the message "Unexpected type of response."

## Wrapping up the application<a name="simple-app-run"></a>

The application body is a short function that just calls each of the above in order.

```
async def app_run():
    service_client = get_service_client()
    messages = create_messages()
    output = await send_messages(service_client, messages)

    if output:
        output_reply(output)
    
if __name__ == "__main__":
    asyncio.run(app_run())
```
