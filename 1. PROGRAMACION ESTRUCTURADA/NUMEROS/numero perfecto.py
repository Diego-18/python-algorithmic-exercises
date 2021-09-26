#!/usr/bin/env python
#-*- coding: cp1252 -*-

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#Algoritmo capaz de verificar si un numero es perfecto

lsseguir="s"
liacum=0

while lsseguir=="s" or lsseguir=="S":
    linumero=int(raw_input("Introduzca el numero: "))

    for liN in range (1,linumero):
        if (linumero%liN==0):
            liacum=liacum+liN

    if liacum==linumero:
        print "El numero es perfecto"

    else:
        print "El numero no es perfecto"

    lsseguir=raw_input("Desea seguir?: (S/N) ")

#UPTP S1-T1