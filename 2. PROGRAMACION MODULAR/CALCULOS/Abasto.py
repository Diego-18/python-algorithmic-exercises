#!/usr/bin/env python
#-*- coding: UTF8 -*-

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#Algoritmo capaz de facturar ciertos articulo vendidos, calculando descuentos y el total de ventas al dia

#Funciones
def fileerI(psTexto):
	liVar=int(raw_input(psTexto))
	return liVar

def fsleerS(psTexto):
	lsVar=raw_input(psTexto)
	return lsVar

def ffleerF(psTexto):
	lfVar=float(raw_input(psTexto))
	return lfVar

def ffMulti(piN1,piN2):
	return piN1*piN2

#Progrmama
lsCliente="s"
lsArticulo="s"
lfAcumT=0
lfAcumC=0
lfdescuento1=0.05
lfdescuento2=0.10
lfdescuento3=0.15

while (lsCliente=="S" or lsCliente=="s"):
	lsNombre=fsleerS("Nombre: ")
	while (lsArticulo=="S" or lsArticulo=="s"):
		lsArticulo=fsleerS("Articulo: ")
		liCantidad=fileerI("Cantidad: ")
		lfPrecio=ffleerF("Precio: ")
		if (liCantidad>3):
			print "Solo se debe llevar 3"
			liCantidad=fileerI("Cantidad: ")
		lfAcumC=lfAcumC+ffMulti(liCantidad,lfPrecio)
		lsArticulo=fsleerS("Hay otro articulo: ")
	if (lfAcumC<500):
		lfdescuento=ffMulti(lfAcumC,lfdescuento1)
	if (lfAcumC>500) and (lfAcumC<1000):
		lfdescuento=ffMulti(lfAcumC,lfdescuento2)
	if (lfAcumC>1000):
		lfdescuento=ffMulti(lfAcumC,lfdescuento3)
	lfAcumT=lfAcumT+(lfAcumC-lfdescuento)
	print "El total a Pagar es",(lfAcumC-lfdescuento)
	lfAcumC=0
	lsCliente=fsleerS("Hay otro cliente: ")
print "El total de venta del dia es: ",lfAcumT
#Fin

#UPTP S1-T1