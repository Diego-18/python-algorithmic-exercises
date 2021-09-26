#!/usr/bin/env python
#-*- coding: UTF8 -*-

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#Algoritmo capaz de calcular el porcentaje de hombres y mujeres

#Inicio
#Entrada
lichombres=int(raw_input("Introduzca la cantidad de hombres: "))
licmujeres=int(raw_input("Introduzca la cantidad de mujeres: "))
#Proceso
lip=lichombres+licmujeres
liporh=(lichombres*lip)/100
liporm=(licmujeres*lip)/100

#Salida
print "El porcentaje de hombres en una comunidad es: ",liporh
print "El porcentaje de mujeres en una comunidad es: ",liporm

#Fin
raw_input ()

#UPTP S1-T1
