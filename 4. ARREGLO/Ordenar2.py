#!/usr/bin/env python
#-*- coding: UTF8 -*-

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#Realice un algoritmo que leido un número, si el numero es primo lo guarde en un arreglo, ordene el arreglo en forma
#Descendente,y muestre en que posición esta el numero 2.

def fiLeerI(psTexto):
	liVar=int(raw_input(psTexto))
	return liVar
	
def fsLeerS(psTexto):
	lsVar=raw_input(psTexto)
	return lsVar
	
def fbPrimo(pfN):
	if (pfN<2):
		return False
	for i in range (2,pfN):
		if (pfN%i==0):
			return False
	return True
	
def faBurbuja (paArreglo):              #Ordena de manera ascendente la lista
	liTamano=len(paArreglo)
	for liX in range (0,liTamano):
		for liJ in range (liX, liTamano-1):
			if (paArreglo[liX]<paArreglo[liJ+1]):
				liAux=paArreglo[liX]
				paArreglo[liX]=paArreglo[liJ+1]
				paArreglo[liJ+1]=liAux
	return paArreglo
	
def fiBuscar(paArreglo,piNum):
	liTamano=len(paArreglo)
	for liI in range(0,liTamano):
		if (paArreglo[liI]==piNum):
			return liI
	return -1
	


laArreglo=[]
lsSeguir="s"
while (lsSeguir=="s" or lsSeguir=="S"):
	liNum=fiLeerI("Introduzca el número: ")
	if (fbPrimo(liNum)==True):
		laArreglo.append(liNum)
	else:
		print "El número no es primo"
	lsSeguir=fsLeerS("Desea seguir?: ")
print laArreglo
print fiBuscar(laArreglo,2)

#UPTP S1-T1