#INICIO$$$$$$$$$$$$$$$$$$
import os

class Nodo():
	def __init__(self,ced,nom,combo,cant):
		self.sig=None
		self.ant=None
		self.ced=ced
		self.nom=nom
		self.combo=combo
		self.cant=cant

	def setNodo(self):
		return self.ced, self.nom, self.combo, self.cant

class lista():
	def __init__(self):
		self.ini=None
		self.fin=None

	def vacia(self):
		if (self.ini==None):
			return True
		else:
			return False

	def cargar(self,ced,nom,combo,cant):
		temp=Nodo(ced,nom,combo,cant)
		if self.vacia()==True:
			self.ini=temp
			self.fin=temp
		else:
			temp.sig=self.ini
			self.ini.ant=temp
			self.ini=temp
		print ("Insertados...")
		leer("Pulse una tecla ")

	def listar(self):
		print("************")
		temp=self.ini
		while (temp!=None):
			print (temp.setNodo())
			temp=temp.sig
	
	def buscar(self,elem):
		print ("****BUSCANDO****")
		temp=self.ini
		while temp!=None:
			if (temp.nom==elem):
				print temp.setNodo()
				z=leer("Pulse una tecla ")
				return
			temp=temp.sig
		z=leer("No esta...")

	def elp(self):
		if self.vacia()==False:
			self.ini=self.ini.sig
			self.ini.ant=None
			print ("Eliminado")
		else:
			print ("Vacia")
			leer("Pulse una tecla ")

def leer(t):
	v=raw_input(t)
	return v

def menu():
	os.system("clear")
	print ("1. Agregar")
	print ("2. Eliminar Primero")
	print ("3. Mostrar todos")
	print ("4. Buscar")
	print ("0. Salir")
	O=int(leer("Opcion: "))
	return O

lis=lista()
opcion=9
while (opcion!=0):
	opcion=menu()
	if (opcion==1):
		x=leer("Nombre: ")
		f=leer("Cedula: ")
		print ("Combo 1=400 Combo 2=500 Combo 3=700")
		g=int(leer("Combo: "))
		h=int(leer("Cantidad: "))
		if g==1:
		  tot=h*400
		elif g==2:
		  tot=h*500
		else:
		  tot=h*700
		lis.cargar(x,f,g,tot)
	if (opcion==2):
		lis.elp()
	if (opcion==3):
		lis.listar()
		z=leer("Pulse una tecla ")
	if (opcion==4):
		x=leer("Cedula: ")
		lis.buscar(x)
	else:
		print "Adios"
