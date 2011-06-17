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
Created on Mai 20, 2011

@author: Khaled Ben Bahri
@contact: khaled.ben_bahri@it-sudparis.eu
@organization: Institut Telecom - Telecom SudParis
@version: 0.1
@license: LGPL - Lesser General Public License
'''

from run_command import RunCommand
from extract_cmd import TransformXmlToCmd, Cmd
from extractVM import TransformXmlToVM, VM

class execution:
    def __init__(self):
        pass

    def prepare_exec(self):
        #extracting list of vms that will be used to extract values
        vmObj = TransformXmlToVM()
        vmObj.readXml('/home/khaled/listeVMsTest.xml')
        vms = vmObj.getVM()
        self.host = "%s,%s,%s" % (vms[0].host, vms[0].user, vms[0].password)
        print 'VM:'
        print self.host


        #extracting of command from xml file:
        cmdCl = TransformXmlToCmd()
        cmdCl.readXml('/home/khaled/cmdCrTest.xml')

        #preapring list of indicator used
        listCr = []
        listCr.append('disk')
        self.cmd = cmdCl.getcmd(listCr)
        #cmd is a list containing objects that contain the indicator and her command
        #print 'commande extraite'
        print self.cmd[0].cmd
        #preparing connexion to run commands
        self.cnx = RunCommand()

        #adding hosts extracted early  
        self.cnx.do_add_host(self.host)
        self.cnx.do_connect()

    #executing command after its extracting and establishing connexion
    def execute(self,cmde):
        #Excuting command on remote host
        # the command is gotten from the previous method saved in the self vble
        r = self.cnx.do_run(self.cmd[0].cmd)
        print'affichage'
        print r[0]
        print'fin'
