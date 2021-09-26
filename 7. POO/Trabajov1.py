import os

#v 0.1 Chavez Diego and Moreno Leidimar

class Nodo:																#Almacen donde se guardaran los datos
    def __init__(self,ced,nom,ape,tel,cor):												
        self.anterior=None												#
        self.siguiente=None												#
        self.cedula=ced													#Variable donde almacenara la cedula
        self.nombre=nom													#Variable donde almacenara el nombre
        self.apellido=ape												#Variable donde almacenara el apellido
        self.telefono=tel												#Variable donde almacenara el telefono
        self.correo=cor													#Variable donde almacenara el Correo
	
    def setNodo(self):													#Funcion para mostrar las variables donde estan almacenados los datos
        return self.cedula, self.nombre, self.apellido, self.telefono, self.correo
  
class Agenda:															#Clase Agenda
    def __init__(self):													#Llama las variables de Inicio y Fin de la lista
        self.inicio=None
        self.fin=None

    def vacia(self):													#Funcion Vacia: permite recorrer la lista y verificar si hay algun elemento o no
        if (self.inicio==None):											#si inicio es igual a Nulo(None) es Verdadera (esta vacia)
            return True													#si inicio es diferente a Nulo(None) es falsa (no esta vacia)
        else:
            return False
          
    def agregar(self,ced,nom,ape,tel,cor):								#Funcion Agregar: permite insertar un elemento a la lista
        temporal=Nodo(ced,nom,ape,tel,cor)								#La variable temporal llama a la clase Nodo en donde se encuentra almacenado todos las variables de la lista
        if (self.vacia()==True):
            self.inicio=temporal										
            self.fin=temporal
        else:
            temporal.siguiente=self.inicio
            self.inicio.anterior=temporal
            self.inicio=temporal
        print ("Elemento Agregado...")
        leer("Continuar...")
  
    def buscar(self,elemento):
        temporal=self.inicio
        while temporal!=None:
            if temporal.cedula==elemento:
                print temporal.setNodo()
                z=leer("Continuar...")
                return
            temporal=temporal.siguiente
        z=leer("Disculpe pero no existe el elemento...")

    def listar(self):
		print("**********")
		temporal=self.inicio
		while temporal!=None:
			print(temporal.setNodo())
			temporal=temporal.siguiente
		z=leer("Continuar...")

    def eliminar(self, elemento):
        temporal=self.inicio
        self.anterior=temporal
        if self.inicio.cedula == elemento:
            self.inicio=self.inicio.siguiente
            z=leer("Eliminado con exito...")
        else:
            while temporal!= None: 
                if temporal.cedula==elemento:
                    self.anterior.siguiente = temporal.siguiente
                self.anterior = temporal
                temporal=temporal.siguiente

	def eliminar(self,num):
		temp=None
		elem=self.inicio
		i=0
		
		while (elem!=None) and (i <num):
			temp=elem 
			elem=elem.siguiente
			i+=1
			
			if (temp==None):
				self.inicio=elem.siguiente
			else:
				temp.siguiente=elem.siguiente 



    def modificar(self,elemento,modif,opcion):
        temporal=self.inicio
        while temporal!=None:
            if temporal.cedula==elemento:
                if opcion=="1":
                    temporal.cedula=modif
                    z=leer("Elemento modificado con exito...")
                elif opcion=="2":
                    temporal.nombre=modif
                    z=leer("Elemento modificado con exito...")
                elif opcion=="3":
                    temporal.apellido=modif
                    z=leer("Elemento modificado con exito...")
                elif opcion=="4":
                    temporal.telefono=modif
                    z=leer("Elemento modificado con exito...")
                elif opcion=="5":
                    temporal.correo=modif
                    z=leer("Elemento modificado con exito...")
			

                    
def leer(texto):
    var=raw_input(texto)
    return var

def Menu():
    os.system("clear")
    print ("1)Agregar")
    print ("2)Buscar")
    print ("3)Eliminar")
    print ("4)Modificar")
    print ("5)Listar")
    print ("6)Salir")
    opc=int(leer("Opcion: "))
    return opc

#PROGRAMA

lis=Agenda()
o=9
mod=0

while (o!=0):
    o=Menu()

    if (o==1):
        z=leer("Cedula: ")
        y=leer("Nombre: ")
        x=leer("Apellido: ")
        w=leer("Telefono: ")
        v=leer("Correo: ")
        lis.agregar(z,y,x,w,v)

    elif (o==2):
        u=leer("Cedula a Buscar: ")
        lis.buscar(u)

    elif (o==3):
        t=leer("Cedula a Eliminar: ")
        lis.eliminar(t)

    elif (o==4):
        u=leer("Cedula de la Persona: ")
        print ("Que desea modificar?: ")
        mod=int(leer("1.Cedula, 2.Nombre, 3.Apellido, 4.Telefono, 5.Correo: "))
        new=""
        lis.modificar(u,new,mod)
        if mod==1:
            new=int(leer("Nueva Cedula: "))
        elif mod==2:
            new=leer("Nuevo Nombre: ")
            lis.modificar(u,newnom)
        elif mod==3:
            new=leer("Nuevo Apellido: ")
            lis.modificar(u,newape)
        elif mod==4:
            new=int(leer("Nuevo Telefono: "))            
            lis.modificar(u,newtel)
        elif mod==5:
            new=leer("Nuevo Correo: ")
            lis.modificar(u,newcor)
        else:
            print ("Opcion Invalida")
            
    elif (o==5):
        lis.listar()

    elif (o==6):
        print ("Adios")

    else:
        print ("Opcion Invalida")
