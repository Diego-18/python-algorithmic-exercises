#!/usr/bin/env python
#-*- coding: UTF-8 -*-

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

import os
from collections import deque

#Funciones:

def fiLeerI(psTexto):
    liVarI=int(raw_input(psTexto))
    return liVarI

def fsLeerS(psTexto):
    lsVarS=raw_input(psTexto)
    return lsVarS

def fiMenu():
    print "1.Cargar"
    print "2.Atender"
    print "3.Imprimir"
    print "4.Salir"
    liOpcion=fiLeerI("Introduzca su opcion: ")
    return liOpcion

def fsContinuar():
    return fsLeerS("Presione ENTER para continuar")

def faCargar(paArreglo):
    os.system("cls")
    lsNombre=fsLeerS("Introduzca el nombre: ")
    paArreglo.append(lsNombre)
    fsContinuar()
    return paArreglo

def faSacar(paArreglo):
    os.system("cls")
    try:
        print paArreglo.popleft()
    except IndexError:
        print "La cola esta vacia"
    fsContinuar()

def faImprimir(paArreglo):
    os.system("cls")
    print paArreglo
    fsContinuar()

#Aplicacion:

laArreglo= deque([])
liOpcion=9
lsSeguir="s"
liacum=0

while (liOpcion!=0):
    liOpcion=fiMenu()

    if (liOpcion==1):
        faCargar(laArreglo)

    if (liOpcion==2):
        while(lsSeguir=="S") or (lsSeguir=="s"):
            os.system("cls")
            print faSacar(laArreglo)
            print "Que desea comprar?"
            print "1.Libreta: 200 bsF"
            print "2.Cuaderno: 130 bsF"
            liOpcion2=fiLeerI("Introduzca su Opcion: ")
            if (liOpcion2==1):
                os.system("cls")
                liNum=fiLeerI("Introduzca la cantidad de Libretas: ")
                liTotal=(liNum*200)
                liacum=liacum+liTotal
                fsContinuar()
            if (liOpcion2==2):
                os.system("cls")
                liNum=fiLeerI("Introduzca la cantidad de Cuadernos: ")
                liTotal=(liNum*130)
                liacum=liacum+liTotal
                fsContinuar()
            lsSeguir=fsLeerS("Desea hacer otra compra?: ")
                   
    if (liOpcion==3):
        print "El total a pagar en bsF es: ",liacum

    if (liOpcion==4):
        print "Adios"
        print "Gracias por su compra"
        print "Vuelva pronto!"
        
#UPTP S2-T1