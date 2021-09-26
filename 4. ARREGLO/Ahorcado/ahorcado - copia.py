#!usr/bin/env python
#-*- coding: UTF8 -*-

import random
#import os
from os import system

def fsContinuar():
	return fsCadenaS ("\n\n     Por favor pulse enter para continuar ")

def fsCadenaS(pTexto):
	lsVar=raw_input(pTexto)
	return lsVar.upper()

def fsCadena(psTexto):
	liValidar=1
	while liValidar!=0:
		lsVar=raw_input(psTexto)
		if lsVar.isalpha()==True:
			liValidar=0
		else:
			print "       ATENCION: solo letras A...Z"
	return lsVar.upper()

def faCargarPiso (paArreglo, piTam):
	lsPiso="_"
	for liX in range (0, piTam):
		paArreglo.append(lsPiso)
	return paArreglo
	
def fsError(piError):
	if piError==1:#1 error
		lsCabeza="   \n\
      ,,,,,,    \n\
     /  _ _\    \n\
    c|  '.'|    \n\
     (  == )    \n\
   __|\_,_/ __  \n\
"
		return lsCabeza
	
	if piError==2:#2 errores
		lsTorax="\n\
      ,,,,,,    \n\
     /  _ _\    \n\
    c|  '.'|    \n\
     (  == )    \n\
   __|\_,_/ __  \n\
  /   \__/    \ \n\
    |       |   \n\
    |       |   \n\
    |       |   \n\
    |_______|   \n\
"
		return lsTorax
	
	if piError==3: #3 errores
		lsBrazos="\n\
      ,,,,,,     \n\
     /  _ _\     \n\
    c|  '.'|     \n\
     (  == )     \n\
   __|\_,_/ __   \n\
  /   \__/    \  \n\
  |__|     |__|  \n\
  | |       | |  \n\
  | |       | |  \n\
  | |_______| |  \n\
 (,,,)     (,,,) \n\
"
		return lsBrazos
	
	if piError==4: #4 errores
		lsPiernas="\n\
      ,,,,,,     \n\
     /  _ _\     \n\
    c|  '.'|     \n\
     (  == )     \n\
   __|\_,_/ __   \n\
  /   \__/    \  \n\
  |__|     |__|  \n\
  | |       | |  \n\
  | |       | |  \n\
  | |_______| |  \n\
 (,,,)     (,,,) \n\
    |  ___  |    \n\
    |  / \  |    \n\
"
		return lsPiernas
	if piError==5: #5 errores
		lsPies="\n\
      ,,,,,,     \n\
     /  _ _\     \n\
    c|  '.'|     \n\
     (  == )     \n\
   __|\_,_/ __   \n\
  /   \__/    \  \n\
  |__|     |__|  \n\
  | |       | |  \n\
  | |       | |  \n\
  | |_______| |  \n\
 (,,,)     (,,,) \n\
    |  ___  |    \n\
    |  / \  |    \n\
    |  | |  |    \n\
    |  | |  |    \n\
    |__|_|__|_   \n\
    (____)____)  \n\
"
		return lsPies
	
	if piError==6: #6 errores y fin
		lsMuerto="\n\
      ,,,,,,   /  \n\
     /  _ _\  /   \n\
    c|  x.x| /    \n\
     (   o )/     \n\
   __|\_,_//__    \n\
  /   \__/    \   \n\
  |__|     |__|   \n\
  | |       | |   \n\
  | | KILLER| |   \n\
  | |_______| |   \n\
 (,,,)     (,,,)  \n\
    |  ___  |     \n\
    |  / \  |     \n\
    |  | |  |     \n\
    |  | |  |     \n\
    |__| |__|     \n\
    | _| | _|     \n\
    |__| |__|     \n\
"
		return lsMuerto

laEspacios_Pisos=[]
laPalabras=["CASAS","ARBOLES","HOJA"]
laPistas=["todos viven en una","da oxigeno","escribimos en ellas"]
liOpcion=9


laDiccionarios={'house':'casa','red':'rojo','bed':'cama','window':'ventana'}

liPosicion=0

liTam=len(laPalabras[liPosicion])
#print liTam

liPisos=faCargarPiso(laEspacios_Pisos, liTam)
#print liPisos


print fsError(6)
fsContinuar()
system("cls")







