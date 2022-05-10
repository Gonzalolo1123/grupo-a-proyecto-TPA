'''
Created on 09-05-2022

@author: Dell
'''

import wx

listaInputsTxtCtrl=[]

class InterfazGrafica(wx.Frame):

    def _init_(self,parent,id):
        wx.Frame._init_(self,parent,id,"ventana")
        panel=wx.Panel(self)
        boton1=wx.Button(panel,label="Ingresar",pos=(130,30))
        boton2=wx.Button(panel,label="Buscar",pos=(130,60))
        boton3=wx.Button(panel,label="Eliminar",pos=(130,90))
        boton4=wx.Button(panel,label="Actualizar",pos=(130,120))
        
        self.Bind(wx.EVT_BUTTON,self.ingresarCliente,boton1)
        self.Bind(wx.EVT_BUTTON,self.buscarCliente,boton2)
        self.Bind(wx.EVT_BUTTON,self.eliminarCliente,boton3)
        self.Bind(wx.EVT_BUTTON,self.actualizarCliente,boton4)
        
        self.dlg1=wx.TextCtrl(panel,pos=(10,30))
        self.dlg2=wx.TextCtrl(panel,pos=(10,60))
        self.dlg3=wx.TextCtrl(panel,pos=(10,90))
        self.dlg4=wx.TextCtrl(panel,pos=(10,120))

        #self.lista = wx.ListBox(panel,choices=listaInputsTxtCtrl,pos=(240,30))
        
        self.Show()

    def ingresarCliente(self,event):
        dniCli1=self.dlg1.GetValue()
        if dniCli1 != (""):
            listaInputsTxtCtrl.append(dniCli1)
            print(listaInputsTxtCtrl)
            print("Cliente Ingresado")
        else:
            print("Por Favor rellenar campo")
        self.dlg1.SetValue('')
        
    def buscarCliente(self,event):
        dniCli2 = self.dlg2.GetValue()
        for i in range(0,len(listaInputsTxtCtrl),1):
            if dniCli2 == listaInputsTxtCtrl[i]:
                print("El cliente se encuentra en la lista en la posicion "+str(i))
            else:
                print("Cliente no encontrado")
        self.dlg2.SetValue('')
        
    def eliminarCliente(self,event):
        dniCli3 = self.dlg3.GetValue()
        for i in range(0, len(listaInputsTxtCtrl),1):
            if dniCli3 == listaInputsTxtCtrl[i]:
                listaInputsTxtCtrl.pop(i)
        print("Cliente Eliminado Exitosamente")
        self.dlg3.SetValue('')
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
        self.dlg2.SetValue('')
        print(listaInputsTxtCtrl)
        