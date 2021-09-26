#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

###Imprimir los numeros impares desde el 1 al 25, ambos inclusive

linumero = 1
h = ''
while linumero <= 25:
    if linumero%2 == 0:
        h += ' %i' % linumero
    linumero += 1
print h
raw_input()

#UPTP S1-T1
