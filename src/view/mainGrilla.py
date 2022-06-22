import wx
import wx.grid as wxgrid
import random

filas = 4
columnas = 4


def scale_bitmap(bitmap, width, height):
    image = wx.ImageFromBitmap(bitmap)
    image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
    result = wx.BitmapFromImage(image)
    return result


class TestFrame(wx.Frame):
    def __init__(self, parent, title):
        '''
        :parent:
        :title:
        '''
        self.click1 = []
        self.click2 = []
        self.fil = None
        self.col = None
        self.cont = 0
        self.matrizaux = []
        res = random.sample(range(1, 32), 8)
        res.extend(res)
        random.shuffle(res)
        self.matrizaux.append(res)
        self.M = [self.matrizaux[0][columnas * i: columnas * (i + 1)] for i in range(filas)]

        frame = wx.Frame.__init__(self, parent=parent, title=title, size=(500,700))
        panel = wx.Panel(self, -1)
        grid = wxgrid.Grid(panel, -1, size=(500, 700))
        grid.CreateGrid(filas, columnas)
        self.grid = wxgrid.Grid(panel, -1, size=(500, 700))
        self.grid.CreateGrid(filas, columnas)
        grid.Position = (40, 25)
        self.grid.Position= (40,25)

        # Grilla 1
        for i in range(0, columnas):
            for j in range(0, filas):
                img1 = wx.Bitmap("backCard.jpg", wx.BITMAP_TYPE_ANY)
                img1 = scale_bitmap(img1, 100, 150)
                self.imageRenderer1 = MyImageRenderer(img1)
                self.grid.SetCellRenderer(j, i, self.imageRenderer1)
                self.grid.SetColSize(i, img1.GetWidth() + 2)
                self.grid.SetRowSize(j, img1.GetHeight() + 2)
        # Grilla 2
        c = 0
        for f in range(0, filas):
            for a in range(0, columnas):
                if c <= 3:
                    img2 = wx.Bitmap("cardsColors/" + str(self.matrizaux[0][c]) + ".jpg", wx.BITMAP_TYPE_ANY)
                    img2 = scale_bitmap(img2, 100, 150)
                    b = 0
                if 7 >= c >= 4:
                    img2 = wx.Bitmap("cardsColors/" + str(self.matrizaux[0][c]) + ".jpg", wx.BITMAP_TYPE_ANY)
                    img2 = scale_bitmap(img2, 100, 150)
                    b = 1
                if 11 >= c >= 8:
                    img2 = wx.Bitmap("cardsColors/" + str(self.matrizaux[0][c]) + ".jpg", wx.BITMAP_TYPE_ANY)
                    img2 = scale_bitmap(img2, 100, 150)
                    b = 2
                if 15 >= c >= 12:
                    img2 = wx.Bitmap("cardsColors/" + str(self.matrizaux[0][c]) + ".jpg", wx.BITMAP_TYPE_ANY)
                    img2 = scale_bitmap(img2, 100, 150)
                    b = 3
                c += 1
                imageRenderer2 = MyImageRenderer(img2)
                grid.SetCellRenderer(b, a, imageRenderer2)
                grid.SetColSize(a, img2.GetWidth() + 2)
                grid.SetRowSize(b, img2.GetHeight() + 2)

            self.Bind(wxgrid.EVT_GRID_CELL_LEFT_CLICK, self.click)
            self.Centre(True)
            self.Show()
            self.grid.SetRowLabelSize(0)
            self.grid.SetColLabelSize(0)
            grid.SetRowLabelSize(0)
            grid.SetColLabelSize(0)
            self.grid.EnableEditing(False)
            grid.EnableEditing(False)
        print(self.M)
    def click(self, event):
        self.col = event.GetCol()
        self.fil = event.GetRow()
        self.cont += 1
        if self.cont == 1:
            self.click1.append(self.fil)
            self.click1.append(self.col)


        if self.cont == 2:
            self.click2.append(self.fil)
            self.click2.append(self.col)
            self.cont = 0
            if self.click1==self.click2:
                self.cont=0
                self.click1 = []
                self.click2 = []
            else:
                # COMPARACION POSICIONES CLICK

                if self.M[self.click1[0]][self.click1[1]] == self.M[self.click2[0]][self.click2[1]]:
                    print("iguales")
                else:
                    print("diferentes")
                    # self.grid.ClearGrid()
                # FIN POSICIONES CLICK

            self.click1 = []
            self.click2 = []

class MyImageRenderer(wxgrid.GridCellRenderer):
    def __init__(self, img):
        wxgrid.GridCellRenderer.__init__(self)
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
        if width > rect.width - 2:
            width = rect.width - 2
        if height > rect.height - 2:
            height = rect.height - 2
        dc.Blit(rect.x + 1, rect.y + 1, width, height, image, 0, 0, wx.COPY, True)


if __name__ == '__main__':
    app = wx.App()
    fr = TestFrame(None, "Test Grid")
    fr.Show()
    app.MainLoop()
