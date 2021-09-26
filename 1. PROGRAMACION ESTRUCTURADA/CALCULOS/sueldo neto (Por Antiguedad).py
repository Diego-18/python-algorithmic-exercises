#!/usr/bin/env python
# -*- coding: UTF-8 -*-

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#Algoritmo capaz de calcular el sueldo neto de un empleado por años de antigüedad

#Entrada
lsnombre=raw_input("Introduzca el nombre del empleado: ")
lfsbase=float(raw_input("Introduzca el sueldo base: "))
liantiguedad=int(raw_input("Introduzca los años de antiguedad: "))
#Proceso
lfaumento1=lfsbase*0.10
lfaumento2=lfsbase*0.05
lfsneto1=lfaumento1+lfsbase
lfsneto2=lfaumento2+lfsbase
#Salida
if (liantiguedad>10) and (lfsbase>10000):
    print "El sueldo neto del empleado es: ",lfsneto1
elif (liantiguedad<=10) and (lfsbase<=10000):
    print "El sueldo neto del empleado es: ",lfsneto2
#Fin
raw_input ()

#UPTP S1-T1