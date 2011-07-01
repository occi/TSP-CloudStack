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

import it.tsp.cloudstack.amqp.pika.connection_amqp as RabbitMQConnection
import time

connection = RabbitMQConnection.connection()
channel = connection.channel()


channel.queue_declare(queue='task_queue')
#channel.queue_declare(queue='task_queue', durable=True)
print ' [Consumer] Waiting for messages. To exit press CTRL+C'

def callback(ch, method, properties, body):
    print " [Consumer] Received %r" % (body,)
    time.sleep( body.count('.') )
    print " [Consumer] Done"
    ch.basic_ack(delivery_tag = method.delivery_tag)

# == Fair dispatch ==
#channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue='task_queue')

channel.start_consuming()