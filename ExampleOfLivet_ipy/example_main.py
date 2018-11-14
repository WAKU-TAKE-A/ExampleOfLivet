# -*- coding: utf-8 -*-

"""
Data Binding Example.

* Run this file.
"""

import wpf
import os.path as path
from System.Windows import Application, Window
from livet import *
from example_vm import ExampleVM

class ExampleMain(Window):
    def __init__(self):
        self.vm = ExampleVM()
        self.DataContext = self.vm
        wpf.LoadComponent(self, path.join(path.dirname(__file__), 'example_v.xaml'))
        print('Init window.')

def RunExample():
    Application().Run(ExampleMain())

if __name__ == '__main__':
    Application().Run(ExampleMain())
