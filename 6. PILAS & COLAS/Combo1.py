#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from collections import deque

#Algoritmo que permita hacer un registro del nombre del cliente y del combo comprado y que aleatoriamente se le obsequie un regalo

#funcion

def fsLeerS(psTexto):
	lsVar=raw_input(psTexto)
	return lsVar

def fsContinuar():
	return fsLeerS("Pulse Enter para Continuar")

def fiLeerI(psTexto):
	liVar=int(raw_input(psTexto))
	return liVar

def faCargar(paArreglo):
	os.system("clear")
	lsVar=fsLeerS("Introduzca el regalo ")
	paArreglo.append(lsVar)
	return paArreglo
	
def faCargar2(paArreglo):
	os.system("clear")
	lsVar=fsLeerS("Introduzca el cliente ")
	paArreglo.append(lsVar)
	return paArreglo

def faSacar(paArreglo):
	os.system("clear")
	print paArreglo.popleft()
	fsLeerS("Que va a comprar")
	print ("1.Combo 1, 2. Combo 2, 3. Combo 3 ")
	Ops=fiLeerI("Opcion: ")
	if (Ops==1):
		liCantidad=fiLeerI("¿Cuantos desea llevar?: ")
		liTotal= (liCantidad*250)
		print liTotal
	if (Ops==2):
		liCantidad2=fiLeerI("¿Cuantos desea llevar? ")
		liTotal= (liCantidad2*300)
		print liTotal
	if (Ops==3):
		liCantidad3=fiLeerI("¿Cuantos desea llevar? ")
		liTotal= (liCantidad3*350)
		print liTotal
	if (liTotal>1000):
		print "por comprar mas de 1000 te damos un regalo"
		try:
			print laArreglo2.pop()
		except IndexError:
			print "se nos agotaron los regalos"
		
		
	fsLeerS("Pulse Enter para continuar ")
	return paArreglo
	
def fiMenu():
	os.system("clear")
	print "1.- Cargar Cola "
	print "2.- Cargar Pila "
	print "3.- Atender "
	print "4.- Buscar "
	print "0.- Salir "
	liOpcion=fiLeerI("Introduzca su Opción ")
	return liOpcion
	
#Inicio del programa

Ops=0
liOpcion=9
laArreglo=deque([])
laArreglo2= deque([])

while (liOpcion!=0):
	liOpcion=fiMenu()
	if (liOpcion==1):
		faCargar2(laArreglo)
	if (liOpcion==2):
		faCargar(laArreglo2)
	if (liOpcion==3):
		faSacar(laArreglo)
	if (liOpcion==4):
		faBuscar(laArreglo)
	if (liOpcion==0):
		print "Adios"
		fsLeerS("Pulse Enter para continuar ")

#UPTP S2-T1