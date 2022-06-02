'''
Created on 09-05-2022

@author: david
'''

import wx
from model.clasebD import botonesDificultad

if __name__=='__main__':
    app = wx.App()
    fr = botonesDificultad(None, "Dificultad" )
    app. MainLoop()