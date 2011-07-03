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

class configMstr:
    def __init__(self):
        pass

    def config(self,ipList,masterIp,user,pwd):
        cs=open('core.log', 'r')
        csList=cs.readlines()
        csList[6]=csList[6].replace('IP_ADRESS',masterIp)
        csCh=''.join(csList)
        print csCh
        m=1
        ip_slv='\n'.join(ipList)
        hdp_home='/usr/local/hadoop-0.20.2'
        hst=masterIp+','+user+','+pwd
        slv=RunCommand()
        slv.do_add_host(hst)
        slv.do_connect()
        rt=slv.do_run("echo '"+csCh+"'>"+hdp_home+"/conf/core-site.xml")
        rt=slv.do_run("echo '"+ip_slv+"'>"+hdp_home+"/conf/slaves")
