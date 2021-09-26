#!/usr/bin/env python
#-*- coding: UTF8 -*-

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#Realice un algoritmo que cargue 20 elementos, ordene el arreglo de mayor a menor y busque en que posicion esta el numero 6.

def fILeerI(psTexto):
	lfVar=int(raw_input(psTexto))
	return lfVar
	
def fsLeerS(psTexto):
	lsVar=raw_input(psTexto)
	return lsVar
	
def faBurbuja (paArreglo):              #Ordena de manera ascendente la lista
	liTamano=len(paArreglo)
	for liX in range (0,liTamano):
		for liJ in range (liX, liTamano-1):
			if (paArreglo[liX]<paArreglo[liJ+1]):
				liAux=paArreglo[liX]
				paArreglo[liX]=paArreglo[liJ+1]
				paArreglo[liJ+1]=liAux
	return paArreglo
	
def fiBuscar(paArreglo,piNum):   #Imprime la ubicacion o posicion de un numero.
	liTamano=len(paArreglo)
	for liI in range(0,liTamano):
		if (paArreglo[liI]==piNum):
			return liI
	return -1
	
#1,2,3,4,5,10,15,18,20,22,6,9,8,7,12,15,22,14,28,30
laLista=[1,2,3,4,5,10,15,18,20,22,6,9,8,7,12,15,22,14,28,30]
laLista=faBurbuja(laLista)
print laLista
print fiBuscar(laLista,6)
