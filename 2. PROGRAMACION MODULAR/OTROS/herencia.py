#!usr/bin/env python
# -*- coding: UTF8 -*-
import os

class clsPersona (object):                 # "clsPersona" "cls" significa= Clase u objeto
	Nombre=''
	Apellido=''
	
	def __init__(self):           # "__init__" es el inicializador del objeto o clase, es indispensable en todo procedimiento de una clase u objeto
		self.Nombre=""
		self.Apellido=""
	
	def GetNombre(self,Pnombre):               # "Get" significa= Obtener la información
		self.Nombre=Pnombre
		
	def GetApellido(self,Papellido):
		self.Apellido=Papellido
		
	def SetNombre(self):                       # "Set" significa= Enviar la información a la pantalla
		return self.Nombre
		
	def SetApellido(self):
		return self.Apellido
		
	def Saludar(self):                         # "Self" significa= Guardar, en sí mismo todo
		print ("Hola")

class clsEstudiante(clsPersona):
	Nota=""
	def __init__(self):
		self.Nota=0
	
	def GetNota(self,pnota):
		self.Nota=pnota
		
	def SetNota(self):
		return self.Nota
		
	def Despedida(self):
		print ("Adiós...")

#Programa

seguir="s"
Estudiante=clsEstudiante()
while (seguir=="s" or seguir=="S"):
	Nombre=raw_input("Nombre: ")
	Apellido=raw_input("Apellido: ")
	Notaf=int(raw_input("Nota: "))
	Estudiante.GetNombre(Nombre)
	Estudiante.GetApellido(Apellido)
	Estudiante.GetNota(Notaf)
	print Estudiante.SetNombre(), Estudiante.SetApellido(), Estudiante.SetNota()
	Estudiante.Saludar()
	seguir=raw_input("Continuar (s/n): ")
Estudiante.Despedida()
