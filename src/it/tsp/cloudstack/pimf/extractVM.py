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

import commands

class VM:
    host = None
    user = None
    password = None
    extract = None

    def __init__(self):
        pass


class TransformXmlToVM:
    __currentNode__ = None

    __vmList__ = None


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


    def getVM(self):
        if self.__vmList__ != None:
            return

        self.__vmList__ = []

        for vms in self.getRootElement().getElementsByTagName("vm"):
            if vms.nodeType == vms.ELEMENT_NODE:
                v = VM()

                try:
                    #extraction of value for each vm
                    v.host = self.getText(vms.getElementsByTagName("host")[0])
                    v.user = self.getText(vms.getElementsByTagName("user")[0])
                    v.password = self.getText(vms.getElementsByTagName("password")[0])
                    v.extract = self.getText(vms.getElementsByTagName("extract")[0])

                except:
                    print 'Un des TAGS suivant est manquants : host, user, password, extractType'

                #if the vm is used to extract value for optimisation process
                if v.extract == 'yes':
                    self.__vmList__.append(v)

        return self.__vmList__


    def getText(self, node):
        return node.childNodes[0].nodeValue

