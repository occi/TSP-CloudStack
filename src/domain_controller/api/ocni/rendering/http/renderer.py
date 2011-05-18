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

from domain_controller.api.ocni.occi.occi_core import category
from domain_controller.api.ocni.occi.occi_core import kind
from domain_controller.api.ocni.occi.occi_core import mixin
from domain_controller.api.ocni.occi.occi_core import action
from domain_controller.api.ocni.occi.occi_core import entity
from domain_controller.api.ocni.occi.occi_core import resource
from domain_controller.api.ocni.occi.occi_core import link

from domain_controller.api.ocni.registry.registry import location_registry

import logging.config

# Loading the logging configuration file
logging.config.fileConfig("../../../../CloNeLogging.conf")
# getting the Logger
logger = logging.getLogger("CloNeLogging")

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
# headers
# ======================================================================================
header_category = "Category"
header_link = "Link"
header_attribute = "X-OCCI-Attribute"
header_location = "X-OCCI-Location"


# ======================================================================================
# OCCI Category rendering
# Rendering of the OCCI Category, Kind and Mixin types
# ======================================================================================
class category_renderer(object):
    def renderer(self, obj):
        header = {}
        category_value = ''
        category_param = ''

        if isinstance(obj, kind):
            _category = obj
            _classe = 'kind'
        elif isinstance(obj, mixin):
            _category = obj
            _classe = 'mixin'
        elif isinstance(obj, action):
            _category = obj.category
            _classe = 'action'
        else:
            logger.warning("Object bad type: Only a kind, mixin or an action can be rendered as a category")
            raise ("Object bad type: Only a kind, mixin or an action can be rendered as a category")

        category_value += _category.term + ';\nscheme="' + _category.scheme + '";\nclass="' + _classe + '";\n'

        if _category.title != '':
            category_param += 'title="' + _category.title + '";\n'

        if _category.related.__len__() > 0:
            __related_objects = ''
            for rel in _category.related:
                __related_objects += rel.__repr__() + " "
            category_param += 'rel="' + __related_objects + '";\n'

        _location_registry = location_registry()
        _location = _location_registry.get_location(_category)
        category_param += 'location=' + _location + ';\n'

        if _classe == 'kind' or _classe == 'mixin':
            __attributes = ''
            for __attribute in _category.attributes:
                __attributes += __attribute + ' '
            category_param += 'attributes="' + __attributes + '";\n'

        if _classe == 'kind' or _classe == 'mixin':
            __actions = ''
            for __action in _category.actions:
                __actions += __action.__repr__() + ' '
            category_param += 'actions="' + __actions + '";'

        header[header_category] = category_value + category_param

        return header[header_category]


# ======================================================================================
# OCCI Link instance rendering
# Rendering of OCCI Link instance references
# ======================================================================================
class link_renderer(object):
    def renderer(self, obj):
        header = {}
        link_value = ''
        link_param = ''

        if isinstance(obj, link):
            _location_registry = location_registry()
            _location_of_obj = _location_registry.get_location(obj)
            _source = obj.source
            _target_location = obj.target
            _target_object = _location_registry.get_object(_target_location)

            link_value += _target_location + ';\nrel="' + _target_object.kind.__repr__() + '";\nself="' + _location_of_obj + '";\n'

            link_param += 'category="' + obj.kind.__repr__() + '";\n'
            

        else:
            logger.warning("Object bad type: Only a Link can be rendered")
            raise ("Object bad type: Only a Link can be rendered")

        header[header_link] = link_value + link_param

        return header[header_link]

# ======================================================================================
# OCCI action instance rendering
# Rendering of references to OCCI Action instances
# ======================================================================================
class action_renderer(object):
    def renderer(self, obj):
        header = {}
        pass

# ======================================================================================
# OCCI Entity attributes rendering
# Rendering of OCCI Entity attributes
# ======================================================================================
class attributes_renderer(object):
    def renderer(self, obj):
        header = {}
        pass

# ======================================================================================
# OCCI Location-URIs rendering
# Rendering of Location-URIs
# ======================================================================================
class location_renderer(object):
    def renderer(self, obj):
        header = {}
        pass


# ======================================================================================
# main
# ======================================================================================
if __name__ == '__main__':
    print 'test'
    pass