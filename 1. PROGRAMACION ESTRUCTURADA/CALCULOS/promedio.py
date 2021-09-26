#!/usr/bin/env python
# -*- coding: UTF8 -*-

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#Algoritmo capaz de calcular el promedio de un estudiante, mostrando si aprobó o reprobó

#Inicio
#Entrada
while lsseguir=="s" or lsseguir=="S":
    lsnombre=raw_input("Introduzca el nombre del estudiante ")
    lscedula=raw_input("Introduzca el numero de cedula del estudiante ")
    lfn1=float(raw_input("Introduzca la nota uno: "))
    lfn2=float(raw_input("Introduzca la nota dos: "))
    lfn3=float(raw_input("Introduzca la nota tres: "))
    lfn4=float(raw_input("Introduzca la nota cuatro: "))
    #Proceso
    lfprom=(lfn1+lfn2+lfn3+lfn4)/4
    if lfprom>=12:
        print "El estudiante aprobó"
    elif lfprom<12:
        print "El estudiante reprobó"
    #Salida
    print "El promedio es de: ",lfprom
    lsseguir=raw_input("Desea seguir?: (S/N) ")
#Fin
raw_input ()

#UPTP S1-T1
