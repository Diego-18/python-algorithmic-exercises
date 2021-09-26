#!/usr/bin/env python
# -*- coding: UTF8 -*-

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#Algoritmo capaz de calcular la comision de un vendedor por ventas generadas 

lsseguir="s"
lfacum=0
lsnombre=raw_input("Introduzca el nombre del vendedor: ")

while (lsseguir=="S") or (lsseguir=="s"):
    lfventa1=float(raw_input("Introduzca la venta numero uno: "))
    lfventa2=float(raw_input("Introduzca la venta numero dos: "))
    lfventa3=float(raw_input("Introduzca la venta numero tres: "))
    lfventa4=float(raw_input("Introduzca la venta numero cuatro: "))
    lsseguir=raw_input("Desea seguir? (S/N)")
    if (lsseguir=="s") or (lsseguir=="S"):
        lfventaa=float(raw_input("Introduzca la venta adicional: "))
        lfventat=lfventa1+lfventa2+lfventa3+lfventa4+lfventaa
        lfcomision=lfventat*0.10
        lfacum=lfacum+lfcomision
    else:
        lfventat=lfventa1+lfventa2+lfventa3+lfventa4
        lfcomision=lfventat*0.10
        lfacum=lfacum+lfcomision
    lsseguir=raw_input("Desea seguir? (S/N)")
print "El vendedor gano una comision por sus ventas totales de: ",lfacum

#UPTP S1-T1