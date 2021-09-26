#!/usr/bin/env python
#-*- coding: UTF-8 -*-
import os 

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#Algoritmo capaz de Cargar, Ordenar, Eliminar, Buscar, Imprimir datos de un arreglo

#Funciones
def fsLeerS(psTexto):
	lsVarS=raw_input(psTexto)
	return lsVarS

def fiLeerI(psTexto):
	liVarI=int(raw_input(psTexto))
	return liVarI

def ffLeerF(psTexto):
	lfVarF=float(raw_input(psTexto))
	return lfVarF

def fiPartir(paArreglo,piInicio,piFinal):
	liMarca = paArreglo[piFinal]
	liComienzo = piInicio-1
	liFinal = piFinal
	liListo = 0
	while not liListo:
		while not liListo:
			liComienzo=liComienzo+1
			if (liComienzo==liFinal):
				liListo = 1
				break
			if (paArreglo[liComienzo]>liMarca):
				paArreglo[liFinal]=paArreglo[liComienzo]
				break
		while not liListo:
			liFinal = liFinal-1
			if liFinal == liComienzo:
				liListo = 1
				break 
			if paArreglo[liFinal] < liMarca:
				paArreglo[liComienzo] = paArreglo[liFinal]
				break
	paArreglo[liFinal] = liMarca
	return liFinal
	
def faQuicksort(paArreglo,piInicio,piFinal):
	if piInicio < piFinal:
		liMitad = fiPartir(paArreglo,piInicio,piFinal)
		faQuicksort(paArreglo,piInicio,liMitad-1)
		faQuicksort(paArreglo,liMitad+1,piFinal)
	else:
		return 

def fiBuscar(paArreglo,piNum):
	liTamano=len(paArreglo)
	for liI in range(0,liTamano):
		if (paArreglo[liI]==piNum):
			return liI
	return -1

def faBurbuja(paArreglo):
	litamano=len(paArreglo)
	for liX in range (0,litamano-2):
		for liJ in range (liX,litamano-1):
			if (paArreglo[liX]>paArreglo[liJ+1]):
				liAux=paArreglo[liX]
				paArreglo[liX]=paArreglo[liJ+1]
				paArreglo[liJ+1]=liAux
	return paArreglo

def faImprimir(paArreglo):
	print paArreglo

def faImprimir2(paArreglo):
	for liX in paArreglo:
		print liX

def faEliminar(paArreglo,piNum):
	liX=fiBuscar(paArreglo,piNum)
	if liX!=-1:
		del(paArreglo[liX])
	return paArreglo

def faCargar(paArreglo):
	liNum=fiLeerI("Introduzca el Numero: ")
	paArreglo.append(liNum)
	return paArreglo
	
def fiMenu():
	print "1.-Cargar Arreglo"
	print "2.-Ordenar Arreglo"
	print "3.-Buscar en el Arreglo"
	print "4.-Eliminar en el Arreglo"
	print "5.-Imprimir el Arreglo"
	print "6.-Imprimir Arreglo por posicion"
	print "0.-Salir"
	liOpcion=fiLeerI("Introduzca su opcion: ")
	return liOpcion

def fsContinuar():
        return fsLeerS("Pulse Enter")

#Programa
liOpcion=9
laArreglo=[]

while (liOpcion!=0):
	liOpcion=fiMenu()
	if (liOpcion==1):
		laArreglo=faCargar(laArreglo)
		
	if (liOpcion==2):
		liFinal=len(laArreglo)-1
		liInicio=0
		faQuicksort(laArreglo,liInicio,liFinal)
		
	if (liOpcion==3):
		liNum=fiLeerI("Introduzca el numero a buscar: ")
		liX=fiBuscar(laArreglo,liNum)
		if (liX==-1):
			print "No Existe"
		else:
			print "Existe en la posicion: ",liX
		fsContinuar()
			
	if (liOpcion==4):
		liNum=fiLeerI("Numero a eliminar: ")
		laArreglo=faEliminar(laArreglo,liNum)
		
	if (liOpcion==5):
		faImprimir(laArreglo)
		fsContinuar()
		
	if (liOpcion==6):
		faImprimir2(laArreglo)
		fsContinuar()
		
	if (liOpcion==0):
		print "Adios"
		fsContinuar()

#UPTP S1-T1