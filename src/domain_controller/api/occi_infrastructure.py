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

from occi_core import category, kind, mixin, resource, link, action
from enum import Enum


class compute(resource):
    """

    The Compute type represents a generic information processing resource, e.g. a virtual machine.
    Compute inherits the Resource base type defined in OCCI Core Model

    """
    # Enumeration for CPU Architecture of the instance
    _cpu_architecture = Enum('x86', 'x64')
    # Enumeration for current state of the instance
    _compute_state = Enum('active', 'inactive', 'suspended')

    # Start action
    _action_start_category = category(term='start',
                                      scheme='http://schemas.ogf/occi/infrastructure/compute/action',
                                      title='Start a compute resource',
                                      attributes=())
    _action_start = action(_action_start_category)

    # Stop action
    _action_stop_category = category(term='stop',
                                     scheme='http://schemas.ogf/occi/infrastructure/compute/action',
                                     title='Stop a compute resource',
                                     attributes=('method'))
    _action_stop = action(_action_stop_category)

    # Restart action
    _action_restart_category = category(term='restart',
                                        scheme='http://schemas.ogf/occi/infrastructure/compute/action',
                                        title='Restart a compute resource',
                                        attributes=('method'))
    _action_restart = action(_action_restart_category)

    # Suspend action
    _action_suspend_category = category(term='suspend',
                                        scheme='http://schemas.ogf/occi/infrastructure/compute/action',
                                        title='Suspend a compute resource',
                                        attributes=('method'))
    _action_suspend = action(_action_suspend_category)

    # The kind instance assigned to the compute type
    _compute_kind = kind(term='compute',
                         scheme='http://schemas.ogf.org/occi/infrastructure',
                         entity_type=resource,
                         title='compute',
                         attributes=('occi.compute.architecture',
                                     'occi.compute.cores',
                                     'occi.compute.hostname',
                                     'occi.compute.speed',
                                     'occi.compute.memory',
                                     'occi.compute.state'),
                         actions=(_action_start,
                                  _action_stop,
                                  _action_restart,
                                  _action_suspend),
                         related=(resource._resource_kind),
                         entities=())


    def __init__(self, id, kind, state, title='', mixins=[], summary='', links=[], architecture='', cores=0, hostname=''
                 , speed=0.0, memory=0):
        super(compute, self).__init__(id=id, kind=kind or self._compute_kind, title=title, mixins=mixins,
                                      summary=summary, links=links)
        # CPU architecture of the instance
        self.architecture = architecture
        # Number of CPU cores assigned to the instance
        self.cores = cores
        # Fully Qualified DNS hostname for the instance
        self.hostname = hostname
        # CPU Clock frequency (speed) in gigahertz
        self.speed = speed
        # Maximum RAM in gigabytes allocated to the instance
        self.memory = memory
        # Current state of the instance
        self.state = state or self._compute_state.inactive


class network(resource):
    """

    The network type represents a L2 networking entity (e.g. virtual switch).
    It can be extended using the mixin mechanism (or sub-typed) to support L3/L4 capabilities such as TCP/IP etc.

    """

    # Enumeration for current state of the instance
    _network_state = Enum('active', 'inactive')

    # UP action
    _action_up_category = category(term='up',
                                   scheme='http://schemas.ogf/occi/infrastructure/network/action',
                                   title='turn UP a network',
                                   attributes=())
    _action_up = action(_action_up_category)

    # DOWN action
    _action_down_category = category(term='down',
                                     scheme='http://schemas.ogf/occi/infrastructure/network/action',
                                     title='turn DOWN a network',
                                     attributes=())
    _action_down = action(_action_down_category)


    # The kind instance assigned to the network type
    _network_kind = kind(term='network',
                         scheme='http://schemas.ogf.org/occi/infrastructure',
                         entity_type=resource,
                         title='network',
                         attributes=('occi.network.vlan',
                                     'occi.network.label',
                                     'occi.network.state'),
                         actions=(_action_up,
                                  _action_down),
                         related=(resource._resource_kind),
                         entities=())


    def __init__(self, id, kind, state, title='', mixins=[], summary='', links=[], vlan=0, label=''):
        super(network, self).__init__(id=id, kind=kind or self._network_kind, title=title, mixins=mixins,
                                      summary=summary, links=links)
        # 802.1q VLAN identifier (e.g. 343)
        self.vlan = vlan
        # Tag based VLANs (e.g. external-dmz)
        self.label = label
        # Current state of the instance
        self.state = state or self._network_state.inactive


