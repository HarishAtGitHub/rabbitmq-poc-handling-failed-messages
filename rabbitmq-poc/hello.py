#!/usr/bin/env python
import pika
try:
    '''
    connection = pika.BlockingConnection(pika.ConnectionParameters(
                   'master'))
    '''
    connection = pika.BlockingConnection()
    channel = connection.channel()
except Exception:
    print("ex")
