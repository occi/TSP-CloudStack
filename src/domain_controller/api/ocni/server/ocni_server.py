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

import logging.config
import eventlet
from eventlet import wsgi
import uuid
import re

from domain_controller.api.ocni.occi.occi_core import Category, Kind, Mixin, Action, Entity, Resource, Link

from domain_controller.api.ocni.occi.occi_infrastructure import Compute, Network, Storage,\
    NetworkInterface, StorageLink, IPNetworking, IPNetworkInterface

from domain_controller.api.ocni.registry.registry import category_registry, location_registry

from domain_controller.api.ocni.rendering.http.renderer import category_renderer

# Loading the logging configuration file
logging.config.fileConfig("../../../../CloNeLogging.conf")
# getting the Logger
logger = logging.getLogger("CloNeLogging")


# ======================================================================================
# the category registry
# ======================================================================================

category_registry = category_registry()

# register OCCI Core kinds
category_registry.register_kind(Entity._kind)
category_registry.register_kind(Resource._kind)
category_registry.register_kind(Link._kind)

# register OCCI Infrastructure kinds
category_registry.register_kind(Compute._kind)
category_registry.register_kind(Network._kind)
category_registry.register_kind(Storage._kind)
category_registry.register_kind(NetworkInterface._kind)
category_registry.register_kind(StorageLink._kind)

# register OCCI Infrastructure mixins
category_registry.register_mixin(IPNetworking())
category_registry.register_mixin(IPNetworkInterface())

# ======================================================================================
# the location registry
# ======================================================================================

location_registry = location_registry()

# register OCCI Core kind locations
location_registry.register_location("/resource/", Resource._kind)
location_registry.register_location("/link/", Link._kind)

# register OCCI Infrastructure kind locations
location_registry.register_location("/compute/", Compute._kind)
location_registry.register_location("/network/", Network._kind)
location_registry.register_location("/storage/", Storage._kind)
location_registry.register_location("/networkinterface/", NetworkInterface._kind)
location_registry.register_location("/storagelink/", StorageLink._kind)

# register OCCI Infrastructure mixin locations
location_registry.register_location("/ipnetworking/", IPNetworking())
location_registry.register_location("/ipnetworkinterface/", IPNetworkInterface())



# ======================================================================================
# Handling the Query Interface
# ======================================================================================
#
#   Retrieval of all registered Kinds and Mixins
#
#       Retrieval of a filtered list of Kinds and Mixins
#
#   Adding a Mixin definition
#
#   Removing a Mixin definition


# ======================================================================================
# Operation on Paths in the Name-space
# ======================================================================================
#
#   Retrieving All resource instances Below a Path
#
#   Deletion of all resource instances below a path


# ======================================================================================
# Operations on Mixins or Kinds
# ======================================================================================
#
#   Retrieving all Resource Instances belonging to Mixin or Kind
#
#   Triggering actions on All Instances of a Mixin or Kind
#
#   Associate resource instances with Mixins
#
#   Unassociated resource instance(s) from a Mixin

# ======================================================================================
# Operations on Resource Instances
# ======================================================================================
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

# ======================================================================================
# Handling Links resource instances
# ======================================================================================
#
#   Creation of a Link during creation of a Resource instance
#
#   Retrieval resource instances of the type Resource with defined Links
#
#   Creation of Link resource instances
#
#   Retrieval of Link resource instances


# CRUD should be available

#def hello_world(env, start_response):
#    if env['PATH_INFO'] != '/':
#        start_response('404 Not Found', [('Content-Type', 'text/plain')])
#        return ['Not Found\r\n']
#    start_response('200 OK', [('Content-Type', 'text/plain')])
#    return ['Hello, World!\r\n']
#
#wsgi.server(eventlet.listen(('', 8090)), hello_world)

if __name__ == '__main__':
    c = category_renderer()
    print '###########################'
    print c.renderer(Link._storage_kind)

    pass