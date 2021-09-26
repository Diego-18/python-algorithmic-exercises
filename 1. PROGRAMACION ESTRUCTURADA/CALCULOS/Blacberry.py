#!/usr/bin/env python
# -*- coding: UTF8 -*-

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#Algoritmo capaz de calcular la cantidad de telefonos blackberry introducidos al sistema

liacum=0
licont=0
lsseguir="s"

while lsseguir=="s" or lsseguir=="S":
    lsempresa=raw_input("Introduzca la empresa: ")
    lsmarca=raw_input("Introduzca la marca del telefono: ")
    limodelo=raw_input("Introduzca el modelo del telefono: ")
    if (lsmarca=="Blackberry"):
        licont=licont+1
    lsseguir=raw_input("Desea seguir? ")
print "La cantidad de telefonos Blackberry es: ",licont
raw_input ()

#UPTP S1-T1