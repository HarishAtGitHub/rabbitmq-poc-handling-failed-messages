# rabbitmq-poc-handling-failed-messages
POC to see how to handle if the message processing by one of the consumes fails

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

