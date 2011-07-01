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
from extract_cmd import TransformXmlToCmd, Cmd
from fixed_thresholds import fixed_thresholds
from extract_cr import TransformXmlToCr
from extract_value import obj_extract
from thread_exec import threadCR
from action import action
import threading
import time
import logging
import Queue

logging.basicConfig(Configformat='%(asctime)s %(message)s',level=logging.INFO)
class threadVM(threading.Thread):
    '''
    this class defines a thread that will be executed in each vm
    it will extract indicators and run an other thread for each indicator
    to calculate consumption thresholds and make decision for its indicator
     this thread will make decision for the entire vm
    '''

    def __init__(self,h,vms):
        threading.Thread.__init__(self)
        self.host=h
        self.listVMs=vms
        pass

    def run(self):

        # extracting list of indicator to be treated for the used paas
        crObj=TransformXmlToCr()
        crObj.readXml('listCRs.xml')
        crList=crObj.getcr()

        # for each indicator, a thread will be executed and run in order to extract his result
        crTh=[]
        i=0
        for cr in crList:
            crTh.append(threadCR(self.host,cr))
            crTh[i].start()
            i=i+1

        # waiting for all threads to be completed
        for th in crTh:
            th.join()

        f=open('content.log','r')
        fileContent=f.readlines()
        print fileContent
        f.close()
        f=open('content.log','w')
        f.write('')
        f.close()

        #browsing all decisions and choosing action to execute
        compactList=[]
        extendList=[]
        testAdd=False
        testRem=False
        testExt=False
        testCmpt=False
        for ind in fileContent:
            d=ind.split(',')
            if 'add' in d[1]:
                # adding vm
                testAdd=True
                break
            elif 'rem' in d[1]:
                # removing vm
                testRem=True
                break
            elif 'ext' in d[1]:
                # indicator will be extended
                testExt=True
                extendList.append(d[0])
            elif 'cmpt' in d[1]:
                testCmpt=True
                # indicator will be compacted.append(d[0])
                compactList.append(d[0])

        # choosing action to optimize
        # choosing vm to edit if removing or modifying
        number=len(self.listVMs)
        #choosing the last vm to edit
        choice=action(self.listVMs[number-1])
        if testAdd:
            # addingVM
            choice.add_vm()
        elif testRem:
            # removing VM
            choice.remove_vm()
        elif testExt:
            # extending VM
            choice.extend_vm(extendList)
        elif testCmpt:
            # compacting vm
            choice.compact_vm(compactList)


            





