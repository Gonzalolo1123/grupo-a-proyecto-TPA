'''
Created on 09-05-2022

@author: Dell
'''

import wx

from model.claseUI import InterfazGrafica

if __name__ == '__mainUI__':
    app=wx.App()
    ventana=InterfazGrafica(None,-1)
    app.MainLoop()