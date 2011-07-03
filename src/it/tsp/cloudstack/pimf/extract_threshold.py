
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

import logging

logging.basicConfig(Configformat='%(asctime)s %(message)s',level=logging.INFO)

class Threshold:
    maxApp = None
    maxPhy = None
    minApp = None

    def __init__(self):
        pass


class TransformXmlToThreshold:
    __currentNode__ = None

    # we have 3 predefined threshold
    __thresholdList__ = None


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


    def getThreshold(self):
        if self.__thresholdList__ != None:
            return

        self.__thresholdList__ = []

        for thresholds in self.getRootElement().getElementsByTagName("thresholdCr"):
            if thresholds.nodeType == thresholds.ELEMENT_NODE:
                c = Threshold()

                try:
                    #extraction of value for each indicator
                    c.maxApp = self.getText(thresholds.getElementsByTagName("maxPhysicalThreshold")[0])
                    c.maxPhy = self.getText(thresholds.getElementsByTagName("maxApplicationThreshold")[0])
                    c.minApp = self.getText(thresholds.getElementsByTagName("minApplicationThreshold")[0])

                except:
                    logging.error('ERROR IN USED TAGS')

                self.__thresholdList__.append(c)

        return self.__thresholdList__

    def getText(self, node):
        return node.childNodes[0].nodeValue

