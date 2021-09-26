#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#Enunciado:
"""Se decea otrorgar una comision a un vendedor la cual sera el 10% de sus
ventas totales. Calcular dicha comision conociendo para ello nombre, cedula
y el monto de cada una de las ventas que ha realizado en un mes"""

#Inicio
lsnombre=raw_input("Introduzca su nombre ")
lsci=raw_input("Introduzca su cedula ")
lsseguir='s'
liacum=0
licont=0

while lsseguir=='s' or lsseguir=='S':
    liventa=int(raw_input("introduzca el monto de su venta "))
    liacum=liacum+liventa
    licont=licont+1
    lsseguir=raw_input("decea seguir? ")
lfcomision=liacum*0.10


#salida
print "el vendedor " +lsnombre+ " de cedula " +lsci+ " tiene una comision de " +str(lfcomision)+" y su total de ventas del mes es " +str(licont)

raw_input()

#UPTP S1-T1