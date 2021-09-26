#!/usr/bin/env python
# -*- coding: UTF8 -*-

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#Algoritmo capaz de calcular el costo unitario y al mayor de un articulo

lsnombre=raw_input("Introduzca el nombre del articulo: ")
lfgmanodeobra=float(raw_input("Introduzca el gasto de mano de obra: "))
lfgmateriap=float(raw_input("Introduzca el gasto de materia prima: "))
lfgfabricacion=float(raw_input("Introduzca el gasto de fabricacion: "))
licantarticulos=int(raw_input("Introduzca la cantidad de articulos obtenidos: "))
lfcostu=(lfgmanodeobra+lfgmateriap+lfgfabricacion)/licantarticulos
lfventa=(lfcostu*0.10)+lfcostu
print "El costo unitario del articulo es: ",lfcostu
print "El costo a vender del articulo es: ",lfventa

#UPTP S1-T1