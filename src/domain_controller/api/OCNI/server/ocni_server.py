# -*- Mode: python; py-indent-offset: 4; indent-tabs-mode: nil; coding: utf-8; -*-

# Copyright (C) 2011 Houssem Medhioub - Institut Telecom
#
# This file is part of CloNeDCP.
#
# CloNeDCP is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as
# published by the Free Software Foundation, either version 3 of
# the License, or (at your option) any later version.
#
# CloNeDCP is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with CloNeDCP.  If not, see <http://www.gnu.org/licenses/>.

'''
Created on Feb 25, 2011

@author: Houssem Medhioub
@contact: houssem.medhioub@it-sudparis.eu
@organization: Institut Telecom - Telecom SudParis
@version: 0.1
@license: LGPL - Lesser General Public License
'''

import eventlet
from eventlet import wsgi
import uuid
import re


# CRUD should be available

def hello_world(env, start_response):
    if env['PATH_INFO'] != '/':
        start_response('404 Not Found', [('Content-Type', 'text/plain')])
        return ['Not Found\r\n']
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return ['Hello, World!\r\n']

wsgi.server(eventlet.listen(('', 8090)), hello_world)


# =======
# Handling the Query Interface
#
#   Retrieval of all registered Kinds and Mixins
#
#       Retrieval of a filtered list of Kinds and Mixins
#
#   Adding a Mixin definition
#
#   Removing a Mixin definition


# =======
# Operation on Paths in the Name-space
#
#   Retrieving All resource instances Below a Path
#
#   Deletion of all resource instances below a path

# =======
# Operations on Mixins or Kinds
#
#   Retrieving all Resource Instances belonging to Mixin or Kind
#
#   Triggering actions on All Instances of a Mixin or Kind
#
#   Associate resource instances with Mixins
#
#   Unassociated resource instance(s) from a Mixin

# =======
# Operations on Resource Instances
#
#   Creating a resource instance
#
#   Retrieving a resource instance
#
#   Updating a resource instance
#
#   Deleting a resource instance
#
#   Triggering an Action on a resource instance

# =======
# Handling Links resource instances
#
#   Creation of a Link during creation of a Resource instance
#
#   Retrieval resource instances of the type Resource with defined Links
#
#   Creation of Link resource instances
#
#   Retrieval of Link resource instances
