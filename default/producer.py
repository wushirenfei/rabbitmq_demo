import pika
import time


# 用户名密码获取认证信息，附带该信息方可成功连接RabbitMQ
credentials = pika.PlainCredentials('tester', 'test_password')
connection = pika.BlockingConnection(pika.ConnectionParameters(
    'localhost', credentials=credentials))

# 一个connection中开启多个channel
channel = connection.channel()
channel2 = connection.channel()

# 声明队列
channel.queue_declare(queue='first_queue', durable=True)

i = 0

while i < 5:
    time.sleep(1)
    a = '{} message'.format(i)
    channel.basic_publish(
        exchange='', routing_key='first_queue', body=a,
        properties=pika.BasicProperties(
            delivery_mode=2,  # make message persistent
        )
    )
    i += 1

connection.close()
