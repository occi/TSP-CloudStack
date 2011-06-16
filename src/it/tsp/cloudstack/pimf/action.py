# -*- Mode: python; py-indent-offset: 4; indent-tabs-mode: nil; coding: utf-8; -*-

# Copyright (C) 2011 Khaled Ben Bahri - Institut Telecom
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

@author: Khaled Ben Bahri
@contact: khaled.ben_bahri@it-sudparis.eu
@organization: Institut Telecom - Telecom SudParis
@version: 0.1
@license: LGPL - Lesser General Public License
'''
import logging

logging.basic(Configformat='%(asctime)s %(message)s',level=logging.DEBUG)

class action:
    '''
    in this class, we will choose method of optimising
    optimising method will add new vm or extend an existing one to add allocate more resources
    or by removing or compacting an existing vm to deallocate resources
    '''

    def __init__(self):
        pass

    # this method is dedicated to add a new VM to the actual architecture
    def add_vm(self):
        logging.info('adding new vm')
        pass

    # this method is dedicated to remove a VM which is not in use
    def remove_vm(self):
        logging.info('removing vm')
        pass

    # this method is dedicated to extend resources of a VM
    def extend_vm(self):
        logging.info('extending vm')
        pass

    # this method is dedicated to compact resources of a VM
    def compact_vm(self):
        logging.info('compacting vm')
        pass

  