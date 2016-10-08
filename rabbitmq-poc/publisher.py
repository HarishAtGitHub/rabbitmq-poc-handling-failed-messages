#!/usr/bin/env python
import pika
import sys
import init_rabbitmq

message = sys.argv[1]
try:
    connection = pika.BlockingConnection()
    channel = connection.channel()
    channel.basic_publish(exchange='mobilesite-integration-exchange',
                          routing_key='mobilesite-integration',
                          body=message,
                          properties=pika.BasicProperties(
                              delivery_mode=2,  # TODO: make message persistent :tells RabbitMQ to save the message to disk(
                              # being extra cautious - see if it has performance concerns)
                          ))
    print('SENT the following message ' + message)
    connection.close()
except Exception as e:
    print(e)
