'''
Created on 18-06-2022

@author: Dell
'''

from model.claseNodo import Nodo

#clase jugador
class Jugador(Nodo):
    '''
    Esta es la clase del jugador.
    '''
    
    def __init__(self, siguiente=None, anterior=None, nombreJugador="nom", dniJugador="dni", puntuacion=0):
        '''
        :siguiente: Es la referencia al nodo siguiente en la lista doblemente enlazada.
        :anterior: Es la referencia al nodo anterior en la lista doblemente enlazada.
        :nombreJugador: Es el nombre del jugador.
        :dniJugador: Es el dni del jugador.
        :puntuacion: Es la puntuacion del jugador.
        '''
        super().__init__(siguiente=None,anterior=None)
        self.nombreJugador=nombreJugador
        self.dniJugador=dniJugador
        self.puntuacion=puntuacion
        
    def setNombreJugador(self,nombreJugador):
        '''
        :nombreJugador: Es el nombre nuevo del jugador.
        '''
        self.nombreJugador=nombreJugador
    
    def getNombreJugador(self):
        return self.nombreJugador
    
    def setDniJugador(self,dniJugador):
        '''
        :dniJugador: Es el dni nuevo del jugador.
        '''
        self.dniJugador=dniJugador
    
    def getDniJugador(self):
        return self.dniJugador
    
    def setPuntuacion(self,puntuacion):
        '''
        :puntuacion: Es la puntuacion nueva del jugador.
        '''
        self.puntuacion=puntuacion
    
    def getPuntuacion(self):
        return self.puntuacion