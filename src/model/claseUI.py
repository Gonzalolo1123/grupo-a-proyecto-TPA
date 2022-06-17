'''
Created on 09-05-2022

@author: Dell
'''

import wx

listaInputsTxtCtrl=[]


class InterfazGrafica(wx.Frame):  
    '''
    Esta clase es la interfaz grafica
    '''
    def __init__(self, parent, id):
        
        '''
        :parent: Es el padre de la ventana.
        :id: Es el identificador de la ventana. Puede tomar un valor de -1 para indicar un valor predeterminado.
        '''
        
        wx.Frame.__init__(self, parent, id, "Jugadores")
        panel = wx.Panel(self)

        #caja de texto 1
        boton1 = wx.Button(panel, label = "Ingresar", pos = (200, 30))
        self.dlg1 = wx.TextCtrl(panel, pos = (10,30))
        self.dlg1_1 = wx.TextCtrl(panel, pos = (145,30), size = (40,20))
        self.dlg1_2 = wx.StaticText(panel, pos = (130, 30), label = "-")
        self.dlg1.SetMaxLength(8)
        self.dlg1_1.SetMaxLength(1)
        
        #caja de texto 2
        boton2 = wx.Button(panel, label="Buscar", pos=(200, 60))
        self.dlg2=wx.TextCtrl(panel,pos=(10,60))
        self.dlg2_1 = wx.TextCtrl(panel, pos=(145,60),size=(40,20))
        self.dlg2_2 = wx.StaticText(panel, pos=(130, 60), label="-")
        self.dlg2.SetMaxLength(8)
        self.dlg2_1.SetMaxLength(1)

        
        #caja de texto 3
        boton3 = wx.Button(panel, label="Eliminar", pos=(200, 90))
        self.dlg3=wx.TextCtrl(panel,pos=(10,90))
        self.dlg3_1 = wx.TextCtrl(panel, pos=(145,90),size=(40,20))
        self.dlg3_2 = wx.StaticText(panel, pos=(130, 90), label="-")
        self.dlg3.SetMaxLength(8)
        self.dlg3_1.SetMaxLength(1)
        
        #caja de texto 4
        boton4 = wx.Button(panel, label="Actualizar", pos=(200, 120))
        self.dlg4=wx.TextCtrl(panel,pos=(10,120))
        self.dlg4_1 = wx.TextCtrl(panel, pos=(145,120),size=(40,20))
        self.dlg4_2 = wx.StaticText(panel, pos=(130, 120), label="-")
        self.dlg4.SetMaxLength(8)
        self.dlg4_1.SetMaxLength(1)
        
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
        '''
        :event: El parametro event liga esta funcion con la interaccion con boton2.
        '''
        
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
        '''
        :event: El parametro event liga esta funcion con la interaccion con boton3.
        '''
        
        dniCli3 = str(self.dlg3.GetValue())+"-"+str(self.dlg3_1.GetValue())
        for i in range(0, len(listaInputsTxtCtrl),1):
            if dniCli3 == listaInputsTxtCtrl[i]:
                listaInputsTxtCtrl.pop(i)
        print("Cliente Eliminado Exitosamente")
        self.dlg3.SetValue('')
        self.dlg3_1.SetValue('')
        print(listaInputsTxtCtrl)
        
    def actualizarCliente(self,event):
        '''
        :event: El parametro event liga esta funcion con la interaccion con boton4.
        '''
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

#clase nodos
class Nodos:
    def __init__(self,siguiente,anterior):
        self.siguiente=siguiente
        self.anterior=anterior
        
    def setSiguiente(self,siguiente):
        self.siguiente=siguiente
        
    def getSiguiente(self):
        return self.siguiente
        
    def setAnterior(self,anterior):
        self.anterior=anterior
        
    def getAnterior(self):
        return self.anterior

#clase jugador
class Jugador(Nodos):
    def __init__(self, siguiente, anterior, nombreJugador, dniJugador, puntuacion=0):
        super().__init__(siguiente,anterior)
        self.nombreJugador=nombreJugador
        self.dniJugador=dniJugador
        self.puntuacion=puntuacion
        
    def setNombreJugador(self,nombreJugador):
        self.nombreJugador=nombreJugador
    
    def getNombreJugador(self):
        return self.nombreJugador
    
    def setDniJugador(self,dniJugador):
        self.dniJugador=dniJugador
    
    def getDniJugador(self):
        return self.dniJugador
    
    def setPuntuacion(self,puntuacion):
        self.puntuacion=puntuacion
    
    def getPuntuacion(self):
        return self.puntuacion


#clase lista de jugadores
class ListaJugadores:
    def __init__(self):
        self.listaJugadores=[]
    
    def esVacia(self):
        pass
    
    def vaciar(self):
        for k in range(len(self.listaJugadores),-1,-1):
            self.listaJugadores.pop(k)
    
    def getCabeza(self):
        pass
    
    def getPrimero(self):
        pass
    
    def ingresar(self,jugadorIngresar,jugadorAnterior):
        pass
    
    def imprimir(self):
        pass
    
    def buscar(self,posicionJugador):
        pass
    
    def buscarPrevio(self,posicionJugadorAnterior):
        pass
    
    def eliminar(self):
        pass
    