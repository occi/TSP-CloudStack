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
from carrot.connection import BrokerConnection
from carrot.messaging import Consumer

logging.config.fileConfig("../../CloNeLogging.conf")
logger = logging.getLogger("CloNeLogging")

config = ConfigObj("amqp.conf")
AMQP_IP = config['AMQP_IP']
AMQP_PORT = config['AMQP_PORT']
AMQP_USER = config['AMQP_USER']
AMQP_PASSWORD = config['AMQP_PASSWORD']

conn = BrokerConnection(hostname=AMQP_IP, port=AMQP_PORT,
                           userid=AMQP_USER, password=AMQP_PASSWORD,
                           virtual_host="/")

consumer = Consumer(connection=conn, queue="feed", exchange="feed", routing_key="importer")
def import_feed_callback(message_data, message):
    feed_url = message_data["import_feed"]
    print("Got feed import message for: %s" % feed_url)
    # something importing this feed url
    # import_feed(feed_url)
    message.ack()
consumer.register_callback(import_feed_callback)
consumer.wait() # Go into the consumer loop.
