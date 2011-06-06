# -*- Mode: python; py-indent-offset: 4; indent-tabs-mode: nil; coding: utf-8; -*-

# Copyright (C) 2011 Houssem Medhioub - Institut Telecom
#
#
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

import logging.config
import eventlet
from eventlet import wsgi
#from webob import Request
import uuid
import re

from domain_controller.api.ocni.occi.occi_core import Category, Kind, Mixin, Action, Entity, Resource, Link

from domain_controller.api.ocni.occi.occi_infrastructure import Compute, Network, Storage,\
    NetworkInterface, StorageLink, IPNetworking, IPNetworkInterface

from domain_controller.api.ocni.registry.registry import category_registry, location_registry

from domain_controller.api.ocni.rendering.http.renderer import category_renderer, link_renderer, action_renderer, attributes_renderer, location_renderer

# Loading the logging configuration file
logging.config.fileConfig("../../../../DCPLogging.conf")
# getting the Logger
logger = logging.getLogger("DCPLogging")

# ======================================================================================
# HTTP Return Codes
# ======================================================================================
return_code = {'OK': 200,
               'Accepted': 202,
               'Bad Request': 400,
               'Unauthorized': 401,
               'Forbidden': 403,
               'Method Not Allowed': 405,
               'Conflict': 409,
               'Gone': 410,
               'Unsupported Media Type': 415,
               'Internal Server Error': 500,
               'Not Implemented': 501,
               'Service Unavailable': 503}


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




class Server(object):
    """

    A class to manage multiple WSGI sockets and applications.

    """
    pass


if __name__ == '__main__':
    logger.debug('############ BEGIN OCCI Category rendering ###############')
    c = category_renderer()
    result = c.renderer(Compute._kind)
    logger.debug(result.get('Category'))
    logger.debug('############# END OCCI Category rendering ################')

    logger.debug('############ BEGIN OCCI Link instance rendering ###############')
    network_instance = Network('/network/123', 'active')
    location_registry.register_location("/network/123", network_instance)

    networkinterface_instance = NetworkInterface('456', 'source', '/network/123', '192.168.1.2', '00:00:10:20:30:40',
                                                 'active')
    location_registry.register_location("/link/networkinterface/456", networkinterface_instance)

    l = link_renderer()
    result = l.renderer(NetworkInterface('456', 'source', '/network/123', 'eth0', '00:01:20:50:90:80', 'active'))
    logger.debug(result.get('Link'))
    logger.debug('############# END OCCI Link instance rendering ################')

    logger.debug('############ BEGIN OCCI Action instance rendering ###############')
    compute_instance = Compute('/compute/123', 'active')
    location_registry.register_location("/compute/123", compute_instance)

    a = action_renderer()
    result = a.renderer(compute_instance, Compute._action_start)
    logger.debug(result.get('Link'))
    logger.debug('############# END OCCI Action instance rendering ################')

    logger.debug('############# Begin OCCI Entity attributes rendering ################')
    att = attributes_renderer()
    result = att.renderer(compute_instance)
    result2 = result.get('X-OCCI-Attribute')
    for r in result2:
        logger.debug('X-OCCI-Attribute' + ': ' + r)
    logger.debug('############# END OCCI Entity attributes rendering ################')

    logger.debug('############# BEGIN OCCI Location-URIs rendering ################')
    location = location_renderer()
    temp = location_registry.locations.values()

    result = location.renderer(temp)
    result2 = result.get('X-OCCI-Location')
    for r in result2:
        logger.debug('X-OCCI-Location' + ': ' + r)
    logger.debug('############# END OCCI Location-URIs rendering ################')
    pass