#!/bin/python
"""
Hello World, but with more meat.
"""

import wx

class HelloFrame(wx.Frame):
    """
    A Frame that says Hello World
    """

    def __init__(self, *args, **kw):
        # ensure the parent's __init__ is called
        super(HelloFrame, self).__init__(*args, **kw)

        # create a panel in the frame
        pnl = wx.Panel(self)

        # and put some text with a larger bold font on it
        st = wx.StaticText(pnl, label="Ricardo", pos=(25,25))
        font = st.GetFont()
        font.PointSize += 5
        st.SetFont(font)

        # create a menu bar
        self.makeMenuBar()

        # and a status bar
        self.CreateStatusBar()
        self.SetStatusText("Welcome to wxPython!")


    def makeMenuBar(self):
        """
        A menu bar is composed of menus, which are composed of menu items.
        This method builds a set of menus and binds handlers to be called
        when the menu item is selected.
        """

        # Make a file menu with Hello and Exit items
        fileMenu = wx.Menu()
        # The "\t..." syntax defines an accelerator key that also triggers
        # the same event

        newItem = fileMenu.Append(-1, "&New...\tCtrl-N",
                "Will open a new text field")
        fileMenu.AppendSeparator()
        # When using a stock ID we don't need to specify the menu item's
        # label
        exitItem = fileMenu.Append(wx.ID_EXIT)

        # Now a help menu for the about item
        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)

        # Make the menu bar and add the two menus to it. The '&' defines
        # that the next letter is the "mnemonic" for the menu item. On the
        # platforms that support it those letters are underlined and can be
        # triggered from the keyboard.
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(helpMenu, "&Help")

        # Give the menu bar to the frame
        self.SetMenuBar(menuBar)

        # Finally, associate a handler function with the EVT_MENU event for
        # each of the menu items. That means that when that menu item is
        # activated then the associated handler function will be called.
        self.Bind(wx.EVT_MENU, self.OnHello, newItem)
        self.Bind(wx.EVT_MENU, self.OnExit,  exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)


    def OnExit(self, event):
        """Close the frame, terminating the application."""
        self.Close(True)


    def OnHello(self, event):
        """Say hello to the user."""
        wx.MessageBox('Here I am')


    def OnAbout(self, event):
        """Display an About Dialog"""
        wx.MessageBox("This is a wxPython Hello World sample",
                      "About Hello World 2",
                      wx.OK|wx.ICON_INFORMATION)


class Mywin(wx.Frame):
    def __init__(self, parent, title):
        super(Mywin, self).__init__(parent, title=title, size=(350, 250))

        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        l1 = wx.StaticText(panel, -1, "Text Field")

        hbox1.Add(l1, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        self.t1 = wx.TextCtrl(panel)

        hbox1.Add(self.t1, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        self.t1.Bind(wx.EVT_TEXT, self.OnKeyTyped)
        vbox.Add(hbox1)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        l2 = wx.StaticText(panel, -1, "password field")

        hbox2.Add(l2, 1, wx.ALIGN_LEFT | wx.ALL, 5)
        self.t2 = wx.TextCtrl(panel, style=wx.TE_PASSWORD)
        self.t2.SetMaxLength(5)

        hbox2.Add(self.t2, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        vbox.Add(hbox2)
        self.t2.Bind(wx.EVT_TEXT_MAXLEN, self.OnMaxLen)

        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        l3 = wx.StaticText(panel, -1, "Multiline Text")

        hbox3.Add(l3, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        self.t3 = wx.TextCtrl(panel, size=(200, 100), style=wx.TE_MULTILINE)

        hbox3.Add(self.t3, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        vbox.Add(hbox3)
        self.t3.Bind(wx.EVT_TEXT_ENTER, self.OnEnterPressed)

        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        l4 = wx.StaticText(panel, -1, "Read only text")

        hbox4.Add(l4, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        self.t4 = wx.TextCtrl(panel, value="ReadOnlyText",style = wx.TE_READONLY|wx.TE_CENTER)
        hbox4.Add(self.t4, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        vbox.Add(hbox4)
        panel.SetSizer(vbox)

        self.Centre()
        self.Show()
        self.Fit()

    def OnKeyTyped(self, event):
        print
        event.GetString()

    def OnEnterPressed(self, event):
        print
        "Enter pressed"

    def OnMaxLen(self, event):
        print
        "Maximum length reached"


if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    app = wx.App()
    Mywin(None, 'TextCtrl demo')
    frm = HelloFrame(None, title='TLS EZ')
    frm.Show()
    app.MainLoop()