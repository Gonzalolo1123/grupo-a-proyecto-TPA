'''
Created on 09-05-2022

@author: Dell
'''

import wx

from model.claseUI import InterfazGrafica

if __name__ == '__main__':
    app=wx.App()
    ventana=InterfazGrafica(None,-1)
    app.MainLoop()