import wx
from model.claseGrilla import TestFrame
if __name__ == '__main__':
    app = wx.App()
    fr = TestFrame(None, "Test Grid")
    fr.Show()
    app.MainLoop()
