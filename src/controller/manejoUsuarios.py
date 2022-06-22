'''
Created on 09-05-2022

@author: Dell
'''

# sod

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