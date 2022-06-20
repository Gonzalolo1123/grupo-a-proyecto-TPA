'''
Created on 10-05-2022

@author: gonza
'''
import wx
import wx.grid as wxgrid

filas = 4
columnas = 4



class TestFrame(wx.Frame):
    def __init__(self,parent,title):     
        frame=wx.Frame.__init__(self,parent=parent,title=title,size=(500,700))
        panel=wx.Panel(self,-1)
        self.grid = wxgrid.Grid(panel, -1,size=(1100,800))
        self.grid.CreateGrid(filas,columnas)
        self.grid.Position = (40,25)
        for i in range(0,columnas):
            for j in range(0,filas):
                img = wx.Bitmap("cartapatra.jpg", wx.BITMAP_TYPE_ANY)
                img = self.scale_bitmap(img, 100, 150)
                imageRenderer = MyImageRenderer(img)
                self.grid.SetCellRenderer(j,i, imageRenderer)
                self.grid.SetColSize(i, img.GetWidth() + 2)
                self.grid.SetRowSize(j, img.GetHeight() + 2)
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
