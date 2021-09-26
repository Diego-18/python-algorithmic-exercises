#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
	
def fiBuscar (paArreglo,piNum):
	liTam=len(paArreglo)
	for liI in range(0,liTam):
		if (paArreglo[liI]==piNum):
			return liI
		return -1
	
def faImprimir(paArreglo):
	os.system("clear")
	print paArreglo
	fsLeerS("Pulse Enter para continuar")

def faImprimir2(paArreglo):
	os.system("clear")
	for liX in paArreglo:
		if liX%2==0: #si es par lo imprimira
			print liX
	fsLeerS("Pulse Enter para continuar")
	
"""
def faImprimir(paArreglo):
	os.system("clear")
	if paArreglo%2==0:
                print paArreglo
	fsLeerS ("Pulse Enter para continuar")
"""

def faCargar(paArreglo):
	os.system("clear")
	liNum=fiLeerI("Introduzca un número ")
	paArreglo.append(liNum)
	return paArreglo

def faSacar(paArreglo):
	os.system("clear")
	try:
		print paArreglo.pop()  #el .pop es para la pila y .popleft es para la cola
	except IndexError:  #en caso de dar error al sacar
		print ("La pila esta vacia")
	fsLeerS("Pulse Enter para continuar")
	return paArreglo

def fiMenu():
	os.system("clear")
	print "1.- Cargar Pila"
	print "2.- Sacar Pila"
	print "3.- Imprimir Pila"
	print "4.- Imprimir Pila por elemento"
	print "5.- Buscar un elemnto"
	print "0.- Salir"
	liOpcion=fiLeerI("Introduzca su Opción ")
	return liOpcion


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
		liNum=fiLeerI("Introduzca el numero a buscar ")
		liX=fiBuscar(laArreglo,liNum)
		if (liX==-1):
			print "No existe"
		else:
			print "Si existe"
		fsContinuar()
	if (liOpcion==0):
		print "Adios"
		fsLeerS("Pulse Enter para continuar")
