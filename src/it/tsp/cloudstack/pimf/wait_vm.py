# -*- Mode: python; py-indent-offset: 4; indent-tabs-mode: nil; coding: utf-8; -*-

# Copyright (C) 2011 Khaled Ben Bahri - Institut Telecom
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

@author: Khaled Ben Bahri
@contact: khaled.ben_bahri@it-sudparis.eu
@organization: Institut Telecom - Telecom SudParis
@version: 0.1
@license: LGPL - Lesser General Public License
'''


import time
import commands

import logging

logging.basicConfig(Configformat='%(asctime)s %(message)s',level=logging.INFO)

class waitVM:
    '''
    this class is dedicated to wait the time token to all vms to will be run
    '''
    def __init__(self,list):
        # this method will take the list of ip address of created vm
        self.vmList=list

    def wait(self):

        for vm in self.vmList:
            run=False
            while (run==False):
                time.sleep(10)
            cmdPing='ping '+vm+' -c 1'
            rt=commands.getstatusoutput(cmdPing)
            if (rt[1].find('ttl')!=-1):
                run=True
            logging.debug('vm running')
        logging.debug('all vms are running')


