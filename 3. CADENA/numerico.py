#! usr/bin/env python
# -*- coding: UTF8 -*-

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#Funciones
def fsLeerS (psTexto):
	lsVar=raw_input(psTexto)
	return lsVar
	
#determina que tipo de cadena es
lsCadena=fsLeerS("Introduzca la cadena ")
if (lsCadena.isalpha()):
	print "alfabetico"

if (lsCadena.isalnum()):
	print "alfanumerico"
	
if (lsCadena.isdigit()):
	print "numerico"


lsLista=lsCadena.split(" ") #convierte la cadena en una lista
print lsLista

lsCadena2=" / ".join(lsLista)
print lsCadena2

#UPTP S1-T1