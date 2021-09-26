#!usr/bin/env python
#-*-coding:UTF-8-*-
#inicio


class Nodo:
	def __init__(self,num):
		self.siguiente=None
		self.anterior=None
		self.numero=num
		
	def setNodo(self):
		return self.numero

class Lista:
	def __init__(self):
		self.inicio=None
		self.fin=None
	
	def vacia(self):
		if self.inicio==None:
			return True
		else:
			return False
			
	def Insertar(self,num):
		temporal=Nodo(num)
		if self.vacia()==True:
			self.inicio=temporal
			self.fin=temporal
		else:
			temporal.siguiente=self.inicio
			self.inicio.anterior=temporal
			self.inicio=temporal
		print("Elemento Insertado...")
		
		
	def listar(self):
		print("********************")
		temporal=self.inicio
		while temporal!=None:
			print(temporal.setNodo())
			temporal=temporal.siguiente
			
	def listar2(self,promedio):
		print("********************")
		temporal=self.inicio
		while temporal!=None:
			if temporal.numero>promedio:
				print(temporal.setNodo())
			temporal=temporal.siguiente
	
	def listar3(self):
		print("********************")
		temporal=self.inicio
		while temporal!=None:
			if primo(temporal.numero)==True:
				print(temporal.setNodo())
			temporal=temporal.siguiente
			
			
	def buscar(self,elemento):
		print("****Buscando******")
		temporal=self.inicio
		while temporal!=None:
			if temporal.numero==elemento:
				
				print temporal.setNodo()
				z=Leer("Continuar...")
				return
			temporal=temporal.siguiente
		print ("No Existe...")
		
	def BorrarP(self):
		if self.vacia()==False:
			self.inicio=self.inicio.siguiente
			self.inicio.anterior=None
			print("Elemento Eliminado...")
		else:
			print("Lista Vacia...")
		
			
	def BorrarU(self):
		if self.fin.anterior==None:
			self.inicio=None
			self.fin=None
		else:
			self.fin=self.fin.anterior
			self.fin.siguiente=None
		print("Elemento Eliminado...")
		
			
def Leer(texto):
	var=raw_input(texto)
	return var

def primo (pfN):
	if (pfN <2):
		return False
	for liN in range(2,pfN):
		if (pfN % liN ==0):
			return False
	return True

def menu():
	print("1.Agregar")
	print("2.Buscar")
	print("3.Eliminar Primero")
	print("4.Eliminar Ultimo")
	print("5.Listar")
	print ("6 listar promedio")
	print ("7 listar primos")
	print("0.Salir")
	op=int(Leer("Seleccione: "))
	return op

lis=Lista()
opcion=9
pro=0
con=0
while (opcion!=0):
	opcion=menu()
	if opcion == 1:
		n=int(raw_input("Numero: "))
		
		if (n%2!=0):
			pro=pro+n
			con=con+1
			lis.Insertar(n)
			promedio=pro/con
		else:
			print "no ingresan datos impares"
	elif opcion == 2:
		x=Leer("Elemento a Buscar: ")
		lis.buscar(x)
	elif opcion == 3:
		lis.BorrarP()
	elif opcion == 4:
		lis.BorrarU()
	elif opcion == 5:
		lis.listar()
	elif opcion==6:
		print promedio , "este es el promedio.."
		lis.listar2(promedio)
		Leer("...")
	elif opcion==7:
		lis.listar3()
		Leer("...")
	elif opcion == 0:
		z=Leer("Adios...")

