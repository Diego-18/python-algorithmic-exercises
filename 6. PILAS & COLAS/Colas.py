#!/usr/bin/env python
# -*- coding: utf-8 -*-

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

import os
from collections import deque

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
	print paArreglo.popleft()
	fsLeerS("Pulse Enter para continuar")
	return paArreglo
	
def fiMenu():
	os.system("clear")
	print "1.- Cargar Cola"
	print "2.- Sacar Cola"
	print "3.- Imprimir Cola"
	print "4.- Imprimir Cola por elemento"
	print "0.- Salir"
	liOpcion=fiLeerI("Introduzca su Opción ")
	return liOpcion


#Programa

liOpcion=9
laArreglo=deque([])

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
	if (liOpcion==0):
		print "Adios"
		fsLeerS("Pulse Enter para continuar")

#UPTP S2-T1