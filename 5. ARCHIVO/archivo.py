#!/usr/bin/env/ python
#-*- coding:UTF8-*-

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#inicio
import os

def fsCadena (psTexto):
	lsVar=raw_input(psTexto)
	return lsVar

def fiEntero(psTexto):
	liVar=int(raw_input(psTexto))
	return liVar

def fsContinuar():
	return fsCadena("pulse enter para continuar")

def foNuevoA(poArchivo):
	lsContenido=fsCadena("contenido ")
	poArchivo=open("132.txt ","w")
	poArchivo.write(lsContenido)
	poArchivo.close
	return poArchivo
	
def foLeerA(poArchivo):
	poArchivo=open("132.txt ","r")
	lsContenido=poArchivo.read()
	print lsContenido
	poArchivo.close
	fsContinuar()
	return poArchivo
	
def foEditarA(poArchivo):
	poArchivo=open("132.txt ","r+")
	lsContenido=poArchivo.read()
	print lsContenido
	lsContenido=fsCadena("agregar contenido ")
	poArchivo.write(lsContenido)
	poArchivo.close()
	return poArchivo

def fiMenu():
	os.system ("cls")
	print "1.- Nuevo Archivo"
	print "2.- Leer Archivo"
	print "3.- Editar Archivo"
	print "0.- Salir"
	liOpcion=fiEntero("Introduzca su opcion ")
	return liOpcion 

"""
loArchivo=open("archivo.txt", "w")                               #abrir archivo para escribir w=write(escribir)
loArchivo.write("seccion 132, edwin y maria, en el salon")       #escribie
loArchivo.close                                                  #cierra y guarda
#crea un archivo llamado archivo.txt que dice seccion 132, edwin y maria, lo cierra y lo guarda


loArchivo=open("archivo.txt", "r")      #abre el archivo para leer r=read(leer)
lsContenido=loArchivo.read()            #agrega el contenido del archivo a la variable lsContenido
print lsContenido                       #muestra lo que contiene la vaariable lsContenido
loArchivo.close                         #esta demas


loArchivo=open("archivo.txt", "r+")           #abre el archivo para leer y escribr
lsContenido=loArchivo.read()                  #agrega el contenido del archivo a la variable lsContenido
print lsContenido                             #muestra lo que contiene la vaariable lsContenido
lsContenido=" algoritmica y programacion"     #indica que en la variable lsContenido vale lo que este entre ->""
loArchivo.write(lsContenido)                  #agrega al archivo lo que esta en lsContenido
loArchivo.close                               #cierra
"""

liOpcion=9   #liOpcion vale nueve para entrar al while
loArchivo=""
while (liOpcion!=0):
	liOpcion=fiMenu()
	if(liOpcion==1):
		foNuevoA(loArchivo)
	if (liOpcion ==2):
		foLeerA(loArchivo)
	if (liOpcion==3):
		foEditarA(loArchivo)
	if (liOpcion==0):
		print "adios"
		fsContinuar()

#UPTP S1-T1