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
Created on Mai 25, 2011

@author: Khaled Ben Bahri
@contact: khaled.ben_bahri@it-sudparis.eu
@organization: Institut Telecom - Telecom SudParis
@version: 0.1
@license: LGPL - Lesser General Public License
'''

from extract_cr import Indicator
import logging

logging.basicConfig(Configformat='%(asctime)s %(message)s',level=logging.INFO)

class fixed_thresholds:

    def __init__(self,c):
        self.mxPhysical=c.maxPhy
        self.mxApp=c.maxApp
        self.mnApp=c.minApp

    def return_maxAdding(self):

        # return the min prefixed thresholds
        if self.mxPhysical<self.mxApp:
            return self.mxPhysical
        else:
            return self.mxApp


    def return_minRemoving(self):

        # the min prefixed threshold is the prefixed threshold fixed by application
        # because the min physical threshold is when we don't use any resource
        return self.mnApp