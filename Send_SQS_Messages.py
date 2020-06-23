#code deployed for creating an SQS message

import boto3
sqs=boto3.resource("sqs")
#sending messages on AWS SQS
queue = sqs.get_queue_by_name(
    QueueName='test')

response = queue.send_message(
    MessageBody='Sending a nice message')

print(response.get("MessageId"))
print(response.get("MD5OfMessageBody"))
