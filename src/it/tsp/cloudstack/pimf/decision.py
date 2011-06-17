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

from chaining import execution
from extract_value import obj_extract
import logging

logging.basicConfig(Configformat='%(asctime)s %(message)s',level=logging.INFO)

class decision:
    '''
    in this class, the decision is taken for an indicator
    the decision will be either adding/removing if it will reach the prefixed thresholds
    or extending/compacting if we will reach only the consumption thresholds
    '''
    def __init__(self):
        pass

    def optimize(self,extracted,mxAdd,mnRem):

        if extracted.value>mxAdd:
            # adding new VM according to this indicator
            logging.info('Adding VM according to : %s ',extracted.cr)
            return 'add'

        elif extracted.value<mnRem:
            # Removing VM according to this indicator
            logging.info('Removing VM according to : %s ',extracted.cr)
            return 'rem'

        elif extracted.value>extracted.maxExt:
            #extending VM according to this indicator
            logging.info('Extending VM according to : %s ',extracted.cr)
            return 'ext'

        elif extracted.value>extracted.minCmpt:
            #compacting VM according to this indicator
            logging.info('Compacting VM according to : %s ',extracted.cr)
            return 'cmpt'

        else:
            #nothing to do
            logging.info('Nothing to do to : %s ',extracted.cr)
            return 'no'
