#!/usr/bin/env python
#-*- coding: UTF-8 -*-

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#Algoritmo capaz de mostrar la division y el modulo de dos numeros

#Funciones
def ffLeerI(psTexto):
	lfVar=int(raw_input(psTexto))
	return lfVar

def ffdivision(piN1,piN2):
	lfValorT=piN1/piN2
	return lfValorT

def ffmodulo(piN1,piN2):
	lfValorT=piN1%piN2
	return lfValorT

lfN1=ffLeerI("Introduzca el primer numero: ")
lfN2=ffLeerI("Introduzca el segundo numero: ")
lfCociente=ffdivision(lfN1,lfN2)
lfModulo=ffmodulo(lfN1,lfN2)
print "El cociente de la division de los 2 numeros es: ",lfCociente
print "El resto de la division de los 2 numeros es: ",lfModulo

#UPTP S1-T1