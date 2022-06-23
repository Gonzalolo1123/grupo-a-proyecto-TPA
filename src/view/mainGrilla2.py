'''
Created on 26-04-2022

@author: gonza
'''
import wx
from model.claseGrilla2 import TestFrame
if __name__ == '__main__':
    app = wx.App()
    fr = TestFrame(None, "Test Grid")
    fr.Show()
    app.MainLoop()