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

import it.tsp.cloudstack.api.occi.config as config


from eventlet import wsgi
import eventlet
from webob import Request, Response

# getting the Logger
logger = config.logger

# getting IP and Port of the OCCI server
OCCI_IP = config.OCCI_IP
OCCI_PORT = config.OCCI_PORT

if __name__ == '__main__':
    
    pass