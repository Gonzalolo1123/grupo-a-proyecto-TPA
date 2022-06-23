'''
Created on 2 jun. 2022

@author: david
'''
import wx
from view import mainGrilla
from controller.controller import controller
class Button(wx.Frame): 
    '''
    Esta es la clase de los botones de dificultad
    '''
  
    def __init__(self, *args, **kwargs):

        self.grilla=Grilla
        '''
        :args: permiten pasar un numero variable de argumentos a una funcion.
        :kwargs: permite pasar argumentos de longitud variable asociados con un nombre.
        '''
  
        super(Button, self).__init__(*args, **kwargs) 
        self.InitUI() 
        
    def InitUI(self): 
        colorBackGround=wx.Colour(127, 179, 213)
        self.pnl = wx.Panel(self) 
  
        self.st = wx.Button(self.pnl, id = 1, label ="Jugar", pos =(170, 50),  name ="jugar") 
        self.st.SetSize((150, 75)) 
        self.st2 = wx.Button(self.pnl, id = 2, label ="Usuarios", pos =(170,150),  name ="usu") 
        self.st2.SetSize((150, 75)) 

        self.SetBackgroundColour(colorBackGround)
        self.SetSize((500, 320)) 
        self.SetTitle('Inicio') 
        self.Centre()
         
