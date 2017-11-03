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

channel.exchange_declare(exchange='direct_exchange', exchange_type='direct')

# 固定队列名称，去除exclusive=True参数，否则无法启动多个
channel.queue_declare(queue='mini_queue')

channel.queue_bind(
    exchange='direct_exchange', routing_key='mini', queue='mini_queue')

channel.basic_consume(callback, queue='mini_queue')

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
