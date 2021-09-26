#!/usr/bin/env python
#-*- coding: cp1252 -*-

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#Algoritmo capaz de calcular la raiz cuadrada de un numero

lsseguir="s"
liacum=0

while lsseguir=="S" or lsseguir=="s":
    linumero=int(raw_input("Introduzca el numero: "))
    lfraiz=linumero**0.5
    print "La raiz del numero es: ",lfraiz
    lsseguir=raw_input("Desea seguir? (S/N): ")

#UPTP S1-T1