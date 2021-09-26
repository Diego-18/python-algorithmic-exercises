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
	
	def vacia(self):
		if self.inicio==None:
			return True
		else:
			return False
			
	def Insertar(self,ced,nom):
		temporal=Nodo(ced,nom)
		if self.vacia()==True:
			self.inicio=temporal
			self.fin=temporal
		else:
			temporal.siguiente=self.inicio
			self.inicio.anterior=temporal
			self.inicio=temporal
		print("Elemento Insertado...")
		Leer("Continuar...")
		
	def listar(self):
		print("**********")
		temporal=self.inicio
		while temporal!=None:
			print(temporal.setNodo())
			temporal=temporal.siguiente
			
	def buscar(self,elemento):
		print("****Buscando******")
		temporal=self.inicio
		while temporal!=None:
			if temporal.cedula==elemento:
				print temporal.setNodo()
				z=Leer("Continuar...")
				return
			temporal=temporal.siguiente
		z=Leer("No Existe...")
		
	def BorrarP(self):
		if self.vacia()==False:
			self.inicio=self.inicio.siguiente
			self.inicio.anterior=None
			print("Elemento Eliminado...")
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
			
def Leer(texto):
	var=raw_input(texto)
	return var

def menu():
	os.system("clear")
	print("1.Agregar")
	print("2.Buscar")
	print("3.Eliminar Primero")
	print("4.Eliminar Ultimo")
	print("5.Listar")
	print("0.Salir")
	op=int(Leer("Seleccione: "))
	return op

lis=Lista()
opcion=9
while (opcion!=0):
	opcion=menu()
	if opcion == 1:
		c=Leer("Cedula: ")
		n=Leer("Nombre: ")
		lis.Insertar(c,n)
	elif opcion == 2:
		x=Leer("Elemento a Buscar: ")
		lis.buscar(x)
	elif opcion == 3:
		lis.BorrarP()
	elif opcion == 4:
		lis.BorrarU()
	elif opcion == 5:
		lis.listar()
		z=Leer("Continuar...")
	elif opcion == 0:
		z=Leer("Adios...")
	else:
		z=Leer("Opcion No Valida...")
