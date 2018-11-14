# -*- coding: utf-8 -*-

"""
ViewModel.
"""

from livet import *

class ExampleVM(ViewModel):

    def __init__(self):
        # Init command.
        self.InitCommand = ViewModelCommand(self.Init)
        # Close command.
        self.CloseCommand = ViewModelCommand(self.Close)
        # CopyAbove command.
        self.CopyAboveCommand = ViewModelCommand(self.CopyAbove)

    def Init(self):
        print("Run Init().")
    
    def Close(self):
        print("Run Close().")

    def CopyAbove(self):
        self.TxtTwo = self.TxtOne

    # TxtOne notification property.
    _TxtOne = 1.0
    @property
    def TxtOne(self):
        print("TxtOne getter")
        return self._TxtOne
    @TxtOne.setter
    def TxtOne(self, value):
        if self._TxtOne == value:
            return
        print("TxtOne setter")
        self._TxtOne = value
        self.RaisePropertyChanged('')

    # TxtTwo notification property.
    _TxtTwo = 2.0
    @property
    def TxtTwo(self):
        print("Txt_Two getter")
        return self._TxtTwo
    @TxtTwo.setter
    def TxtTwo(self, value):
        if self._TxtTwo == value:
            return
        print("Txt_Two setter")
        self._TxtTwo = value
        self.RaisePropertyChanged('')
        