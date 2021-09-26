#!/usr/bin/env python
#-*- coding: cp1252 -*-

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#Empresa

class ClsPersona(object):
	Nombre=""
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
		print "Buenos Dias"
	
	def Despedir(self):
		print "Hasta mañana"
	
class ClsAdministrativo(ClsPersona):
	DiasL=""
	Horas=""
	Cargo=""
	Antiguedad=""
	
	def __Init__(self):
		self.DiasL=""
		self.Horas=""
		self.Cargo=""
		self.Antiguedad=""
		
	def GetDiasL(self, pdiasL):
		self.DiasL=pdiasL
	
	def GetHoras(self, phoras):
		self.Horas=phoras
	
	def GetCargo(self, pcargo):
		self.Cargo=pcargo
	
	def GetAntiguedad(self, pantiguedad):
		self.Antiguedad=pantiguedad
	
	def SetDiasL(self):
		return self.DiasL
	
	def SetHoras(self):
		return self.Horas
	
	def SetCargo(self):
		return self.Cargo
	
	def SetAntiguedad(self):
		return self.Antiguedad
	
	def Calcular(self, vhoras):
		sb=self.DiasL*vhoras
		if self.Horas>40:
			he=self.Horas-40
			she=he*100
			sb=sb+she
		else:
			sb=sb
		
		if self.Cargo=="1":
			porc=sb*0.25
			return sb+porc
		
		elif self.Cargo=="2":
			porc=sb*0.20
			return sb+porc
		
		elif self.Cargo=="3":
			porc=sb*0.15
			return sb+porc
		
		elif self.Cargo=="4":
			porc=sb*0.10
			return sb+porc
		
		else:
			porc=sb*0.05
			return sb+porc
		
		if self.Antiguedad==1:
			print "Usted ha ascendido a Novato"
		
		elif self.Antiguedad>=5:
			print "Usted a ascendido a Master"
		
		elif self.Antiguedad>=15:
			print "Usted a escendido a Supervisor"
		
		elif self.Antiguedad>=20:
			print "Usted a ascendido a Gerente"
		
class ClsObrero(ClsPersona):
	DiasL=""
	Horas=""
	Cargo=""
	Antiguedad=""
	
	def __Init__(self):
		self.DiasL=""
		self.Horas=""
		self.Cargo=""
		self.Antiguedad=""
		
	def GetDiasL(self, pdiasL):
		self.DiasL=pdiasL
	
	def GetHoras(self, phoras):
		self.Horas=phoras
	
	def GetCargo(self, pcargo):
		self.Cargo=pcargo
	
	def GetAntiguedad(self, pantiguedad):
		self.Antiguedad=pantiguedad
	
	def SetDiasL(self):
		return self.DiasL
	
	def SetHoras(self):
		return self.Horas
	
	def SetCargo(self):
		return self.Cargo
	
	def SetAntiguedad(self):
		return self.Antiguedad
	
	def Calcular(self, vhoras):
		sb=self.DiasL*vhoras
		if self.Horas>40:
			he=self.Horas-40
			she=he*100
			sb=sb+she
		else:
			return sb
		
		if self.Cargo=="1":
			porc=sb*0.15
			return sb+porc
		
		else:
			porc=sb*0.10
			return sb+porc
		
		if self.Antiguedad>=5:
			print "Usted a ascendido a Supervisor"

#Programa:

Administrativo=ClsAdministrativo()
Obrero=ClsObrero()
Seguir="S"
Opc=0
Horas=0

while  (Seguir=="s") or (Seguir=="S"):
        print "1.Administrativo 2.Obrero 3.Salir"
        Opc=int(raw_input("Introduzca la Opcion: "))

        if (Opc==1):
                vhoras=160
                print "Datos del Administrativo:"
                nombA=raw_input("Nombre: ")
                apeA=raw_input("Apellido: ")
                cedA=int(raw_input("Cedula: "))
                edadA=int(raw_input("Edad: "))
                DiasA=int(raw_input("Dias Laborados: "))
                HorasA=int(raw_input("Horas: "))
                CargA=int(raw_input("1.Gerente 2.Supervisor 3.Master 4.Novato 5.Pasante: "))
                AntA=int(raw_input("Antiguedad: "))
                Administrativo.GetNombre(nombA)
                Administrativo.GetApellido(apeA)
                Administrativo.GetCedula(cedA)
                Administrativo.GetEdad(edadA)
                Administrativo.GetDiasL(DiasA)
                Administrativo.GetHoras(HorasA)
                Administrativo.GetCargo(CargA)
                Administrativo.GetAntiguedad(AntA)
                print Administrativo.SetNombre(), Administrativo.SetApellido(), Administrativo.SetCedula(), Administrativo.SetEdad()
                print Administrativo.SetDiasL(), Administrativo.SetHoras(), Administrativo.SetCargo(), Administrativo.SetAntiguedad()
                Administrativo.Saludar()
                print Administrativo.Calcular(HorasA)
                Administrativo.Despedir()

        if (Opc==2):
                vhoras=160
                print "Datos del Obrero:"
                nombO=raw_input("Nombre: ")
                apeO=raw_input("Apellido: ")
                cedO=int(raw_input("Cedula: "))
                edadO=int(raw_input("Edad: "))
                DiasO=int(raw_input("Dias Laborados: "))
                HorasO=int(raw_input("Horas: "))
                CargO=int(raw_input("1.Supervisor 2.Ayudante"))
                AntO=int(raw_input("Antiguedad: "))
                Obrero.GetNombre(nombO)
                Obrero.GetApellido(apeO)
                Obrero.GetCedula(cedO)
                Obrero.GetEdad(edadO)
                Obrero.GetDiasL(DiasO)
                Obrero.GetHoras(HorasO)
                Obrero.GetCargo(CargO)
                Obrero.GetAntiguedad(AntO)
                print Obrero.SetNombre(), Obrero.SetApellido(), Obrero.SetCedula(), Obrero.SetEdad()
                print Obrero.SetDiasL(), Obrero.SetHoras(), Obrero.SetCargo(), Obrero.SetAntiguedad()
                Obrero.Saludar()
                print Obrero.Calcular(HorasO)
                Obrero.Despedir()

        Seguir=raw_input("Desea Seguir? (S/N): ")
if (Seguir!="S") or (Seguir!="s"):
	print "Adios"

#UPTP S2-T1