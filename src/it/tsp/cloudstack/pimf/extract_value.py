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

class obj_cmp:
    value=None
    maxExt=None
    minCmpt=None

    def __init__(self):
        pass

class obj_extract:
    def __init__(self):
        pass

    # treating indicator to extract list of value to determine threshold
    # cmde is an abject of type Cmd passed as an argument
    def extract(self,host,cmde,cr):

        sommeExt = 0
        sommeExtCarree = 0
        sommeCmpt = 0
        sommeCmptCarree = 0

        nbMesures = 3

        # preparing connection to host
        exe=RunCommand()
        exe.do_add_host(host)
        exe.do_connect()

        result=treat_result(cr)

        # executing commands for many times : nbMesures
        for i in range(nbMesures):
            #waiting and extracting value
            time.sleep(1)

            #execution of command

            res=exe.do_run(cmde.cmd)

            #traitement de la valeur extraite
            valeur=result.return_result(res)

            #calcul des sommes d'extension
            sommeExt = sommeExt + valeur.value
            sommeExtCarree = sommeExtCarree + math.pow(valeur.value, 2)
            #Calcul des sommes de compatage
            sommeCmpt = sommeCmpt + valeur.complement
            sommeCmptCarree = sommeCmptCarree + math.pow(valeur.complement, 2)

        #determining the average and other parameters
        moyExt = sommeExt / nbMesures
        ecartTypeExt = sommeExtCarree / nbMesures - math.pow(moyExt, 2)
        moyCmpt = sommeCmpt / nbMesures
        ecartTypeCmpt = sommeCmptCarree / nbMesures - math.pow(moyCmpt, 2)

        # determining thresholds
        seuilExt = float(cmde.tempsExt) * float(cmde.zExt) * ecartTypeExt
        seuilCmpt = float(cmde.tempsCmpt) * float(cmde.zCmpt) * ecartTypeCmpt

        # extraction of the value to compare with thresholds
        res=exe.do_run(cmde.cmd)
        valeur=result.return_result(res)

        # creating the object that will be returned
        # this object contains value to compare and thresholds
        to_return=obj_cmp()
        to_return.value=valeur
        to_return.maxExt=seuilExt
        to_return.minCmpt=seuilCmpt

        print 'seuilExt ',seuilExt
        print 'seuilCmpt ',seuilCmpt
        #closing connection to host
        exe.do_close()

        # returning obj to be compared
        return to_return