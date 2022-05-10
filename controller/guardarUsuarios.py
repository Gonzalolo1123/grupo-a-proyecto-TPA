'''
Created on 09-05-2022

@author: Dell
'''

from model.claseUI import listaInputsTxtCtrl

usuariosGuardados=open("usuariosGuardados.txt","w")

for i in range(0,len(listaInputsTxtCtrl),1):
    usuariosGuardados.write(listaInputsTxtCtrl[i]+"\n")

usuariosGuardados.close()
