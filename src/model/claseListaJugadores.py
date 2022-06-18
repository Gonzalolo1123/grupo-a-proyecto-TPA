'''
Created on 18-06-2022

@author: Dell
'''

from model.claseNodo import Nodo

#clase lista de jugadores
class ListaJugadores: 
    def __init__(self): 
        cabeza=Nodo() 
        cola=Nodo() 
        cabeza.setSiguiente(cola) 
        cola.setAnterior(cabeza) 
        self.listaJugadores=[cabeza, cola]
        
    def getLen(self):
        return len(self.listaJugadores)
 
    def esVacia(self): 
        if self.listaJugadores[0].getSiguiente() == self.listaJugadores[-1]: 
            return True 
        else: 
            return False 

    def vaciar(self):
        if self.listaJugadores.esVacia == True: 
            return False 
        else:
            lenNumMenosUno=self.getLen()-1
            for l in range(lenNumMenosUno,0,-1):
                self.listaJugadores.eliminar(self.listaJugadores[l].getDniJugador())

    def getCabeza(self): 
        return self.listaJugadores[0] 
 
    def getPrimero(self): 
        if self.esVacia == True: 
            return False 
        else: 
            return self.listaJugadores[1] 

    def ingresar(self,objJugador): 
        if self.buscar(objJugador.getDniJugador) == True: 
            return False 
        else: 
            lenNumMenosUno=self.getLen()-1
            self.listaJugadores.append(self.listaJugadores[lenNumMenosUno])

            self.listaJugadores[lenNumMenosUno]=objJugador
            self.listaJugadores[lenNumMenosUno].setAnterior(self.listaJugadores[lenNumMenosUno-1])
            self.listaJugadores[lenNumMenosUno].setSiguiente(self.listaJugadores[lenNumMenosUno+1])

            self.listaJugadores[lenNumMenosUno+1].setAnterior(self.listaJugadores[lenNumMenosUno])
            self.listaJugadores[lenNumMenosUno-1].setSiguiente(self.listaJugadores[lenNumMenosUno])
             
    def imprimir(self): 
        if self.esVacia == True: 
            return False 
        else:
            lenNumMenosUno=self.getLen()-1
            for g in range(1,lenNumMenosUno,1):
                infoDni=self.listaJugadores[g].getDniJugador()
                infoNombre=self.listaJugadores[g].getNombreJugador()
                infoPuntos=self.listaJugadores[g].getPuntuacion()
                infoJugador=str(g)+".-"+str(infoDni)+"-"+str(infoNombre)+"-"+str(infoPuntos)
                print(infoJugador)
 
    def buscar(self,dniJugador): 
        if self.esVacia == True: 
            return False 
        else: 
            lenNumMenosUno=self.getLen()-1
            for p in range(1,lenNumMenosUno,1): 
                dniCheck=self.listaJugadores[p].getDniJugador() 
                if dniCheck == dniJugador: 
                    return p 

    def buscarPrevio(self,dniJugador): 
        if self.esVacia == True: 
            return False 
        else: 
            for h in range(0,len(self.listaJugadores),1): 
                dniCheck=self.listaJugadores[h].getDniJugador() 
                if dniCheck == dniJugador: 
                    return h-1 

    def eliminar(self, dniJugador): 
        if self.buscar(dniJugador) == False: 
            return False 
        else:
            indiceElementoEliminar=self.listaJugadores.buscar(dniJugador)
            self.listaJugadores[indiceElementoEliminar-1].setSiguiente(self.listaJugadores[indiceElementoEliminar+1])
            self.listaJugadores[indiceElementoEliminar+1].setAnterior(self.listaJugadores[indiceElementoEliminar-1])
            self.listaJugadores.pop[indiceElementoEliminar]