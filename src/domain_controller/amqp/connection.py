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
from configobj import ConfigObj

from kombu.connection import BrokerConnection
from kombu.messaging import Exchange, Queue, Consumer, Producer

# Loading the logging configuration file
logging.config.fileConfig("../../CloNeLogging.conf")
# getting the Logger
logger = logging.getLogger("CloNeLogging")

config = ConfigObj("amqp.conf")
AMQP_IP = config['AMQP_IP']
AMQP_PORT = config['AMQP_PORT']
AMQP_USER = config['AMQP_USER']
AMQP_PASSWORD = config['AMQP_PASSWORD']


class RabbitMQConnection:
    def __init__(self):
        try:
            print "d"
        except Exception as exep:
            logger.warning("Could not connect to the AMQP broker. | '"  + str(exep))

    def producer(self):
        self.media_exchange = Exchange("media", "direct", durable=True)
        self.video_queue = Queue("video", exchange=self.media_exchange, key="video")

        self.connection = BrokerConnection(hostname=AMQP_IP, port=5672,
                                          userid=AMQP_USER, password=AMQP_PASSWORD,
                                          virtual_host="/",
                                          transport="amqplib")
        self.channel = self.connection.channel()
        # produce
        producer = Producer(self.channel, exchange=self.media_exchange, serializer="json")
        producer.publish({"name": "/tmp/lolcat1.avi", "size": 1301013})

        print self.connection.get_transport_cls()
        
    def consumer(self):
        self.media_exchange = Exchange("media", "direct", durable=True)
        self.video_queue = Queue("video", exchange=self.media_exchange, key="video")

        self.connection = BrokerConnection(hostname=AMQP_IP, port=5672,
                                          userid=AMQP_USER, password=AMQP_PASSWORD,
                                          virtual_host="/")
        self.channel = self.connection.channel()



        # consume
        consumer = Consumer(self.channel, self.video_queue)
        consumer.register_callback(self.process_media)
        consumer.consume()
        # Process messages on all channels
        while True:
            self.connection.drain_events()



    def process_media(self, message_data, message):
        feed_url = message_data["name"]
        print ("Got feed import message for: %s" % feed_url)
        # something importing this feed url
        # import_feed(feed_url)
        message.ack()


if __name__ == '__main__':
    pass