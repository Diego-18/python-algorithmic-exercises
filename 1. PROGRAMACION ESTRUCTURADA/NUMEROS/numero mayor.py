#!/usr/bin/env python
# -*- coding: UTF8 -*-

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#Algoritmo capaz de verificar el mayor de cuatro numeros

#Inicio
lin1=int(raw_input("Introduzca el numero uno "))
lin2=int(raw_input("Introduzca el numero dos "))
lin3=int(raw_input("Introduzca el numero tres "))
lin4=int(raw_input("Introduzca el numero cuatro "))
if (lin1>lin2) and (lin1>lin3) and (lin1>lin4):
    print "El numero mayor es: ",lin1
elif (lin2>lin1) and (lin2>lin3) and (lin2>lin4):
    print "El numero mayor es: ",lin2
elif (lin3>lin1) and (lin3>lin2) and (lin3>lin4):
    print "El numero mayor es: ",lin3
elif (lin4>lin1) and (lin4>lin2) and (lin4>lin3):
    print "El numero mayor es: ",lin4
#Fin
raw_input () 

#UPTP S1-T1