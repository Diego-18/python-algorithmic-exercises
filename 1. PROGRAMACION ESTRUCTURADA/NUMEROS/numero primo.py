#!/usr/bin/env python
# -*- coding: UTF8 -*-

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#Algoritmo capaz de verificar si un numero es primo

lsseguir="s"

while (lsseguir=="S") or (lsseguir=="s"):
    linumero=int(raw_input("Introduzca el numero: "))
    licont=0
    for liN in range (1,linumero+1):
        if (linumero%liN==0):
            licont=licont+1
    if (licont==2):
        print "El numero es primo"
    else:
        print "El numero no es primo"
    lsseguir=raw_input("Desea seguir?")
    
#UPTP S1-T1