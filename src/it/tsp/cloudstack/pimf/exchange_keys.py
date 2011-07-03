
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
from extractVM import VM

class exchangeKeys:
    '''
    this class has the role to exchange keys between different vms
        '''
    def __init__(self):
        pass

    def exchange(self,vmList):
        m=1
        key_mstr=[]
        mstr=RunCommand()
        key_slv=''
        ip_slv=''
        ip_mstr=''
        for vm in vmList:
            to_exec=vm.host+','+vm.user+','+vm.password

            if m==1:
                ip_mstr=vm.host

                mstr.do_add_host(to_exec)
                mstr.do_connect()
                key=mstr.do_run("cd .ssh \nssh-keygen -q -t rsa -f id_rsa  -C '' -N ''")
                key_mstr=mstr.do_run('cat .ssh/id_rsa.pub')
                m=0
            else:
                slv=RunCommand()
                slv.do_add_host(to_exec)
                slv.do_connect()
                print 'connected to slaves'
                exec_key_slv=slv.do_run("cd .ssh \nssh-keygen -q -t rsa -f id_rsa  -C '' -N ''")
                key_slv+=slv.do_run('cat .ssh/id_rsa.pub')[0]+'\n'
                inject_slv=slv.do_run('echo '+key_mstr[0]+'>.ssh/authorized_keys')
                scan_slv=slv.do_run('ssh-keyscan '+ip_mstr+'>.ssh/known_hosts')
                ip_slv+=vm.host+'\n'

        inject_mstr=mstr.do_run("echo '"+key_slv+"'>.ssh/authorized_keys")
        prep_scan_mstr=mstr.do_run("echo '"+ip_slv+"'>hosts")
        scan_mstr=mstr.do_run("ssh-keyscan -f hosts>.ssh/known_hosts")
        return key_mstr[0]