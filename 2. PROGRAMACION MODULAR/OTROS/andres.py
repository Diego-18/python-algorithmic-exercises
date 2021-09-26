#! /usr/bin/env python
# -*- coding: UTF8 -*-
import os

#Andres Alvarado C.I 25.035.719

def Leer (psTexto):
	Var=raw_input(psTexto)
	return Var

class Elemento():
	def __init__(self,num):
		self.siguiente=None
		self.anterior=None
		self.numero=num
	
	def SetElemento(self):
		return self.numero

def Primo(num):
		cont=0
		for N in range(1,num+1):
			if num%N==0:
				cont=cont+1
			if cont==2:
				return True
			else:
				return False

class Lista():
	def __init__(self):
		self.inicio=None
		self.fin=None
	
	def Vacia(self):
		if self.inicio==None:
			return True
		else:
			return False
		
	def Agregar(self,num):
		temporal=Elemento(num)
		if self.Vacia()==True:
			if (num%2!=0):
				self.inicio=temporal
				self.fin=temporal
			else:
				print "No es posible cargar el número, solo numeros impares"
		else:
			if (num%2!=0):
				temporal.siguiente=self.inicio
				self.inicio.anterior=temporal
				self.inicio=temporal
			else:
				print "No se ha agregado el numero, introduzca un numero impar"
		print ("Elemento Agregado...")
		Leer("Continuar...")
				
	def Listar(self):
		print "**********"
		temporal=self.inicio
		while temporal!=None:
			if Primo(temporal.numero)==True:
				print (temporal.SetElemento())
				temporal=temporal.siguiente
		Leer("Continuar...")
	
	def buscar(self,elemento):
		print ("****Buscando****")
		temporal=self.inicio
		while temporal!=None:
			if temporal.numero==elemento:
				print temporal.SetElemento()
				z=Leer("Continuar...")
				return
			temporal=temporal.siguiente
		z=Leer("No existe...")

	def BorrarP(self):
		if self.Vacia()==False:
			self.inicio=self.inicio.siguiente
			self.inicio.anterior=None
			print("Elemento Eliminado...")
			Leer("Continuar...")
		else:
			print("Lista Vacia...")
			Leer("Continuar...")
			
	def BorrarU(self):
		if self.fin.anterior==None:
			self.inicio=None
			self.fin=None
		else:
			self.fin=self.fin.anterior
			self.fin.siguiente=None
		print("Elemento Eliminado...")
		Leer("Continuar...")
		
	def Listar2(self):
		print ("**********")
		temporal=self.inicio
		while temporal!=None:
			print(temporal.SetElemento())
			temporal=temporal.siguiente
		Leer("Continuar...")

def Menu():
	os.system("clear")
	print "1. Agregar"
	print "2. Buscar"
	print "3. Imprimir"
	print "4. Borrar Primero"
	print "5. Borrar Ultimo"
	print "6. Imprimir todos los numeros cargados"
	print "7. Imprimir promedio de los numeros primos impresos"
	print "8. Imprimir los numeros por encima del promedio"
	print "0. Salir"
	opcion=int(Leer("Introduzca su opción: "))
	return opcion

#Programa

opciones=9
lista=Lista()

while opciones!=0:
	opciones=Menu()
	if opciones==1:
		numero=int(Leer("Introduzca número: "))
		lista.Agregar(numero)
	elif opciones==2:
		dato=int(Leer("Introduzca el numero: "))
		lista.buscar(dato)
	elif opciones==3:
		lista.Listar()
	elif opciones==4:
		lista.BorrarP()
	elif opciones==5:
		lista.BorrarU()
	elif opciones==6:
		print lista.Listar2()
	else:
		print "Adiós..."
