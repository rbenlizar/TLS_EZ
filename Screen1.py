#!/bin/python

import wx


class screen1(wx.Panel):

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.createControlsInt()

    def createControlsInt(self):
        form1=wx.FlexGridSizer(rows=5, cols=2, vgap=10, hgap=10)
        sizer=wx.BoxSizer(wx.HORIZONTAL)
        self.importCheckBox = wx.CheckBox(self, label='Import Existing CSR')
        self.importField = wx.TextCtrl(self, value='Please enter path to CSR')
        self.pkCheckBox = wx.CheckBox(self, label='Import Private Key')
        self.pkField = wx.TextCtrl(self, value='Please enter path to existing Private Key')
        self.keySizeLabel = wx.StaticText(self, label='Key Size: ')
        self.keySizeField = wx.TextCtrl(self, value='Enter Key Size')
#        self.nextButton = wx.Button(self, label='Next')
#        self.cancelButton = wx.Button(self, label='Cancel')
#        sizer.Add(self.nextButton, 0, 0, 0)
#        sizer.Add(self.cancelButton, 0,0,0)
        form1.Add(self.importCheckBox)
        form1.Add(self.importField,0,wx.EXPAND,0)
        form1.Add(self.pkCheckBox)
        form1.Add(self.pkField,0,wx.EXPAND,0)
        form1.Add(self.keySizeLabel)
        form1.Add(self.keySizeField, 0,wx.RIGHT,200)
#        form1.SetSizeHints(self)
#        sizer.SetSizeHints(self)

        self.SetSizer(form1)

#        self.SetSizer(sizer)

app= wx.App()
frame = wx.Frame(None, -1, 'win.py')

panel = screen1(frame, wx.ID_ANY)
frame.Show()
frame.Centre()
app.MainLoop()