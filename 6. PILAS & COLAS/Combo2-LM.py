#! usr/bin/env python
# -*- coding: utf8 -*-
import os
from collections import deque

#Algoritmo que permita hacer un registro del nombre del cliente y del combo comprado y que aleatoriamente se le obsequie un regalo dependiendo del color

#funciones

def fsLeerS (pstexto):
	lsVars= raw_input(pstexto)
	return lsVars

def fiLeerI (pstexto):
	liNum= int(raw_input(pstexto))
	return liNum
	
def fsContinuar():
	return fsLeerS ("pulse enter para continuar ")
			
def faCargar (paArreglo):
	os.system("clear")
	lsVar= fsLeerS ("Nombre del cliente ")
	paArreglo.append (lsVar)

def faCargar2 (paArreglo):
	os.system("clear")
	lsVar= fsLeerS ("Introduzca el Color ")
	paArreglo.append (lsVar)
	
def faSacar(paArreglo):
	os.system("clear")
	try:
		print paArreglo.popleft()
		print "Que combo desea Comprar"
		print "Combo 1 - 220bs / Combo 2 - 260 / Combo 3 - 300bs"
		liOP= fiLeerI ("Selecccione el Combo")
		if (liOP==1):
			liCantidad= fiLeerI ("Cuantos Combos desea llevar")
			liTotal= liCantidad*220
			print "El monto total es ", liTotal
		if (liOP==2):
			liCantidad= fiLeerI ("Cuantos Combos desea llevar")
			liTotal= liCantidad*260
			print "El monto total es ", liTotal
			fsContinuar()
		if (liOP==3):
			liCantidad= fiLeerI ("Cuantos Combos desea llevar")
			liTotal= liCantidad*300
		lsColor= paPila.pop()
		print "Su Color de Promocion es ", lsColor
		if (lsColor=="Blanco" or "blanco"):
			print "Mas suerte en su proxima compra"
			
		if (lsColor=="Azul" or "azul"):
			print "Usted ha ganado un descuento del 5%!"
			lfDescuento= (liTotal*0.05)
			lfTotal2= liTotal-lfDescuento
			print "Su total a pagar es ", lfTotal2
			
		if (lsColor=="Morado" or "morado"):
			print "Usted ha ganado un descuento del 10%!"
			lfDescuento= (liTotal*0.10)
			lfTotal2= liTotal-lfDescuento
			print "Su total a pagar es ", lfTotal2
			
	except IndexError:
		print ("no hay mas clientes en la cola")

def faImprimir (paArreglo):
	for liX in range (0,5):
		print paArreglo[liX]
	fsContinuar()
	
def fiMenu ():
	os.system ("clear")
	print "1.- Cargar Cola"
	print "2.- Cargar Pila"
	print "3.- Atender"
	print "4.- Imprimir"
	print "0.- Salir"
	liOpcion= fiLeerI ("Seleccione su Opcion ")
	return liOpcion

#Inicio

liOpcion=9
paCola=deque([])
paPila=[]
while (liOpcion!=0):
	liOpcion=fiMenu()
	if (liOpcion==1):
		faCargar(paCola)
	if (liOpcion==2):
		faCargar2(paPila)
	if (liOpcion==3):
		faSacar(paCola)
	if (liOpcion==4):
		faImprimir(paCola)
	if (liOpcion==0):
		print "Adios"
		fsContinuar()
#UPTP S2-T1