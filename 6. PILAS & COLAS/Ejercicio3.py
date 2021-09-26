#!/usr/bin/env python
#-*- coding: UTF-8 -*-
import os
from collections import deque

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#Pila

#Funciones:

def fiEntero(psTexto):
    liVarI=int(raw_input(psTexto))
    return liVarI

def fsCadena(psTexto):
    lsVarS=raw_input(psTexto)
    return lsVarS

def fsContinuar():
    return fsCadena("Presione ENTER para continuar")

def faCargarC(paArreglo):
    os.system("cls")
    lsNombre=fsCadena("Introduzca el nombre: ")
    paArreglo.append(lsNombre)
    return paArreglo

def faCargarP(paArreglo2):
    os.system("cls")
    lsColor=fsCadena("Introduzca el color: ")
    paArreglo2.append(lsColor)
    return paArreglo2

def faSacar(paArreglo, paArreglo2):
    os.system("cls")

    print paArreglo.popleft()

    print "1.Combo1, 2.Combo2, 3.Combo3"
    liOpcion=fiEntero("Introduzca la Opcion: ")
    liCantidad=fiEntero("Cuantos desea llevar?: ")

    if (liOpcion==1):
        liCombo=200
        
    if (liOpcion==2):
        liCombo=300

    if (liOpcion==3):
        liCombo=400

    lsColor=paArreglo2.pop()
    print lsColor
    if (lsColor=="Blanco"):
        liDescuento=0

    if (lsColor=="Azul"):
        lfDescuento=0.10

    if (lsColor=="Morado"):
        lfDescuento=0.20
        
    lfDescuentoT=(liCantidad*liCombo*lfDescuento)
    lfTotal=(liCantidad*liCombo)-lfDescuentoT
    print "El monto total a pagar es: ",lfTotal


def fiMenu():
    os.system("cls")
    print "1.Introduzca la Cola"
    print "2.Introduzca la Pila"
    print "3.Atender"
    print "0.Salir del Sistema"
    liOpcion=fiEntero("Introduzca la Opcion: ")
    return liOpcion

#Programa:

liOpcion=9
laArreglo=deque([])
laArreglo2=deque([])

while (liOpcion!=0):
    liOpcion=fiMenu()
    
    if (liOpcion==1):
        faCargarC(laArreglo)

    if (liOpcion==2):
        faCargarP(laArreglo2)

    if (liOpcion==3):
        faSacar(laArreglo,laArreglo2)

    if (liOpcion==0):
        print "Adios"
 

#UPTP S2-T1