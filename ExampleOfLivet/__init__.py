# -*- coding: utf-8 -*-

"""
Livet for IronPython.

* Environment variable 'IRONPYTHON_HOME' is required. It is the installation location of IronPython.
* "Livet.dll" is required. The version is 1.3.
"""

__author__  = "Nishida Takehito <takehito.nishida@gmail.com>"
__version__ = "0.9.1.0"
__date__    = "2018/10/17"

#
# append path.
#
import os
import os.path as path
from sys import path as systemPath
from System import Environment as env
IRONPYTHON_HOME = env.GetEnvironmentVariable("IRONPYTHON_HOME")

if IRONPYTHON_HOME is None:
    raise Exception("Error : Set path of IRONPYTHON_HOME.")

IPY_LIB = path.join(IRONPYTHON_HOME, "Lib")
IPY_DLLS = path.join(IRONPYTHON_HOME, "DLLs")
IPY_LIVET = path.join(IRONPYTHON_HOME, "Lib\\livet")

_lstPath = []
_lstPath.append(IPY_LIB)
_lstPath.append(IPY_DLLS)
_lstPath.append(IPY_LIVET)

for i in _lstPath:
    if os.path.exists(i):
        systemPath.append(i)
    else:
        raise Exception("There is no '" + i + "'.")

#
# Import modules.
#
import clr
clr.AddReferenceToFile("Livet.dll")
from Livet import ViewModel
from Livet.Commands import ViewModelCommand
