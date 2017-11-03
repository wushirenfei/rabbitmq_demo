import pika
import time

credentials = pika.PlainCredentials('tester', 'test_password')
connection = pika.BlockingConnection(pika.ConnectionParameters(
    'localhost', credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='topic_exchange', exchange_type='topic')

routing_mapping = {
    0: 'tech.front',
    1: 'tech.end.t1',
    2: 'hr.g1.t1',
    3: 'hr.g2.t1',
    4: 'hr.g2.t2.',
}

i = 0

while i < 5:
    time.sleep(1)
    a = '{} message'.format(i)
    routing = routing_mapping[i % 5]

    channel.basic_publish(
        exchange='topic_exchange', routing_key=routing, body=a)

    i += 1

connection.close()
