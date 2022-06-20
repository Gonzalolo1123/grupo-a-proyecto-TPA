'''
Created on 09-05-2022

@author: Dell
'''

import wx
from model.claseListaJugadores import ListaJugadores

lis=ListaJugadores()


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
        
        self.textoDni1 = wx.StaticText(panel, pos = (36, 94), label = "Dni")
        
        self.campoDniA1 = wx.TextCtrl(panel, pos = (60,90), size = (64,20))
        self.campoDniA1.SetMaxLength(8)
        
        self.textoGuion1 = wx.StaticText(panel, pos = (132, 90), label = "-")
        
        self.campoDniB1 = wx.TextCtrl(panel, pos = (145,90), size = (20,20))
        self.campoDniB1.SetMaxLength(1)
        
        self.textoNombre1 = wx.StaticText(panel, pos = (10,62), label = "Nombre")
        
        self.campoNombre1 = wx.TextCtrl(panel, pos = (60,60), size = (105,20))
        
        #caja de texto 2
        
        boton2 = wx.Button(panel, label="Buscar", pos=(10, 150))
        
        self.textoDni2 = wx.StaticText(panel, pos = (36, 214), label = "Dni")
        
        self.campoDniA2 = wx.TextCtrl(panel, pos = (60,210), size = (64,20))
        self.campoDniA2.SetMaxLength(8)
        
        self.textoGuion2 = wx.StaticText(panel, pos = (132, 210), label = "-")
        
        self.campoDniB2 = wx.TextCtrl(panel, pos = (145,210), size = (20,20))
        self.campoDniB2.SetMaxLength(1)
        
        self.textoNombre2 = wx.StaticText(panel, pos = (10,182), label = "Nombre")
        
        self.campoNombre2 = wx.TextCtrl(panel, pos = (60,180), size = (105,20))
        
        #caja de texto 3
        
        boton3 = wx.Button(panel, label="Eliminar", pos=(10, 270))
        
        self.textoDni3 = wx.StaticText(panel, pos = (36, 334), label = "Dni")
        
        self.campoDniA3 = wx.TextCtrl(panel, pos = (60,330), size = (64,20))
        self.campoDniA3.SetMaxLength(8)
        
        self.textoGuion3 = wx.StaticText(panel, pos = (132, 330), label = "-")
        
        self.campoDniB3 = wx.TextCtrl(panel, pos = (145,330), size = (20,20))
        self.campoDniB3.SetMaxLength(1)
        
        self.textoNombre3 = wx.StaticText(panel, pos = (10,302), label = "Nombre")
        
        self.campoNombre3 = wx.TextCtrl(panel, pos = (60,300), size = (105,20))
        
        #caja de texto 4
        
        boton4 = wx.Button(panel, label="Actualizar", pos=(10, 390))
        
        self.textoDni4 = wx.StaticText(panel, pos = (36, 454), label = "Dni")
        
        self.campoDniA4 = wx.TextCtrl(panel, pos = (60,450), size = (64,20))
        self.campoDniA4.SetMaxLength(8)
        
        self.textoGuion4 = wx.StaticText(panel, pos = (132, 450), label = "-")
        
        self.campoDniB4 = wx.TextCtrl(panel, pos = (145,450), size = (20,20))
        self.campoDniB4.SetMaxLength(1)
        
        self.textoNombre4 = wx.StaticText(panel, pos = (10,422), label = "Nombre")
        
        self.campoNombre4 = wx.TextCtrl(panel, pos = (60,420), size = (105,20))
        
        #self.lista = wx.ListBox(panel,choices=listaInputsTxtCtrl,pos=(240,30))

        self.Bind(wx.EVT_BUTTON,self.ingresarJugador,boton1)
        self.Bind(wx.EVT_BUTTON,self.buscarJugador,boton2)
        self.Bind(wx.EVT_BUTTON,self.eliminarJugador,boton3)
        self.Bind(wx.EVT_BUTTON,self.actualizarJugador,boton4)
        self.Show()

    def ingresarJugador(self,event):
        '''
        :event: El parametro event liga esta funcion con la interaccion con boton1.
        '''
        
        infoNombre=str(self.campoNombre1.GetValue())
        infoDni=str(self.campoDniA1.GetValue())+"-"+str(self.campoDniB1.GetValue())
        if infoNombre != ("") and infoDni != ("-"):
            lis.ingresar(infoNombre, infoDni)
            print("Cliente Ingresado")
        else:
            print("Por Favor rellenar campo")
            
        lis.imprimir()
        self.campoNombre1.SetValue('')
        self.campoDniA1.SetValue('')
        self.campoDniB1.SetValue('')

    def buscarJugador(self,event):
        '''
        :event: El parametro event liga esta funcion con la interaccion con boton2.
        '''
        
        infoNombre=str(self.campoNombre2.GetValue())
        infoDni=str(self.campoDniA2.GetValue())+"-"+str(self.campoDniB2.GetValue())
        if infoNombre != ("") and infoDni != ("-"):
            if lis.buscar(infoNombre, infoDni) == False:
                pass
            else:
                indiceJugador=lis.buscar(infoNombre, infoDni)
        
        self.campoNombre2.SetValue('')
        self.campoDniA2.SetValue('')
        self.campoDniB2.SetValue('')

    def eliminarJugador(self,event):
        '''
        :event: El parametro event liga esta funcion con la interaccion con boton3.
        '''
        
        infoNombre=str(self.campoNombre3.GetValue())
        infoDni=str(self.campoDniA3.GetValue())+"-"+str(self.campoDniB3.GetValue())
        if infoNombre != ("") and infoDni != ("-"):
            lis.eliminar(infoNombre, infoDni)
        
        lis.imprimir()
        self.campoNombre3.SetValue('')
        self.campoDniA3.SetValue('')
        self.campoDniB3.SetValue('')
        
    def actualizarJugador(self,event):
        '''
        :event: El parametro event liga esta funcion con la interaccion con boton4.
        '''
        
        
        
        lis.imprimir()
        self.campoNombre4.SetValue('')
        self.campoDniA4.SetValue('')
        self.campoDniB4.SetValue('')
        