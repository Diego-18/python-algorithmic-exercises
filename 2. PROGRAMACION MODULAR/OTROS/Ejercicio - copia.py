import os

#Funciones:

class Nodo:																#Clase Nodo(Almacen)
	def __init__(self,ced,nom,ape,tel,corr):
		self.anterior=None
		self.siguiente=None
		self.Nombre=nom
		self.Cedula=ced
		self.Apellido=ape
		self.Telefono=tel
		self.Correo=corr
		
class Lista:															#Clase Lista
	def __init__(self):
		self.inicio=None
		self.fin=None
		
	def Vacia(self):													#Funcion Vacia
		if self.inicio==None:
			return True
		else:
			return False
	
	def Agregar(self,nom,ced,ape,tel,corr):								#Funcion Agregar
		temporal=Nodo(ced,nom,ape,tel,corr)
		if Vacia!=True:
			self.inicio=temporal
			self.fin=temporal
		else:
			temporal.siguiente=self.inicio
			self.inicio.siguiente=temporal
			self.inicio=temporal
		print ("Elemento Insertado")
		leer("Continuar...")

	def Buscar(self,elemento):											#Funcion Buscar
		print("****Buscando******")
		temporal=self.inicio
		while temporal!=None:
			if temporal.cedula==elemento:
				print temporal.setNodo()
				z=Leer("Continuar...")
				return
			temporal=temporal.siguiente
		z=Leer("No Existe...")
	
	def listar(self):													#Funcion Imprimir
		print("**********")
		temporal=self.inicio
		while temporal!=None:
			print(temporal.setNodo())
			temporal=temporal.siguiente
		
def leer(texto):														#Funcion Leer
	var=raw_input(texto)
	return var
	
def Menu():
	os.system ("clear")															#Funcion Menu
	print ("1.Agregar")
	print ("2.Buscar")
	print ("3.Eliminar")
	print ("4.Modificar")
	print ("5.Listar")
	print ("6.Salir")
	opc=int(leer("Opcion: "))
	return opc

#Programa:

lis=Lista()
opcion=9

while (opcion!=0):
	
	opcion=Menu()
	
	if opcion == 1:
		c=int(leer("Cedula: "))
		n=leer("Nombre: ")
		a=leer("Apellido: ")
		t=int(leer("Telefono: "))
		co=leer("Correo: ")
		lis.Insertar(c,n,a,t,co)
		
	elif opcion == 2:
		x=int(leer("Elemento a Buscar: "))
		lis.buscar(x)
		
#	elif opcion == 3:
#		lis.
		
#	elif opcion == 4:
#		lis.
		
	elif opcion == 5:
		lis.listar()
		z=Leer("Continuar...")
		
	elif opcion == 0:
		z=Leer("Adios...")
	
	else:
		z=Leer("Opcion No Valida...")
