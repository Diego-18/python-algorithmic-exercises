#!usr/bin/env python
# -*- coding: UTF8 -*-

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

#Programa

Persona=clsPersona()
VarNombre=raw_input("Nombre: ")
VarApellido=raw_input("Apellido: ")
Persona.GetNombre(VarNombre)
Persona.GetApellido(VarApellido)
print Persona.SetNombre(), Persona.SetApellido()
Persona.Saludar()
