#!/usr/bin/env python
#-*- coding:UTF8 -*-

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#Algoritmo capaz de calcular el promedio de un estudiante


def fileerI (psnota):
   liVar=int(raw_input(psnota))
   return liVar

def fbprom (psnota,pinnota):
    lfacum=0
    if psnota>=0:
        lfacum=lfacum+psnota
        return True
    return False
    if (psnota==True):
        lfprom=lfacum/pinnota
    return lfprom

def fsnombre (psnombre):
    lsVar=raw_input(psnombre)
    return lsVar

lsseguir="s"
lfprom=0
lfnota=0
lfacum=0
linnota=0

while lsseguir=="S" or lsseguir=="s":
    lsVar=raw_input("Nombre del estudiante: ")
    lsVar=raw_input("Nota: ")
    while lsseguir=="S" or lsseguir=="s":
        lsVarI=raw_input("Nota: ")
        lsseguir=raw_input("Desea Seguir?: (S/N) ")
    lfprom=fbprom(psnota,pinnota)
    print "El promedio de nota del estudiante es: ",lfprom
    lsseguir=raw_input("Desea Seguir?: (S/N) ")

#UPTP S1-T1