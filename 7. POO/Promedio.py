#!/usr/bin/env python
#-*- coding: UTF-8 -*-

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#Inicio

class ClsEstudiante(object):
	__Nombre=""
	__Apellido=""
	
	def __Init__(Self):
		Self.__Nombre=""
		Self.__Apellido=""
	
	def GetNombre(Self, pNombre):
		Self.__Nombre=pNombre
	
	def GetApellido(Self, pApellido):
		Self.__Apellido=pApellido
	
	def SetNombre(Self):
		return Self.__Nombre
	
	def SetApellido(Self):
		return Self.__Apellido

class ClsNotas(ClsEstudiante):
	__Nota1=""
	__Nota2=""
	__Nota3=""
	__Nota4=""
	
	def __Init__(Self):
		Self.__Nota1=0
		Self.__Nota2=0
		Self.__Nota3=0
		Self.__Nota4=0
	
	def GetNota1(Self, pNota1):
		Self.__Nota1=pNota1
	
	def SetNota1(Self):
		return Self.__Nota1
	
	def GetNota2(Self, pNota2):
		Self.__Nota2=pNota2
	
	def SetNota2(Self):
		return Self.__Nota2
	
	def GetNota3(Self, pNota3):
		Self.__Nota3=pNota3
	
	def SetNota3(Self):
		return Self.__Nota3
	
	def GetNota4(Self, pNota4):
		Self.__Nota4=pNota4
	
	def SetNota4(Self):
		return Self.__Nota4

class ClsPromedio(ClsNotas):
	__Promedio=""
	
	def __Init__(Self):
		Self.__Promedio=0
	
	def SetPromedio(Self, pNota1, pNota2, pNota3, pNota4):
		Self.__Promedio=(pNota1+pNota2+pNota3+pNota4)/4
		return Self.__Promedio

class ClsCalificaciones(ClsPromedio):
	__Calificacion=""
	
	def __Init__(Self):
		Self.__Calificacion=""
	
	def SetCalificacion(Self):
		if Self.__Nota>=12:
			print "Aprobo"
		else:
			print "Reprobo"

#Programa:

Seguir="S"
Estudiante=ClsEstudiante()

while(Seguir=="S"):
	NomE=raw_input("Nombre: ")
	ApeE=raw_input("Apellido: ")
	Nota1E=int(raw_input("Nota1: "))
	Nota2E=int(raw_input("Nota2: "))
	Nota3E=int(raw_input("Nota3: "))
	Nota4E=int(raw_input("Nota4: "))
	Estudiante.GetNombre(NomE)
	Estudiante.GetApellido(ApeE)
	print Estudiante.SetNombre(), Estudiante.SetApellido()  
	print Nota.SetNota1(), Nota.SetNota2(), Nota.SetNota3(), Nota.SetNota4()
	print Promedio.SetPromedio()
	print Calificaciones.SetCalificacion()
	Seguir=raw_input("Continuar(S/N) ")

#UPTP S2-T1