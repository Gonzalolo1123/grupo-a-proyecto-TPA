'''
Created on 2 jun. 2022

@author: david
'''
import wx

class Button(wx.Frame): 
    '''
    Esta es la clase de los botones de dificultad
    '''
  
    def __init__(self, *args, **kwargs):

        
        '''
        :args: permiten pasar un numero variable de argumentos a una funcion.
        :kwargs: permite pasar argumentos de longitud variable asociados con un nombre.
        '''
  
        super(Button, self).__init__(*args, **kwargs) 
        self.InitUI() 
        

    def InitUI(self): 
        self.pnl = wx.Panel(self) 
  
        self.st = wx.Button(self.pnl, id = 1, label ="Jugar", pos =(120, 70), 
                                          size =(300, 40),  name ="Vamo a juga") 
        self.st.SetSize((100, 50)) 
  
        self.SetSize((350, 250)) 
        self.SetTitle('Inicio') 
        self.Centre() 
  
