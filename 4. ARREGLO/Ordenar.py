#!/usr/bin/env python
# -*- coding: utf-8 -*-

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#Arreglo capaz de Buscar, Ordenar

def fiLeerI(psTexto):
	liVar=int(raw_input(psTexto))
	return liVar

def fiPartir(paArreglo, piInicio, piFin):
    liMarca = paArreglo[piFin]
    liComienzo = piInicio-1
    liFinal = piFin
    liListo = 0
    while not liListo:
        while not liListo:
            liComienzo = liComienzo+1
            if liComienzo == liFinal:
                liListo = 1
                break
            if paArreglo[liComienzo] > liMarca:
                paArreglo[liFinal] = paArreglo[liComienzo]
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


def faQuicksort(paArreglo, piInicio, piFin):
    if piInicio < piFin:
        liMitad = fiPartir(paArreglo, piInicio, piFin)
        faQuicksort(paArreglo, piInicio, liMitad-1)
        faQuicksort(paArreglo, liMitad+1, piFin)
    else:
        return

def faBurbuja(paArreglo):
	liTamano=len(paArreglo)
	for liX in range(0,liTamano):
		for liJ in range(liX,liTamano-1):
			if paArreglo[liX]>paArreglo[liJ+1]:
				liAux=paArreglo[liX]
				paArreglo[liX]=paArreglo[liJ+1]
				paArreglo[liJ+1]=liAux
	return paArreglo

def fiBuscar(paArreglo,piNum):
	liTamano=len(paArreglo)
	for liI in range(0,liTamano):
		if (paArreglo[liI]==piNum):
			return liI
	return -1

laArreglo = []
for liI in range(0,10):
	liNum=fiLeerI("Numero: ")
	laArreglo.append(liNum)
print laArreglo
liInicio = 0
liFin = len(laArreglo)-1
faQuicksort(laArreglo,liInicio,liFin)
print laArreglo
print fiBuscar(laArreglo,6)

#UPTP S1-T1