class storage(resource):
    """

    The storage type represent resources that record information to a data storage device.

    """

    # Enumeration for current state of the instance
    _storage_state = Enum('online', 'offline', 'backup', 'snapshot', 'resize', 'degraded')

    # online action
    _action_online_category = category(term='online',
                                       scheme='http://schemas.ogf/occi/infrastructure/storage/action',
                                       title='turn Online a storage',
                                       attributes=())
    _action_online = action(_action_online_category)

    # offline action
    _action_offline_category = category(term='offline',
                                        scheme='http://schemas.ogf/occi/infrastructure/storage/action',
                                        title='turn Offline a storage',
                                        attributes=())
    _action_offline = action(_action_offline_category)


    # backup action
    _action_backup_category = category(term='backup',
                                       scheme='http://schemas.ogf/occi/infrastructure/storage/action',
                                       title='backup a storage',
                                       attributes=())
    _action_backup = action(_action_backup_category)

    # snapshot action
    _action_snapshot_category = category(term='snapshot',
                                         scheme='http://schemas.ogf/occi/infrastructure/storage/action',
                                         title='snapshot a storage',
                                         attributes=())
    _action_snapshot = action(_action_snapshot_category)

    # resize action
    _action_resize_category = category(term='resize',
                                       scheme='http://schemas.ogf/occi/infrastructure/storage/action',
                                       title='resize a storage',
                                       attributes=('size'))
    _action_resize = action(_action_resize_category)

    # The kind instance assigned to the storage type
    _storage_kind = kind(term='storage',
                         scheme='http://schemas.ogf.org/occi/infrastructure',
                         entity_type=resource,
                         title='storage',
                         attributes=('occi.storage.size',
                                     'occi.storage.state'),
                         actions=(_action_online,
                                  _action_offline,
                                  _action_backup,
                                  _action_snapshot,
                                  _action_resize),
                         related=(resource._resource_kind),
                         entities=())

    def __init__(self, id, kind, size, state, title='', mixins=[], summary='', links=[]):
        super(storage, self).__init__(id=id, kind=kind or self._storage_kind, title=title, mixins=mixins,
                                      summary=summary, links=links)

        # Storage size in gigabytes of the instance
        self.size = size or 0
        # Current state of the instance
        self.state = state or self._storage_state.offline


class network_interface(link):
    """

    The network_interface type represents an L2 client device (e.g. network adapter).
    It can be extended using the mix-in mechanism or sub-typed to support L3/L4 capabilities such as TCP/IP etc.
    network_interface inherits the link base type defined in the OCCI Core Model.

    """

    # Enumeration for current state of the instance
    _network_interface_state = Enum('active', 'inactive')


    # The kind instance assigned to the network_interface type
    _network_interface_kind = kind(term='networkinterface',
                                   scheme='http://schemas.ogf.org/occi/infrastructure',
                                   entity_type=link,
                                   title='network interface',
                                   attributes=('occi.networkinterface.interface',
                                               'occi.networkinterface.mac',
                                               'occi.networkinterface.state'),
                                   actions=(),
                                   related=(link._link_kind),
                                   entities=())


    def __init__(self, id, kind, source, target, interface, mac, state, title='', mixins=[]):
        super(network_interface, self).__init__(id=id, kind=kind or self._network_interface_kind, source=source,
                                                target=target, title=title, mixins=mixins)

        # identifier that relates the link to the link's device interface
        self.interface = interface
        # MAC address associated with the link's device interface
        self.mac = mac
        # Current state of the instance
        self.state = state or self._network_interface_state.inactive

    pass


