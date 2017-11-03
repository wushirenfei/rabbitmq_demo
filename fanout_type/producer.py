import pika
import time

credentials = pika.PlainCredentials('tester', 'test_password')
connection = pika.BlockingConnection(pika.ConnectionParameters(
    'localhost', credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='fanout_exchange', exchange_type='fanout')

i = 0

while i < 5:
    time.sleep(1)
    a = '{} message'.format(i)
    channel.basic_publish(exchange='fanout_exchange', routing_key='', body=a)
    i += 1

connection.close()
