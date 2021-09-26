#!/usr/bin/env python
# -*- coding: utf-8 *-*

"""
visPersona.py
Copyright 2014 José B. Silva H. y Pausides D. Calderon

Este programa es software libre; usted puede redistribuirlo y / o modificarlo
Bajo los términos de la Licencia Pública General de GNU según lo publicado por
La Fundación para el Software Libre; ya sea la versión 2 de la Licencia, o
(A su elección) cualquier versión posterior.
Este programa se distribuye con la esperanza de que sea útil,
Pero SIN NINGUNA GARANTÍA; ni siquiera la garantía implícita de
COMERCIALIZACIÓN o IDONEIDAD PARA UN PROPÓSITO PARTICULAR. consulte la
GNU General Public License para más detalles.
"""
import os

def fsLeerS(psTexto):
	lsVar=raw_input(psTexto)
	return lsVar

def fsContinuar():
	return fsLeerS("Pulse Enter para Continuar")

class visPersona(object):
	
	#Vista del menú de opciones
	def fiMenu(self):
		os.system("cls")
		lsMenu = "Menu del Gestor de Persona \n"
		lsMenu += "(1) Crear una persona \n"
		lsMenu += "(2) Ver listado de personas \n"
		lsMenu += "(3) Buscar una persona \n"
		lsMenu += "(4) Editar una persona \n"
		lsMenu += "(5) Eliminar una persona \n"
		lsMenu += "(0) Salir \n"
		print lsMenu
		liOpcion = int(raw_input("Introduzca su opcion: "))
		return liOpcion
	
	#Vista del formulario para crear nueva persona
	def fsCrear(self):
		print "CREAR UNA NUEVA PERSONA"
		lsCedula = raw_input("Introduzca el numero de cedula de identidad: ")
		lsNombres = raw_input("Introduzca los nombres de la persona: ")
		lsApellidos = raw_input("Introduzca los apellidos de la persona: ")
		return lsCedula,lsNombres,lsApellidos
    
    #Vista de confirmación de operacion
	def fsMensaje(self):
		print "Operacion realizada con exito!"
		fsContinuar()
		
		
	
	#Vista del Listado de las personas
	def fsListar(self,paArreglo):
		print "LISTADO DE PERSONAS"
		for laRegistro in paArreglo:
			print "Cedula: "+laRegistro[0]+ " Nombres: "+laRegistro[1]+" Apellidos: "+laRegistro[2]
		fsContinuar()
	
	#Vista del formulario de busqueda
	def fsBuscar(self):
		print "BUSCAR UNA PERSONA"
		lsCedula = raw_input("Introduzca el número de cédula de identidad: ")
		return lsCedula
	
	#Vista de muestra de una persona
	def fsMostrar(self,psCedula,psNombres,psApellidos):
		print "Cedula: "+psCedula+ " Nombres: "+psNombres+" Apellidos: "+psApellidos
		fsContinuar()
	
	#Vista del formulario de modificar una persona
	def fsModificar(self):
		print "MODIFICAR UNA PERSONA"
		lsNombres = raw_input("Introduzca los nombres de la persona: ")
		lsApellidos = raw_input("Introduzca los apellidos de la persona: ")
		return lsNombres,lsApellidos