class storage_link(link):
    """

    The storage_link type represents a link from a resource to a target storage instance.
    This enables a storage instance be attached to a compute instance, with all the prerequisite low-level
        operations handled by the OCCI implementation.
    storage inherits the link base type defined in the OCCI Core Model.

    """

    # Enumeration for current state of the instance
    _storage_link_state = Enum('active', 'inactive')

    # The kind instance assigned to the storage_link type
    _storage_link_kind = kind(term='storagelink',
                              scheme='http://schemas.ogf.org/occi/infrastructure',
                              entity_type=link,
                              title='storage link',
                              attributes=('occi.storagelink.deviceid',
                                          'occi.storagelink.mountpoint',
                                          'occi.storagelink.state'),
                              actions=(),
                              related=(link._link_kind),
                              entities=())

    def __init__(self, id, kind, source, target, deviceid, state, mountpoint='', title='', mixins=[]):
        super(storage_link, self).__init__(id=id, kind=kind or self._storage_link_kind, source=source,
                                           target=target, title=title, mixins=mixins)

        # Device identifier as defined by the OCCI service provider
        self.deviceid = deviceid
        # point to where the storage is mounted in the guest OS
        self.mountpoint = mountpoint
        # Current state of the instance
        self.state = state or self._storage_link_state.inactive


class ip_networking(mixin):
    """

    Mixin
    In order to support L3/L4 capabilities (e.g. IP, TCP etc.) an OCCI mixin is herewith defined.

    """

    # Enumeration for the address allocation mechanism
    _ip_networking_state = Enum('dynamic', 'static')

    def __init__(self, address='', gateway='', allocation=_ip_networking_state.static):
        super(ip_networking, self).__init__(term='ipnetwork',
                                            scheme='http://schemas.ogf.org/occi/infrastructure/network',
                                            title='ip network mixin',
                                            attributes=('occi.network.address',
                                                        'occi.network.gateway',
                                                        'occi.network.allocation'),
                                            actions=(),
                                            related=(),
                                            entities=[])

        # Internet protocol (IP) network address (e.g. 192.168.0.1/24, fc@@::/7)
        self.address = address
        # Internet Protocol (IP) network address (e.g. 192.168.0.1, fc00::)
        self.gateway = gateway
        # Address allocation mechanism: dynamic e.g. uses the dynamic host configuration protocol,
        #    static e.g. uses user supplied static network configurations
        self.allocation = allocation


class ip_network_interface(mixin):
    """

    Mixin
    In order to support L3/L4 capabilities (e.g. IP, TCP etc.) with the network_interface type,
        an OCCI mixin instance is herewith defined.

    """

    # Enumeration for the address allocation mechanism
    _ip_network_interface_state = Enum('dynamic', 'static')

    def __init__(self, address, allocation, gateway=''):
        super(ip_network_interface, self).__init__(term='ipnetworkinterface',
                                                   scheme='http://schemas.ogf.org/occi/infrastructure/networkinterface',
                                                   title='ip network interface mixin',
                                                   attributes=('occi.networkinterface.address',
                                                               'occi.networkinterface.gateway',
                                                               'occi.networkinterface.allocation'),
                                                   actions=(),
                                                   related=(),
                                                   entities=[])
        # Internet Protocol (IP network address (e.g. 192.168.0.1/24, fc00::/7) of the link
        self.address = address
        # Internet Protocol (IP network address (e.g. 192.168.0.1/24, fc00::/7)
        self.gateway = gateway
        # Address allocation mechanism: dynamic e.g. uses the dynamic host configuration protocol,
        #    static e.g. uses user supplied static network configurations
        self.allocation = allocation


class os_tpl(mixin):
    """

    Mixin
    OCCI OS Template Mixin
    OS (Operating System) Templates allow clients specific what operating system must be installed
        on a requested Compute resource.
    A implementation-defined OS Template Mixin MUST be related to the OCCI OS Template Mixin
        in order to give absolute type information.


    """

    def __init__(self):
        super(os_tpl, self).__init__(term='os_tpl',
                                     scheme='http://schemas.ogf.org/occi/infrastructure',
                                     title='OCCI OS template',
                                     attributes=(),
                                     actions=(),
                                     related=(),
                                     entities=[])
        pass


class resource_tpl(mixin):
    """

    Mixin
    OCCI Resource template Mixin
    A resource Template is a provider defined Mixin instance that refers to a preset Resource configuration.
    The Mixin.attributes (inherits from Category) is empty for a Template Mixin.
    An implementation-defined Resource Template Mixin MUST be related to the OCCI Resource Template Mixin
        in order to give absolute type information.

    """

    def __init__(self):
        super(resource_tpl, self).__init__(term='resource_tpl',
                                           scheme='http://schemas.ogf.org/occi/infrastructure',
                                           title='OCCI resource template',
                                           attributes=(),
                                           actions=(),
                                           related=(),
                                           entities=[])
        pass

if __name__ == '__main__':
    pass
