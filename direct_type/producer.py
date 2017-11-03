import pika
import time

credentials = pika.PlainCredentials('tester', 'test_password')
connection = pika.BlockingConnection(pika.ConnectionParameters(
    'localhost', credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='direct_exchange', exchange_type='direct')

i = 0
while i < 5:
    time.sleep(1)
    a = '{} message'.format(i)
    if i < 2:
        channel.basic_publish(
            exchange='direct_exchange', routing_key='mini', body=a)
    else:
        channel.basic_publish(
            exchange='direct_exchange', routing_key='max', body=a)

    i += 1

connection.close()


