#!/usr/bin/env python
#-*- coding: UTF8 -*-

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#Algoritmo capaz de calcular el sueldo neto de un empleado con deducciones y bonificacion

#Inicio
#Entrada
lsnombre=raw_input("Introduzca el nombre del empleado: ")
lssexo=raw_input("Introduzca el sexo del empleado: ")
lscedula=raw_input("Introduzca la cedula del empleado: ")
lfsbase=float(raw_input("Introduzca el sueldo base del empleado: "))
lfbono=float(raw_input("Introduzca el bono del empleado: "))
#Proceso
lfsneto=lfsbase+lfbono
#Salida
print "el sueldo neto del empleado es: ",lfsneto
#Fin
raw_input ()

#UPTP S1-T1