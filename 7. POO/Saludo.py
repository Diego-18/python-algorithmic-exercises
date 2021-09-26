#!/usr/bin/env python
#-*-coding=cp1252 -*-

#Inicio

class ClsPersona(object):
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

class ClsEstudiante(ClsPersona):
	Trayecto=""
	Semestre=""
	UC=""
	
	def __Init__(self):
		self.Nota=""
		self.Trayecto=""
		self.Semestre=""
		self.UC=""
	
	def GetTrayecto(self, ptrayecto):
		self.Trayecto=ptrayecto
	
	def GetSemestre(self, psemestre):
		self.Semestre=psemestre
	
	def GetUC(self, puc):
		self.UC=puc
	
	def SetTrayecto(self):
		return self.Trayecto
	
	def SetSemestre(self):
		return self.Semestre
	
	def SetUC(self):
		return self.UC
	
	def Calcular(self, n1, n2, n3, n4,vuc):
		prom=(n1+n2+n3+n4)/4
		if (prom>=12):
			print "Aprobo"
			return prom
		else:
			print "Reprobo"
			return prom
		return self.UC*vuc
			
	def Saludar(self):
		print "Epale Men"
	
	def Despedida(self):
		print "Nos vemos Men"
		
class ClsDocente(ClsPersona):
	PNF=""
	Sueldo=""
	Cargo=""
	
	def __Init__(self):
		self.PNF=""
		self.Sueldo=""
		self.Cargo=""
		
	def GetPNF(self, ppnf):
		self.PNF=ppnf
	
	def GetSueldo(self, psueldo):
		self.Sueldo=psueldo
	
	def GetCargo(self, pcargo):
		self.Cargo=pcargo
	
	def SetPNF(self):
		return self.PNF
	
	def SetSueldo(self):
		return self.Sueldo
	
	def SetCargo(self):
		return self.Cargo
	
	def Calcular(self,sb):
		if (self.Cargo==1):
			return (sb*0.10)+sb
		else:
			return (sb*0.20)+sb

	def Saludar(self):
		print "Buenos Dias"
	
	def Despedida(self):
		print "Hasta Ma*ana"
		
#Programa: 

Universitario=ClsEstudiante()
Docente=ClsDocente()
opc=0
Seguir="S"
vuc=0

while (Seguir=="S"):
	print "1.Estudiante 2.Docente 3.Salir"
	opc=int(raw_input("Opcion: "))
	
	if (opc==1):
		vuc=100
		print "Datos del Estudiante: "
		nombE=raw_input("Nombre: ")
		apeE=raw_input("Apellido: ")
		cedE=int(raw_input("Cedula: "))
		n1=int(raw_input("Nota: "))
		n2=int(raw_input("Nota: "))
		n3=int(raw_input("Nota: "))
		n4=int(raw_input("Nota: "))
		trayE=int(raw_input("Trayecto: "))
		semesE=int(raw_input("Semestre: "))
		uc=int(raw_input("Cuantas U/C solicitara este semestre: "))
		Universitario.GetNombre(nombE)
		Universitario.GetApellido(apeE)
		Universitario.GetCedula(cedE)
		Universitario.GetTrayecto(trayE)
		Universitario.GetSemestre(semesE)
		Universitario.GetUC(uc)
		print Universitario.SetNombre(), Universitario.SetApellido(), Universitario.SetCedula(),
		Universitario.Saludar()
		print Universitario.SetTrayecto(), Universitario.SetSemestre(), Universitario.SetUC(),
		print Universitario.Calcular(n1, n2, n3, n4, vuc)
		Universitario.Despedida()
	
	if (opc==2):
		print "Datos del Docente: "
		nombD=raw_input("Nombre: ")
		apeD=raw_input("Apellido: ")
		cedD=int(raw_input("Cedula: "))
		sueD=int(raw_input("Sueldo: "))
		cargD=int(raw_input("1.Novato 2.Experto"))
		Docente.GetNombre(nombD)
		Docente.GetApellido(apeD)
		Docente.GetCedula(cedD)
		Docente.GetSueldo(sueD)
		Docente.GetCargo(cargD)
		print Docente.SetNombre(), Docente.SetApellido(), Docente.SetCedula(),
		Docente.Saludar()
		print Docente.SetSueldo(), Docente.SetCargo(),
		print Docente.Calcular(sueD)
		Docente.Despedida()
	Seguir=raw_input("Desea Seguir?: ")
if (Seguir!="S"):
	print "ADIOS"