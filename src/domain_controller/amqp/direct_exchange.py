# -*- Mode: python; py-indent-offset: 4; indent-tabs-mode: nil; coding: utf-8; -*-

# Copyright 2011 Institut Telecom - Telecom SudParis.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

'''
Created on Feb 25, 2011

@author: Houssem Medhioub
@contact: houssem.medhioub@it-sudparis.eu
@organization: Institut Telecom - Telecom SudParis
@version: 0.1
@license: Apache License, Version 2.0
'''
import logging.config
from kombu.messaging import Exchange, Queue, Consumer, Producer
import connection_amqp

# Loading the logging configuration file
logging.config.fileConfig("../../CloNeLogging.conf")
# getting the Logger
logger = logging.getLogger("CloNeLogging")

class direct_exchange:

    def __init__(self, exchange_name):
        rabbitCon = connection_amqp.RabbitMQConnection()
        self.connection = rabbitCon.connection()
        self.channel = self.connection.channel()

        self.media_exchange = Exchange(exchange_name, type="direct", durable=True)

    def producer(self, routingKey):
        producer = Producer(self.channel, exchange=self.media_exchange, serializer="json", routing_key=routingKey)
        #producer.exchange.delete()
        producer.publish({"name": "/tmp/lolcat1.avi", "size": 1301013})
        pass

    def consumer(self, queue_name, queue_key):
        video_queue = Queue(queue_name, exchange=self.media_exchange, routing_key=queue_key, auto_delete=True)

        consumer = Consumer(self.channel, video_queue)

        #To delete the queue
        #bound_science_news = video_queue(self.channel)
        #bound_science_news.delete()

        consumer.register_callback(self.process_media)
        consumer.consume()
        # Process messages on all channels
        while True:
            self.connection.drain_events()
        pass

    def process_media(self, message_data, message):
        feed_url = message_data["name"]
        print ("Got feed import message for: %s" % feed_url)
        # something importing this feed url
        # import_feed(feed_url)
        message.ack()

if __name__ == '__main__':
    pass