#!/usr/bin/env python
#-*- coding: UTF8 -*-

import os


class clsNodo:
	def __init__(self,pNum):
		self.siguiente=None
		self.anterior=None
		self.aNumero=pNum
		
	def setNodo(self):
		return self.aNumero

class clsLista:
	def __init__(self):
		self.inicio=None
		self.fin=None

	def fVacia(self):
		if self.inicio==None:
			return True
		else:
			return False
			
	def fInsertar(self,pNum):
		temporal=clsNodo(pNum)
		if self.fVacia()==True:
			self.inicio=temporal
			self.fin=temporal
		else:
			temporal.siguiente=self.inicio
			self.inicio.anterior=temporal
			self.inicio=temporal
		print("Elemento Insertado...")
		fsContinuar()


	def fListar(self):
		print("**********")
		temporal=self.inicio
		while temporal!=None:

				print(temporal.setNodo())
				temporal=temporal.siguiente

	def fListarPrim(self):
		print("**********")
		temporal=self.inicio
		while temporal!=None:
			if fbPrimo(temporal.aNumero)==True:
				print(temporal.setNodo())
				temporal=temporal.siguiente

	def fListarProm(self):
		print("**********")
		temporal=self.inicio
		while temporal!=None:
			if (temporal.aNumero)>=liPromedio:
				print(temporal.setNodo())
				temporal=temporal.siguiente


	def fBuscar(self,pElemento):
		print("****Buscando******")   #esta linea es para que salga el mensaje que busca solamente, pero se puede quitar
		temporal=self.inicio
		while temporal!=None:  
			if temporal.aNumero==pElemento:
				print temporal.setNodo()
				fsContinuar()
				return
			temporal=temporal.siguiente
		print ("No Existe...")
		fsContinuar()
		
	def fBorrarP(self):
		if self.fVacia()==False:
			self.inicio=self.inicio.siguiente
			self.inicio.anterior=None
			print("Elemento Eliminado...")
		else:
			print("Lista Vacia...")
			fsContinuar()
			
	def fBorrarU(self):
		if self.fin.anterior==None:
			self.inicio=None
			self.fin=None
		else:
			self.fin=self.fin.anterior
			self.fin.siguiente=None
		print("Elemento Eliminado...")
		fsContinuar()


def fsCadena(pTexto):
	lsVar=raw_input(pTexto)
	return lsVar


def fiEntero(pTexto):
	liVar=int(raw_input(pTexto))
	return liVar


def fsContinuar():
	return fsCadena ("Pulse enter para continuar ")


def fiMenu():
	os.system("clear")
	print("1. Agregar")
	print("2. Buscar")
	print("3. Eliminar Primero")
	print("4. Eliminar Ultimo")
	print("5. Listar")
	print("6. Listar promedio")
	print("6. Listar primo")
	print("0. Salir")
	op=fiEntero("Seleccione su opcion: ")
	return op

def fbPar(psTexto):
	if (psTexto%2)==0:
		return True
	return False

def fbPrimo(psTexto):
	if (psTexto<2):
		return False
	for  i in range (2, psTexto):
		if (psTexto%i==0):
			return False
	return True


liPromedio=0
liSuma=0
liContador=0
lis=clsLista()
liOpcion=9
while (liOpcion!=0):
	liOpcion=fiMenu()

	if liOpcion == 1:  #en la opcion agregar deben ser o cadena o entero o flotante aquellos elementos que se vallan a buscar
		lsNumero=fiEntero("Introduzca el numero: ")
		if fbPar(lsNumero)==False:
			lis.fInsertar(lsNumero)
			liSuma=lsNumero+liSuma
			liContador=liContador+1
		else:
			print "no es un numero impar "
			fsContinuar()

	elif liOpcion == 2:
		lsElemento=fsCadena("Elemento a Buscar: ")
		lis.fBuscar(lsElemento)

	elif liOpcion == 3:
		lis.fBorrarP()

	elif liOpcion == 4:
		lis.fBorrarU

	elif liOpcion == 5:
		lis.fListar()
		fsContinuar()

	elif liOpcion == 6:
		liPromedio=liSuma/liContador
		print (liPromedio+1)
		fsContinuar()
	
	elif liOpcion==7:
		lis.fListarPrim()
		fsContinuar()
		
	elif liOpcion == 0:
		print ("Adios...")
		fsContinuar()

	else:
		lsValido=fsCadena("Opcion No Valida...") #lsValido puede llamarse como sea Z, x, p, q, ñ, etc
