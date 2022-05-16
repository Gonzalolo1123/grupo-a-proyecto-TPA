'''
Created on 10 may. 2022

@author: david
'''
import wx

class botonesDificultad(wx.Frame):
    
    def __init__(self,parent,title):
        
        wx. Frame.__init__(self, parent,title=title, size=(300,250))
        self.boton1 = wx.Button(self, 0, u"Facil", size=(100, 50), pos=(100,10))
        self.boton2 = wx.Button(self, 0, u"Medio", size=(100, 50), pos=(100,70))
        self.boton3 = wx.Button(self, 0, u"Dificil", size=(100, 50), pos=(100,130))
        
        self.Centre(True)
        self.Show()
        
if __name__=='__main__':
    app = wx.App()
    fr = botonesDificultad(None, "Dificultad" )
    app. MainLoop()
    
#hygyuihg8yiu