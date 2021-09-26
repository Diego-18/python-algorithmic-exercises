#! usr/bin/env python
#-*- coding: utf8 -*

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#Funciones

def ffLeerF (lsTexto):
    lfVar=float(raw_input(lsTexto))
    return lfVar

def fsLeerS (lsTexto):
    lsVar=raw_input(lsTexto)
    return lsVar
    
def ffCalcular (N1,N2,OP):
	if (OP=="S" or OP=="s"):
		return N1+N2
	elif (OP=="R" or OP=="r"):
		return N1-N2
	elif (OP=="M" or OP=="m"):
		return N1*N2
	else:
		return N1/N2

#Variables
liNum=0
liNum=0
lsOperador=" "
lsSeguir="s"
	
while (lsSeguir=="s" or lsSeguir=="S"):
	liNum1=ffLeerF("Introduzca el numero 1: ")
	liNum2=ffLeerF("Introduzca el numero 2: ")
	lsOperador=fsLeerS("Introduzca la inicial de la operacion que desea realizar: ")
	lfResultado=ffCalcular(liNum1,liNum2,lsOperador)
	print ("El resultado es: ") +str(lfResultado)
	lsSeguir=fsLeerS("Desea seguir?: ")

#UPTP S2-T1