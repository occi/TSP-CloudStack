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

from run_command import RunCommand
from extract_cmd import TransformXmlToCmd, Cmd
from extract_value import obj_extract,obj_cmp
from fixed_thresholds import fixed_thresholds
from decision import decision
import threading
import time
import logging

logging.basic(Configformat='%(asctime)s %(message)s',level=logging.DEBUG)
class threadCR(threading.Thread):
    '''
    this class defines a thread that will treat an indicator
    it will extract values, determines consumption thresholds
    and makes decision for its indicator
    '''

    def __init__(self,h,c):
        self.host=h
        self.cr=c
        pass

    def run(self):

        #extracting of command from xml file:
        cmdCl = TransformXmlToCmd()
        cmdCl.readXml('/home/khaled/cmdCrTest.xml')
        cmd = cmdCl.getcmd(self.cr.name)
        #cmd is a list containing objects that contain the indicator and her command

        # calling the obj_extract class to execute command and extract its result
        ex=obj_extract()
        result=ex.extract(self.host,cmd[0],self.cr.name)

        # definition of fixed threshold of each indicator
        fixedTh=fixed_thresholds(self.cr)
        mxAdd=fixedTh.return_maxAdding()
        mnRem=fixedTh.return_minRemoving()

        # decision for each indicator
        d=decision()
        crDecision=d.optimize(result,mxAdd,mnRem)
        return crDecision
