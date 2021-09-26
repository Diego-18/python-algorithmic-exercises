#!usr/bin/env python
#-*-coding:UTF-8-*-
#luis matamoro y luis vivas

class Nodo:
    def __init__(self,ced,nom,apel,tel,cor,cont):
        self.siguiente=None
        self.anterior=None
        self.nombre=nom
        self.cedula=ced
        self.apellido=apel
        self.telefono=tel
        self.correo=cor
        self.contador=cont
    def setNodo(self):
        return self.cedula,self.nombre, self.apellido, self.telefono, self.correo, self.contador

class Lista:
    def __init__(self):
        self.inicio=None
        self.fin=None
    def vacio(self):
        if self.inicio==None:
            return True
        else:
            return False

    def Insertar(self,ced,nom,apel,tel,cor,cont):
        temporal=Nodo(ced,nom,apel,tel,cor,cont)
        if self.vacio()==True:
            self.inicio=temporal
            self.fin=temporal
        else:
            temporal.siguiente=self.inicio
            self.inicio.anterior=temporal
            self.inicio=temporal
        print "elemento insertado"

    def Listar(self):
        JAJA=Leer("nombre,   apellido , cedula  , telefono    , correo, posicion")
        temporal=self.inicio
        while temporal!=None:
            print (temporal.setNodo())
            temporal=temporal.siguiente


    def Buscar(self,elemento):
        buscando=Leer("*****Buscando******")
        temporal=self.inicio
        while temporal!=None:
            if temporal.nombre==elemento:
                print temporal.setNodo()
                return
            temporal=temporal.siguiente
        z=Leer("No Existe...")

    def BorrarPosicion(self,pos):
        anterior=self.inicio
        actual=self.inicio
        v=0
        if pos >0:
            while v !=pos and actual.siguiente !=None:
                anterior=actual
                actual=actual.siguiente
                v+=+1
            if v==pos:
                anterior.siguiente=actual.siguiente

    def Modificar(self,dato):
        temporal=self.inicio
        if temporal.nombre==dato:
            print (temporal.setNodo())
            print "1. Apellido"
            print "2. Cedula"
            print "3. Nombre"
            print "4. Telefono"
            print "5. Correo"
            Dato=int(Leer("eliga el dato a modificar: "))

            if (Dato==1):
                nuevoDato=Leer("Introduzca el apellido: ")
                if nuevoDato.isalpha()==True:
                    temporal.nombre=(nuevoDato.upper())
                    vm=Leer("------MODIFICACION EXITOSA------")
                else:
                    print  "los apellidos solo tienen letras---- te toca hacer el proceso de nuevo"
                    vm=Leer("intente de nuevo siguiendo las indicaciones")

            if (Dato==2):
                print "***ingresa la cedula sin espacios ni puntos entre los numeros***"
                nuevoDato=Leer("Introduzca el nuevo cedula: ")
                if nuevoDato.isdigit()==True:
                    temporal.apellido=nuevoDato
                    vm=Leer("------MODIFICACION EXITOSA------")
                else:
                    print "ocurrio un error"
                    vm=Leer("intente de nuevo siguiendo las indicaciones")

            if (Dato==3):
                nuevoDato=Leer("Introduzca el nuevo nombre: ")
                if nuevoDato.isalpha()==True:
                    temporal.cedula=(nuevoDato.upper())
                    vm=Leer("------MODIFICACION EXITOSA------")
                else:
                    print "los nombres no llevan letras"

            if (Dato==4):
                print "el telefono no debe tener espacio entre los numeros ni - "
                nuevoDato=Leer("Introduzca el nuevo telefono: ")
                if nuevoDato.isdigit()==True:
                    temporal.telefono=nuevoDato
                    vm=Leer("------MODIFICACION EXITOSA------")
                else:
                    print "ocurrio un error-- sigue la indicacion para la proxima"

            if (Dato==5):
                nuevoDato=Leer("Introduzca el nuevo correo: ")
                temporal.correo=nuevoDato
                vm=Leer("------MODIFICACION EXITOSA------")
        else:
            ll=Leer("esa persona no se encuentra en la lista --salao--")
        

def Leer(texto):
    var=raw_input(texto)
    return var

def menu():
    print("1.Agregar")
    print("2.Buscar")
    print("3.Eliminar")
    print ("4.Modificar")
    print("5.Listar")
    print("0.Salir")
    op=int(Leer("Seleccione su opcion: "))
    return op

lis=Lista()
opcion=9
con=0
while (opcion!=0):
    opcion=menu()
    con=con+1
    if opcion == 1:
        print "la cedula solo debe ser numeros sin espacios entre si"
        ce=Leer("Cedula: ")
        if ce.isdigit()==True:
            print "vas bien"
        else:
            print "lo siento la cedula solo debe ser los numeros seguidos sin espeacio y sin letras"

        n=Leer("Nombre: ")
        if n.isalpha()==True:
            print "vas bien"
        else:
            print "lo siento el nombre solo debe tener letras-error"
        
        ap=Leer("Apellido: ")
        if ap.isalpha()==True:
            print "vas bien"
        else:
            print "lo siento el apellido solo debe tener letras-error"
        
        tele=Leer("Telefono: ")
        if tele.isdigit()==True:
            print "vas bien"
        else:
            print "lo siento el telefono solo debe ser los numeros seguidos sin espeacio y sin letras-error"
            
        co=Leer("Correo: ")
        
        if ce.isdigit()==True and n.isalpha()==True and ap.isalpha()==True and tele.isdigit()==True:
            lis.Insertar((n.upper()),(ap.upper()),ce,tele,co,con)
            wtf=Leer("...continuar...")
        else:
            print "por no seguir las indicaciones previas estos datos no entraron"
        
    if opcion == 2:
        x=Leer("Elemento a Buscar (apellido): ")
        lis.Buscar(x.upper())

    if opcion == 3:
        y=int(raw_input("lugar que desea eliminar desde el primero: "))
        lis.BorrarPosicion(y)
        t=Leer("...Continuar...")

    if opcion==4:
        w=Leer("ingrese el apellido para buscar los datos que corresponden y poder modificarlo a gusto: ")
        lis.Modificar(w.upper())

    if opcion == 5:
        lis.Listar()
        z=Leer("...Continuar...")

    if opcion == 0:
        z=Leer("Adios...")
