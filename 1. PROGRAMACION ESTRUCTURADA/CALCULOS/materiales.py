#!/usr/bin/env python
# -*- coding: UTF8 -*-

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#Algoritmo capaz de calcular el costo total a pagar por materiales de construccion

#Entrada
licantcemento=int(raw_input("Introduzca la cantidad de cemento: "))
licantcabilla=int(raw_input("Intoduzca la cantidad de cabillas: "))
licostcabilla=int(raw_input("Introduzca el costo de la cabilla por unidad: "))
licostcemento=int(raw_input("Introduzca el costo del cemento por unidad: "))

#Proceso
litotalcemento=licostcemento*licantcemento
litotalcabilla=licostcabilla*licantcabilla
lidcemento=litotalcemento*0.12
lidcabilla=litotalcabilla*0.12
lictotal1=(litotalcemento+litotalcabilla)-(lidcemento+lidcabilla)
lictotal2=litotalcemento+litotalcabilla

#Salida
if (licantcemento>20) and (licantcabillas>25):
    print "El costo total de los materiales es de: ",lictotal1
    
else:
    print "El costo total de los materiales es de: ",lictotal2
raw_input ()

#UPTP S1-T1