# -*- Mode: python; py-indent-offset: 4; indent-tabs-mode: nil; coding: utf-8; -*-

# Copyright (C) 2011 Houssem Medhioub - Institut Telecom
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

"""
Created on Feb 25, 2011

@author: Houssem Medhioub
@contact: houssem.medhioub@it-sudparis.eu
@organization: Institut Telecom - Telecom SudParis
@version: 0.1
@license: LGPL - Lesser General Public License
"""

#==============================================================================================
#==  This function creates a new class in the provided namespace (gl) with the name         ===
#==    classname inheriting from all classes in parentclasses, which is a list of strings.  ===
#==============================================================================================
def create_new_class(classname, parentclasses, gl = globals()):
    """"""
    if len(parentclasses) > 0:
        parent = map(lambda p: p.__name__, parentclasses)
        createclass = 'class %s (%s):\n\tpass' % (classname, ','.join(parent))
    else:
        createclass = 'class %s:\n\tpass' % classname
    exec createclass in gl
    gl[classname] = eval(classname, gl)

if __name__ == '__main__':
    class clazz1:
        def __init__(self, a):
            self.a = a

        def foo(self):
            return "clazz1: " + str(self.a)

    class clazz2:
        def __init__(self, b, a):
            self.b = b
            self.a = a

        def bar(self):
            return "clazz2: " + str(self.b) + str(self.a)

    # to create a new class names 'Test' that inherit from 'Foobar' and 'Barfoo'
    create_new_class("Test", [clazz1, clazz2], globals())
    print Test.__bases__
    t = Test("23")
    print t.foo() # this will print "foo23"
    # To instantiate an object from a class who's name is stored as string
    t2 = globals()['Test']('23')
    print t2.foo()
    #print t.bar() # this will throw an exception, because self.b is not defined

    pass