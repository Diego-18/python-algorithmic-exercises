#!/usr/bin/enb python
# -*- coding: UTF8 -*-

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#Algoritmo capaz de calcular el sueldo neto de un empleado con deducciones (seguro social,paro forsoso,fahov,caja chica)
#y bonificacion(por estado civil, por cantidad de hijos).

#Inicio
#Entrada
lsnombre=raw_input("Introduzca el nombre del empleado: ")
lfsmin=float(raw_input ("introduzca el sueldo minimo "))
licanthijos=int(raw_input ("introduzca la cantidad de hijos "))
lsedocivil=raw_input ("introduzca el estado civil ")
#Proceso
lfsso=lfsmin*0.02
lfpfors=lfsmin*0.01
lffahov=lfsmin*0.01
lfcaja=lfsmin*0.10
lfbonhijo=licanthijos*650
lfbonedocivil=0
if (lsedocivil=="c") or (lsedocivil=="C"):
    lfbonedocivil=lfsmin+850
lfsneto=lfsmin-(lfsso+lfpfors+lffahov+lfcaja)+(lfbonhijo+lfbonedocivil)
#Salida
print "el sueldo neto del empleado es: ",lfsneto
#Fin
raw_input()

#UPTP S1-T1