#!/usr/bin/env python
#-*- coding: cp1252 -*-

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#Algoritmo capaz de verificar si un numero es par y primo


lsseguir="s"
licont=0

while lsseguir=="s" or lsseguir=="S":
    linumero=int(raw_input("Introduzca el numero: "))
    licont=0
    if (linumero%2==0):
        print "El numero es par"
    elif (linumero%2!=0):
        print "El numero no es par"
    for liN in range (1,linumero+1):
        if (linumero%liN==0):
            licont=licont+1
    if licont==2:
        print "El numero es primo"
    else:
        print "El numero no es primo"
    lsseguir=raw_input("Desea seguir?: (S/N) ")

#UPTP S1-T1