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
import time
import math
from run_command import RunCommand
from treat_commandResult import treat_result
from extract_cmd import Cmd
import logging

logging.basic(Configformat='%(asctime)s %(message)s',level=logging.DEBUG)

class obj_cmp:
    '''
    this class define the structure of the returned object by the class below
    this object contain the value to compare and and the consumption thresholds for an indicator
    '''
    cr=None
    value=None
    maxExt=None
    minCmpt=None

    def __init__(self):
        pass

class obj_extract:
    '''
    this class is used to execute command to extract value
    and calculates thresholds
    '''
    def __init__(self):
        pass

    # treating indicator to extract list of value to determine threshold
    # cmde is an abject of type Cmd passed as an argument
    def extract(self,host,cmde,cr):

        sumExt = 0
        sumExtSqr = 0
        sumCmpt = 0
        sumCmptSqr = 0

        nbMeasures = 3

        # preparing connection to host
        exe=RunCommand()
        exe.do_add_host(host)
        logging.debug('host added')
        exe.do_connect()
        logging.debug('connection established')

        result=treat_result(cr)

        # executing commands for many times : nbMeasures
        for i in range(nbMeasures):
            #waiting and extracting value
            time.sleep(1)

            #execution of command

            res=exe.do_run(cmde.cmd)
            logging.debug('command executed')

            # treatment of the extracted value
            valeur=result.return_result(res)
            logging.debug('result of command treated')

            #determning of the sum of values dedicated for extension
            sumExt = sumExt + valeur.value
            sumExtSqr = sumExtSqr + math.pow(valeur.value, 2)
            # determining the sum of values dedicated for compacting
            sumCmpt = sumCmpt + valeur.complement
            sumCmptSqr = sumCmptSqr + math.pow(valeur.complement, 2)

        #determining the average and other parameters
        moyExt = sumExt / nbMeasures
        ecartTypeExt = sumExtSqr / nbMeasures - math.pow(moyExt, 2)
        moyCmpt = sumCmpt / nbMeasures
        ecartTypeCmpt = sumCmptSqr / nbMeasures - math.pow(moyCmpt, 2)

        # determining thresholds
        thresholdExt = float(cmde.tempsExt) * float(cmde.zExt) * ecartTypeExt
        thresholdCmpt = float(cmde.tempsCmpt) * float(cmde.zCmpt) * ecartTypeCmpt
        logging.info('consumption threshold determined')

        # extracting values to compare with thresholds
        res=exe.do_run(cmde.cmd)
        valeur=result.return_result(res)

        # creating the object that will be returned
        # this object contains value to compare and thresholds
        to_return=obj_cmp()
        to_return.cr=cr.lower()
        to_return.value=valeur
        to_return.maxExt=thresholdExt
        to_return.minCmpt=thresholdCmpt

        print 'seuilExt ',thresholdExt
        print 'seuilCmpt ',thresholdCmpt
        #closing connection to host
        exe.do_close()
        logging.debug('connection to host closed')

        # returning obj to be compared
        return to_return