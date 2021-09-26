#!/usr/bin/env python
#-*- coding: UTF8 -*-

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#Algoritmo capaz de crear, leer, editar un archivo 

import os
def fsLeerS(psTexto):
	lsVar=raw_input(psTexto)
	return lsVar

def fiLeerI(psTexto):
	liVar=int(raw_input(psTexto))
	return liVar

def fsContinuar():
	return fsLeerS("Pulse Enter")

def fiMenu():                                 #Muestra un menu
	os.system("clear")
	print "1.- Nuevo Archivo"
	print "2.- Leer Archivo"
	print "3.- Editar Archivo"
	print "0.- Salir"
	liOpcion=fiLeerI("Introduzca su opción: ")
	return liOpcion

def foNuevoA(poArchivo):
	os.system("clear")
	lsContenido=fsLeerS("Contenido: ")
	poArchivo=open("132.txt","w")
	poArchivo.write(lsContenido)
	poArchivo.close()
	return poArchivo

def foLeerA(poArchivo):
	os.system("clear")
	poArchivo=open("132.txt", "r")
	lsContenido=poArchivo.read()
	print lsContenido
	poArchivo.close()
	fsContinuar()
	return poArchivo

def foEditarA(poArchivo):
	os.system("clear")
	poArchivo=open("132.txt","r+")
	lsContenido=poArchivo.read()
	print lsContenido
	lsContenido=fsLeerS ("Agregar contenido: ")
	poArchivo.write(lsContenido)
	poArchivo.close()
	return poArchivo

#Programa

liOpcion=9
loArchivo=" "
while (liOpcion!=0):
	liOpcion=fiMenu()
	if (liOpcion==1):
		foNuevoA(loArchivo)
	if (liOpcion==2):
		foLeerA(loArchivo)
	if (liOpcion==3):
		foEditarA(loArchivo)
	if (liOpcion==0):
		print "Adiós"
	fsContinuar()

#UPTP S1-T1