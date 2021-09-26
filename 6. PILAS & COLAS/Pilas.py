#!/usr/bin/env python
# -*- coding: utf-8 -*-

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#Algoritmo que permita Cargar, Sacar, Imprimir, Buscar un integrante de la Pila

import os

#Funciones
def fsLeerS(psTexto):
	lsVar=raw_input(psTexto)
	return lsVar

def fsContinuar():
	return fsLeerS("Pulse Enter para Continuar")

def fiLeerI(psTexto):
	liVar=int(raw_input(psTexto))
	return liVar
	
def faImprimir(paArreglo):
	os.system("clear")
	print paArreglo
	fsLeerS("Pulse Enter para continuar")

def faImprimir2(paArreglo):
	os.system("clear")
	for liX in paArreglo:
		print liX
	fsLeerS("Pulse Enter para continuar")

def faCargar(paArreglo):
	os.system("clear")
	liNum=fiLeerI("Introduzca un número ")
	paArreglo.append(liNum)
	return paArreglo

def faSacar(paArreglo):
	os.system("clear")
	print paArreglo.pop()
	fsLeerS("Pulse Enter para continuar")
	return paArreglo

def fiBuscar(paArreglo,piNum):
    liTamano=len(paArreglo)
    for liX in range (0,liTamano):
        if (paArreglo[liX]==piNum):
            return liX
    return -1
	
def fiMenu():
	os.system("clear")
	print "1.- Cargar Pila"
	print "2.- Sacar Pila"
	print "3.- Imprimir Pila"
	print "4.- Imprimir Pila por elemento"
	print "5.- Buscar en la Pila"
	print "0.- Salir"
	liOpcion=fiLeerI("Introduzca su Opción ")
	return liOpcion


#Programa

liOpcion=9
laArreglo=[]

while (liOpcion!=0):
	liOpcion=fiMenu()
	if (liOpcion==1):
		faCargar(laArreglo)
	if (liOpcion==2):
		faSacar(laArreglo)
	if (liOpcion==3):
		faImprimir(laArreglo)
	if (liOpcion==4):
		faImprimir2(laArreglo)
	if (liOpcion==5):
            liNum=fiLeerI("Introduzca el numero a buscar: ")
            liJ=fiBuscar(laArreglo,liNum):
            if (liJ==-1):
                print "No existe"
            else:
                print "Si existe",liJ    
	if (liOpcion==0):
		print "Adios"
		fsLeerS("Pulse Enter para continuar")
#UPTP S2-T1