'''
Created on 09-05-2022

@author: Dell
'''

import wx

listaInputsTxtCtrl=[]


class InterfazGrafica(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, "Jugadores")
        panel = wx.Panel(self)

        #caja de texto 1
        boton1 = wx.Button(panel, label = "Ingresar", pos = (200, 30))
        self.dlg1 = wx.TextCtrl(panel, pos = (10,30))
        self.dlg1_1 = wx.TextCtrl(panel, pos = (145,30), size = (40,20))
        self.dlg1_2 = wx.StaticText(panel, pos = (130, 30), label = "-")
        self.dlg1.SetMaxLength(8)
        
        #caja de texto 2
        boton2 = wx.Button(panel, label = "Buscar", pos = (200, 60))
        self.dlg2 = wx.TextCtrl(panel,pos = (10,60))
        self.dlg2_1 = wx.TextCtrl(panel, pos = (145,60), size = (40,20))
        self.dlg2_2 = wx.StaticText(panel, pos = (130, 60), label = "-")
        
        #caja de texto 3
        boton3 = wx.Button(panel, label="Eliminar", pos=(200, 90))
        self.dlg3=wx.TextCtrl(panel,pos=(10,90))
        self.dlg3_1 = wx.TextCtrl(panel, pos=(145,90),size=(40,20))
        self.dlg3_2 = wx.StaticText(panel, pos=(130, 90), label="-")
        
        #caja de texto 4
        boton4 = wx.Button(panel, label="Actualizar", pos=(200, 120))
        self.dlg4=wx.TextCtrl(panel,pos=(10,120))
        self.dlg4_1 = wx.TextCtrl(panel, pos=(145,120),size=(40,20))
        self.dlg4_2 = wx.StaticText(panel, pos=(130, 120), label="-")
        #self.lista = wx.ListBox(panel,choices=listaInputsTxtCtrl,pos=(240,30))

        self.Bind(wx.EVT_BUTTON,self.ingresarCliente,boton1)
        self.Bind(wx.EVT_BUTTON,self.buscarCliente,boton2)
        self.Bind(wx.EVT_BUTTON,self.eliminarCliente,boton3)
        self.Bind(wx.EVT_BUTTON,self.actualizarCliente,boton4)
        self.Show()

    def ingresarCliente(self,event):
        dniCli1=str(self.dlg1.GetValue())+"-"+str(self.dlg1_1.GetValue())
        if dniCli1 != (""):
            listaInputsTxtCtrl.append(dniCli1)
            print(listaInputsTxtCtrl)
            print("Cliente Ingresado")
        else:
            print("Por Favor rellenar campo")
        self.dlg1.SetValue('')
        self.dlg1_1.SetValue('')

    def buscarCliente(self,event):
        dniCli2 = str(self.dlg2.GetValue())+"-"+str(self.dlg2_1.GetValue())
        if len(listaInputsTxtCtrl) == 0:
            print("la lista se encuentra vacia")
        else:
            for i in range(0,len(listaInputsTxtCtrl),1):
                if dniCli2 == listaInputsTxtCtrl[i]:
                    print("El cliente se encuentra en la lista en la posicion "+str(i))
                else:
                    print("Cliente no encontrado")
        self.dlg2.SetValue('')
        self.dlg2_1.SetValue('')

    def eliminarCliente(self,event):
        dniCli3 = str(self.dlg3.GetValue())+"-"+str(self.dlg3_1.GetValue())
        for i in range(0, len(listaInputsTxtCtrl),1):
            if dniCli3 == listaInputsTxtCtrl[i]:
                listaInputsTxtCtrl.pop(i)
        print("Cliente Eliminado Exitosamente")
        self.dlg3.SetValue('')
        self.dlg3_1.SetValue('')
        print(listaInputsTxtCtrl)
        
    def actualizarCliente(self,event):
        dniCli2 = self.dlg2.GetValue()
        dniCli4 = self.dlg4.GetValue()
        for i in range(0, len(listaInputsTxtCtrl), 1):
            if dniCli2 == listaInputsTxtCtrl[i]:
                listaInputsTxtCtrl[i]= dniCli4
                print("Cliente Actualizado")
            else:
                print("Cliente no encontrado")
        self.dlg4.SetValue('')
        self.dlg4_1.SetValue('')
        self.dlg2.SetValue('')
        self.dlg2_1.SetValue('')

        print(listaInputsTxtCtrl)
