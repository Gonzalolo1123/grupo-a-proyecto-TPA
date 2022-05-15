'''
Created on 10-05-2022

@author: gonza
'''
import wx
import wx.grid as wxgrid
from random import randint
filas = 4
columnas = 4

class TestFrame(wx.Frame):
    def __init__(self,title):
            wx.Frame.__init__(self,title=title)
            self.grid = wxgrid.Grid(self, -1)
            self.grid.CreateGrid(filas,columnas)
            self.grid.SetRowLabelSize(0)


        # Modificando los encabezados y anchos de columna
            anchos = [100, 100,100,100]
            encabezados = ["", "","",""]
            for n, col in enumerate(range(columnas)):
                self.grid.SetColLabelValue(col, encabezados[n])
                self.grid.SetColSize(col, anchos[n])

                self.Centre(True)
                self.Show()

if __name__=='__main__':
    app = wx.App()
    fr = TestFrame(None, "Test Grid")
    app.MainLoop()