

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
class exchangeNew:
    def __init__(self):
        pass

    def exchange(self,mstr,slv,key):
        slv_hst=slv+','+mstr.user+','+mstr.password
        mstr_hst=mstr.host+','+mstr.user+','+mstr.password
        key_slv=''
        slv=RunCommand()
        slv.do_add_host(slv_hst)
        slv.do_connect()
        print 'connected to slave'
        exec_key_slv=slv.do_run("cd .ssh \nssh-keygen -q -t rsa -f id_rsa  -C '' -N ''")
        key_slv+=slv.do_run('cat .ssh/id_rsa.pub')[0]+'\n'
        inject_slv=slv.do_run('echo '+key+'>.ssh/authorized_keys')
        scan_slv=slv.do_run('ssh-keyscan '+mstr.host+'>.ssh/known_hosts')

        inject_mstr=mstr_hst.do_run("echo '"+key_slv+"'>.ssh/authorized_keys")
        scan_mstr=mstr_hst.do_run('ssh-keyscan '+slv+'>.ssh/known_hosts')
        pass
