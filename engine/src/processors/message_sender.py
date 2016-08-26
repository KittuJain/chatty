import logging
import pika

class MessageSender:
  def __init__(self, connection, queue):
    self.queue = queue
    self.logger = logging.getLogger("MessageSender")
    try:
      self.channel = connection.channel()
      self.logger.info("create channel connection for %s", queue)
      self.channel.queue_declare(queue=queue, durable=True)
    except Exception as e:
      self.logger.error('Error connecting to task queue %s',e)


  def send(self, message):
    self.channel.basic_publish(exchange='',
                               routing_key=self.queue,
                               body=message,
                               properties=pika.BasicProperties(delivery_mode = 2, )
                              )