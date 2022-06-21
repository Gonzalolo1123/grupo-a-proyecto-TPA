'''
Created on 09-05-2022

@author: Dell
'''
from model.claseListaJugadores import ListaJugadores

class manejoUsuarios:
    
    def __init__(self):
        pass
    
    def guardarUsuarios(self,listaDatosGuardar):
        archivo=open("usuariosGuardados.txt","w")
        for k in range(0,len(listaDatosGuardar),1):
            archivo.write(listaDatosGuardar[k]+"\n")
        archivo.close()
        
    def recuperarUsuarios(self):
        listaRecuperada=ListaJugadores()
        archivo=open("usuariosGuardados.txt","r")
        while True:
            linea=archivo.readline()
            if linea=="":
                break
            
            lineaNueva1=linea.split(".-")
            lineaNueva2=lineaNueva1.pop(-1)
            lineaNueva3=lineaNueva2.split("\n")
            lineaNueva4=lineaNueva3.pop(0)
            datosJugadorRecuperados=lineaNueva4.split("/")
            
            listaRecuperada.ingresar(datosJugadorRecuperados[0], datosJugadorRecuperados[1])
            
            indiceJugadorRecuperado=listaRecuperada.buscar(datosJugadorRecuperados[0], datosJugadorRecuperados[1])
            
            listaRecuperada.actualizarPuntuacion(indiceJugadorRecuperado,datosJugadorRecuperados[2])
        archivo.close()
        return listaRecuperada

listaTest=["1.-sergio/2020-1/666","2.-nacho/2121-2/222","3.-robertito/80080012-5/0"]
a=manejoUsuarios()
a.guardarUsuarios(listaTest)
print("espacio")
a.recuperarUsuarios()