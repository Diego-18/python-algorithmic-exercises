import os

#Creado por Diego Chavez Seccion:232

class Nodo:
	def __init__(self,nom,ced,com,cant,cost):
		self.siguiente=None
		self.anterior=None
		self.cedula=ced
		self.nombre=nom
		self.combo=com
		self.cantidad=cant
				
	def SetNodo(self):
		return self.nombre, self.cedula, self.combo, self.cantidad
	
class Lista:
	def __init__(self):
		self.inicio=None
		self.fin=None
	
	def Vacia():
		if self.inicio==None:
			return True
		else:
			return False
	
	def Agregar(self,ced,nom,com,cant):
		temporal=Nodo(ced,nom,com,cant)
		if self.Vacia==True:
			self.inicio=temporal
			self.fin=temporal
		else:
			temporal.siguiente=self.inicio
			self.inicio.anterior=temporal
			self.inicio=temporal
		print ("ELEMENTO INSERTADO...")
		Leer("Continuar...")
	
	def Buscar(self,elemento):
		print("****BUSCANDO****")
		temporal=self.inicio
		while temporal!=None:
			if (temporal.ced==elemento):
				print (temporal.ced.setNodo())
				z=Leer("Continuar...")
				return
			temporal=temporal.siguiente
		z=Leer("No existe...")
	
	def Imprimir(self):
		print ("##########################")
		temporal=self.inicio
		while temporal!=None:
			print (temporal.SetNodo())
			temporal=temporal.siguiente
		z=Leer("Continuar...")
	
	def EliminarP(self):
		if self.Vacia()==False:
			self.inicio=self.inicio.siguiente
			self.inicio.anterio=None
			print ("Eliminado")
		else:
			print ("Lista Vacia")
			z=Leer("Continuar...")
	
def Leer(texto):
	var=raw_input(texto)
	return var

def menu():
	os.system=("clear")
	print ("1.Agregar")
	print ("2.Buscar")
	print ("3.Imprimir")
	print ("4.Eliminar Primero")
	print ("5.Salir")
	opc=int(Leer("Opcion: "))
	return opc

lis=Lista()
op=9
co=0

while op!=0:
	op=menu()
	if op==1:
	    c=Leer("Cedula: ")
	    n=Leer("Nombre: ")
	    print ("1.Combo1, 2.Combo2, 3.Combo3: ")
	    g=int(Leer("Combo: "))
	    h=int(Leer("Cantidad: "))
	    if g==1:
                tot=h*400
            elif g==2:
                tot=h*500
            else:
                tot=h*700
	    lis.Agregar(c,n,co,g,tot)
	if op==2:
		c=Leer("Cedula: ")
		lis.Buscar(c)
		z=Leer("Continuar...")
	if op==3:
		lis.Imprimir()
	if op==4:
		lis.EliminarrP()
	else:
		print "Adios" 
