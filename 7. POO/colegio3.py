#!/usr/bin/env python 
#-*- coding: cp1252 -*-

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#Colegio

#Inicio:

class Persona(object):
	Nombre=""
	Apellido=""
	
	def __Init__(self):
		self.Nombre=""
		self.Apellido=""
	
	def GetNombre(self, pnombre):
		self.Nombre=pnombre
	
	def GetApellido(self, papellido):
		self.Apellido=papellido
	
	def SetNombre(self):
		return self.Nombre
	
	def SetApellido(self):
		return self.Apellido
	
class EstudianteP(Persona):
	Grado=""
	Turno=""
	
	def __Init__(self):
		self.Grado=""
		self.Turno=""
	
	def GetGrado(self, pgrado):
		self.Grado=pgrado
	
	def GetTurno(self, pturno):
		self.Turno=pturno
	
	def SetGrado(self):
		return self.Grado
	
	def SetTurno(self):
		return self.Turno
	
	def Calcular(self):
		if (self.Grado==1):
			return "Usted debera pagar mensualmente 300 bs"
		if (self.Grado==2):
			return "Usted debera pagar mensualmente 400 bs"
		if (self.Grado==3):
			return "Usted debera pagar mensualmente 500 bs"
		if (self.Grado==4):
			return "Usted debera pagar mensualmente 600 bs"
		if (self.Grado==5):
			return "Usted debera pagar mensualmente 700 bs"
		if (self.Grado==6):
			return "Usted debera pagar mensualmente 800 bs"
		if (self.Grado==7):
			return "Usted debera pagar mensualmente 900 bs"
			
class EstudianteS(Persona):
	Axo=""
	Cedula=""
	
	def __Init__(self):
		self.Axo=""
		self.Cedula=""
	
	def GetAxo(self, paxo):
		self.Axo=paxo
	
	def GetCedula(self, pcedula):
		self.Cedula=pcedula
	
	def SetAxo(self):
		return self.Axo
	
	def SetCedula(self):
		return self.Cedula
	
	def Calcular(self):
		if (self.Axo==1):
			return "Usted debera pagar mensualmente 1000 bs"
		if (self.Axo==2):
			return "Usted debera pagar mensualmente 1100 bs"
		if (self.Axo==3):
			return "Usted debera pagar mensualmente 1200 bs"
		if (self.Axo==4):
			return "Usted debera pagar mensualmente 1300 bs"
		if (self.Axo==5):
			return "Usted debera pagar mensualmente 1400 bs"
		
class EstudianteU(Persona):
	Carrera=""
	Trayecto=""
	Semestre=""
	UC=""
	Cedula=""
	
	def __Init__(self):
		self.Carrera=""
		self.Trayecto=""
		self.Semestre=""
		self.UC=""
	
	def GetCarrera(self, pcarrera):
		self.Carrera=pcarrera
	
	def GetTrayecto(self, ptrayecto):
		self.Trayecto=ptrayecto
	
	def GetSemestre(self, psemestre):
		self.Semestre=psemestre
	
	def GetUC(self, puc):
		self.UC=puc
	
	def GetCedula(self, pcedula):
		self.Cedula=pcedula
	
	def SetCarrera(self):
		return self.Carrera
	
	def SetTrayecto(self):
		return self.Trayecto
	
	def SetSemestre(self):
		return self.Semestre
	
	def SetUC(self):
		return self.UC
	
	def SetCedula(self):
		return self.Cedula

	def Calcular(self, vuc):
		if self.UC>=1:
			return self.UC*vuc
		else:
			return "Hasta luego"
			
#Programa:
Primaria=EstudianteP()
Secuandaria=EstudianteS()
Universidad=EstudianteU()
Seguir="S"
opc=0

while (Seguir=="S"):
	print ("1.Primaria 2.Secundaria 3.Universidad")
	opc=int(raw_input("Opcion: "))
	
	if (opc==1):
		print "Datos del Alumno de la Escuela Fermin Toro"
		nombP=raw_input("Nombre: ")
		apelP=raw_input("Apellido: ")
		graP=int(raw_input("Grado: "))
		turnP=raw_input("Turno: ")
		Primaria.GetNombre(nombP)
		Primaria.GetApellido(apelP)
		Primaria.GetGrado(graP)
		Primaria.GetTurno(turnP)
		print Primaria.SetNombre(), Primaria.SetApellido(),
		print Primaria.SetGrado(), Primaria.SetTurno(),
		print Primaria.Calcular()
	
	if (opc==2):
		print "Datos del Alumno del Liceo Fermin Toro"
		nombS=raw_input("Nombre: ")
		apelS=raw_input("Apellido: ")
		cedulS=int(raw_input("Cedula: "))
		axoS=int(raw_input("Año: "))
		Secuandaria.GetNombre(nombS)
		Secuandaria.GetApellido(apelS)
		Secuandaria.GetCedula(cedulS)
		Secuandaria.GetAxo(axoS)
		print Secuandaria.SetNombre(), Secuandaria.SetApellido(), Secuandaria.SetCedula(),
		print Secuandaria.SetAxo(),
		print Secuandaria.Calcular()

	if (opc==3):
		print "Datos del Alumno de la Universidad Fermin Toro"
		vuc=200
		nombU=raw_input("Nombre: ")
		apelU=raw_input("Apellido: ")
		cedulU=int(raw_input("Cedula: "))
		carU=raw_input("Carrera: ")
		trayU=int(raw_input("Trayecto: "))
		semesU=int(raw_input("Semestre: "))
		ucU=int(raw_input("Cuantas U/C ingresara en este semestre: "))
		Universidad.GetNombre(nombU)
		Universidad.GetApellido(apelU)
		Universidad.GetCedula(cedulU)
		Universidad.GetCarrera(carU)
		Universidad.GetTrayecto(trayU)
		Universidad.GetSemestre(semesU)
		Universidad.GetUC(ucU)
		print Universidad.SetNombre(), Universidad.SetApellido(), Universidad.SetCedula(),
		print Universidad.SetCarrera(), Universidad.SetTrayecto(), Universidad.SetSemestre(),
		print Universidad.Calcular(vuc)	
	Seguir=raw_input("Desea seguir?: ")
if Seguir!="S":
	print "Adios"

#UPTP S2-T1