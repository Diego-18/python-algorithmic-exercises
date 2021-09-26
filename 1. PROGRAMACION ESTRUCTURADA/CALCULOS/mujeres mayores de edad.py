#!/usr/bin/env python
# -*- coding: UTF8 -*-

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#Algoritmo capaz de calcular la cantidad de mujeres mayores de edad

#Inicio
#Entrada
liacum=0
licont=0
lsseguir="s"

#Proceso
while lsseguir=="s" or lsseguir=="S":
    liedad=int(raw_input("Introduzca la edad: "))
    lssexo=raw_input("Introduzca el sexo: ")
    if liedad>=18 and (lssexo=="f") or (lssexo=="F") or (lssexo=="femenino"):
        licont=licont+1
    lsseguir=raw_input("Desea seguir? ")
print "La cantidad de mujeres en la seccion es: ",licont
raw_input ()

#UPTP S1-T1