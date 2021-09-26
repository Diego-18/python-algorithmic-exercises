#!/usr/bin/env python
#-*- coding: UTF-8 -*-

#Inicio:

class Persona(object):
	Nombre=""
	Apellido=""
	Cedula=""
	
	def __Init__(self):
		self.Nombre=""
		self.Apellido=""
		self.Cedula=""
	
	def GetNombre(self, pnombre):
		self.Nombre=pnombre
	
	def GetApellido(self, papellido):
		self.Apellido=papellido
	
	def GetCedula(self, pcedula):
		self.Cedula=pcedula
	
	def SetNombre(self):
		return self.Nombre
	
	def SetApellido(self):
		return self.Apellido
	
	def SetCedula(self):
		return self.Cedula
	
	def Saludar(self):
		print "Buenos Dias"
	
	def Despedirse(self):
		print "Hasta Luego"

class Docente(Persona):
	Horas=""
	Cargo=""
	
	def __Init__(self):
		self.Horas=""
		self.Cargo=""
	
	def GetHoras(self, phoras):
		self.Horas=phoras
	
	def GetCargo(self, pcargo):
		self.Cargo=pcargo
	
	def SetHoras(self):
		return self.Horas
	
	def SetCargo(self):
		return self.Cargo
	
	def Calcular(self, vhoras, noc):
		sb=self.Horas*vhoras
		if (self.Cargo==1):
			car=(sb*0.10)
		elif (self.Cargo==2):
			car=(sb*0.15)
		else:
			car=(sb*0.20)
		if (noc=="S"):
			return sb+car+1500
		else:
			return sb+car

class Estudiante(Persona):
	Carrera=""
	Semestre=""
	UC=""
	
	def __Init__(self):
		self.Carrera=""
		self.Semestre=""
		self.UC=""
	
	def GetCarrera(self, pcarrera):
		self.Carrera=pcarrera
	
	def GetSemestre(self, psemestre):
		self.Semestre=psemestre
	
	def GetUC(self, puc):
		self.UC=puc
	
	def SetCarrera(self):
		return self.Carrera
	
	def SetSemestre(self):
		return self.Semestre
	
	def SetUC(self):
		return self.UC
	
	def Calcular(self, vuc):
		return self.UC*vuc

#Programa:

Docente=Docente()
Estudiante=Estudiante()
Seguir="S"
opc=0

while (Seguir=="S"):
	print "1.Docente 2.Estudiante 3.Salir"
	opc=int(raw_input("Opcion: "))
	
	if (opc==1):
		vhoras=200
		nomD=raw_input("Nombre: ")
		apellD=raw_input("Apellido: ")
		cedD=int(raw_input("Cedula: "))
		horD=int(raw_input("Horas L.: "))
		cargD=int(raw_input("1.Novato 2.Master"))
		noc=raw_input("Trabajo horas nocturnas?: ")
		Docente.GetNombre(nomD)
		Docente.GetApellido(apellD)
		Docente.GetCedula(cedD)
		Docente.GetHoras(horD)
		Docente.GetCargo(cargD)
		print Docente.SetNombre(), Docente.SetApellido(), Docente.SetCedula(), 
		print Docente.SetCargo(), Docente.SetHoras()
		Docente.Saludar()
		print Docente.Calcular(vhoras, noc)
		Docente.Despedirse()
	
	if (opc==2):
		vuc=300
		nomE=raw_input("Nombre: ")
		apellE=raw_input("Apellido: ")
		cedE=int(raw_input("Cedula: "))
		carrE=raw_input("Carrera: ")
		semesE=int(raw_input("Semestre: "))
		ucE=int(raw_input("Cuantas U/C solicitara?: "))
		Estudiante.GetNombre(nomE)
		Estudiante.GetApellido(apellE)
		Estudiante.GetCedula(cedE)
		Estudiante.GetCarrera(carrE)
		Estudiante.GetSemestre(semesE)
		Estudiante.GetUC(ucE)
		print Estudiante.SetNombre(), Estudiante.SetApellido(), Estudiante.SetCedula(), 
		print Estudiante.SetCarrera(), Estudiante.SetSemestre(), Estudiante.SetUC()
		Estudiante.Saludar()
		print Estudiante.Calcular(vuc)
		Estudiante.Despedirse()	
	Seguir=raw_input("Desea Seguir?: ")
if Seguir!="S":
	print "ADIOS"
