#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#Enunciado:
"""Calcular el monto neto a cancelar por un cliente de una libreria
sabiendo que cada cuaderno cuesta 15bsf, los lapices 8bsf. Como dato
de entrada se tiene: Nombre, cedula, cantidad de cuadernos y lapices
comprados. Mostrar como salida: Nombre, cedula y monto a calcular
por el cliente"""

#Entrada
lsnombre=raw_input("Introduzca su nombre ")
lsci=raw_input("Introduzca su cedula ")
licantcuaderno=int(raw_input("Introduzca la cantidad de cuadernos "))
licantlapiz=int(raw_input("Introduzca la cantidad de lapices "))

#Proceso
licuaderno=15
lilapiz=8
lipagar=(licuaderno*licantcuaderno)+(lilapiz*licantlapiz)

#Salida
print " el cliente " +lsnombre+ " de numero de cedula " +lsci+ " tiene un monto a pagar de " + str(lipagar)

raw_input()

#UPTP S1-T1