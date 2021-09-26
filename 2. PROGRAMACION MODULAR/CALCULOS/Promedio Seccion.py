#!/usr/bin/env python
#-*- coding: UTF8 -*-

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#Algoritmo capaz de calcular la nota promedio de una seccion

#Funciones

def ffleerF(psTexto):
	lfVar=float(raw_input(psTexto))
	return lfVar
	
def ffPromedio (pfAcum,piCont):
	lfProm=pfAcum/piCont
	return lfProm

def fsleerS(psTexto):
	lsVar=raw_input(psTexto)
	return lsVar
	
#Programa

lsseguir="S"
lfAcum=0
licont=0

while lsseguir=="S" or lsseguir=="s":
	lfAcumE=0
	for liX in range (0,3):
		lfNota=ffleerF("Introduzca la nota: ")
		lfAcumE=lfAcumE+lfNota
	lfPromedio=ffPromedio(lfAcumE,3)
	print "El promedio es: ",lfPromedio
	licont=licont+1
	lfAcum=lfAcum+lfPromedio
	lsseguir=fsleerS("Desea Seguir?: ")
lfPromedioG=ffPromedio(lfAcum,licont)
print "El promedio de la seccion es: ",lfPromedioG
#Fin

#UPTP S1-T1