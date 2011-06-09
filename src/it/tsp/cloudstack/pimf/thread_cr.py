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
from fixed_thresholds import fixed_thresholds
from extract_cr import TransformXmlToCr
from extract_value import obj_extract
from thread_exec import threadCR
import threading
import time

class threadVM(threading.Thread):

    def __init__(self,h):
        self.host=h
        pass

    def run(self):

        # extracting list of indicator to be treated for the used paas
        crObj=TransformXmlToCr()
        crList=crObj.getcr()

        # for each indicator, a thread will be executed and run to extract his parameters
        crTh=[]
        i=0
        for cr in crList:
            crTh.append(threadCR(self.host,cr))
            crTh[i].run()
            i=i+1

