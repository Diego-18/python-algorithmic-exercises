#!/usr/bin/env python
#-*- coding: UTF8 -*-
import os

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

class clsNodo:
	def __init__(self,pCed,pNom):
		self.siguiente=None
		self.anterior=None
		self.aCedula=pCed     #Atributo-Cedula sera igua a Parametro-Ced
		self.aNombre=pNom     #Atributo-Nombre sera igua a Parametro-Nom
		
	def setNodo(self):
		return self.aCedula,self.aNombre   #envia o retorna los atributos Cedula y Nombre



class clsLista:
	def __init__(self):
		self.inicio=None
		self.fin=None

	def fVacia(self):
		if self.inicio==None:
			return True
		else:
			return False
			
	def fInsertar(self,pCed,pNom):
		temporal=clsNodo(pCed,pNom)
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
			
	def fBuscar(self,pElemento):
		print("****Buscando******")   #esta linea es para que salga el mensaje que busca solamente, pero se puede quitar
		temporal=self.inicio
		
		while temporal!=None:   #dentro del while se colocan tantos IF como la cantidad de atributos q se busquen
								#como por ejemplo en este caso hay 2, el aCedula y el aNombre, si tuviera aEdad
								#o cualquier otro atributo que se buscara, color, talla etc, se coloca el IF con ese
								#atributo solamente y solo se cambia la primera linea, if temporal.ATRIBUTOEJEMPLO==pElemento:
								#lo que sigue dentro del if es solo copiar y pegar
			if temporal.aCedula==pElemento:
				print temporal.setNodo()
				fsContinuar()
				return
			
			if temporal.aNombre==pElemento:
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
	print("0. Salir")
	op=fiEntero("Seleccione su opcion: ")
	return op

lis=clsLista()
liOpcion=9
while (liOpcion!=0):
	liOpcion=fiMenu()

	if liOpcion == 1:  #en la opcion agregar deben ser o cadena o entero o flotante aquellos elementos que se vallan a buscar
		lsCI=fsCadena("Cedula: ")
		lsNombre=fsCadena("Nombre: ")
		lis.fInsertar(lsCI,lsNombre)

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

	elif liOpcion == 0:
		print ("Adios...")
		fsContinuar()

	else:
		lsValido=fsCadena("Opcion No Valida...") #lsValido puede llamarse como sea Z, x, p, q, ñ, etc

#UPTP S2-T1