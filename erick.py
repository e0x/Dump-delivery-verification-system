#!/usr/bin/python

import wx


class AppFrame( wx.Frame ):

    def __init__(self, title):
        
        wx.Frame.__init__( self, None, wx.ID_ANY, title=title, size=(800, 600) )
        self.Panel = wx.Panel( self )
        #self.Panel.BackgroundColour = (200, 240, 250) # light blue   

        # Add Buttons
        self.Querybtn = wx.Button(self.Panel, label="Consultar", pos=(1, 5))
        self.Addbtn = wx.Button(self.Panel, label="agregar")
        self.Savebtn = wx.Button(self.Panel, label="Salvar")
        self.Clearbtn = wx.Button(self.Panel, label="Limpiar")
        self.Delbtn = wx.Button(self.Panel, label="Borrar")
        
        # Add static text and input fields and they own Sizer
        self.Ced_vSizer = wx.BoxSizer(wx.VERTICAL)
        self.CedTxt = wx.StaticText(self.Panel, wx.ID_ANY, 'Cedula:')
        self.CedInput = wx.TextCtrl(self.Panel, wx.ID_ANY)
        self.Ced_vSizer.Add(self.CedTxt, proportion=0, flag=wx.EXPAND|wx.ALL, border=5)
        self.Ced_vSizer.Add(self.CedInput, proportion=1, flag=wx.EXPAND|wx.ALL, border=5)
        self.Ced_vSizer.Add(self.Querybtn, proportion=1, flag=wx.EXPAND|wx.ALL, border=5) 
        
        # Add Static text and Text Ctlr of name , tel, Address and they own Sizer
        self.NameText = wx.StaticText(self.Panel, wx.ID_ANY, 'Nombre:')
        self.NameInput = wx.TextCtrl(self.Panel, wx.ID_ANY, size = wx.Size(400, 20))
        self.DirText = wx.StaticText(self.Panel, wx.ID_ANY, 'Direccion:')
        self.DirInput = wx.TextCtrl(self.Panel, wx.ID_ANY, size = wx.Size(400, 20))
        self.TelText  = wx.StaticText(self.Panel, wx.ID_ANY, 'Telefono:')
        self.TelInput = wx.TextCtrl(self.Panel, wx.ID_ANY, size = wx.Size(100, 20))
        self.DataFields = wx.FlexGridSizer(rows = 3, cols = 2, hgap = 5, vgap = 10)
        self.DataFields.AddMany([(self.NameText, 0, wx.ALIGN_CENTER_VERTICAL),
                                  (self.NameInput, 0, wx.ALIGN_CENTER_VERTICAL),
                                  (self.DirText, 0, wx.ALIGN_CENTER_VERTICAL),
                                  (self.DirInput, 1, wx.EXPAND),
                                  (self.TelText, 0, wx.ALIGN_CENTRE_VERTICAL),
                                  self.TelInput])
        
        # Add list crtl
        self.listctrl = wx.ListCtrl(self.Panel, style=wx.LC_REPORT|wx.BORDER_SUNKEN)
        self.listctrl.InsertColumn(0, 'ID')
        self.listctrl.InsertColumn(1, 'Detalle', width=wx.EXPAND)
        
        # Add textcrtl for add more details
        self.AddTextCrtl = wx.TextCtrl(self.Panel, -1, '', style=wx.MULTIPLE)

        # Add Sizer's for layout managment
        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        self.topSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.midSizer = wx.BoxSizer(wx.VERTICAL)
        self.bottomSizer = wx.BoxSizer(wx.HORIZONTAL)
        


        # Add elements to the top sizer
        self.topSizer.Add(self.Ced_vSizer, 0, wx.ALIGN_LEFT)
        self.topSizer.Add(self.DataFields, 0, wx.ALIGN_LEFT)
        self.mainSizer.Add(self.topSizer, proportion=1, flag=wx.ALL, border=5)

        # add list crtl to the own size
        self.midSizer.Add(self.Addbtn, proportion=0, flag=wx.CENTER|wx.ALL, border=10)
        self.midSizer.Add(self.AddTextCrtl, proportion=0, flag=wx.EXPAND|wx.ALL, border=5)
        self.midSizer.Add(self.listctrl, proportion=1, flag=wx.EXPAND|wx.ALL)
        self.mainSizer.Add(self.midSizer, proportion=2, flag=wx.EXPAND|wx.ALL, border=5)
        # Add buttons in the own sizer

        # Add elements to the bottom sizer
        self.bottomSizer.Add(self.Delbtn, proportion=0, flag=wx.EXPAND|wx.ALL, border=5)
        self.bottomSizer.Add(self.Clearbtn, proportion=0, flag=wx.EXPAND|wx.ALL, border=5)
        self.bottomSizer.Add(self.Savebtn, proportion=0, flag=wx.EXPAND|wx.ALL, border=5)
        self.mainSizer.Add(self.bottomSizer, proportion=1, flag=wx.EXPAND|wx.ALL, border=55)
        # set hbox sizer to vbox sizer


        # setsizer panel
        self.Panel.SetSizer(self.mainSizer)
        
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
        self.index = 0
        self.ID = 1

    def OnAddBtn(self, event):
        self.parent.listctrl.InsertStringItem(self.index, str(self.ID))
        self.parent.listctrl.SetStringItem (self.index, 1, self.parent.AddTextCrtl.GetValue()) 
        self.index += 1
        self.ID += 1
        self.parent.AddTextCrtl.Clear()

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

