#!/usr/bin/env python
#-*- coding: UTF8 -*-

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#Realice un algoritmo que cargue 10 numeros a una lista, y ordenelos de menor a mayor

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
			if (paArreglo[liX]>paArreglo[liJ+1]):
				liAux=paArreglo[liX]
				paArreglo[liX]=paArreglo[liJ+1]
				paArreglo[liJ+1]=liAux
	return paArreglo
	
laLista=[]
for liN in range (1,11):
	liNum=fILeerI("Introduzca el número: ")
	laLista.append(liNum)
	LaLista=faBurbuja(laLista)
print LaLista

#UPTP S1-T1