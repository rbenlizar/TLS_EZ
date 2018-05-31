#!/bin/python

import wx


class screen1(wx.Panel):

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.policies = ['Strict','Loose']
        self.createControlsInt()

    def createControlsInt(self):
        form1=wx.FlexGridSizer(rows=5, cols=2, vgap=10, hgap=10)
        sizer=wx.BoxSizer(wx.HORIZONTAL)
        self.importCheckBox = wx.CheckBox(self, label='Import Existing CSR')
        self.importField = wx.TextCtrl(self, value='Please enter path to CSR')
        self.policyLabel= wx.StaticText(self, label='Select a Policy')
        self.policyDropdown = wx.ComboBox(self, choices= self.policies, style=wx.CB_DROPDOWN)
        self.pkCheckBox = wx.CheckBox(self, label='Import Private Key')
        self.pkField = wx.TextCtrl(self, value='Please enter path to existing Private Key')
        self.keySizeLabel = wx.StaticText(self, label='Key Size: ')
        self.keySizeField = wx.TextCtrl(self, value='Enter Key Size')
        self.nextButton = wx.Button(self, label='Next')
        self.cancelButton = wx.Button(self, label='Cancel')
        form1.Add(self.importCheckBox)
        form1.Add(self.importField,0,wx.EXPAND,0)
        form1.Add(self.pkCheckBox)
        form1.Add(self.pkField,0,wx.EXPAND,0)
        form1.Add(self.keySizeLabel)
        form1.Add(self.keySizeField, 0,wx.RIGHT,200)
        form1.Add(self.policyLabel)
        form1.Add(self.policyDropdown)
        sizer.Add(form1)
        sizer.Add(self.nextButton, 0, wx.TOP, 100)
        sizer.Add(self.cancelButton, 0,wx.TOP,100)
        sizer.SetSizeHints(self)
        self.SetSizerAndFit(sizer)

    def bindEvents(self):
        for control, event, handler in \
            [(self.importCheckBox, wx.EVT_CHECKBOX, self.onImportPath)]:
#             (self.nameTextCtrl, wx.EVT_TEXT, self.onNameEntered),
#             (self.nameTextCtrl, wx.EVT_CHAR, self.onNameChanged),
#             (self.referrerComboBox, wx.EVT_COMBOBOX, self.onReferrerEntered),
#             (self.referrerComboBox, wx.EVT_TEXT, self.onReferrerEntered),
#             (self.insuranceCheckBox, wx.EVT_CHECKBOX, self.onInsuranceChanged),
#             (self.colorRadioBox, wx.EVT_RADIOBOX, self.onColorchanged)]:
            control.Bind(event, handler)


app= wx.App()
frame = wx.Frame(None, -1, 'win.py')

panel = screen1(frame, wx.ID_ANY)
frame.Show()
frame.Centre()
app.MainLoop()