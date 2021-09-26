#!/usr/bin/env python
#-*- coding: UTF8 -*-

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#Realice un algoritmo que leida una serie de numeros, si el numero es par lo guarde en una lista

#Funcion
def fILeerI(psTexto):
	lfVar=int(raw_input(psTexto))
	return lfVar
	
def fsLeerS(psTexto):
	lsVar=raw_input(psTexto)
	return lsVar

def fbPar(pfN):
	if (pfN%2==0):
		return True
	return False

#Programa
lsSeguir="s"
laLista=[]
while (lsSeguir=="s" or lsSeguir=="S"):
	liNum=fILeerI("Introduzca un número: ")
	if (fbPar(liNum)==True):
		laLista.append(liNum)
	else:
		print "El numero no fue agregado a la lista"
	lsSeguir=fsLeerS("Desea introducir otro número?: ")
print laLista

for liN in laLista:
	print liN

#UPTP S1-T1