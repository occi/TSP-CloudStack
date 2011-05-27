# -*- Mode: python; py-indent-offset: 4; indent-tabs-mode: nil; coding: utf-8; -*-

# Copyright (C) 2011 Houssem Medhioub - Institut Telecom
#
# This file is part of TSP-CloudStack.
#
# TSP-CloudStack is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as
# published by the Free Software Foundation, either version 3 of
# the License, or (at your option) any later version.
#
# TSP-CloudStack is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with TSP-CloudStack.  If not, see <http://www.gnu.org/licenses/>.

'''
Created on Feb 25, 2011

@author: Houssem Medhioub
@contact: houssem.medhioub@it-sudparis.eu
@organization: Institut Telecom - Telecom SudParis
@version: 0.1
@license: LGPL - Lesser General Public License
'''

import logging.config
from kombu.messaging import Exchange, Queue, Consumer, Producer
import connection_amqp

# Loading the logging configuration file
logging.config.fileConfig("../../CloNeLogging.conf")
# getting the Logger
logger = logging.getLogger("CloNeLogging")

class topic_exchange:
    def __init__(self, exchange_name):
        rabbitCon = connection_amqp.RabbitMQConnection()
        self.connection = rabbitCon.connection()
        self.channel = self.connection.channel()

        self.media_exchange = Exchange(exchange_name, type="topic", durable=True)

    def producer(self):
        producer = Producer(self.channel, exchange=self.media_exchange, serializer="json")
        #producer.exchange.delete()
        producer.publish({"name": "/tmp/lolcat1.avi", "size": 1301013})
        pass

    def consumer(self, queue_name):
        video_queue = Queue(queue_name, exchange=self.media_exchange)

        consumer = Consumer(self.channel, video_queue)
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