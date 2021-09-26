#!/usr/bin/env python
#-*- coding: UTF-8 -*-

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#Algoritmo capaz de calcular el sueldo neto de un empleado calculando sus deducciones, 
#su bono y de igual forma la cantidad de dinero que la empresa necesita para solventar el pago de nomina

#Funciones
def fsLeerS(psTexto):
	lsVar=raw_input(psTexto)
	return lsVar

def ffLeerF(psTexto):
	lfVar=float(raw_input(psTexto))
	return lfVar

def fiLeerI(psTexto):
	liVar=int(raw_input(psTexto))
	return liVar

def ffSueldo(piN1,piN2):
	lfVar=piN1*piN2
	return lfVar
	
#Programa

lfacum=0
lihoras=0
liS_hora=30
liNumeroO=0
liObreros=50
licont=0

for lihoras in range (1,51): 
	lihoras=fiLeerI("Introduzca la cantidad de horas trabajadas: ")
	lfSueldoN=ffSueldo(lihoras,liS_hora)
	print "El sueldo del trabajador es: ",lfSueldoN
	lfacum=lfacum+lfSueldoN
	print "La empresa necesita para solventar la nomina: ",lfacum

lfacum=0
lihoras=0
liS_hora=30
liObreros=50
#Fin

#UPTP S1-T1