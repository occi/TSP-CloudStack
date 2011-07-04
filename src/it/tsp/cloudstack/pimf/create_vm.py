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
class createVM:
    '''
    this class is dedicated to create a vm
    and return its id,ip address, username and password
    '''
    id=None
    ip=None
    def __init__(self):
        pass

    def getID(self,rt):
        deb=rt.find('<ID>')+4
        end=rt.find('</ID>')
        self.id=rt[deb:end]

    def getIP(self,rt):
        deb=rt.find('<IP>')+4
        end=rt.find('</IP>')
        self.ip=rt[deb:end]
    
    def create(self):
        '''
        this method is dedicated to create a vm
        '''
        cmdCurl='curl -X POST -u onadmin:2169279e8caff5398eeeb55a9be126890243bdc4 http://157.159.249.20:4567/compute -T compute.xml'
        rt=commands.getstatusoutput(cmdCurl)
        self.getID(rt[1])
        self.getIP(rt[1])
        