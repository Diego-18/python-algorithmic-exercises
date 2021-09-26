#!/usr/bin/env python
#-*- coding: UTF8 -*-

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#realize un algoritmo que cargue 10 numeros y los arreglo con burbuja

def fiLeerI(piTexto):
	liVarI=int(raw_input(piTexto))
	return liVarI

def faBurbuja(paArreglo):
	litamano=len(paArreglo)
	for liX in range (0,litamano-2):
		for liJ in range (liX,litamano-1):
			if (paArreglo[liX]>paArreglo[liJ+1]):
				liAux=paArreglo[liX]
				paArreglo[liX]=paArreglo[liJ+1]
				paArreglo[liJ+1]=liAux
	return paArreglo

laArreglo=[]
for liX in range (0,11):
	liNum=fiLeerI("Introduzca el numero: ")
	laArreglo.append(liNum)
print laArreglo
laArreglo=faBurbuja(laArreglo)
print laArreglo

#UPTP S1-T1
