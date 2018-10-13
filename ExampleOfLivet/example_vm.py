# -*- coding: utf-8 -*-

"""
ViewModel.
"""

from livet import *

class ExampleVM(ViewModel):

    def __init__(self):
        # Set command.
        self.Run_Btn_One_Command = ViewModelCommand(self.Run_Btn_One)

    # Txt_One property.
    _Txt_One = 1.0
    @property
    def Txt_One(self):
        print("Txt_One getter")
        return self._Txt_One
    @Txt_One.setter
    def Txt_One(self, value):
        if self._Txt_One == value:
            return
        print("Txt_One setter")
        self._Txt_One = value
        self.RaisePropertyChanged("")

    # Txt_Two property.
    _Txt_Two = 2.0
    @property
    def Txt_Two(self):
        print("Txt_Two getter")
        return self._Txt_Two
    @Txt_Two.setter
    def Txt_Two(self, value):
        if self._Txt_Two == value:
            return
        print("Txt_Two setter")
        self._Txt_Two = value
        self.RaisePropertyChanged("")
    
    def Run_Btn_One(self):
        self.Txt_Two = self.Txt_One