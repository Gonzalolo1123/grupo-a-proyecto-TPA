'''
Created on 2 jun. 2022

@author: david
'''
import wx

class botonesDificultad(wx.Frame):
    '''
    Esta es la clase de los botones de dificultad
    '''
    def __init__(self,parent,title):
        '''
        :parent: Es el padre de la ventana.
        :title: Es el nombre de la ventana.
        '''
        
        wx. Frame.__init__(self, parent,title=title, size=(300,250))
        self.boton1 = wx.Button(self, 0, "Facil", size=(100, 50), pos=(100,10))
        self.boton2 = wx.Button(self, 0, "Medio", size=(100, 50), pos=(100,70))
        self.boton3 = wx.Button(self, 0, "Dificil", size=(100, 50), pos=(100,130))

        self.Centre(True)
        self.Show()