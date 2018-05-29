#!/bin/python

import wx


class screen1(wx.Panel):

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.createControlsInt()

    def createControlsInt(self):
        sizer=wx.BoxSizer(wx.HORIZONTAL)
        self.nextButton = wx.Button(self, label='Next')
        self.cancelButton = wx.Button(self, label='Cancel')
        sizer.Add(self.nextButton)
        sizer.Add(self.cancelButton)
        self.SetSizer(sizer)

#app= wx.App()
#frame = wx.Frame(None, -1, 'win.py')
#
#panel = screen1(frame, wx.ID_ANY)
#frame.Show()
#frame.Centre()
#app.MainLoop()

