#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

""" x-delayed-message """

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

#channel.exchange_declare(exchange='direct_logs',
#                         exchange_type='direct')

#channel.exchange_declare("test-exchange", type="x-delayed-message", arguments={"x-delayed-type":"direct"},durable=True,auto_delete=True)
channel.exchange_declare(exchange='test-exchange',
                         exchange_type='x-delayed-message',
                         arguments={"x-delayed-type":"direct"})


severity = sys.argv[1] if len(sys.argv) > 2 else 'task_queue'
message = ' '.join(sys.argv[2:]) or 'Delay message '

channel.queue_declare(queue='task_queue',durable=True)

channel.queue_bind(queue="task_queue", exchange="test-exchange") #routing_key="task_queue"

for i in range(0,5):
    channel.basic_publish(exchange='test-exchange',
                        routing_key='task_queue',
                        properties=pika.BasicProperties(
                            headers={'x-delay': 10000} # Add a key/value header
                        ),
                        body=message + str(i))
    print(" [x] Sent %r:%r" % (severity, message))
connection.close()