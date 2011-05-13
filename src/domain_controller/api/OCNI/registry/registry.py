# -*- Mode: python; py-indent-offset: 4; indent-tabs-mode: nil; coding: utf-8; -*-

# Copyright (C) 2011 Houssem Medhioub - Institut Telecom
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

@author: Houssem Medhioub
@contact: houssem.medhioub@it-sudparis.eu
@organization: Institut Telecom - Telecom SudParis
@version: 0.1
@license: LGPL - Lesser General Public License
'''

import logging.config

# Loading the logging configuration file
logging.config.fileConfig("../../CloNeLogging.conf")
# getting the Logger
logger = logging.getLogger("CloNeLogging")

# ======================================================================================
# Location registry
# ======================================================================================
class location_registry(object):
    locations = {}

    def register_location(self, location, object):
        if  object.__repr__() in self.locations :
            logger.warning('the location \'' + location + '\' is already registered')
            raise ('the location \'' + location + '\' is already registered')
        


# ======================================================================================
# category registry
# ======================================================================================
class category_registry(object):
    categories = {}
    
if __name__ == '__main__':
    pass