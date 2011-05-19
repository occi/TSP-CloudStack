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

from domain_controller.api.ocni.occi.occi_core import Category, Kind, Mixin, Action, Entity, Resource, Link

from domain_controller.api.ocni.occi.occi_infrastructure import Compute, Network, Storage,\
    NetworkInterface, StorageLink, IPNetworking, IPNetworkInterface


# Loading the logging configuration file
logging.config.fileConfig("../../../../CloNeLogging.conf")
# getting the Logger
logger = logging.getLogger("CloNeLogging")

# ======================================================================================
# Location registry
# ======================================================================================
class location_registry(object):
    """

    A registry containing all the locations

    """

    # locations[object_id] = location
    locations = {}

    # objects[location] = object
    objects = {}

    def __init__(self):
        pass

    def register_location(self, location, object):
        if  object.__repr__() in location_registry.locations:
            logger.warning('the location \'' + location + '\' is already registered')
            raise ('the location \'' + location + '\' is already registered')
        elif location in location_registry.objects:
            logger.warning('the object \'' + object + '\' is already registered')
            raise ('the object \'' + object + '\' is already registered')
        else:
            logger.debug("Registering the location \'" + location + "\' to the object \'" + object.__repr__() + "\'")
            location_registry.locations[object.__repr__()] = location
            location_registry.objects[location] = object

    def unregister_location(self, location):
        if location in location_registry.objects:
            logger.debug("Un-registering the location \'" + location + "\'")
            del location_registry.locations[location_registry.objects[location].__repr__()]
            del location_registry.objects[location]
        else:
            logger.WARNING("The location \'" + location + "\'" + " is not registered")

    def get_location(self, object):
        return location_registry.locations.get(object.__repr__())

    def get_object(self, location):
        return location_registry.objects.get(location)

    def get_object_under_location(self, location_path):
        _objects = []
        for _location in location_registry.objects:
            if _location.startswith(location_path):
                _objects.append(location_registry.objects[_location])
        return _objects


# ======================================================================================
# category registry
# ======================================================================================
class category_registry(object):
    """

    A registry containing all the Kinds, Mixins and actions

    """

    # A dictionary of all kinds
    kinds = {}
    # A dictionary of all mixins
    mixins = {}
    # A dictionary of all actions
    actions = {}

    def __init__(self):
    #        self.register_kind(entity._entity_kind)
    #        self.register_kind(resource._resource_kind)
    #        self.register_kind(link._link_kind)
    #
    #        self.register_kind(compute._compute_kind)
    #        self.register_kind(network._network_kind)
    #        self.register_kind(storage._storage_kind)
    #        self.register_kind(network_interface._network_interface_kind)
    #        self.register_kind(storage_link._storage_link_kind)
    #
    #        self.register_mixin(ip_networking())
    #        self.register_mixin(ip_network_interface())
        pass

    def register_kind(self, _kind):
        logger.debug("Registering the kind: " + _kind.__repr__())
        if isinstance(_kind, Kind):
            category_registry.kinds[_kind.__repr__()] = _kind
            for _action in _kind.actions:
                self.register_action(_action)
        else:
            logger.warning("Cannot register the category: bad type")

    def register_mixin(self, _mixin):
        logger.debug("Registering the mixin: " + _mixin.__repr__())
        if isinstance(_mixin, Mixin):
            category_registry.mixins[_mixin.__repr__()] = _mixin
            for _action in _mixin.actions:
                self.register_action(_action)
        else:
            logger.warning("Cannot register the category: bad type")

    def register_action(self, _action):
        logger.debug("Registering the action: " + _action.__repr__())
        category_registry.actions[_action.category.__repr__()] = _action

    def unregister_kind(self, _kind):
        logger.debug("Un-registering the kind: " + _kind.__repr__())
        del category_registry.kinds[_kind.__repr__()]

    def unregister_mixin(self, _mixin):
        logger.debug("Un-registering the mixin: " + _mixin.__repr__())
        del category_registry.mixins[_mixin.__repr__()]

    def unregister_action(self, _action):
        logger.debug("Un-registering the action: " + _action.__repr__())
        del category_registry.actions[_action.__repr__()]

    def get_kind(self, kind_id):
        return category_registry.kinds[kind_id]

    def get_mixin(self, mixin_id):
        return category_registry.mixins[mixin_id]

    def get_action(self, action_id):
        return category_registry.actions[action_id]

    def get_category(self, category_id):
        return category_registry.kinds.get(category_id) or category_registry.mixins.get(category_id)

    def get_kinds(self):
        return category_registry.kinds

    def get_mixins(self):
        return category_registry.mixins

    def get_actions(self):
        return category_registry.actions

    def get_categories(self):
        return dict(category_registry.kinds.items() + category_registry.mixins.items())

# ======================================================================================
# backend registry                     (To do)
# ======================================================================================
class backend_registry():
    backends = {}

    def register_backend(self):
        pass

    def unregister_backend(self):
        pass

    def get_backend(self):
        pass

# ======================================================================================
# rendering registry                     (To do)
# ======================================================================================
class rendering_registry():
    renderers = {}

    def register_renderer(self):
        pass

    def unregister_renderer(self):
        pass

    def get_renderer(self):
        pass

# ======================================================================================
# main
# ======================================================================================

if __name__ == '__main__':
    #ca = category_registry()
    #print ca.kinds
    #print ca.mixins
    #print ca.actions
    #print ca.get_categories()
    path = "/-/"
    loc = path.lstrip('/')
    print loc
    print not loc
    pass