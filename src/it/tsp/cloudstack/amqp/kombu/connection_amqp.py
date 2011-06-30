# -*- Mode: python; py-indent-offset: 4; indent-tabs-mode: nil; coding: utf-8; -*-

# Copyright (C) 2011 Houssem Medhioub - Institut Telecom
#
# This library is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as
# published by the Free Software Foundation, either version 3 of
# the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this library.  If not, see <http://www.gnu.org/licenses/>.

'''
Created on Feb 25, 2011

@author: Houssem Medhioub
@contact: houssem.medhioub@it-sudparis.eu
@organization: Institut Telecom - Telecom SudParis
@version: 0.1
@license: LGPL - Lesser General Public License
'''

import os
import logging.config
from configobj import ConfigObj
from kombu.connection import BrokerConnection
from kombu.messaging import Exchange, Queue, Consumer, Producer

def get_absolute_path_from_relative_path(filename):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), filename))

# Loading the logging configuration file
logging.config.fileConfig(get_absolute_path_from_relative_path("../AMQPLogging.conf"))
# getting the Logger
logger = logging.getLogger("AMQPLogging")

config = ConfigObj(get_absolute_path_from_relative_path("./amqp.conf"))
AMQP_IP = config['AMQP_IP']
AMQP_PORT = config['AMQP_PORT']
AMQP_USER = config['AMQP_USER']
AMQP_PASSWORD = config['AMQP_PASSWORD']
AMQP_TRANSPORT = config['AMQP_TRANSPORT']


class RabbitMQConnection:
    def connection(self):
        try:
            logger.info("Connection to the AMQP broker '" + AMQP_IP + ":" + AMQP_PORT + "' ...")
            connection = BrokerConnection(hostname=AMQP_IP,
                                          port=AMQP_PORT,
                                          userid=AMQP_USER,
                                          password=AMQP_PASSWORD,
                                          virtual_host="/",
                                          transport=AMQP_TRANSPORT)
            #channel = connection.channel()
            logger.info("Connection to the AMQP broker established.")
            return connection
        except Exception as exep:
            logger.warning("Could not connect to the AMQP broker '" + AMQP_IP + ":" + AMQP_PORT + "'. | " + str(exep))

    def producer(self):
        self.connection = BrokerConnection(hostname=AMQP_IP, port=AMQP_PORT,
                                           userid=AMQP_USER, password=AMQP_PASSWORD,
                                           virtual_host="/",
                                           transport=AMQP_TRANSPORT)
        self.channel = self.connection.channel()
        # produce

        self.media_exchange = Exchange("media", "direct", durable=True)

        producer = Producer(self.channel, exchange=self.media_exchange, serializer="json")
        producer.publish({"name": "/tmp/lolcat1.avi", "size": 1301013})

        print self.connection.get_transport_cls()

    def consumer(self):
        self.connection = BrokerConnection(hostname=AMQP_IP, port=AMQP_PORT,
                                           userid=AMQP_USER, password=AMQP_PASSWORD,
                                           virtual_host="/")
        self.channel = self.connection.channel()

        # consume

        self.media_exchange = Exchange("media", "direct", durable=True)
        self.video_queue = Queue("video", exchange=self.media_exchange, key="video")

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
    con = RabbitMQConnection()
    con.connection()
    pass