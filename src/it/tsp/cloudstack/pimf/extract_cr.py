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

import logging

logging.basic(Configformat='%(asctime)s %(message)s',level=logging.DEBUG)

class Indicator:
    '''
    this class wil specify the fixed characteristics for used indicators in architecture
    these parameters are specifics of installed architecture
    '''
    name=None
    maxApp = None
    maxPhy = None
    minApp = None

    def __init__(self):
        pass

class TransformXmlToCr:
    __currentNode__ = None

    __crList__ = None


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


    def getcr(self):
        if self.__crList__ != None:
            return

        self.__crList__ = []

        for crs in self.getRootElement().getElementsByTagName("cr"):
            if crs.nodeType == crs.ELEMENT_NODE:
                obj=Indicator()
                try:
                    #extraction of value for each indicator
                    obj.name = self.getText(crs.getElementsByTagName("name")[0])
                    obj.maxPhy = self.getText(crs.getElementsByTagName("maxPhysicalThreshold")[0])
                    obj.maxApp = self.getText(crs.getElementsByTagName("maxApplicationThreshold")[0])
                    obj.minApp = self.getText(crs.getElementsByTagName("minApplicationThreshold")[0])

                except:
                    logging.error('ERROR IN USED TAGS')

                self.__crList__.append(obj)

        return self.__crList__

    def getText(self, node):
        return node.childNodes[0].nodeValue

