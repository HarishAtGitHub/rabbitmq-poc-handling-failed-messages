#!/usr/bin/env python
import pika
import sys
try:

    # step 1: create a tcp connection
    connection = pika.BlockingConnection()
    # step 2: create a channel within the tcp connection and start communicating
    # in that channel
    # why do we need a channel and not just a connection ?
    # answer: read page 14 of 'rabitmq in action' book
    channel = connection.channel()
    # does it create problems if queue already exists ?
    # no . this as per documentation creates queue if it does not already exist
    # ref : http://pika.readthedocs.io/en/0.10.0/modules/channel.html#pika.channel.Channel.queue_declare

    #auto-delete False is default so that it does not delete itself when the last consumer disconnects

    # create exchange - exchange is where message reaches
    # exchange server delivers it to the appropriate que based on routing key
    channel.exchange_declare(exchange='poc-exchange',
                             durable=True)
    channel.queue_declare(queue='poc-q',
                          durable=True,
                          arguments={
                              'x-dead-letter-exchange' : 'poc-exchange-rejects',
                              'x-dead-letter-routing-key' : 'poc-rejects'
                          }
                          )
    channel.queue_bind(queue='poc-q',
                       exchange='poc-exchange',
                       routing_key='poc')

    # create rejected message queue
    channel.exchange_declare(exchange='poc-exchange-rejects',
                             durable=True)
    channel.queue_declare(queue='poc-q-rejects',
                          durable=True)
    channel.queue_bind(queue='poc-q-rejects',
                       exchange='poc-exchange-rejects',
                       routing_key='poc-rejects')
    connection.close()
    print('Success ! doing initial setup of rabbitmq')
except Exception as e:
    print(e)

