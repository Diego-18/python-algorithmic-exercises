#!/usr/bin/env python
# -*- coding: UTF8 -*-

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#Algoritmo capaz de verificar si un numero es par o impar

lsseguir="s"

while (lsseguir=="s") or (lsseguir=="S"):
    linumero=int(raw_input("Introduzca el numero: "))
    if (linumero%2)==0:
        print "El numero es par"
    else:
        print "El numero no es par"
    lsseguir=raw_input("Desea seguir?")

#UPTP S1-T1