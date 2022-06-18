'''
Created on 18-06-2022

@author: Dell
'''

#clase nodos
class Nodo:
    def __init__(self,siguiente=None,anterior=None):
        self.siguiente=siguiente
        self.anterior=anterior
        
    def setSiguiente(self,siguiente):
        self.siguiente=siguiente
        
    def getSiguiente(self):
        return self.siguiente
        
    def setAnterior(self,anterior):
        self.anterior=anterior
        
    def getAnterior(self):
        return self.anterior