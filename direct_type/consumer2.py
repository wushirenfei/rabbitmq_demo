import pika
import time


def callback(ch, method, properties, body):
    time.sleep(1)
    print("consumer_e [x] Received %r" % (body,))
    ch.basic_ack(delivery_tag=method.delivery_tag)

credentials = pika.PlainCredentials('tester', 'test_password')
connection = pika.BlockingConnection(pika.ConnectionParameters(
    'localhost', credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='direct_exchange', exchange_type='direct')

result = channel.queue_declare(exclusive=True)

queue_name = result.method.queue

channel.queue_bind(
    exchange='direct_exchange', routing_key='max', queue=queue_name)

channel.basic_consume(callback, queue=queue_name)


print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
