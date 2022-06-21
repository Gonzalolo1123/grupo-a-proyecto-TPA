'''
Created on 09-05-2022

@author: david
'''

import wx
from model.clasebD import Button
def main(): 
    app = wx.App() 
    ex = Button(None) 
    ex.Show() 
    app.MainLoop() 
  
  
if __name__ == '__main__': 
    main() 
