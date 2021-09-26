#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#Enunciado:
"""Realice un algoritmo que sepa la entrega de una carga de pantalones,
sabiendo que son modelos diferentes, mostrar como salida, cuantos hay de
jeans, gabardina, pinjoy y levis"""

#Entrada
lsseguir="S"
lilevis=0
lijeans=0
ligabardina=0
lipinjoy=0

while lsseguir=="S" or lsseguir=="s":
    print "1:Levis ; 2:Gabardina ; 3:Pjinjoy ; 4:Jeans "
    lipant=int(raw_input("Introduzca el pantalon "))
    if lipant==1 :
        lilevis=lilevis+1
    elif lipant==2:
        ligabardina=ligabardina+1
    elif lipant==3:
        lipinjoy=lipinjoy+1
    elif lipant==4:
        lijeans=lijeans+1
    else:
        print "su numero no es valido"
    lsseguir=raw_input("Decea continuar? ")
print " levis son: " +str(lilevis)+", Gabardina son: "+ str(ligabardina)+ ", Pinjoys son:" + str(lipinjoy) + ", Jeans son: " + str(lijeans)

raw_input()

#UPTP S1-T1