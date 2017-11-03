import pika
import time


def callback(ch, method, properties, body):
    time.sleep(2)
    print(" [x] Received %r" % (body,))
    ch.basic_ack(delivery_tag=method.delivery_tag)

credentials = pika.PlainCredentials('tester', 'test_password')
connection = pika.BlockingConnection(pika.ConnectionParameters(
    'localhost', credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='fanout_exchange', exchange_type='fanout')

channel.queue_declare(queue='fanout_consumer2')

channel.queue_bind(queue='fanout_consumer2', exchange='fanout_exchange')

channel.basic_consume(callback, queue='fanout_consumer2')

print('Consumer1 waiting for messages. To exit press CTRL+C')
channel.start_consuming()
