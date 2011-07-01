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

import pika
import os
import logging.config
from configobj import ConfigObj

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
AMQP_VIRTUAL_HOST = config['AMQP_VIRTUAL_HOST']

def connection():
    try:
        logger.info("Connection to the AMQP broker '" + AMQP_IP + ":" + AMQP_PORT + "' ...")
        connection = pika.BlockingConnection(pika.ConnectionParameters(
            host=AMQP_IP,
            port=int(AMQP_PORT),
            virtual_host=AMQP_VIRTUAL_HOST,
            credentials=pika.PlainCredentials(AMQP_USER, AMQP_PASSWORD)))

        logger.info("Connection to the AMQP broker established.")
        return connection
    except Exception as exep:
        logger.warning("Could not connect to the AMQP broker '" + AMQP_IP + ":" + AMQP_PORT + "'. | " + str(exep))

if __name__ == '__main__':
    connection()
    pass