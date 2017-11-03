import pika
import time


def callback(ch, method, properties, body):
    time.sleep(2)
    print("consumer [x] Received %r" % (body,))
    ch.basic_ack(delivery_tag=method.delivery_tag)


credentials = pika.PlainCredentials('tester', 'test_password')
connection = pika.BlockingConnection(pika.ConnectionParameters(
    'localhost', credentials=credentials))

channel = connection.channel()

channel.exchange_declare(exchange='topic_exchange', exchange_type='topic')

result = channel.queue_declare(exclusive=True)

queue_name = result.method.queue

channel.queue_bind(
    exchange='topic_exchange', routing_key='*.*.t1', queue=queue_name)

channel.basic_consume(callback, queue=queue_name)

print('Consumer1 waiting for messages. To exit press CTRL+C')
channel.start_consuming()
