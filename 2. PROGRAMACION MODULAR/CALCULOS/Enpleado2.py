#!/usr/bin/env python
#-*- coding:UTF8 -*-

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#Algoritmo capaz de calcular el sueldo neto de un empleado calculando sus deducciones, 
#sus bonos y de igual forma la cantidad de dinero que la empresa necesita para solventar el pago de nomina

def fsleerS (psNombre):
    lsValorS=raw_input(psNombre)
    return lsValorS

def ffleerF (psSueldo_B):
    lfValorF=raw_input(psSueldo_B)
    return lfValorF

def fileerI (psHijos):
    liValorI=raw_input(psHijos)
    return liValorI

def fsleerS (psProfesion):
    lsValorS=raw_input(psProfesion)
    return lsValorS

def fsleerS (psEc):
    lsValorS=raw_input(psEc)
    return lsValorS

def ffCalculo (pfmultiplicando, pfmultiplicador):
        lfPorcentaje=pfmultiplicando*pfmultiplicador
        return lfPorcentaje

#Programa

lfSueldo=0
lfacum=0
libon_hijo=650
lfpp=750
lfSso=0.04
lfPf=0.01
lfFahov=0.01
lfCa=0.10
lfbon_ec=650
lsseguir="s"

while lsseguir=="s" or lsseguir=="S":
    lsNombre=fsleerS("Introduzca el nombre del empleado: ")
    lfSueldo=ffleerF("Introduzca el sueldo base del empleado: ")
    liHijos=fileerI("Introduzca la Cantidad de hijos: ")
    lsProfesionalismo=fsleerS("Eres Profesional: ")
    lsec=fsleerS("Cual es tu estado civil: ")

    #Total deducciones

    lftsso=ffCalculo(lfSueldo,lfSso)
    lftpf=ffCalculo(lfSueldo,lfPf)
    lftfahov=ffCalculo(lfSueldo,lfFahov)
    lftca=ffCalculo(lfSueldo,lfCa)

    #Total Asignaciones

    if liHijos>0:
        lft_bonoh=ffCalculo(libon_hijo*liHijos)

    if (lsProfesionalismo=="Si"):
        lfpp=lfpp

    if (lsec=="C") or (lsec=="c"):
        lsec=lsec
        
    lfSueldo_N=lfSueldo+(lft_bonoh+lfpp+lsec)-(lft_sso+lft_pf+lft_fahov+lft_ca)
    print "El sueldo neto del empleado es: ",lfSueldo_N
    lfacum=lfacum+lfSueldo_N
    lfSueldo=0
    lfacum=0
    libon_hijo=0
    lfpp=0
    lfSso=0
    lfPf=0
    lfFahov=0
    lfCa=0
    lfbon_ec=0
    lsseguir=raw_input("Desea Seguir?: (S/N) ")
print "La empresa necesita para pagar la nomina: ",lfacum

#UPTP S1-T1