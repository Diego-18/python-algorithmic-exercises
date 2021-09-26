#!/usr/bin/env python
#-*- coding: cp1252 -*-

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#Algoritmo capaz de calcular el sueldo neto de un empleado con deducciones y bonificacion y de igual forma calcular 
#el monto que debe tener la empresa para el pago de nomina
lsseguir="s"
liacum=0
while lsseguir=="s" or lsseguir=="S":
    lsnombre=raw_input("Introduzca el nombre del empleado: ")
    lfsbase=float(raw_input("Introduzca el sueldo base del empleado: "))
    lichijos=int(raw_input("Introduzca la cantidad de hijos: "))
    lsecivil=raw_input("Introduzca el estado civil: ")
    lfsso=lfsbase*0.02
    lfpf=lfsbase*0.01
    lffahov=lfsbase*0.01
    lfcajaa=lfsbase*0.10

    if (lichijos>0):
        lfbonoh=lichijos*650
    elif (lichijos==0):
        lfbonoh=0

    lfsneto=lfsbase+lfbonoh-(lfsso+lfpf+lffahov+lfcajaa)
    print "El sueldo neto del empleado es: ",lfsneto
    lsseguir=raw_input("Desea seguir?: (S/N) ")
    liacum=liacum+lfsneto
print "La empresa requiere para pagarle a todos sus empleados un total de: ",liacum

#UPTP S1-T1