#!/usr/bin/env python
#-*- coding: cp1252 -*-

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#Algoritmo capaz mostrar mensajes por edad

lsseguir="s"

while lsseguir=="s" or lsseguir=="S":
    liedad=raw_input("Introduzca la edad: ")

    if (liedad<15):
        print "A DORMIR"

    elif (liedad>=15) and (liedad<=17):
        print "A ESTUDIAR"

    elif (liedad>=18):
        print "A TRABAJAR"

    lsseguir=raw_input("Desea seguir?: (S/N) ")

#UPTP S1-T1