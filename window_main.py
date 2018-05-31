#!/bin/python

import wx
import Screen1

class main_window(wx.Frame):

    def __init__(self, *args, **kw):
        # ensure the parent's __init__ is called
        super().__init__(*args, **kw)

        # create a panel in the frame
        panel = wx.Panel(self)

        # create a menu bar
        self.makeMenuBar()

        # and a status bar
        self.CreateStatusBar()
        self.SetStatusText("TLS_EZ the easiest certificate management tool THERE IS")


    def makeMenuBar(self):
        """
        A menu bar is composed of menus, which are composed of menu items.
        This method builds a set of menus and binds handlers to be called
        when the menu item is selected.
        """

        # Make a file menu
        fileMenu = wx.Menu()

        # Make a file submenu called 'New'
        OptionsNew = wx.Menu()

        # Make a submenu for creating certificates
        OptionsCertificate = wx.Menu()
        OptionsCertificate.Append(wx.ID_ANY, 'Root CA', 'Creates cert for a self-signed root certificate authority')
        OptionsCertificate.Append(wx.ID_ANY, 'Intermediate CA', 'Creates cert for an intermediate certificate authority')
        OptionsCertificate.Append(wx.ID_ANY, 'Server Certificate', 'Creates cert for a server')
        OptionsCertificate.Append(wx.ID_ANY, 'Client Certificate', 'Creates cert for client')

        # Make a submenu for creating certificate signing requests
        OptionsCSR = wx.Menu()
        OptionsCSR.Append(wx.ID_ANY, 'Intermediate CA', 'Creates a CSR to Root CA on behalf of an intermediate CA')
        OptionsCSR.Append(wx.ID_ANY, 'Server Certificate', 'Creates a CSR to Intermediate CA on behalf of a server')
        OptionsCSR.Append(wx.ID_ANY, 'Client Certificate', 'Creates a CSR to Intermediate Ca on behalf of client')

        # Append the submenus to the file menu
        fileMenu.Append(wx.ID_ANY, '&New',  OptionsNew)
        OptionsNew.Append(wx.ID_ANY, '&Certificate', OptionsCertificate)
        OptionsNew.Append(wx.ID_ANY, '&Certificate Req.', OptionsCSR)

        # Separate the file menu options for ecstatics
        fileMenu.AppendSeparator()

        #Append the Quit option to file menu
        exitItem = wx.MenuItem(fileMenu, wx.ID_EXIT, '&Quit\tCtrl+W')
        fileMenu.Append(exitItem)

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
        self.Bind(wx.EVT_MENU, self.OnExit,  exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)


    def OnExit(self, event):
        """Close the frame, terminating the application."""
        self.Close(True)

    def OnAbout(self, event):
        """Display an About Dialog"""
        wx.MessageBox("This product is owned and distributed by RavRic Solutions Inc.","About TLS_EZ", wx.OK|wx.ICON_INFORMATION)

if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    app = wx.App()
    mainFrame = main_window(None, title='TLS EZ')
    first=Screen1.screen1(mainFrame)
    mainFrame.Show()
    first.Show()
    app.MainLoop()