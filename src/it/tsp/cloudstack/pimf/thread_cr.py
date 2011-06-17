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

    def __init__(self,h):
        threading.Thread.__init__(self)
        self.host=h
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

        print 'fin exectous les threads'
        f=open('content.log','r')
        fileContent=f.readlines()
        print fileContent
        f.close()
        f=open('content.log','w')
        f.write('')
        f.close()

t=threadVM('157.159.103.116,vadmin,sector7g')
t.start()


