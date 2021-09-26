#! usr/bin/env python
# -*- coding: utf8 -*-
import os
from collections import deque

#Objeto
class clsPersona (object):
	Nombre=""
	Apellido=""
	
	def _Init_(Self):
		self.Nombre= ""
		self.Apellido= ""
		
	def GetNombre(Self,pNombre):
		Self.Nombre= pNombre
		
	def GetApellido(Self,pApellido):
		Self.Apellido= pApellido
		
	def SetNombre(Self):
		return Self.Nombre
		
	def SetApellido (Self):
		return Self.Apellido
	
	def Saludar (Self):
		print ("Hola")
		
class Estudiante(clsPersona):
	Notaf=""
	
	def _Init_(Self):
		self.Notaf=0
	
	def GetNota(Self,pNotaf):
		Self.Notaf= pNotaf
	
	def SetNota(Self):
		return Self.Notaf
	
	def Despedir (Self):
		print ("Adios")

#Programa
Persona = clsPersona()
Hijo = Estudiante()
varNombre= raw_input("Nombre: ")
varApellido= raw_input("Apellido: ")
varNombre2= raw_input("Nombre: ")    #Hacer una variable de Nombre para el Hijo
varApellido2= raw_input("Apellido: ")#Igual para el Apellido
varNota= int(raw_input("Nota :"))
Persona.GetNombre (varNombre)
Persona.GetApellido (varApellido)
print Persona.SetNombre() , Persona.SetApellido()
Persona.Saludar()

Hijo.GetNombre(varNombre2)
Hijo.GetApellido(varApellido2)
Hijo.GetNota(varNota)
print Hijo.SetNombre(), Hijo.SetApellido(),"Su nota es", Hijo.SetNota()
Hijo.Despedir()
