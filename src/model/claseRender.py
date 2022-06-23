'''
Created on 22-06-2022

@author: Dell
'''

import wx
import wx.grid as wxgrid

def scale_bitmap(bitmap, width, height):
    '''
    :bitmap: Es el mapa de bits que conforma la carta.
    :width: Es el grosor de la carta.
    :height: Es la altura de la carta.
    '''
    image = wx.ImageFromBitmap(bitmap)
    image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
    result = wx.BitmapFromImage(image)
    return result

class MyImageRenderer(wxgrid.GridCellRenderer):
    '''
    Es la clase
    '''
    def __init__(self, img):
        '''
        :img: Es la imagen.
        '''
        wxgrid.GridCellRenderer.__init__(self)
        self.img = img

    def Draw(self, grid, attr, dc, rect, row, col, isSelected):
        '''
        :grid: Es.
        :attr: Es.
        :dc: Es.
        :rect: Es.
        :row: Es.
        :col: Es.
        :isSelected: Es.
        '''
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
        if width > rect.width - 2:
            width = rect.width - 2
        if height > rect.height - 2:
            height = rect.height - 2
        dc.Blit(rect.x + 1, rect.y + 1, width, height, image, 0, 0, wx.COPY, True)