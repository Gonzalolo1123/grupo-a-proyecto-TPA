'''
Created on 18-06-2022

@author: Dell
'''

from model.claseNodo import Nodo

#clase jugador
class Jugador(Nodo):
    def __init__(self, siguiente=None, anterior=None, nombreJugador="nom", dniJugador="dni", puntuacion=0):
        super().__init__(siguiente=None,anterior=None)
        self.nombreJugador=nombreJugador
        self.dniJugador=dniJugador
        self.puntuacion=puntuacion
        
    def setNombreJugador(self,nombreJugador):
        self.nombreJugador=nombreJugador
    
    def getNombreJugador(self):
        return self.nombreJugador
    
    def setDniJugador(self,dniJugador):
        self.dniJugador=dniJugador
    
    def getDniJugador(self):
        return self.dniJugador
    
    def setPuntuacion(self,puntuacion):
        self.puntuacion=puntuacion
    
    def getPuntuacion(self):
        return self.puntuacion