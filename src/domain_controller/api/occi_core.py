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
occi_core module implements the OCCI Core Model

Created on Feb 25, 2011

@author: Houssem Medhioub
@contact: houssem.medhioub@it-sudparis.eu
@organization: Institut Telecom - Telecom SudParis
@version: 0.1
@license: Apache License, Version 2.0
'''

class category(object):
    """

    The category type is the basis of the type identification mechanism used by the OCCI classification system.

    """
    def __init__(self):
        # Unique identifier of the category instance within the categorisation scheme
        self.term = ''
        # The categorisation scheme 
        self.scheme = ''
        # The display name of an instance
        self.title = ''
        # The set of resource attribute names defined by the category instance
        self.attributes = []

    def __repr__(self):
        return "identifier: " + self.scheme + "#" + self.term

class kind(category):
    """

    The kind type, together with the Mixin type, defines the classification system of the OCCI Core Model.
    The Kind type represents the type identification mechanism for all Entity types present in the model.

    """
    def __init__(self):
        super(kind, self).__init__()
        # set of actions defined by the Kind instance
        self.actions = []
        # set of related Kind instances
        self.related = []
        # Entity type uniquely identified by the Kind instance
        self.entity_type = ''
        # set of resource instances, i.e. Entity sub-type instances.
        # Resources instantiated from the Entity sub-type which is uniquely identified by this Kind instance.
        self.entities = []


class mixin(category):
    """

    The Mixin type complements the Kind type in defining the OCCI Core Model type classification system.
    The Mixin type represent an extension mechanism, which allows new resource capabilities to be added
        to resource instances both at creation-time and/or run-time.
    A Mixin instance can be associated with any existing resource instance and thereby add new resource
        capabilities, i.e. attributes and Actions, to the resource instance. However, a Mixin can never
        be applied to a type.

    """
    def __init__(self):
        super(mixin, self).__init__()
        # set of actions defined by the Mixin instance
        self.actions = []
        # set of related Mixin instances
        self.related = []
        # set of resource instances, i.e. Entity sub-type instances, associated with the Mixin instance.
        self.entities = []


class action(object):
    """

    The Action type is an abstract type. Each sub-type of Action defines an invocable
        operation applicable to an Entity sub-type instance or a collection thereof.

    """
    __category_instance = category()
    __category_instance.term = 'action'
    __category_instance.scheme = 'http://schemas.ogf/occi/core'
    __category_instance.title = 'Action'
    __category_instance.attributes = []

    def __init__(self):
        self.category = self.__category_instance

    def __repr__(self):
        return "identifier: " + self.category.scheme + '#' + self.category.term


class entity(object):
    """

    The Entity type is an abstract type of the Resource type and the Link type.

    """
    _entity_kind = kind()
    _entity_kind.term = 'entity'
    _entity_kind.scheme = 'http://schemas.ogf/occi/core'
    _entity_kind.title = 'Entity type'
    _entity_kind.attributes = ['id', 'title']
    _entity_kind.actions = []
    _entity_kind.related = []
    _entity_kind.entity_type = ''
    _entity_kind.entities = []

    def __init__(self):
        # A unique identifier (within the service provider's name-space) of the Entity sub-type instance.
        self.id = ''
        # The display name of the instance.
        self.title = ''
        # The Kind instance uniquely identifying the Entity sub-type of the resource instance.
        self.kind = self._entity_kind
        # The Mixin instances associated to this resource instance.
        # Consumers can expect the attributes and Actions of the associated Mixins to be exposed byt the instance.
        self.mixins = []
        
    def __repr__(self):
        return "identifier: " + self.id
    
class resource(entity):
    """

    The resource type inherits Entity and describes a concrete resource that can be inspired and manipulated.
    A resource is suitable to represent real world resources, e.g. virtual machines, networks, services , etc.
        through specialisation

    """
    __resource_kind = kind()
    __resource_kind.term = 'resource'
    __resource_kind.scheme = 'http://schemas.ogf/occi/core'
    __resource_kind.title = 'Resource'
    __resource_kind.attributes = ['summary']
    __resource_kind.actions = []
    # Why here I can't put just entity.kind!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    __resource_kind.related = [entity._entity_kind]
    __resource_kind.entity_type = ''
    __resource_kind.entities = []

    def __init__(self):
        super(resource, self).__init__()
        # A summarising description of the Resource instance
        self.summary = ''
        # a set of Link compositions.
        self.links = []
        self.kind = self.__resource_kind

class link(entity):
    """

    An instance of the Link type defines a base association between two Resource instances.
    A Link instance indicates that one Resource instance is connected to another.

    """
    __link_kind = kind()
    __link_kind.term = 'link'
    __link_kind.scheme = 'http://schemas.ogf/occi/core'
    __link_kind.title = 'Link'
    __link_kind.attributes = ['source', 'target']
    __link_kind.actions = []
    # Why here I can't put just entity.kind!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    __link_kind.related = [entity._entity_kind]
    __link_kind.entity_type = ''
    __link_kind.entities = []

    def __init__(self):
        super(link, self).__init__()
        # The Resource instances the Link instance originates from.
        self.source = ''
        # The Resource instances the Link instance points to.
        self.target = ''
        self.kind = self.__link_kind


if __name__ == '__main__':
    pass