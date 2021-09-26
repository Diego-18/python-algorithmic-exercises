#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os
from collections import deque

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#Funciones:

def fiEntero(psTexto):
	liVarI=int(raw_input(psTexto))
	return liVarI

def fsCadena(psTexto):
	lsVarS=raw_input(psTexto)
	return lsVarS

def fsContinuar():
	return fsCadena("Presione ENTER para continuar")

def faCargarP(paArreglo):
	os.system("clear")
	lsColor=fsCadena("Introduzca el Color: ")
	paArreglo.append(lsColor)
	return paArreglo


def faCargarC(paArreglo):
	os.system("clear")
	lsNombre=fsCadena("Introduzca el nombre: ")
	paArreglo.append(lsNombre)
	return paArreglo

def faImprimir(paArreglo):
	for liX in range(0,5):
		print paArreglo[liX]
	fsContinuar()

def faSacar(paArreglo,paArreglo2):
	lsColor=paArreglo2.pop()
	if lsColor=="Azul":
		lfDescuento=0.05
	elif lsColor=="Morado":
		lfDescuento=0.10
	elif:
		lfDescuento=0
		
	print paArreglo.popleft()
	print "Que desea llevar?"
	print "1.Combo 1, 2.Combo 2, Combo 3"
	liOps=fiEntero("Introduzca la Opcion: ")
	liCant=fiEntero ("Cuantos desea llevar?: ")
	
	if liOps==1:
		lfMonto=(liCant*200)
		lfDes=lfMonto*lfDescuento
		lfTotal=lfMonto-lfDes
		print ("El monto a pagar es: "), lfTotal
		fsContinuar()
	
	elif liOps==2:
		lfMonto=(liCant*300)
		lfDes=lfMonto*lfDescuento
		lfTotal=lfMonto-lfDes
		print ("El monto a pagar es: "), lfTotal
		fsContinuar()	
		
	elif liOps==3:
		lfMonto=(liCant*400)
		lfDes=lfMonto*lfDescuento
		lfTotal=lfMonto-lfDes
		print ("El monto a pagar es: "), lfTotal		
	
		fsContinuar()
	
def fiMenu():
	os.system("clear")
	print "1.Cargar Pila"
	print "2. Cargar Cola"
	print "3. Imprimir 5 primeros"
	print "4. Atender"
	print "5. Salir"
	liOpcion=fiEntero("Introduzca la Opcion: ")
	return liOpcion

#Programa:

laPila=[]
laCola=deque([])
liOpcion=9
liOps=0
lfTotal=()


while (liOpcion!=5):
    liOpcion=fiMenu()
    if (liOpcion==1):
        faCargarP(laPila)
		
    if (liOpcion==2):
        faCargarC(laCola)
		
    if (liOpcion==3):
        faImprimir(laCola)
		
    if (liOpcion==4):
        faSacar(laCola, laPila)
		
    if (liOpcion==5):
        print "Adios"
        print "Gracias por su compra"
        fsContinuar()
#UPTP S2-T1