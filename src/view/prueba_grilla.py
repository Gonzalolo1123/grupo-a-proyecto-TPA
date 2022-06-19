'''
Created on 18-06-2022

@author: gonza
'''
#en este archivo lo que estoy intentando es hacer funcionar el click para agregar una imagen en la casilla que se seleccione
#si logramos eso estamos al otro lado 
import wx
import wx.grid as wxgrid
import random
filas = 4
columnas = 4
tamaño= (1100,800)
class TestFrame(wx.Frame):
    def __init__(self,parent,title):
            '''
            :parent:
            :title:
            '''
            frame=wx.Frame.__init__(self,parent=parent,title=title,size=tamaño)
            panel=wx.Panel(self,-1)
            self.grid = wxgrid.Grid(panel, -1,size=tamaño)
            self.grid.CreateGrid(filas,columnas)
            matrizaux = []
            res = random.sample(range(1, 32), 8)
            res.extend(res)
            random.shuffle(res)
            matrizaux.append(res)
            self.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK,self.click())
            for c in matrizaux[0]:
                img = wx.Bitmap("cardsColors/" + str(c) + ".jpg", wx.BITMAP_TYPE_ANY)
                img = self.scale_bitmap(img, 100, 150)
                self.imageRenderer = MyImageRenderer(img)

            self.Centre(True)
            self.Show()
            self.grid.SetRowLabelSize(0)
            self.grid.SetColLabelSize(0)

    def click(self, event):
        col=event.GetColPos
        self.grid.SetCellRenderer(col, 1, self.imageRenderer)
        self.grid.SetColSize(1, img.GetWidth() + 2)
        self.grid.SetRowSize(col, img.GetHeight() + 2)
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
