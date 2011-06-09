
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

# a returbed value has the used value and its complement the free value
class returned_values:
    value=None
    complement=None

    def __init__(self):
        pass

class treat_result:

    def __init__(self,cr):
        self.cr=cr.lower()


    def treat_disk(self,rt):

        # the result of executing command to extract disk size is
        # /dev/sda1              24G  1.7G   21G   8% /
        val=returned_values()
        r=rt[0].split("G")
        val.value=float(r[1])
        val.complement=float(r[2])

        return val


    def treat_hdfs(self,rt):
        pass

    def treat_cpu(self,rt):
        pass

    def treat_memory(self,rt):
        pass

    def treat_bandwidth(self,rt):
        pass

    def return_result(self,rt):

        # choosing method depending of the used indicator
        if self.cr=='disk':
            return self.treat_disk(rt)
        elif self.cr=='hdfs':
            return self.treat_hdfs(rt)
        elif self.cr=='cpu':
            return self.treat_cpu(rt)
        elif self.cr=='memory':
            return self.treat_memory(rt)
        else:
            return self.treat_bandwidth(rt)
