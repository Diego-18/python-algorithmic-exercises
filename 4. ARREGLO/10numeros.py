#!/usr/bin/env python
#-*- coding: UTF8 -*-

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#realize un algoritmo que cargue 10 numeros y los arreglo con quicksort

def fiLeerI(psTexto):
	liVar=int(raw_input(psTexto))
	return liVar
	
def fsLeerS(psTexto):
	lsVar=raw_input(psTexto)
	return lsVar
		
def ffLeerF(psTexto):
	lfVar=raw_input(psTexto)
	return lfVar

def fiPartir (paArreglo, piInicio, piFin):
	liMarca=paArreglo[piFin]
	liComienzo=piInicio-1
	liFinal=piFin
	liListo=0
	while not liListo:
		while not liListo:
			liComienzo=liComienzo+1
			if (liComienzo==liFinal):
				liListo=1
				break
			if (paArreglo[liComienzo]>liMarca):                #De menor a mayor (>)....de mayor a menor (<)
				paArreglo[liFinal]=paArreglo[liComienzo]
				break
		while not liListo:
			liFinal=liFinal-1
			if (liFinal==liComienzo):
				liListo=1
				break
			if (paArreglo[liFinal]<liMarca):                  #De menor a mayor(<)... de mayor a menor (>)
				paArreglo[liComienzo]=paArreglo[liFinal]
				break
	paArreglo[liFinal]=liMarca
	return liFinal
	
def faQuickSort(paArreglo,piInicio,piFin):
	if (piInicio<piFin):
		liMitad=fiPartir(paArreglo,piInicio,piFin)
		faQuickSort(paArreglo,piInicio,liMitad-1)
		faQuickSort(paArreglo,liMitad+1,piFin)
	else:
		return

#Programa
laArreglo=[]
for liX in range (0,10):
	liNum=fiLeerI("Número: ")
	laArreglo.append(liNum)
print laArreglo
liInicio=0
liFinal=len(laArreglo)-1
faQuickSort(laArreglo,liInicio,liFinal)
print laArreglo

