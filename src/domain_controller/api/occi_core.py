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
        return self.scheme + "#" + self.term

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


class entity(object):
    """

    The Entity type is an abstract type of the Resource type and the Link type.

    """
    kind_instance = kind()
    kind_instance.term = 'entity'
    kind_instance.scheme = 'http://schemas.ogf/occi/core'
    kind_instance.title = 'Entity type'
    kind_instance.attributes = ['id', 'title']
    kind_instance.actions = []
    kind_instance.related = []
    kind_instance.entity_type = ''
    kind_instance.entities = []

    def __init__(self):
        # A unique identifier (within the service provider's name-space) of the Entity sub-type instance.
        self.id = ''
        # The display name of the instance.
        self.title = ''
        # The Kind instance uniquely identifying the Entity sub-type of the resource instance.
        self.kind = self.kind_instance
        # The Mixin instances associated to this resource instance.
        # Consumers can expect the attributes and Actions of the associated Mixins to be exposed byt the instance.
        self.mixins = []
        

class resource(entity):
    """

    The resource type inherits Entity and describes a concrete resource that can be inspired and manipulated.
    A resource is suitable to represent real world resources, e.g. virtual machines, networks, services , etc.
        through specialisation

    """
    kind_instance = kind()
    kind_instance.term = 'resource'
    kind_instance.scheme = 'http://schemas.ogf/occi/core'
    kind_instance.title = 'Resource'
    kind_instance.attributes = ['summary']
    kind_instance.actions = []
    kind_instance.related = [entity.kind_instance]
    kind_instance.entity_type = ''
    kind_instance.entities = []

    def __init__(self):
        super(resource, self).__init__()
        # A summarising description of the Resource instance
        self.summary = ''
        # a set of Link compositions.
        self.links = []
        self.kind = self.kind_instance

class link(entity):
    """

    An instance of the Link type defines a base association between two Resource instances.
    A Link instance indicates that one Resource instance is connected to another.

    """
    kind_instance = kind()
    kind_instance.term = 'link'
    kind_instance.scheme = 'http://schemas.ogf/occi/core'
    kind_instance.title = 'Link'
    kind_instance.attributes = ['source', 'target']
    kind_instance.actions = []
    kind_instance.related = [entity.kind_instance]
    kind_instance.entity_type = ''
    kind_instance.entities = []

    def __init__(self):
        super(link, self).__init__()
        # The Resource instances the Link instance originates from.
        self.source = ''
        # The Resource instances the Link instance points to.
        self.target = ''
        self.kind = self.kind_instance

class action(object):
    """

    The Action type is an abstract type. Each sub-type of Action defines an invocable
        operation applicable to an Entity sub-type instance or a collection thereof.

    """
    category_instance = category()
    category_instance.term = 'action'
    category_instance.scheme = 'http://schemas.ogf/occi/core'
    category_instance.title = 'Action'
    category_instance.attributes = []

    def __init__(self):
        self.category = self.category_instance
        
if __name__ == '__main__':
    pass