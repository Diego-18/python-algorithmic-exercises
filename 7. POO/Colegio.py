#!usr/bin/env python
#!-*- coding: utf8  -*-

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

"""
clase persona

estudiante 4notas y promedio, y si esta aprobado o reprobado, si tiene mas de 15 tiene beca estudio, 
si tiene menos de 15 tiene beca comedor
 
 profesor sueldo depediendo de las horas q trabaja y si tiene mas de 36 horaws se considera
 dedicacion exclusiva tiene aumento de 15% sobre su suieldo base y tiene bono por hijo q tenga de 1000 x c/u
las horas valen 100
"""

import os

class clsPersona(object):
	__aNombre=""
	__aApellido=""
	__aCedula=""
	
	def __init__(self):
		self.__aNombre
		self.__aApellido
		self.__aCedula
	
	def GetNombre(self,pNombre):
		self.__aNombre=pNombre
	def setNombre(self):
		return self.__aNombre
		
	def GetApellido(self, pApellido):
		self.__aApellido=pApellido
	def setApellido(self):
		return self.__aApellido
		
	def GetCedula(self, pCI):
		self.__aCedula=pCI
	def setCedula(self):
		return self.__aCedula



class clsEstudiante(clsPersona):
	__aNota1=""
	__aNota2=""
	__aNota3=""
	__aNota4=""
	__aPromedio=""
	
	def __init__(self):
		self.__aNota1=0
		self.__aNota2=0
		self.__aNota3=0
		self.__aNota4=0
		self.__aPromedio=0
	
	def GetNota1(self,pNota1):
		self.__aNota1=pNota1
	def setNota1(self):
		return self.__aNota1
		
	def GetNota2(self,pNota2):
		self.__aNota2=pNota2
	def setNota2(self):
		return self.__aNota2

	def GetNota3(self,pNota3):
		self.__aNota3=pNota3
	def setNota3(self):
		return self.__aNota3

	def GetNota4(self,pNota4):
		self.__aNota1=pNota4
	def setNota4(self):
		return self.__aNota4

	def ffPromedio(self,pNota1, pNota2, pNota3, pNota4):
		lfPromedio= (pNota1 + pNota2 + pNota3 + pNota4) / 4
		if lfPromedio>=15 :
			print "Tiene Beca Estudio "
		else:
			print "Tiene Beca Comedor "
		print "su pormedio es "
		return lfPromedio


class clsProfesor(clsPersona):
	__aHijo=""
	__aHoras=""
	
	def __init__(self):
		__aHijo=0
		__aHoras=0

	def GetHijo(self,pHijo):
		self.__aHijo=pHijo
	def setHijo(self):
		return self.__aHijo

	def GetHoras(self,pHoras):
		self.__aHoras=pHoras
	def setHoras(self):
		return self.__aHoras

	def ffSueldo(self):
		lfDedicacion=0
		lfBonoH=0
		lfSueldoB= self.__aHoras * 100
		
		if self.__aHoras >= 36:
			lfDedicacion= lfSueldoB*0.15
			print "Ha trabajado mas de 36 horas tiene bono de dedicacion exclusiva de ", lfDedicacion
		
		if self.__aHijo >=1 :
			lfBonoH= self.__aHijo * 1000
			print "Tiene un bono de hijos de ", lfBonoH
	
		lfSueldoNeto=lfSueldoB + lfDedicacion + lfBonoH
		print "Su sueldo neto es "
		return lfSueldoNeto


def fsCadena(psTexto):
	lsVar=raw_input(psTexto)
	return lsVar

def fiEntero(piTexto):
	liVar=int(raw_input(piTexto))
	return liVar

def ffFlotante(pfTexto):
	lfVar=int(raw_input(pfTexto))
	return lfVar

def fiMenu():
	os.system ("clear")
	print "1. Estudiante"
	print "2. Profesor "
	print "0. Salir "
	liOpcion=fiEntero("Introduzca su opcion ")
	return liOpcion

def fsContinuar():
	return fsCadena("pulse una tecla para continuar ")
	
Estudiante=clsEstudiante()
Profesor=clsProfesor()
liOpcion=9

while liOpcion!= 0 :
	liOpcion=fiMenu()


	if liOpcion==1:
		print "DATOS DEL ESTUDIANTE"
		lsNombreE=fsCadena("Introduzca su nombre ")
		lsApellidoE=fsCadena("Introduzca su Apellido ")
		lsCIE=fsCadena("Introduzca su cedula ")
		lfNota1=ffFlotante("Introduzca la nota 1 ")
		lfNota2=ffFlotante("Introduzca la nota 2 ")
		lfNota3=ffFlotante("Introduzca la nota 3 ")
		lfNota4=ffFlotante("Introduzca la nota 4 ")

		Estudiante.GetNombre(lsNombreE)
		Estudiante.GetApellido(lsApellidoE)
		Estudiante.GetCedula(lsCIE)
		Estudiante.GetNota1(lfNota1)
		Estudiante.GetNota1(lfNota2)
		Estudiante.GetNota1(lfNota3)
		Estudiante.GetNota1(lfNota4)

		print Estudiante.setNombre() , Estudiante.setApellido() , Estudiante.setCedula()
		print Estudiante.ffPromedio(lfNota1,lfNota2, lfNota3,lfNota4)
		fsContinuar()


	if liOpcion==2:
		print "DATOS DEL PROFESOR"
		lsNombreP=fsCadena("Introduzca su nombre ")
		lsApellidoP=fsCadena("Introduzca su Apellido ")
		lsCIP=fsCadena("Introduzca su cedula ")
		liHijo=fiEntero("Cuantos hijos tiene? ")
		liHoras=fiEntero("Cuantas horas ha trabajado? ")
		
		Profesor.GetNombre(lsCIP)
		Profesor.GetApellido(lsApellidoP)
		Profesor.GetCedula(lsCIP)
		Profesor.GetHijo(liHijo)
		Profesor.GetHoras(liHoras)
		
		print Profesor.setNombre() , Profesor.setApellido() , Profesor.setApellido()
		print Profesor.ffSueldo()
		
		fsContinuar()


	if liOpcion==0:
		print "Adios"
	
#UPTP S2-T1