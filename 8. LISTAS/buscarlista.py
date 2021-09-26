#! /usr/bin/env python
# -*- coding: UTF8 -*-
import os

#Gilianneth Parra C.I 23.577.838
#Andres Alvarado C.I 25.035.719

def Leer (psTexto):
	Var=raw_input(psTexto)
	return Var

class Elemento():
	def __init__(self,ced,nom):
		self.siguiente=None
		self.anterior=None
		self.cedula=ced
		self.nombre=nom
	
	def SetElemento(self):
		return self.cedula,self.nombre

class Lista():
	def __init__(self):
		self.inicio=None
		self.fin=None
	
	def Vacio(self):
		if self.inicio==None:
			return True
		else:
			return False
		
	def Agregar(self,ced,nom):
		temporal=Elemento(ced,nom)
		if self.Vacio()==True:
			self.inicio=temporal
			self.fin=temporal
		else:
			temporal.siguiente=self.inicio
			self.inicio.anterior=temporal
			self.inicio=temporal
		print ("Elemento Agregado...")
		Leer("Continuar...")
		
	def Listar(self):
		print "**********"
		temporal=self.inicio
		while temporal!=None:
			print (temporal.SetElemento())
			temporal=temporal.siguiente
		Leer("Continuar...")
	
	def buscar(self,elemento):
		print ("****Buscando****")
		temporal=self.inicio
		while temporal!=None:
			if temporal.cedula==elemento:
				print temporal.SetElemento()
				z=Leer("Continuar...")
				return
			temporal=temporal.siguiente
		z=Leer("No existe...")
		

def Menu():
	os.system("clear")
	print "1. Agregar"
	print "2. Buscar"
	print "3. Imprimir"
	print "0. Salir"
	opcion=int(Leer("Introduzca su opción: "))
	return opcion

#Programa

opciones=9
lista=Lista()

while opciones!=0:
	opciones=Menu()
	if opciones==1:
		cedula=Leer("Introduzca su cédula: ")
		nombre=Leer("Introduzca su nombre: ")
		lista.Agregar(cedula,nombre)
	elif opciones==2:
		dato=Leer("Introduzca la cedula a buscar: ")
		lista.buscar(dato)
	elif opciones==3:
		lista.Listar()
	else:
		print "Adiós..."

#UPTP S2-T1