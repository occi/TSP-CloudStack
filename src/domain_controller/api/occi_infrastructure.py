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

from occi_core import category, kind, resource, link, action
from enum import Enum


class compute(resource):
    """

    The Compute type represents a generic information processing resource, e.g. a virtual machine.
    Compute inherits the Resource base type defined in OCCI Core Model

    """
    # Enumeration for CPU Architecture of the instance
    __cpu_architecture = Enum('x86', 'x64')
    # Enumeration for current state of the instance
    __vm_state = Enum('active', 'inactive', 'suspended')

    # The list of actions (start, stop, restart and suspend)
    action_start = action()
    __action_start_category = category()

    def __init__(self):
        super(compute, self).__init__()
        # CPU architecture of the instance
        self.architecture = self.__cpu_architecture.x86
        # Number of CPU cores assigned to the instance
        self.cores = 0
        # Fully Qualified DNS hostname for the instance
        self.hostname = ''
        # CPU Clock frequency (speed) in gigahertz
        self.speed = 1,2
        # Maximum RAM in gigabytes allocated to the instance
        self.memory = 128
        # Current state of the instance
        self.state = self.__vm_state.inactive

if __name__ == '__main__':
    c = compute()
    print c.action_start
    pass
