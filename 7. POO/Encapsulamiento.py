#!/usr/bin/env python 
#-*- coding: UTF-8 -*-

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#Inicio

class ClsPersona(object):         #Se coloca el piso o guion para transformar las variables publicas en privadas (Encapsulamiento)...
	__Nombre=""				 #Este metodo utiliza Get y Set (obligatoriamente) ya que accesar por otro metodo es imposible...
	__Apellido=""
	
	def __Init__(Self):			
		Self.__Nombre=""			
		Self.__Apellido=""
		
	def GetNombre(Self,pnombre): 
		Self.__Nombre=pnombre
		
	def GetApellido(Self,papellido):
		Self.__Apellido=papellido
	
	def SetNombre(Self):		
		return Self.__Nombre
	
	def SetApellido(Self):		
		return Self.__Apellido

class ClsEstudiante(ClsPersona):
	__Nota=""
	
	def __Init__(Self):			
		Self.__Nota=0
	
	def GetNota(Self,pnota):
		Self.__Nota=pnota
	
	def SetNota(Self):
		return Self.__Nota
	
	def Saludar(Self):
		print ("Epale Brother")

class ClsProfesor(ClsPersona):
	__Sueldo=""
	
	def __Init__(Self):
		Self.__Sueldo=0
		
	def GetSueldo(Self, psueldo):
		Self.__Sueldo=psueldo
	
	def SetSueldo(Self):
		return Self.__Sueldo
	
	def Saludar(Self):
		print ("Buenos Dias")

#Programa:
Seguir="S"
Estudiante=ClsEstudiante()
Docente=ClsProfesor()
O=0

while(Seguir=="S"):
	print ("1.Docente, 2.Alumno")
	O=int(raw_input("Introduzca su opcion: "))
	if (O==2):
		print ("Datos Estudiante: ")
		NomE=raw_input("Nombre: ")
		ApeE=raw_input("Apellido: ")
		NotaE=int(raw_input("Nota: "))
		Estudiante.GetNombre(NomE)
		Estudiante.GetApellido(ApeE)
		Estudiante.GetNota(NotaE)
		print Estudiante.SetNombre(), Estudiante.SetApellido(), Estudiante.SetNota()
		Estudiante.Saludar()
		
	if (O==1):
		print ("Datos Docente: ")
		NomP=raw_input("Nombre: ")
		ApeP=raw_input("Apellido: ")
		SueldoP=float(raw_input("Sueldo: "))
		Docente.GetNombre(NomP)
		Docente.GetApellido(ApeP)
		Docente.GetSueldo(SueldoP)
		print Docente.SetNombre(), Docente.SetApellido(), Docente.SetSueldo()
		Docente.Saludar()
		
	Seguir=raw_input("Continuar(S/N) ")
#UPTP S2-T1