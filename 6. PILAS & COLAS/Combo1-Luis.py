#!/usr/bin/env python
# -*- coding: utf-8 -*-

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#Algoritmo que permita hacer un registro de articulo comprado y el nombre del cliente

import os
from collections import deque
 
def fiLeerI(psTexto):
	 liVar=int(raw_input(psTexto))
	 return liVar

def fsLeerS(psTexto):
	lsVar=raw_input(psTexto)
	return lsVar

def faCargar(paArreglo):
	liN=fsLeerS("introduzca el nombre de la persona que esta  en la cola: ")
	paArreglo.append(liN)
	return paArreglo

def faSacar(paArreglo):
	try:
		print paArreglo.popleft()
		print "1._libreta a 200bs?"
		print "2._cuaderno a 130bs?"
		liOpcion2=fiLeerI("que vas a comprar, 1 o 2? ")
		if (liOpcion2==1):
			liN2=fiLeerI("cuantas va a comprar?" )
			liMu=(200*liN2)
			print "vas a pagar por las", liN2, "libretas", liMu,"Bsf"
		if (liOpcion2==2):
			liN3=fiLeerI("cuantos cuadernos comprara?")
			liMu2=(130*liN3)
			print "vas a pagar por ", liN3, "cuadernos", liMu2,"Bsf"
	except IndexError:
		print "la cola esta vacia"
	return paArreglo

def Imprimir(paArreglo):
	print paArreglo

def fiMenu():
	print "1._Cargar"
	print "2._Atender"
	print "3._Imprimir"
	print "0._ salir"
	liOpcion=fiLeerI("eliga una opcion: ")
	return liOpcion

liOpcion=9
paArreglo=deque([])
while (liOpcion!=0):
	liOpcion=fiMenu()
	if (liOpcion==1):
		faCargar(paArreglo)
	if (liOpcion==2):
		faSacar(paArreglo)
	if (liOpcion==3):
		Imprimir(paArreglo)
	if (liOpcion==0):
		print "adios"

#UPTP S2-T1