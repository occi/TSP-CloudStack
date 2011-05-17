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

==================================
OCCI Core version 1.1
==================================
'''

class category(object):
    """

    The Category type is the basis of the type identification mechanism used by the OCCI classification system.

    """

    def __init__(self, term, scheme, title='', attributes=()):
        # Unique identifier of the category instance within the categorisation scheme
        # @AttributeType string
        # @AttributeMultiplicity 1
        # @AttributeMutability immutable
        self.term = term
        # The categorisation scheme
        # @AttributeType URI
        # @AttributeMultiplicity 1
        # @AttributeMutability immutable
        self.scheme = scheme
        # The display name of an instance
        # @AttributeType string
        # @AttributeMultiplicity 0..1
        # @AttributeMutability immutable
        self.title = title
        # The set of resource attribute names defined by the category instance
        # @AttributeType string
        # @AttributeMultiplicity 0..*
        # @AttributeMutability immutable
        self.attributes = attributes

    def __repr__(self):
        return  self.scheme + "#" + self.term


class kind(category):
    """

    The kind type, together with the Mixin type, defines the classification system of the OCCI Core Model.
    The Kind type represents the type identification mechanism for all Entity types present in the model.

    """

    def __init__(self, term, scheme, entity_type, title='', attributes=(), actions=(), related=(), entities=()):
        super(kind, self).__init__(term=term, scheme=scheme, title=title, attributes=attributes)
        # set of actions defined by the Kind instance
        # @AttributeType Action
        # @AttributeMultiplicity 0..*
        # @AttributeMutability immutable
        self.actions = actions
        # set of related Kind instances
        # @AttributeType Kind
        # @AttributeMultiplicity 0..*
        # @AttributeMutability immutable
        self.related = related
        # Entity type uniquely identified by the Kind instance
        # @AttributeType Entity
        # @AttributeMultiplicity 1
        # @AttributeMutability immutable
        self.entity_type = entity_type
        # set of resource instances, i.e. Entity sub-type instances.
        # Resources instantiated from the Entity sub-type which is uniquely identified by this Kind instance.
        # @AttributeType Entity
        # @AttributeMultiplicity 0..*
        # @AttributeMutability immutable
        self.entities = entities


class mixin(category):
    """

    The Mixin type complements the Kind type in defining the OCCI Core Model type classification system.
    The Mixin type represent an extension mechanism, which allows new resource capabilities to be added
        to resource instances both at creation-time and/or run-time.
    A Mixin instance can be associated with any existing resource instance and thereby add new resource
        capabilities, i.e. attributes and Actions, to the resource instance. However, a Mixin can never
        be applied to a type.

    """
    
    def __init__(self, term, scheme, title='', attributes=(), actions=(), related=(), entities=[]):
        super(mixin, self).__init__(term=term, scheme=scheme, title=title, attributes=attributes)
        # set of actions defined by the Mixin instance
        # @AttributeType Action
        # @AttributeMultiplicity 0..*
        # @AttributeMutability immutable
        self.actions = actions
        # set of related Mixin instances
        # @AttributeType Mixin
        # @AttributeMultiplicity 0..*
        # @AttributeMutability immutable
        self.related = related
        # set of resource instances, i.e. Entity sub-type instances, associated with the Mixin instance.
        # @AttributeType Entity
        # @AttributeMultiplicity 0..*
        # @AttributeMutability mutable
        self.entities = entities



class action(object):
    """

    The Action type is an abstract type. Each sub-type of Action defines an invocable
        operation applicable to an Entity sub-type instance or a collection thereof.

    """

    # The category instance assigned to the action type
    __category_instance = category(term='action',
                                   scheme='http://schemas.ogf.org/occi/core',
                                   title='Action',
                                   attributes=())

    def __init__(self, category):
        # The identifying Category of the Action
        # @AttributeType Category
        # @AttributeMultiplicity 1
        # @AttributeMutability immutable
        self.category = category or self.__category_instance


    # __repr__ is also the unique id of Category
    def __repr__(self):
        return  self.category.scheme + '#' + self.category.term


class entity(object):
    """

    The Entity type is an abstract type of the Resource type and the Link type.

    """

    # The kind instance assigned to the entity type
    _entity_kind = kind(term='entity',
                        scheme='http://schemas.ogf.org/occi/core',
                        entity_type='', # entity
                        title='Entity type',
                        attributes=('occi.core.id',
                                    'occi.core.title'),
                        actions=(),
                        related=(),
                        entities=())

    def __init__(self, id, kind, title='', mixins=[]):
        # A unique identifier (within the service provider's name-space) of the Entity sub-type instance.
        # occi.core.id
        # @AttributeType URI
        # @AttributeMultiplicity 1
        # @AttributeMutability immutable
        self.id = id
        # The display name of the instance.
        # occi.core.title
        # @AttributeType string
        # @AttributeMultiplicity 0..1
        # @AttributeMutability mutable
        self.title = title
        # The Kind instance uniquely identifying the Entity sub-type of the resource instance.
        # @AttributeType Kind
        # @AttributeMultiplicity 1
        # @AttributeMutability immutable
        self.kind = kind or self._entity_kind
        # The Mixin instances associated to this resource instance.
        # Consumers can expect the attributes and Actions of the associated Mixins to be exposed byt the instance.
        # @AttributeType Kind
        # @AttributeMultiplicity 0..*
        # @AttributeMutability mutable
        self.mixins = mixins

    # __repr__ is also the unique id of Entity
    def __repr__(self):
        return self.id


class resource(entity):
    """

    The resource type inherits Entity and describes a concrete resource that can be inspired and manipulated.
    A resource is suitable to represent real world resources, e.g. virtual machines, networks, services , etc.
        through specialisation

    """

    # The kind instance assigned to the resource type
    _resource_kind = kind(term='resource',
                          scheme='http://schemas.ogf.org/occi/core',
                          entity_type='', #resource
                          title='Resource',
                          attributes=('occi.core.summary'),
                          actions=(),
                          related=(entity._entity_kind),
                          entities=())

    def __init__(self, id, kind, title='', mixins=[], summary='', links=[]):
        super(resource, self).__init__(id=id, kind=kind or self._resource_kind, title=title, mixins=mixins)
        # A summarising description of the Resource instance
        # occi.core.summary
        # @AttributeType string
        # @AttributeMultiplicity 0..1
        # @AttributeMutability mutable
        self.summary = summary
        # a set of Link compositions.
        # @AttributeType Link
        # @AttributeMultiplicity 0..*
        # @AttributeMutability mutable
        self.links = links


class link(entity):
    """

    An instance of the Link type defines a base association between two Resource instances.
    A Link instance indicates that one Resource instance is connected to another.

    """

    # The kind instance assigned to the link type
    _link_kind = kind(term='link',
                      scheme='http://schemas.ogf.org/occi/core',
                      entity_type='', # link
                      title='Link',
                      attributes=('occi.core.source',
                                  'occi.core.target'),
                      actions=(),
                      related=(entity._entity_kind),
                      entities=())

    def __init__(self, id, kind, source, target, title='', mixins=[]):
        super(link, self).__init__(id=id, kind=kind or self._link_kind, title=title, mixins=mixins)
        # The Resource instances the Link instance originates from.
        # occi.core.source
        # @AttributeType Resource
        # @AttributeMultiplicity 1
        # @AttributeMutability mutable
        self.source = source
        # The Resource instances the Link instance points to.
        # occi.core.target
        # @AttributeType Resource
        # @AttributeMultiplicity 1
        # @AttributeMutability mutable
        self.target = target

if __name__ == '__main__':
#    e = entity('&', None)
#    print e.kind.scheme
    pass