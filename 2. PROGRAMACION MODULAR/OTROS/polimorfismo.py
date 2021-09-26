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


class clsEstudiante (clsPersona):
	Nota=""
	def __init__(self):
		self.nota=0
	def GetNota(self,pNota):
		self.Nota=pNota
	def SetNota(self):
		return self.Nota
	def Saludar(self):
		print ("Epale")

class clsProfesor (clsPersona):
	Sueldo=""
	def __init__(self):
		self.Sueldo=0
	def GetSueldo(self,pSueldo):
		self.Sueldo=pSueldo
	def SetSueldo(self):
		return self.Sueldo
	def Saludar(self):
		print ("Buenos días")

#Programa
Seguir="s"
Estudiante=clsEstudiante()
Docente=clsProfesor()
while (Seguir=="s" or Seguir=="S"):
	print ("Datos del Estudiante")
	Nombre_E=raw_input("Nombre del estudiante: ")
	Apellido_E=raw_input("Apellido del estudiante: ")
	Nota_E=raw_input("Nota del estudiante: ")
	Estudiante.GetNombre(Nombre_E)
	Estudiante.GetApellido(Apellido_E)
	Estudiante.GetNota(Nota_E)
	print ("La nota del estudiante"), Estudiante.SetNombre(), Estudiante.SetApellido(), ("es de:"), Estudiante.SetNota(), ("puntos")
	Estudiante.Saludar()
	print ("Datos del Docente")
	Nombre_P=raw_input("Nombre del docente: ")
	Apellido_P=raw_input("Apellido del docente: ")
	Sueldo_P=raw_input("Sueldo del docente: ")
	Docente.GetNombre(Nombre_P)
	Docente.GetApellido(Apellido_P)
	Docente.GetSueldo(Sueldo_P)
	print ("El sueldo del docente"), Docente.SetNombre(), Docente.SetApellido(), ("es de:"), Docente.SetSueldo(), ("Bsf.")
	Seguir=raw_input("Continuar (s/n): ")
