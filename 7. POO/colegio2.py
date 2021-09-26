#!/usr/bin/env python
#-*- coding:cp1252 -*-

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#Inicio:

class ClsPersona(object):
	Nombres=""
	Apellido=""
	Cedula=""
	Edad=""

	def __Init__(self):
		self.Nombre=""
		self.Apellido=""
		self.Cedula=""
		self.Edad=""

	def GetNombre(self, pnombre):
		self.Nombre=pnombre

	def GetApellido(self, papellido):
		self.Apellido=papellido

	def GetCedula(self, pcedula):
		self.Cedula=pcedula

	def GetEdad(self, pedad):
		self.Edad=pedad

	def SetNombre(self):
		return self.Nombre

	def SetApellido(self):
		return self.Apellido

	def SetCedula(self):
		return self.Cedula

	def SetEdad(self):
		return self.Edad

	def Saludar(self):
		print "Buenos dias"

	def Despedida(self):
		print "Hasta Mañana"

class ClsDocente(ClsPersona):
	DiasL=""
	Horas=""
	Cargo=""

	def __Init__(self):
		self.DiasL=""
		self.Horas=""
		self.Cargo=""

	def GetDias(self, pdias):
		self.DiasL=pdias

	def GetHoras(self, phoras):
		self.Horas=phoras

	def GetCargo(self, pcargo):
		self.Cargo=pcargo

	def SetDias(self):
		return self.DiasL

	def SetHoras(self):
		return self.Horas

	def SetCargo(self):
		return self.Cargo

	def Calcular(self, ):
		sb=self.DiasL*160
		if (self.Horas>45):
			  he=self.Horas-45
			  she=he*100
			  return sb+she
		else:
			return sb

		if self.Cargo=="1":
			return (sb*0.10)+sb

		elif self.Cargo=="2":
			return (sb*0.15)+sb

		elif self.Cargo=="3":
			return (sb*0.20)+sb

class ClsObrero(ClsPersona):
	DiasL=""
	Horas=""
	Cargo=""

	def __Init__(self):
		self.DiasL=""
		self.Horas=""
		self.Cargo=""

	def GetDias(self, pdias):
		self.DiasL=pdias

	def GetHoras(self, phoras):
		self.Horas=phoras

	def GetCargo(self, pcargo):
		self.Cargo=pcargo

	def SetDias(self):
		return self.DiasL

	def SetHoras(self):
		return self.Horas

	def SetCargo(self):
		return self.Cargo

	def Calcular(self):
		sb=self.DiasL*160
		if (self.Horas>45):
			he=self.Horas-45
			she=he*80
		else:
			return sb

		if self.Cargo==1:
			return (sb*0.05)+sb

		elif self.Cargo==2:
			return (sb*0.10)+sb

class ClsEstudiante(ClsPersona):
	Carrera=""
	Semestre=""
	Trayecto=""
	UC=""

	def __Init__(self):
		self.Carrera=""
		self.Semestre=""
		self.Trayecto=""
		self.UC=""

	def GetCarrera(self, pcarrera):
		self.Carrera=pcarrera

	def GetSemestre(self, psemestre):
		self.Semestre=psemestre

	def GetTrayecto(self, ptrayecto):
		self.Trayecto=ptrayecto

	def GetUC(self, puc):
		self.UC=puc

	def SetCarrera(self):
		return self.Carrera

	def SetSemestre(self):
		return self.Semestre

	def SetTrayecto(self):
		return self.Trayecto

	def SetUC(self):
		return self.UC

	def Calcular(self, pn1, pn2, pn3, pn4):
		Nt=(pn1+pn2+pn3+pn4)/4
		if (Nt>=12):
			return "Aprobaste"
			if (self.Semestre==1):
				print "Usted paso al Semestre II"
				return self.UC*200
			if (self.Semestre==2):
				print "Usted ya es TSU"
				print "Usted paso al semestre III"
				print "Cuantas U/C meterá para este semestre: "
				return self.UC*200
			if (self.Semestre==3):
				print "Usted paso al semestre IV"
				return self.UC*200
			if (self.Semestre==4):
				print "Usted ya es Ingeniero"

			else:
				return "Reprobaste"



