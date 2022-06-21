'''
Created on 09-05-2022

@author: Dell
'''

import wx
from model.claseListaJugadores import ListaJugadores


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
        self.lis=ListaJugadores()
        
        # lista de jugadores
        
        self.listaJugadoresUI = wx.ListBox(panel, pos = (210,90), size = (300,400), choices = [])
        self.textoEstructuraLista = wx.StaticText(panel, pos = (210,62), label = "nombre del jugador / dni del jugador / puntuacion del jugador")
        botonActualizarListaJugadoresUI = wx.Button(panel, label = "Actualizar lista", pos = (210, 30))
        

        # boton 1
        
        boton1 = wx.Button(panel, label = "Ingresar Jugador", pos = (10, 30))
        
        # campo nombre 1
        
        self.textoNombre1 = wx.StaticText(panel, pos = (10,62), label = "Nombre")
        
        self.campoNombre1 = wx.TextCtrl(panel, pos = (60,60), size = (105,20))
        
        # campo dni 1
        
        self.textoDni1 = wx.StaticText(panel, pos = (36, 94), label = "Dni")
        
        self.campoDniA1 = wx.TextCtrl(panel, pos = (60,90), size = (64,20))
        self.campoDniA1.SetMaxLength(8)
        
        self.textoGuion1 = wx.StaticText(panel, pos = (132, 90), label = "-")
        
        self.campoDniB1 = wx.TextCtrl(panel, pos = (145,90), size = (20,20))
        self.campoDniB1.SetMaxLength(1)
        
        # boton 2
        
        boton2 = wx.Button(panel, label="Seleccionar Jugador", pos=(10, 150))
        
        # campo nombre 2
        
        self.textoNombre2 = wx.StaticText(panel, pos = (10,182), label = "Nombre")
        
        self.campoNombre2 = wx.TextCtrl(panel, pos = (60,180), size = (105,20))
        
        # campo dni 2
        
        self.textoDni2 = wx.StaticText(panel, pos = (36, 214), label = "Dni")
        
        self.campoDniA2 = wx.TextCtrl(panel, pos = (60,210), size = (64,20))
        self.campoDniA2.SetMaxLength(8)
        
        self.textoGuion2 = wx.StaticText(panel, pos = (132, 210), label = "-")
        
        self.campoDniB2 = wx.TextCtrl(panel, pos = (145,210), size = (20,20))
        self.campoDniB2.SetMaxLength(1)
        
        # boton 3
        
        boton3 = wx.Button(panel, label="Eliminar Jugador", pos=(10, 270))
        
        # campo nombre 3
        
        self.textoNombre3 = wx.StaticText(panel, pos = (10,302), label = "Nombre")
        
        self.campoNombre3 = wx.TextCtrl(panel, pos = (60,300), size = (105,20))
        
        # campo dni 3
        
        self.textoDni3 = wx.StaticText(panel, pos = (36, 334), label = "Dni")
        
        self.campoDniA3 = wx.TextCtrl(panel, pos = (60,330), size = (64,20))
        self.campoDniA3.SetMaxLength(8)
        
        self.textoGuion3 = wx.StaticText(panel, pos = (132, 330), label = "-")
        
        self.campoDniB3 = wx.TextCtrl(panel, pos = (145,330), size = (20,20))
        self.campoDniB3.SetMaxLength(1)
        
        # boton 4
        
        boton4 = wx.Button(panel, label="Actualizar Jugador", pos=(10, 390))
        
        # campo nombre 4
        
        self.textoNombre4 = wx.StaticText(panel, pos = (10,422), label = ("Nombre"+"\n"+"viejo"))
        
        self.campoNombre4 = wx.TextCtrl(panel, pos = (60,428), size = (105,20))
        
        # campo dni 4
        
        self.textoDni4 = wx.StaticText(panel, pos = (28, 460), label = ("Dni"+"\n"+"viejo"))
        
        self.campoDniA4 = wx.TextCtrl(panel, pos = (60,466), size = (64,20))
        self.campoDniA4.SetMaxLength(8)
        
        self.textoGuion4 = wx.StaticText(panel, pos = (132, 466), label = "-")
        
        self.campoDniB4 = wx.TextCtrl(panel, pos = (145,466), size = (20,20))
        self.campoDniB4.SetMaxLength(1)
        
        # nuevos datos
        # campo nombre 5
        
        self.textoNombre5 = wx.StaticText(panel, pos = (10,498), label = ("Nombre"+"\n"+"nuevo"))
        
        self.campoNombre5 = wx.TextCtrl(panel, pos = (60,504), size = (105,20))
        
        # campo dni 5
        
        self.textoDni5 = wx.StaticText(panel, pos = (22, 536), label = ("Dni"+"\n"+"nuevo"))
        
        self.campoDniA5 = wx.TextCtrl(panel, pos = (60,542), size = (64,20))
        self.campoDniA5.SetMaxLength(8)
        
        self.textoGuion5 = wx.StaticText(panel, pos = (132, 542), label = "-")
        
        self.campoDniB5 = wx.TextCtrl(panel, pos = (145,542), size = (20,20))
        self.campoDniB5.SetMaxLength(1)
        
        #self.lista = wx.ListBox(panel,choices=listaInputsTxtCtrl,pos=(240,30))

        self.Bind(wx.EVT_BUTTON,self.ingresarJugador,boton1)
        self.Bind(wx.EVT_BUTTON,self.seleccionarJugador,boton2)
        self.Bind(wx.EVT_BUTTON,self.eliminarJugador,boton3)
        self.Bind(wx.EVT_BUTTON,self.actualizarJugador,boton4)
        self.Bind(wx.EVT_BUTTON,self.actualizarListaJugadoresUI,botonActualizarListaJugadoresUI)
        self.Show()

    def ingresarJugador(self,event):
        '''
        :event: El parametro event liga esta funcion con la interaccion con boton1.
        '''
        
        infoNombre=str(self.campoNombre1.GetValue())
        infoDni=str(self.campoDniA1.GetValue())+"-"+str(self.campoDniB1.GetValue())
        if infoNombre != ("") and infoDni != ("-"):
            self.lis.ingresar(infoNombre, infoDni)
        else:
            pass
            
        self.lis.imprimir()
        self.campoNombre1.SetValue('')
        self.campoDniA1.SetValue('')
        self.campoDniB1.SetValue('')
        self.campoNombre2.SetValue('')
        self.campoDniA2.SetValue('')
        self.campoDniB2.SetValue('')
        self.campoNombre3.SetValue('')
        self.campoDniA3.SetValue('')
        self.campoDniB3.SetValue('')
        self.campoNombre4.SetValue('')
        self.campoDniA4.SetValue('')
        self.campoDniB4.SetValue('')
        self.campoNombre5.SetValue('')
        self.campoDniA5.SetValue('')
        self.campoDniB5.SetValue('')

    def seleccionarJugador(self,event):
        '''
        :event: El parametro event liga esta funcion con la interaccion con boton2.
        '''
        
        infoNombre=str(self.campoNombre2.GetValue())
        infoDni=str(self.campoDniA2.GetValue())+"-"+str(self.campoDniB2.GetValue())
        if infoNombre != ("") and infoDni != ("-"):
            if self.lis.buscar(infoNombre, infoDni) == False:
                pass
            else:
                indiceJugador=self.lis.buscar(infoNombre, infoDni)
        
        self.campoNombre1.SetValue('')
        self.campoDniA1.SetValue('')
        self.campoDniB1.SetValue('')
        self.campoNombre2.SetValue('')
        self.campoDniA2.SetValue('')
        self.campoDniB2.SetValue('')
        self.campoNombre3.SetValue('')
        self.campoDniA3.SetValue('')
        self.campoDniB3.SetValue('')
        self.campoNombre4.SetValue('')
        self.campoDniA4.SetValue('')
        self.campoDniB4.SetValue('')
        self.campoNombre5.SetValue('')
        self.campoDniA5.SetValue('')
        self.campoDniB5.SetValue('')

    def eliminarJugador(self,event):
        '''
        :event: El parametro event liga esta funcion con la interaccion con boton3.
        '''
        
        infoNombre=str(self.campoNombre3.GetValue())
        infoDni=str(self.campoDniA3.GetValue())+"-"+str(self.campoDniB3.GetValue())
        if infoNombre != ("") and infoDni != ("-"):
            if self.lis.buscar(infoNombre, infoDni) == False:
                pass
            else:
                self.lis.eliminar(infoNombre, infoDni)
        
        self.lis.imprimir()
        self.campoNombre1.SetValue('')
        self.campoDniA1.SetValue('')
        self.campoDniB1.SetValue('')
        self.campoNombre2.SetValue('')
        self.campoDniA2.SetValue('')
        self.campoDniB2.SetValue('')
        self.campoNombre3.SetValue('')
        self.campoDniA3.SetValue('')
        self.campoDniB3.SetValue('')
        self.campoNombre4.SetValue('')
        self.campoDniA4.SetValue('')
        self.campoDniB4.SetValue('')
        self.campoNombre5.SetValue('')
        self.campoDniA5.SetValue('')
        self.campoDniB5.SetValue('')
        
    def actualizarJugador(self,event):
        '''
        :event: El parametro event liga esta funcion con la interaccion con boton4.
        '''
        
        infoNombreViejo=str(self.campoNombre4.GetValue())
        infoDniViejo=str(self.campoDniA4.GetValue())+"-"+str(self.campoDniB4.GetValue())
        infoNombreNuevo=str(self.campoNombre5.GetValue())
        infoDniNuevo=str(self.campoDniA5.GetValue())+"-"+str(self.campoDniB5.GetValue())
        if infoNombreViejo != ("") and infoNombreViejo != ("-"):
            if infoNombreNuevo != ("") and infoDniNuevo != ("-"):
                if self.lis.buscar(infoNombreViejo, infoDniViejo) == False:
                    pass
                else:
                    indiceJugadorViejo=self.lis.buscar(infoNombreViejo, infoDniViejo)
                    self.lis.actualizar(indiceJugadorViejo, infoNombreNuevo, infoDniNuevo)
            else:
                pass
        else:
            pass
        
        self.lis.imprimir()
        self.campoNombre1.SetValue('')
        self.campoDniA1.SetValue('')
        self.campoDniB1.SetValue('')
        self.campoNombre2.SetValue('')
        self.campoDniA2.SetValue('')
        self.campoDniB2.SetValue('')
        self.campoNombre3.SetValue('')
        self.campoDniA3.SetValue('')
        self.campoDniB3.SetValue('')
        self.campoNombre4.SetValue('')
        self.campoDniA4.SetValue('')
        self.campoDniB4.SetValue('')
        self.campoNombre5.SetValue('')
        self.campoDniA5.SetValue('')
        self.campoDniB5.SetValue('')
        
    def actualizarListaJugadoresUI(self,event):
        '''
        :event: El parametro event liga esta funcion con la interaccion con botonActualizarListaJugadoresUI.
        '''
        
        self.listaJugadoresUI.Clear()
        self.lis.actualizarListaDatos()
        self.lisDatos=self.lis.getListaJugadoresDatos()
        conAgregarDatos=len(self.lisDatos)
        for u in range(0,conAgregarDatos,1):
            datoDeLista=self.lisDatos[u]
            self.listaJugadoresUI.Append(datoDeLista)
        