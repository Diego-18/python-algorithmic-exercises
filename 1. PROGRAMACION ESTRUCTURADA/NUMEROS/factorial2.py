#!/usr/bin/env python
# -*- coding: UTF8 -*-

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#Algoritmo capaz de calcular el factorial de un numero
#*factorial* podria llamarse *acum*, se le asigna el valor del numero introducido ya que sino se le 
#da valor da error de variable indefinida, si se declarase en 0 el resultado=0 ya que multiplica

linumero=int(raw_input("Introduzca el numero: "))
lifactorial=linumero
for liN in range (1,linumero):
    lifactorial=lifactorial*liN
print "El factorial del numero es: ",lifactorial

#UPTP S1-T1