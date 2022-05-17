'''
Created on 10-05-2022

@author: gonza
'''
import wx.grid 
filas = 5
columnas = 2
dsa=columnas*filas
class TestFrame(wx.Frame):
    def __init__(self,parent,title):
            fr=wx.Frame.__init__(self,parent=parent,title=title,size=(1100,800))
            panel=wx.Panel(self,-1)
            self.grid = wx.grid.Grid(panel, -1,size=(1100,800))
            self.grid.CreateGrid(filas,columnas)

            contFilas = 0
            #Ciclo imagenes en grilla
            for i in range(0,dsa,1):
                img = wx.Bitmap("Sin_carta.jpg", wx.BITMAP_TYPE_ANY)
                img = self.scale_bitmap(img, 100, 150)
                imageRenderer = MyImageRenderer(img)
                if contFilas<filas:
                    self.grid.SetCellRenderer(contFilas,i%columnas, imageRenderer)
                    self.grid.SetColSize(i%columnas, img.GetWidth() + 2)
                    self.grid.SetRowSize(contFilas, img.GetHeight() + 2)
                    if i==columnas:
                        contFilas=+1
            self.Centre(True)
            self.Show()
            self.grid.SetRowLabelSize(0)
            self.grid.SetColLabelSize(0)
    def scale_bitmap(self,bitmap, width, height):
        image = wx.ImageFromBitmap(bitmap)
        image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
        result = wx.BitmapFromImage(image)
        return result

class MyImageRenderer(wx.grid.GridCellRenderer):
    def __init__(self, img):
        wx.grid.GridCellRenderer.__init__(self)
        self.img = img
    def Draw(self, grid, attr, dc, rect, row, col, isSelected):
        image = wx.MemoryDC()
        image.SelectObject(self.img)
        dc.SetBackgroundMode(wx.SOLID)
        if isSelected:
            dc.SetBrush(wx.Brush(wx.BLUE, wx.SOLID))
            dc.SetPen(wx.Pen(wx.BLUE, 1, wx.SOLID))
        else:
            dc.SetBrush(wx.Brush(wx.WHITE, wx.SOLID))
            dc.SetPen(wx.Pen(wx.WHITE, 1, wx.SOLID))
        dc.DrawRectangle(rect)
        width, height = self.img.GetWidth(), self.img.GetHeight()
        if width > rect.width-2:
            width = rect.width-2
        if height > rect.height-2:
            height = rect.height-2
        dc.Blit(rect.x+1, rect.y+1, width, height, image, 0, 0, wx.COPY, True)

if __name__=='__main__':
    app = wx.App()
    fr = TestFrame(None, "Test Grid")
    fr.Show()
    app.MainLoop()
