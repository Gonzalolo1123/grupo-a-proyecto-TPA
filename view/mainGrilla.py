'''
Created on 16 may. 2022

@author: gonza
'''

import wx
from model.claseGrilla import TestFrame

if __name__=='__main__':
    app = wx.App()
    fr = TestFrame(None, "Test Grid")
    app.MainLoop()