
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

from exchange_keys import exchangeKeys
from config_mstr import configMstr
from config_slv import configSlv
from run_command import RunCommand

class manageHdfs:
    def __init__(self):
        # list of created vms as parameter
        self.listVM=[]
        self.listSlv=[]
        self.mstr=self.listVM[0]
        self.user=self.listVM[0].user
        self.pwd=self.listVM[0].password
        self.mstr_key=None
        m=1
        for vm in self.listVM:
            if m<>1:
                self.listSlv.append(vm.host)
            m+=1



    def config(self):
        keys=exchangeKeys()
        self.mstr_key=keys.exchange(self.listVM)

        cfgMstr=configMstr()
        cfgMstr.config(self.listSlv,self.mstr.host,self.user,self.pwd)

        cfgSlv=configSlv()
        cfgSlv.config(self.listSlv,self.mstr.host,self.user,self.pwd)

        # starting hadoop daemons
        strt=RunCommand()
        strt.do_add_host(self.mstr.host+','+self.user+','+self.pwd)
        strt.do_connect()
        cmd=''
        exec_strt=strt.do_run(cmd)
        strt.do_close()

    def configNew(self):
        # exchange with new node
        # configSlv and masters file in mstr
        pass