#Programa:

Seguir="S"
Docente=ClsDocente()
Obrero=ClsObrero()
Estudiante=ClsEstudiante()
Opc=0

while (Seguir=="S"):
	print "1.Docente 2.Estudiante 3.Obrero"
	Opc=int(raw_input("Opcion: "))

	if (Opc==1):
		print ("Datos del Docente: ")
		nomD=raw_input("Nombre: ")
		apeD=raw_input("Apellido: ")
		cedD=int(raw_input("Cedula: "))
		edadD=int(raw_input("Edad: "))
		dialD=int(raw_input("Dias L.: "))
		horasD=int(raw_input("Horas L.: "))
		cargD=int(raw_input("1.Novato 2.Medio 3.Experto: "))
		Docente.GetNombre(nomD)
		Docente.GetApellido(apeD)
		Docente.GetCedula(cedD)
		Docente.GetEdad(edadD)
		Docente.GetDias(dialD)
		Docente.GetHoras(horasD)
		Docente.GetCargo(cargD)
		print Docente.SetNombre(), Docente.SetApellido(), Docente.SetCedula(), Docente.SetEdad(),
		Docente.Saludar()
		print Docente.SetDias(), Docente.SetHoras(), Docente.SetCargo(),
		print Docente.Calcular()
		Docente.Despedida()

	if (Opc==2):
		print ("Datos del Estudiante: ")
		nomE=raw_input("Nombre: ")
		apeE=raw_input("Apellido: ")
		cedE=int(raw_input("Cedula: "))
		edadE=int(raw_input("Edad: "))
		carrera=raw_input("Carrera: ")
		tra=int(raw_input("Trayecto: "))
		nota1=int(raw_input("Nota: "))
		nota2=int(raw_input("Nota: "))
		nota3=int(raw_input("Nota: "))
		nota4=int(raw_input("Nota: "))
		semes=int(raw_input("Introduzca el semestre que curso: "))
		uc=int(raw_input("Cantidad de U/C: "))
		Estudiante.GetNombre(nomE)
		Estudiante.GetApellido(apeE)
		Estudiante.GetCedula(cedE)
		Estudiante.GetEdad(edadE)
		Estudiante.GetCarrera(carrera)
		Estudiante.GetTrayecto(tra)
		Estudiante.GetSemestre(semes)
		Estudiante.GetUC(uc)
		print Estudiante.SetNombre(), Estudiante.SetApellido(),Estudiante.SetCedula(), Estudiante.SetEdad(),
		Estudiante.Saludar()
		print Estudiante.SetCarrera(), Estudiante.SetTrayecto(),Estudiante.SetSemestre(),
		print Estudiante.Calcular(nota1, nota2, nota3, nota4)
		Estudiante.Despedida()

	if (Opc==3):
		print ("Datos del Obrero: ")
		nomO=raw_input("Nombre: ")
		apeO=raw_input("Apellido: ")
		cedO=int(raw_input("Cedula: "))
		edadO=int(raw_input("Edad: "))
		dialO=int(raw_input("Dias L.: "))
		horasO=int(raw_input("Horas L.: "))
		cargO=int(raw_input("1.Supervisor 2.Ayudante: "))
		Obrero.GetNombre(nomO)
		Obrero.GetApellido(apeO)
		Obrero.GetCedula(cedO)
		Obrero.GetEdad(edadO)
		Obrero.GetDias(dialO)
		Obrero.GetHoras(horasO)
		Obrero.GetCargo(cargO)
		print Obrero.SetNombre(), Obrero.SetApellido(), Obrero.SetCedula(), Obrero.SetEdad(),
		Obrero.Saludar()
		print Obrero.SetDias(), Obrero.SetHoras(), Obrero.SetCargo(),
		print Obrero.Calcular()
		Obrero.Despedida()
	Seguir=raw_input("Desea seguir?: ")

#UPTP S2-T1