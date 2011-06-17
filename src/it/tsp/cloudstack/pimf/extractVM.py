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

class VM:
    '''
    this class will define the structure of vm (host,username,passwd,type of priority)
    the priority define if the vm will be used to extract value or not in hte used architecture
    '''
    host = None
    user = None
    password = None
    extract = None

    def __init__(self):
        pass


class TransformXmlToVM:
    '''
    list of vm with its characteristics are saved in an xml file
    this class will extract characteristics of vms that will be used to treat values to optimise architecture
    '''
    __currentNode__ = None

    __vmList__ = None


    def __init__(self):
        pass
        #self.readXml()


    def readXml(self, file):
        '''
        this method is use to read the xml file
        '''
        from xml.dom.minidom import parse

        self.doc = parse(file)


    def getRootElement(self):
        if self.__currentNode__ == None:
            self.__currentNode__ = self.doc.documentElement

        return self.__currentNode__


    def getVM(self):
        '''
        this method is used to extract list of vm that will be used to extract measurements
        '''
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
                    logging.error('ERROR IN USED TAGS')

                #if the vm is used to extract value for optimisation process
                if v.extract == 'yes':
                    self.__vmList__.append(v)

        return self.__vmList__


    def getText(self, node):
        # return the text of a tag in the xml file
        return node.childNodes[0].nodeValue

