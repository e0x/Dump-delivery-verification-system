#!/usr/bin/python

import wx


class AppFrame( wx.Frame ):

    def __init__(self, title):
        
        wx.Frame.__init__( self, None, wx.ID_ANY, title=title, size=(800, 600) )
        self.frmPanel = wx.Panel( self )
        self.frmPanel.BackgroundColour = (200, 240, 250) # light blue

        # Add another panel 
        self.BtnPanel = wx.Panel(self.frmPanel)
        self.BtnPanel.SetBackgroundColour( wx.NamedColor( 'GREY' ) )

        # Add Buttons
        self.Querybtn = wx.Button(self.frmPanel, label="Consultar")
        self.Addbtn = wx.Button(self.frmPanel, label="agregar")
        self.Savebtn = wx.Button(self.frmPanel, label="Salvar")
        self.Clearbtn = wx.Button(self.frmPanel, label="Limpiar")
        self.Delbtn = wx.Button(self.frmPanel, label="Borrar")

        # Add panel to a sizer
        PnlAndBtn_vSizer = wx.BoxSizer( wx.VERTICAL )
        PnlAndBtn_vSizer.Add( self.BtnPanel, 1, wx.EXPAND|wx.ALL, 1)

        # Add buttons in the own sizer
        btn_hSizer = wx.BoxSizer( wx.HORIZONTAL ) 
        
        btn_hSizer.Add(self.Querybtn, proportion=0,
                flag=wx.ALIGN_LEFT|wx.ALL, border=5)

        btn_hSizer.AddStretchSpacer()

        btn_hSizer.Add(self.Addbtn, proportion=0, flag=wx.EXPAND|wx.ALL, 
                border=5)
        btn_hSizer.Add(self.Savebtn, proportion=0, flag=wx.EXPAND|wx.ALL,
                border=5)
        btn_hSizer.Add(self.Clearbtn, proportion=0, flag=wx.EXPAND|wx.ALL,
                border=5)
        btn_hSizer.Add(self.Delbtn, proportion=0, flag=wx.EXPAND|wx.ALL,
                border=5)
        
        btn_hSizer.AddStretchSpacer()

        PnlAndBtn_vSizer.Add( btn_hSizer, 0, wx.EXPAND|wx.ALL, 5 )

        # SetSizer both sizers in the most senior control that has sizer in it.
        self.frmPanel.SetSizer(PnlAndBtn_vSizer)
        self.frmPanel.Layout()

        # Must call before any event handler is referenced.
        self.eventsHandler = EventsHandler(self)

        # Bind event handlers to all controls that have one.
        self.Addbtn.Bind( wx.EVT_BUTTON, self.eventsHandler.OnAddBtn )
        self.Querybtn.Bind( wx.EVT_BUTTON, self.eventsHandler.OnQueryBtn )
        self.Savebtn.Bind( wx.EVT_BUTTON, self.eventsHandler.OnSaveBtn )
        self.Clearbtn.Bind( wx.EVT_BUTTON, self.eventsHandler.OnClearBtn )
        self.Delbtn.Bind( wx.EVT_BUTTON, self.eventsHandler.OnDelBtn )

    # End __init__

# End AppFrame class


class EventsHandler():
    
    def __init__(self, parent):
        self.parent = parent

    def OnAddBtn(self, event):
        pass

    def OnQueryBtn(self, event):
        pass

    def OnSaveBtn(self, event):
        pass

    def OnClearBtn(self, event):
        pass

    def OnDelBtn(self, event):
        pass

#end events class


def Main():

    app = wx.App(redirect=False)
    appFrm = AppFrame(title='Control de Entrega')
    appFrm.Show()
    app.MainLoop()

#end Main

if __name__ == '__main__':
    Main()
