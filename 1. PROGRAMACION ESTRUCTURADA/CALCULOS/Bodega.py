#!/usr/bin/env python
#-*-coding:UTF8-*-

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#Elabore un programa que calcule el monto a pagar de una factura de una bodega, considere que todos los articulos pagan el iva del 12% muestre la cantidad de articulos que llevo la persona.
lsseguir="s"
licont=0
lfacum=0

while lsseguir=="s" or lsseguir=="S":
	lsarticulo=raw_input("Introduzca el articulo: ")
	lfarticulo=float(raw_input("Introduzca el precio del articulo: "))
	licantidad=int(raw_input("Introduzca el numero de articulos: "))
	licont=licont+licantidad
	licosto=licantidad*lfarticulo
	lffactura=(lfarticulo*0.12)+licosto
	lfacum=lfacum+lffactura
	lsseguir=raw_input("Desea seguir? (S/N) ")
	while lsseguir=="s" or lsseguir=="S":
		lsarticulo=raw_input("Introduzca el nombre del articulo: ")
		lfarticulo=float(raw_input("Introduzca el precio del articulo: "))
		licantidad=int(raw_input("Introduzca el numero de articulos: "))
		licosto=licantidad*lfarticulo
		lffactura=(lfarticulo*0.12)+licosto
		lfacum=lfacum+lffactura
		lsseguir=raw_input("Desea seguir? (S/N) ")
		licont=licont+licantidad
print "La cantidad de aticulos que llevo el cliente es: ",licont
print "El monto a pagar del cliente es: ",lfacum

#UPTP S1-T1