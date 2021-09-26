################################
# Elaborado por: DIEGO CHAVEZ  #
################################

import os

class Nodo:
	def __init__(self,ced,nom):
		self.siguiente=None
		self.anterior=None
		self.cedula=ced
		self.nombre=nom
	
	def setNodo(self):
		return self.cedula,self.nombre
		
class Lista:
	def __init__(self):
		self.inicio=None
		self.fin=None
	
	def Vacia():
		if self.inicio==None:
			return True
		else:
			return False
				
	def Insertar(self,ced,nom):
		temporal=Nodo(ced,nom)
		if self.Vacia==True:
			self.inicio=temporal
			self.fin=temporal
		else:
			temporal.siguiente=self.inicio
			self.inicio.anterior=temporal
			self.inicio=temporal
		print("Elemento Insertado...")
		Leer("Continuar...")
			
	def Imprimir(self):
		temporal=self.inicio
		while temporal!=None:
			print(temporal.setNodo())
			temporal=temporal.siguiente
	
	def buscar(self, elemento):
		print ("****BUSCANDO****")
		temporal=self.inicio
		while temporal!=None:
			if temporal.cedula==elemento:
				print temporal.setNodo()
				z=Leer("Continuar")
				return
			temporal=temporal.siguiente
		z=Leer("No existe...")		
			
def Leer(texto):
	Var=raw_input(texto)
	return Var
	
def menu():
	os.system("clear")
	print "1.Agregar"
	print "2.Buscar"
	print "3.Imprimir"
	print "4. Salir"
	opc=int(Leer("Opcion: "))
	return opc

lis=Lista()
op=9

while (op!=0):
	op=menu()
	if op==1:
		x=Leer("Nombre:")
		y=Leer("Cedula: ")
		lis.Insertar(x,y)
		
	elif op==2:
		d=Leer("Cedula: ")
		lis.Buscar(d)
		
	elif op==3:
		lis.Imprimir()
		z=Leer("Continuar...")
	else:
		print "Adios"

#UPTP S2-T1