#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.assertExchange('', "x-delayed-message", {"autoDelete": False,"durable": True,"passive": True,"arguments": {'x-delayed-type': "direct"} } )

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello Test World!', headers={"headers": {"x-delay": 10000} })
print(" [x] Sent 'Hello World!'")

connection.close()


