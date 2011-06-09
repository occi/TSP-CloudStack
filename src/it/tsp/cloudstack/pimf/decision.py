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

from chaining import execution
from extract_value import obj_extract


class decision:
    def __init__(self,):
        pass

    def optimize(self,extracted,mxAdd,mnRem):

        if extracted.value>mxAdd:
            # adding new VM according to this indicator
            return 'add'

        elif extracted.value<mnRem:
            # Removing VM according to this indicator
            return 'rem'

        elif extracted.value>extracted.maxExt:
            #extending VM according to this indicator
            return 'ext'
        elif extracted.value>extracted.minCmpt:
            #compacting VM according to this indicator
            return 'cmpt'
        else:
            #nothing to do
            return 'no'

        
        