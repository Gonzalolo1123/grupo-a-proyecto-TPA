'''
Created on 09-05-2022

@author: Dell
'''

import wx
from model.claseJugador import Jugador
from model.claseListaJugadores import ListaJugadores

listaInputsTxtCtrl=[]


class InterfazGrafica(wx.Frame):  
    '''
    Esta clase es la interfaz grafica
    '''
    def __init__(self, parent, iden):
        
        '''
        :parent: Es el padre de la ventana.
        :id: Es el identificador de la ventana. Puede tomar un valor de -1 para indicar un valor predeterminado.
        '''
        
        wx.Frame.__init__(self, parent, iden, "Jugadores")
        panel = wx.Panel(self)

        #caja de texto 1
        boton1 = wx.Button(panel, label = "Ingresar", pos = (10, 30))
        
        self.textoNombre1 = wx.StaticText(panel, pos = (10, 62), label = "Nombre")
        
        self.campoDniA1 = wx.TextCtrl(panel, pos = (60,60))
        self.campoDniA1.SetMaxLength(8)
        
        self.textoGuion1 = wx.StaticText(panel, pos = (180, 60), label = "-")
        
        self.campoDniB1 = wx.TextCtrl(panel, pos = (195,60), size = (40,20))
        self.campoDniB1.SetMaxLength(1)
        
        #caja de texto 2
        boton2 = wx.Button(panel, label="Buscar", pos=(10, 150))
        
        self.textoNombre2 = wx.StaticText(panel, pos = (10, 182), label = "Nombre")
        
        self.campoDniA2=wx.TextCtrl(panel,pos=(60,180))
        self.campoDniA2.SetMaxLength(8)
        
        self.textoGuion2 = wx.StaticText(panel, pos=(180, 180), label="-")
        
        self.campoDniB2 = wx.TextCtrl(panel, pos=(195,180),size=(40,20))
        self.campoDniB2.SetMaxLength(1)

        
        #caja de texto 3
        boton3 = wx.Button(panel, label="Eliminar", pos=(10, 270))
        
        self.textoNombre3 = wx.StaticText(panel, pos = (10, 302), label = "Nombre")
        
        self.campoDniA3=wx.TextCtrl(panel,pos=(60,300))
        self.campoDniA3.SetMaxLength(8)
        
        self.textoGuion3 = wx.StaticText(panel, pos=(180, 300), label="-")
        
        self.campoDniB3 = wx.TextCtrl(panel, pos=(195,300),size=(40,20))
        self.campoDniB3.SetMaxLength(1)
        
        #caja de texto 4
        boton4 = wx.Button(panel, label="Actualizar", pos=(10, 390))
        
        self.textoNombre4 = wx.StaticText(panel, pos = (10, 422), label = "Nombre")
        
        self.campoDniA4=wx.TextCtrl(panel,pos=(60,420))
        self.campoDniA4.SetMaxLength(8)
        
        self.textoGuion4 = wx.StaticText(panel, pos=(180, 420), label="-")
        
        self.campoDniB4 = wx.TextCtrl(panel, pos=(195,420),size=(40,20))
        self.campoDniB4.SetMaxLength(1)
        
        #self.lista = wx.ListBox(panel,choices=listaInputsTxtCtrl,pos=(240,30))

        self.Bind(wx.EVT_BUTTON,self.ingresarCliente,boton1)
        self.Bind(wx.EVT_BUTTON,self.buscarCliente,boton2)
        self.Bind(wx.EVT_BUTTON,self.eliminarCliente,boton3)
        self.Bind(wx.EVT_BUTTON,self.actualizarCliente,boton4)
        self.Show()

    def ingresarCliente(self,event):
        '''
        :event: El parametro event liga esta funcion con la interaccion con boton1.
        '''
        
        dniCli1=str(self.campoDniA1.GetValue())+"-"+str(self.campoDniB1.GetValue())
        if dniCli1 != (""):
            listaInputsTxtCtrl.append(dniCli1)
            print(listaInputsTxtCtrl)
            print("Cliente Ingresado")
        else:
            print("Por Favor rellenar campo")
        self.campoDniA1.SetValue('')
        self.campoDniB1.SetValue('')

    def buscarCliente(self,event):
        '''
        :event: El parametro event liga esta funcion con la interaccion con boton2.
        '''
        
        dniCli2 = str(self.campoDniA2.GetValue())+"-"+str(self.campoDniB2.GetValue())
        if len(listaInputsTxtCtrl) == 0:
            print("la lista se encuentra vacia")
        else:
            for i in range(0,len(listaInputsTxtCtrl),1):
                if dniCli2 == listaInputsTxtCtrl[i]:
                    print("El cliente se encuentra en la lista en la posicion "+str(i))
                else:
                    print("Cliente no encontrado")
        self.campoDniA2.SetValue('')
        self.campoDniB2.SetValue('')

    def eliminarCliente(self,event):
        '''
        :event: El parametro event liga esta funcion con la interaccion con boton3.
        '''
        
        dniCli3 = str(self.campoDniA3.GetValue())+"-"+str(self.campoDniB3.GetValue())
        for i in range(0, len(listaInputsTxtCtrl),1):
            if dniCli3 == listaInputsTxtCtrl[i]:
                listaInputsTxtCtrl.pop(i)
        print("Cliente Eliminado Exitosamente")
        self.campoDniA3.SetValue('')
        self.campoDniB3.SetValue('')
        print(listaInputsTxtCtrl)
        
    def actualizarCliente(self,event):
        '''
        :event: El parametro event liga esta funcion con la interaccion con boton4.
        '''
        dniCli2 = str(self.campoDniA2.GetValue())+"-"+str(self.campoDniB2.GetValue())
        dniCli4 = str(self.campoDniA4.GetValue())+"-"+str(self.campoDniB4.GetValue())
        for i in range(0, len(listaInputsTxtCtrl), 1):
            if dniCli2 == listaInputsTxtCtrl[i]:
                listaInputsTxtCtrl[i]= dniCli4
                print("Cliente Actualizado")
                
        self.campoDniA4.SetValue('')
        self.campoDniB4.SetValue('')
        self.campoDniA2.SetValue('')
        self.campoDniB2.SetValue('')

        print(listaInputsTxtCtrl)
