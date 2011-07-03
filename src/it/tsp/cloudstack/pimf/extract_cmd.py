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

import commands
import logging

logging.basicConfig(Configformat='%(asctime)s %(message)s',level=logging.INFO)

class Cmd:
    '''
    this class defines the characteristic of an indicator with its command
    in addition of command it have the parameters of optimization
    the xml file tied to this class is fixed and contains parameters for all indicators
    '''
    critere = None
    cmd = None
    tempsExt = None
    tempsCmpt = None
    zExt = None
    zCmpt = None

    def __init__(self):
        pass


class TransformXmlToCmd:
    '''
    this class is used to extract command and other parameters tied to each indicator
    '''
    __currentNode__ = None

    __cmdList__ = None


    def __init__(self):
        pass
        #self.readXml()


    def readXml(self, file):
        from xml.dom.minidom import parse

        self.doc = parse(file)


    def getRootElement(self):
        if self.__currentNode__ == None:
            self.__currentNode__ = self.doc.documentElement

        return self.__currentNode__


    def getcmd(self, crList):
        if self.__cmdList__ != None:
            return

        self.__cmdList__ = []

        for cmds in self.getRootElement().getElementsByTagName("cmdCr"):
            # browsing each one to extract characteristics
            if cmds.nodeType == cmds.ELEMENT_NODE:
                c = Cmd()

                try:
                    #extraction of value for each vm
                    c.critere = self.getText(cmds.getElementsByTagName("critere")[0])
                    c.cmd = self.getText(cmds.getElementsByTagName("cmd")[0])
                    c.tempsExt = self.getText(cmds.getElementsByTagName("tempsExt")[0])
                    c.tempsCmpt = self.getText(cmds.getElementsByTagName("tempsCmpt")[0])
                    c.zExt = self.getText(cmds.getElementsByTagName("zExt")[0])
                    c.zCmpt = self.getText(cmds.getElementsByTagName("zCmpt")[0])

                except:
                    logging.error('ERROR IN USED TAGS')

                #if the indicator is used for this case
                if c.critere in crList:
                    self.__cmdList__.append(c)

        return self.__cmdList__


    def getText(self, node):
        return node.childNodes[0].nodeValue

