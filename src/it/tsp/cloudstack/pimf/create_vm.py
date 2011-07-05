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

from run_command import RunCommand
import commands

import logging

logging.basicConfig(Configformat='%(asctime)s %(message)s',level=logging.INFO)

class createVM:
    '''
    this class is dedicated to create a vm
    and return its id,ip address, username and password
    '''

    def __init__(self):
        pass

    def getID(self,rt):
        '''
        this method is dedicated to get th id of the created vm
        '''
        deb=rt.find('<ID>')+4
        end=rt.find('</ID>')
        self.id=rt[deb:end]

    def getIP(self,rt):
        '''
        this method is dedicated to get the ip address of the created vm
        '''
        deb=rt.find('<IP>')+4
        end=rt.find('</IP>')
        self.ip=rt[deb:end]
    
    def create(self):
        '''
        this method is dedicated to create a vm
        '''
        self.user='ubuntu'
        self.password='intrs2m'
        cmdCurl='curl -X POST -u onadmin:2169279e8caff5398eeeb55a9be126890243bdc4 http://157.159.249.20:4567/compute -T compute.xml'
        rt=commands.getstatusoutput(cmdCurl)
        logging.debug('creating vm launched through occi')
        self.getID(rt[1])
        self.getIP(rt[1])

        # adding the new created vm to the list of saved vms
        vm=self.id+','+self.ip+','+self.user+','+self.password+'\n'
        logging.debug('adding the new vm to the list of created vm')
        vms = open('vms.log', 'a')
        vms.write(vm)
        vms.close()
        