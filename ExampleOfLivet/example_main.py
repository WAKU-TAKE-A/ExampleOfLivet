# -*- coding: utf-8 -*-

"""
Data Binding Example.

* Run this file.
"""

import wpf
from System.Windows import Application, Window
from livet import *
from example_vm import ExampleVM

class ExampleMain(Window):
    def __init__(self):
        self.vm = ExampleVM()
        self.DataContext = self.vm
        fn_v = path.join(IRONPYTHON_LIVET, 'example_v.xaml')
        wpf.LoadComponent(self, fn_v)
        print('Init window.')

def RunExample():
    Application().Run(ExampleMain())

if __name__ == '__main__':
    Application().Run(ExampleMain())
