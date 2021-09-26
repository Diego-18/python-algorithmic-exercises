#!/usr/bin/env python
#-*- coding: UTF-8 -*-
import os
from collections import deque

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#Algoritmo que permita registrar el nombre del paciente y la cantidad a pagar

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
    lsNombre=fsCadena("Introduzca el nombre del paciente: ")
    paArreglo.append(lsNombre)
    fsContinuar()
    return paArreglo

def faCargarP(paArreglo2):
    os.system("cls")
    lsRegalo=fsCadena("Introduzca el regalo: ")
    paArreglo2.append(lsRegalo)
    fsContinuar()
    return paArreglo2

def faSacar(paArreglo, paArreglo2):
    os.system("cls")
    print paArreglo.popleft()
    liEdad=fiEntero("Introduzca su edad: ")
    lfConsulta=600

    if (liEdad<=15):
        liDescuento=0.30
        
    if (liEdad>15) or (liEdad<50):
        liDescuento=0.10

    if (liEdad>=50):
        liDescuento=0.50
        
    lfTotal=(lfConsulta-liDescuento)

    print "El monto total a pagar es: ",lfTotal
    print "Usted se ha gannado un regalo"
    print paArreglo2.pop()
    fsContinuar()

def faImprimir(paArreglo):
    os.system("cls")
    for lsX in paArreglo in range [0,4]:
        print lsX

def fiMenu():
    os.system("cls")
    print "1.Introduzca la Cola"
    print "2.Introduzca la Pila"
    print "3.Imprima los 5 primeros de la cola"
    print "4.Atender"
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
        faImprimir(laArreglo)

    if (liOpcion==4):
        faSacar(laArreglo, laArreglo2)

    if (liOpcion==0):
        print "Adios"
        print "Que se mejore pronto"
        fsContinuar()

#UPTP S2-T1