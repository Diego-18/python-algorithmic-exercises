#!/usr/bin/env python
#-*- coding: UTF8 -*-

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#Muestre los numeros perfectos del 1 al 3000000

#Funcion
def fbPerfecto(pinumero):
	liacum=0
	for liN in range (1,pinumero):
	    if(pinumero%liN==0):
		    liacum=liacum+liN
	if (liacum==pinumero):
		return True 
	return False
	
#Programa
for liX in range (1,3000000+1):
	if (fbPerfecto(liX)==True):
		print liX

#UPTP S1-T1