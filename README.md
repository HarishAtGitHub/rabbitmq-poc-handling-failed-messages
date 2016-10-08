# rabbitmq-poc-handling-failed-messages
POC to see how to handle if the message processing by one of the consumer fails.

Rabbitmq is a message broker software implementing the AMQP protocol.

This POC shows the feature in Rabbitmq known as dead lettering to handle the case where the message
has been sent from rabbitmq to a consumer but consumer fails  to process the message.

This set up has a main queue.

Then it has a deadletter queue which receives the messages that were rejected by the consumer.

The main queue is configured with this deadletter queue.

Then there are two consumers receiver1.py and receiver2.py which consumes messages from the main queue.

Publisher.py is a producer.

# How to execute ?

```python
python receiver1.py

python receiver2.py

python receiver-rejects.py

python publisher.py <inputmessage>
```

You will observer that I reject all the messages that I get in receiver1. So what happens is it goes to the dead letter queue
and as 'receiver-rejects' has subscribed to this queue, it gets the rejected messages and it starts processing.

There are two possibilities after that:

1) The receive-rejects job gets the failed messages and tries to process it again and now it the processing is successfull.

2) If it fails again, either it can requeue and retry or it can send an email to someone saying that the following message was failed.

In this poc just for the sake of simplicity I am making the message processing successful at the 'receiver-rejects' end.
