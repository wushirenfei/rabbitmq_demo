import pika
import time


def callback(ch, method, properties, body):
    time.sleep(1)
    # 1/0
    print("consumer_2 [x] Received %r" % (body,))
    ch.basic_ack(delivery_tag=method.delivery_tag)

credentials = pika.PlainCredentials('tester', 'test_password')
connection = pika.BlockingConnection(pika.ConnectionParameters(
    'localhost', credentials=credentials))

channel = connection.channel()

channel.queue_declare(queue='first_queue')

channel.basic_consume(callback, queue='first_queue')

print('Consumer_2 waiting for messages. To exit press CTRL+C')
channel.start_consuming()
