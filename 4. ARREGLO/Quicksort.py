#!/usr/bin/env python
#-*- coding: UTF-8 -*-                                                                                                           fe

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#Algoritmo capaz de Ordenar datos de un arreglo por metodo quicksort

def fiLeerI(piTexto):
	liNum=int(raw_input(piTexto))
	return liNum

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

#Programa

laArreglo=[]

for liX in range (0,10):
	liNum=fiLeerI("Numero: ")
	laArreglo.append(liNum)
print laArreglo
liInicio = 0
liFinal=len(laArreglo)-1
faQuicksort(laArreglo,liInicio,liFinal)
print laArreglo

#UPTP S1-T1