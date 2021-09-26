#!/usr/bin/env python
#-*- coding: cp1252 -*-

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#Inicio:

class Objeto(object):
	Color=""
	Marca=""
	Modelo=""
	
	def __Init__(self):
		self.Color=""
		self.Marca=""
		self.Modelo=""
	
	def GetColor(self, pcolor):
		self.Color=pcolor
	
	def GetMarca(self, pmarca):
		self.Marca=pmarca
	
	def GetModelo(self, pmodelo):
		self.Modelo=pmodelo
	
	def SetColor(self):
		return self.Color
	
	def SetMarca(self):
		return self.Marca
	
	def SetModelo(self):
		return self.Modelo

class Car(Objeto):
	Axo=""
	
	def __Init__(self):
		self.Axo=""
	
	def GetAxo(self, paxo):
		self.Axo=paxo
	
	def SetAxo(self):
		return self.Axo
	
	def Calcular(self):
		if (self.Axo>=1980) and (self.Axo<=1990):
			return 100000
		if (self.Axo>=1991) and (self.Axo<=2000):
			return 200000
		if (self.Axo>=2001) and (self.Axo<=2010):
			return 300000
		if (self.Axo>=2011) and (self.Axo<=2015):
			return 400000
	
class Motor(Objeto):
	Axo=""
	
	def __Init__(self):
		self.Axo=""
	
	def GetAxo(self, paxo):
		self.Axo=paxo
	
	def SetAxo(self):
		return self.Axo
	
	def Calcular(self):
		if (self.Axo>=1980) and (self.Axo<=1990):
			return 50000
		if (self.Axo>=1991) and (self.Axo<=2000):
			return 100000
		if (self.Axo>=2001) and (self.Axo<=2010):
			return 1500000
		if (self,Axo>=2011) and (self.Axo<=2015):
			return 200000	

#Programa:

Seguir="S"
Carro=Car()
Moto=Motor()	
opc=0
cost=0

while (Seguir=="S"):
	print ("1.Automoviles 2.Motos")
	opc=int(raw_input("Opcion: "))
	
	if opc==1:
		colorC=raw_input("Color: ")
		marcaC=raw_input("Marca: ")
		modeloC=raw_input("Modelo: ")
		axoC=int(raw_input("Año: "))
		Carro.GetColor(colorC)
		Carro.GetMarca(marcaC)
		Carro.GetModelo(modeloC)
		Carro.GetAxo(axoC)
		print Carro.SetColor(), Carro.SetMarca(), Carro.SetModelo(), Carro.SetAxo(),
		print Carro.Calcular()
	
	if opc==2:
		colorM=raw_input("Color: ")
		marcaM=raw_input("Marca: ")
		modeloM=raw_input("Modelo: ")
		axoM=int(raw_input("Año: "))
		Moto.GetColor(colorM)
		Moto.GetMarca(marcaM)
		Moto.GetModelo(modeloM)
		Moto.GetAxo(axoM)
		print Moto.SetColor(), Moto.SetMarca(), Moto.SetModelo(), Moto.SetAxo(),
		print Moto.Calcular()
	Seguir=raw_input("Desea Seguir?: ")

#UPTP S2-T1