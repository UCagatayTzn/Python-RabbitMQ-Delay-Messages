#!/usr/bin/env python
import pika
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

#channel.queue_declare(queue='task_queue')
print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    if "Hello World!.....1" == body:
        print(" wait 5 seconds ...")
        time.sleep(5)
    print(" [x] Received %r" % body)
    #time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


#channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)

channel.start_consuming()



""" delayed message """
"""
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='test-exchange',
                         exchange_type='x-delayed-message',
                         arguments={"x-delayed-type":"direct"})

# channel.assertExchange

result = channel.queue_declare(queue='task_queue', durable=True)

# ======
#channel.assertQueue
# ======


#queue_name = result.method.queue

#binding_keys = sys.argv[1:]
#if not binding_keys:
#    sys.stderr.write("Usage: %s [binding_key]...\n" % sys.argv[0])
#    sys.exit(1)

#for binding_key in binding_keys:

channel.queue_bind(exchange='test-exchange',
                    queue='task_queue'
                    ) #routing_key='task_queue'

# ======
#channel.bindQueue
# ======

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r:%r" % ('task_queue', body))

channel.basic_consume(queue='task_queue', on_message_callback=callback)

channel.start_consuming()
"""
