'''
Created on 18-06-2022

@author: Dell
'''

#clase nodos
class Nodo:
    '''
    Esta es la clase de los nodos.
    '''
    def __init__(self,siguiente=None,anterior=None):
        '''
        :siguiente: Es la referencia al nodo siguiente en la lista doblemente enlazada.
        :anterior: Es la referencia al nodo anterior en la lista doblemente enlazada.
        '''
        self.siguiente=siguiente
        self.anterior=anterior
        
    def setSiguiente(self,siguiente):
        '''
        :siguiente: Es la referencia nueva al nodo siguiente en la lista doblemente enlazada.
        '''
        self.siguiente=siguiente
        
    def getSiguiente(self):
        return self.siguiente
        
    def setAnterior(self,anterior):
        '''
        :anterior: Es la referencia nueva al nodo anterior en la lista doblemente enlazada.
        '''
        self.anterior=anterior
        
    def getAnterior(self):
        return self.anterior