#!/usr/bin/env python
#-*-coding:UTF-8-*-

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#Algoritmo capaz de facturar el total a pagar en un restaurante

lsseguir="s"
liacum=0
licont=0

while lsseguir=="S" or lsseguir=="s":
    lfplato1=float(raw_input("Introduzca el costo del primer plato: "))
    lfplato2=float(raw_input("Introduzca el costo del segundo plato: "))
    lfplato3=float(raw_input("Introduzca el costo del tercer plato: "))
    licantidad=3
    licont=licantidad
    liacum=liacum+(lfplato1+lfplato2+lfplato3)
    lsseguir=raw_input("Desea seguir? (S/N): ")
    while lsseguir=="S" or lsseguir=="s":
        lfplatoa=float(raw_input("Introduzca el costo del plato adicional: "))
        licont=licont+1
        liacum=liacum+lfplatoa
        lsseguir=raw_input("Desea seguir? (S/N): ")
if (licont>5):
    lfbono1=liacum-100
else:
    lfbono1=0
if (liacum>=1000):
    lfbono2=liacum-300
else:
    lfbono2=0
licostot=liacum-(lfbono1+lfbono2)
    
print "La cantidad de platos que comio el cliente es de: ",licont
print "La cantidad que debe pagar el cliente es de: ",licostot

#UPTP S1-T1