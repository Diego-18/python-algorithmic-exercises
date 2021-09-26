#!usr/bin/env python
#-*-coding:UTF-8-*-

"""
Junio del 2015
Universidad Politecnica Territorial de Portuguesa "Juan de Jesus Montilla"
Programa Nacional de Formacion en Informatica Seccion 232
Maria J. Carrasco C.  v24.019.728
Edwin A. Betancourt T. v24.587.403
"""

import os
#importa utilidades del sistema operativo


#from modFunciones import fsCadena
#importa la funcion (o clase) fsCadena del archivo modFunciones.py

#import modFunciones  
#importa todas las funciones (o clases) del archivo modFunciones
#y al utilizar la funcion cadena seria modFunciones.fsCadena


"""
clsNombre es una clase
aNombre es un atributo o argumento


FUNCIONES
fNombre es una funcion
fbNombre es una funcion booleana
fsNombre es una funcion cadena
fiNombre es una funcion entero

PARAMETROS
pNombre es un parametro
piNombre es un parametro entero
psNombre es un parametro cadena

VARIABLES
lsNombre es una variable cadena
liNombre es una variable entero
lfNombre es una variable flotante
"""


class clsElemento:
	def __init__(self,pCed,pNom, pApe, pTel, pEmail):
		self.siguiente=None
		self.anterior=None
		self.aCedula=pCed      #Atributo-Cedula sera igual a Parametro-Ced
		self.aNombre=pNom		#Atributo-Nombre sera igual a Parametro-Nom
		self.aApellido=pApe		 #Atributo-Apellido sera igual a Prametro-Ape
		self.aTelefono=pTel     #Atributo-Telefono sera igual a Parametro-Tel
		self.aEmail=pEmail     #Atributo-Email sera igual a Parametro-Email

	def setElemento(self):
		return self.aCedula, self.aNombre, self.aApellido, self.aTelefono, self.aEmail
	"""envia o retorna los atributos Cedula, Nombre, Apellido, Telefono y Email"""



class clsLista:
	def __init__(self):
		self.inicio=None
		self.fin=None


	def fbVacia(self):  #Esta funcion indica si clsLista esta vacia=Verdad o si tiene algo=Falso
		if self.inicio==None:
			return True
		else:
			return False


	def fInsertar(self,pCed,pNom, pApe, pTel, pEmail):   #Opcion 1 en el fiMenu (Agregar)
		temporal=clsElemento(pCed,pNom, pApe, pTel, pEmail)
		self.liCedula=pCed #esta linea es para que fbExiste pueda hacer la comparacion
		if self.fbVacia()==True:
			self.inicio=temporal
			self.fin=temporal
		else:
			if self.fbExiste(self)==True:  #si recibe TRUE es porque exsite ya la cedula
				return						#interrumpe el ciclo para que no haga mas nada
			if self.fbExiste(self)==False:
				temporal.siguiente=self.inicio
				self.inicio.anterior=temporal
				self.inicio=temporal
		print("\n\n   Datos Insertados exitosamente...")
		print lsRegistro
		print ("   "), (temporal.setElemento())
		fsContinuar()

	def fbExiste(self, liCedula):
		temporal=self.inicio
		while temporal!=None:
			if str(temporal.aCedula)==str(self.liCedula):
				print ("\n\n         ATENCION: Ya existe ese numero de CEDULA registrado ")
				print lsRegistro, (" "), temporal.setElemento()
				fsContinuar()
				return True  #si ya existe retorna TRUE a fInsertar para que romapa el ciclo y no inserte nada
			temporal=temporal.siguiente
		return False


	def fListar(self):    #Opcion 5 en el fiMenu (Listar)
		print lsRegistro #Variable que contiene el encabezado de datos registrados
		temporal=self.inicio
		if self.inicio == None:
			print "\n\n   No hay ningun dato a mostrar, ESTA VACIO...\n   Por favor seleccione la opcion 1 para agregar. "
		else:
			while temporal!=None:
				print ("   "), (temporal.setElemento())
				temporal=temporal.siguiente


	
	def fBuscar(self,pElemento):   #Opcion 2 en el fiMenu (Buscar)
		print("\n\n   ********************* B U S C A N D O  ********************")
		print ("\n   Cedula  -  Nombre  -  Apellido  -  Telefono   -   CorreoE \n")
		temporal=self.inicio
		if self.inicio == None:
			print "\n\n   No hay ningun dato a buscar, ESTA VACIO...\n   Por favor seleccione la opcion 1 para agregar. "
			fsContinuar()
		
		else:
			temporal=self.inicio
			while temporal!=None: 
				
				"""dentro del WHILE se colocan tantos IF como la cantidad de atributos q se busquen como por
				ejemplo en este caso el aCedula, el aNombre, aApelldo, etc.. si tuviera aEdad o cualquier
				otro atributo que se buscara, color, talla etc, se coloca el IF con ese atributo solamente
				y solo se cambia la primera linea, if temporal.ATRIBUTOEJEMPLO==pElemento: , es decir el
				condiciona. Lo que sigue dentro del IF es solo copiar y pegar"""
				if str(temporal.aCedula)==pElemento:		#aCedula fue guardada como entero(integer) en la lista, por ello debe ser tranformada a cadena (string)
					print ("   "), temporal.setElemento()	#encerrandolo enparentesis con el str, ya que pElemeto fue introducida como cadena y pueden estar escritas
															#iguales y al hacer la comparacion de igualdad sera falsa si son de tipos diferentes comparando a
															#pesar de que sea similar aCedula 24587403 (es de tipo entero) con pElemento 24587403 (es de tipo cadena)
				if temporal.aNombre==pElemento:
					print ("   "), temporal.setElemento()
					
				if temporal.aApellido==pElemento:
					print ("   "), temporal.setElemento()
					
				if str(temporal.aTelefono)==(pElemento):
					print ("   "), temporal.setElemento()
					
				if temporal.aEmail==pElemento:
					print ("   "), temporal.setElemento()
					
				temporal=temporal.siguiente
				#break
				
			print ("\n\n     Se ha culminado la busqueda completamente...")
			fsContinuar()



	def fEliminar(self, pCI):  #Opcion 3 solo elimina buscando por la cedula
		if self.fbVacia() == True:
			print "\n\n   No hay ningun dato a eliminar, ESTA VACIO...\n   Por favor seleccione la opcion 1 para agregar. "
			fsContinuar()
		else:
			temporal=self.inicio
			self.anterior=temporal
			while temporal!= None: 
				if temporal.aCedula==int(pCI):
					print "\n   Este es su opcion a elminimar"
					print ("   "),temporal.setElemento()
					liValidar=fbDecicion("\n   Esta seguro que decea eliminar?\n    Escriba su opcion: Si -  No: ")
					if fbCancelar(liValidar)==True:
						return
					if liValidar==1:
						self.anterior.siguiente = temporal.siguiente
						print ("\n\n   **************** E L I M I N A N D O ****************")
						print ("\n   Cedula  -  Nombre  -  Apellido  -  Telefono   -   CorreoE \n")
						print ("   "),temporal.setElemento()
						print("\n   Persona eliminada exitosamente...")
						fsContinuar()
						if self.fbVacia() == True:
							print "\n\n   Se han eliminado todas las personas... "
							fsContinuar()
					return
				self.anterior = temporal
				temporal=temporal.siguiente
 			print "\n\n   No existe una persona registrada con ese numero de cedula..."
			fsContinuar()

	def fVaciar(self):  #Opcion 6 Vaciar
		if self.fbVacia() == True:
			print "\n\n   No hay datos para vacias,  ESTA VACIO...\n   Por favor seleccione la opcion 1 para agregar. "
			fsContinuar()
		else:
			temporal=self.inicio
			self.anterior=temporal
			lis.fListar()
			liValidar=fbDecicion("\n   Esta seguro que decea vaciar todos?\n    Escriba su opcion: Si -  No: ")
			if fbCancelar(liValidar)==True:
				return
			if liValidar==1:
				while self.inicio!= None: 
					self.inicio=self.inicio.siguiente  #esta linea permite eliminar el unico o el ultimo que existe
					self.anterior.siguiente = temporal.siguiente
					if self.fbVacia() == True:
						print "\n\n   Todos los datos han sido eliminados exitosamente\n   Esta completamente VACIO... "
						fsContinuar()
						return
					temporal=temporal.siguiente
				fsContinuar()


 	def fModificar(self,pCI):   #Opcion 4 de fiMenuMod
		if self.fbVacia()==True:
			print("\n\n   No hay ningun dato, ESTA VACIO...\n   Por favor seleccione la opcion 1 para agregar. ")
			fsContinuar()
		else:
			temporal=self.inicio
			while temporal!=None:
				if temporal.aCedula==int(pCI):
					print ("      "),temporal.setElemento()
					fsContinuar()
					liOpcionM=9
					while liOpcion!=0:
						liOpcionM=fiMenuMod()
						if fbCancelar(liOpcionM)==True:
							return
						if liOpcionM==1:  #Modificar Cedula
							liValidar=fbDecicion("   Esta seguro que decea modificar la CEDULA?\n    Escriba su opcion: Si -  No: ")
							if liValidar==1:
								print lsRegistrado #Variable que contiene el encabezado de datos
								print ("   "),temporal.setElemento()
								liCINew=fiEntero("\n     Por favor introduzca la nueva CEDULA para cambiarla:\n    ")
								if fbCancelar(liCINew)==True:
									return
								temporal.aCedula=liCINew
								print ("\n   Se modifico la CEDULA correctamente...")
								print lsRegistrado #Variable que contiene el encabezado de datos
								print ("   "),temporal.setElemento() 
								fsContinuar()
							else:
								print("  El registro no fue modificado...")
								fsContinuar
						
						elif liOpcionM==2:  #Modificar Nombre
							liValidar=fbDecicion("   Esta seguro que decea modificar el NOMBRE?\n   Escriba su opcion: Si -  No: ")
							if liValidar==1:
								print lsRegistrado #Variable que contiene el encabezado de datos
								print ("   "),temporal.setElemento()
								lsNombreNew=fsCadena("   Por favor introduzca el nuevo NOMBRE para cambiarlo:\n    ")
								if fbCancelar(lsNombreNew)==True:
									return
								temporal.aNombre=lsNombreNew
								print("\n   Se modifico el NOMBRE correctamente...")
								print lsRegistrado #Variable que contiene el encabezado de datos
								print ("   "),temporal.setElemento()
								fsContinuar()
							else:
								print ("   El registro no fue modificado...")
								fsContinuar()
						
						elif liOpcionM==3:  #Modificar Apellido
							liValidar=fbDecicion("   Esta seguro que decea modificar el APELLIDO?\n   Escriba su opcion: Si -  No: ")
							if liValidar==1:
								print lsRegistrado #Variable que contiene el encabezado de datos
								print ("   "),temporal.setElemento()
								lsApellidoNew=fsCadena("   Por favor introduzca el nuevo APELLIDO para cambiarlo:\n    ")
								if fbCancelar(lsApellidoNew)==True:
									return
								temporal.aApellido=lsApellidoNew
								print("\n   Se modifico el APELLIDO correctamente...")
								print lsRegistrado #Variable que contiene el encabezado de datos
								print ("   "),temporal.setElemento()
								fsContinuar()
							else:
								print("   El registro no fue modificado...")
								fsContinuar()
						
						elif liOpcionM==4:  #Modificar Telefono
							liValidar=fbDecicion("   Esta seguro que decea modificar el TELEFONO?\n   Escriba su opcion: Si -  No: ")
							if liValidar==1:
								print lsRegistrado #Variable que contiene el encabezado de datos
								print ("   "),temporal.setElemento()
								liTelefonoNew=fiEntero("   Por favor introduzca el nuevo TELEFONO para cambiarlo:\n    ")
								if fbCancelar(liTelefonoNew)==True:
									return
								temporal.aTelefono=liTelefonoNew
								print ("\n   Se modifico el TELEFONO correctamente...")
								print lsRegistrado #Variable que contiene el encabezado de datos
								print ("   "),temporal.setElemento()
								fsContinuar()
							else:
								print("   El registro no fue modificado...")
								fsContinuar()
						
						elif liOpcionM==5:  #Modificar Email
							liValidar=fbDecicion("   Esta seguro que decea modificar el CORREO ELECTRONICO?\n   Escriba su opcion: Si -  No: ")
							if liValidar==1:
								print lsRegistrado #Variable que contiene el encabezado de datos
								print ("   "),temporal.setElemento()
								lsEmailNew=fsCadenaS("   Por favor introduzca el nuevo CORREO ELECTRONICO para cambiarlo:\n    ")
								if fbCancelar(lsEmailNew)==True:
									return
								temporal.aEmail=lsEmailNew
								print ("\n   Se modifico el CORREO ELECTRONICO correctamente...")
								print lsRegistrado #Variable que contiene el encabezado de datos
								print ("   "),temporal.setElemento()
								fsContinuar()
							else:
								print ("   El registro no fue modificado...")
								fsContinuar()
						elif liOpcionM==0:
							print ("   Ha elegido ir al menu principal...")
							fsContinuar()
							return
						else:
							lsValido=fsCadenaS("\n\n   OPCION SELECCIONADA NO VALIDA... \n   Por favor introduzca su opcion del 0 al 5 ")
					return
				temporal=temporal.siguiente
			print ("   No existe una persona registrada con ese numero de cedula...")
			fsContinuar()




def fbDecicion(psTexto):
	lsValidacion=fsCadena(psTexto)
	if (lsValidacion=="S") or (lsValidacion=="SI") :   #no importa las mayusculas porque fsCadena de la linea 248 las pasa a mayuscula
		print ("\n      Acepto el cambio ")
		liCodigo=fiEntero("    Por favor introduzca este codigo: 8910\n    Para verificar y proseguir: ")
		if (liCodigo==8910):
			print ("\n    Codigo correcto!!!")
			liDecicion=1
			return liDecicion
	elif (lsValidacion=="N") or (lsValidacion=="NO"):  #aplica aca tambien, no importa sino solo las mayusculas
		liDecicion=2
		print ("\n      Denego el cambio ")
		return liDecicion
	
	elif lsValidacion==232 or lsValidacion=="SALIR" or lsValidacion=="232":
		print "     operacion cancelada por el usuario"
		liDecicion=232
		return liDecicion


def fsCadenaS(pTexto):
	lsVar=raw_input(pTexto)
	return lsVar.upper()


def fsCadena(psTexto):
	liValidar=1
	while liValidar!=0:
		lsVar=raw_input(psTexto)
		if lsVar.isalpha()==True:
			liValidar=0
		else:
			print "       ATENCION: solo letras A...Z"
	return lsVar.upper()


def fbCancelar(psTexto):
	if psTexto==232 or psTexto=="232" or psTexto=="SALIR":
		print ("     ATENCION: Operacion cancelada por el USUARIO!!! ")
		fsContinuar()
		return True
	return False


def fiEnteroS(piTexto):
	liVar=int(raw_input(piTexto))
	return liVar


def fiEntero(piTexto):
	liValidar=1
	while liValidar!=0:
		liVar=raw_input(piTexto)
		if liVar.isdigit()==True:
			liValidar=0
		else:
			print "       ATENCION: solo numeros 0...9"
	return int(liVar)


def fsContinuar():
	return fsCadenaS ("\n\n     Por favor pulse enter para continuar ")


def fiMenuMod():
	os.system("cls") #usar este limpia pantallas en Windows
#	os.system("clear") #usar este limpia pantallas en linux
	print ("\n\n         ¿QUE DECEA MODIFICAR?\n")
	print ("  1. Editar CEDULA")
	print ("  2. Editar NOMBRE")
	print ("  3. Editar APELLIDO")
	print ("  4. Editar TELEFONO")
	print ("  5. Editar EMAIL")
	print ("  0. Ir al menu principal"), lsCancelar
	liOpcionMod=fiEntero("\n\n   Por favor seleccione su opcion y presione enter: ")
	return liOpcionMod



def fiMenuIns():
	os.system("cls") #usar este limpia pantallas en Windows
#	os.system("clear") #usar este limpia pantallas en linux
	print ("\n\n            INSTRUCCIONES ACERCA DE... \n ")
	print ("  1. Agregar")
	print ("  2. Buscar")
	print ("  3. Eliminar")
	print ("  4. Modificar")
	print ("  5. Listar")
	print ("  6. Vaciar")	
	print ("  0. Ir al menu principal"), lsCancelar
	liOpcionIns=fiEntero("\n\n   Por favor seleccione su opcion y presione enter: ")
	return liOpcionIns

def fsInstrucciones():
	liOpcionIns=9
	while (liOpcionIns!=0):
		liOpcionIns=fiMenuIns()
		
		if liOpcionIns == 1:    #Agregar elementos
			print lsAgregar
			fsContinuar()
			
		elif liOpcionIns == 2:    #Buscar elementos 
			print lsBuscar
			fsContinuar()
			
		elif liOpcionIns == 3:   #Eliminar elementos
			print Eliminar
			fsContinuar()
			
		elif liOpcionIns == 4:    #Modificar elementos
			print lsModificar
			fsContinuar()
			
		elif liOpcionIns == 5:  #Listar los elemnetos
			print lsListar
			fsContinuar()
			
		elif liOpcionIns == 6: #vaciar la lista
			print lsVaciar
			fsContinuar()
			
		elif (liOpcionIns == 0) or (liOpcionIns==232):
			fsContinuar()

		else:
			lsValido=fsCadenaS("\n\n   OPCION SELECCIONADA NO VALIDA... \n   Por favor introduzca su opcion del 0 al 6")


def fiMenu():
	os.system("cls") #usar este limpia pantallas en Windows
#	os.system("clear") #usar este limpia pantallas en linux
	lsTitulo="BIENVENIDO AL PROYECTO DE PROGRAMACION"
	print ("\n\n"),lsTitulo.center(50, " "),("\n")
	print ("  1. Agregar")
	print ("  2. Buscar")
	print ("  3. Eliminar")
	print ("  4. Modificar")
	print ("  5. Listar")
	print ("  6. Vaciar")
	print ("  7. Intrucciones Basicas")	
	print ("  0. Salir"), lsCancelar
	liOpcionMenu=fiEntero("\n\n   Por favor seleccione su opcion y presione enter: ")
	return liOpcionMenu


def fIntroducir():
	liCI=fiContarCI()  #la funcion retorna 3 valores, la cedula de 7-8 digitos, 232. true
	if fbCancelar(liCI)==True  or liCI==True:  #si la liCI vale 232 valdra true y cancela 
		return
	lsNombre=fsCadena("     Por favor introduzca el NOMBRE: ")
	if fbCancelar(lsNombre)==True:
		return
	lsApellido=fsCadena("     Por favor introduzca el APELLIDO: ")
	if fbCancelar(lsApellido)==True:
		return
	liTelefono=fiContarTlf()
	if fbCancelar(liTelefono==True) or liTelefono==True:
		return
	lsEmail=fsEmail()  #se usa la fsCadenaS ya  que el correo puede llevar numeros o simbolos
	if fbCancelar(lsEmail==True) or lsEmail==True:
		return
	lis.fInsertar(liCI,lsNombre, lsApellido, liTelefono, lsEmail)
	return 


def fiContarCI():
	liEntrar=1
	while liEntrar!=0:
		liCI=fiEntero("     Por favor introduzca la CEDULA: ")
		if fbCancelar(liCI)==True:
			return True
		if (len(str(liCI))<=6) or (len(str(liCI))>=9):
			print ("       La cedula debe contener de 7 a 8 digitos ")
			liEntrar=1
		if (len(str(liCI))==7) or (len(str(liCI))==8):
			liEntrar=0
	return liCI


def fiContarTlf():
	liEntrar=1
	while liEntrar!=0:
		liTlf=fiEntero("     Por favor introduzca el TELEFONO: 0")
		if fbCancelar(liTlf)==True:
			return True
		if (len(str(liTlf))!=10):
			print ("       El telefono debe contener 11 digitos ")
			liEntrar=1
		if (len(str(liTlf))==10):
			liEntrar=0  #podria colocarse break para romper el while
			return int(liTlf)
	return


def fsEmail():
	liEntrar=1
	while liEntrar!=0:
		lsEmail=fsCadenaS("     Por favor introduzca el Correo: ")
		if fbCancelar(lsEmail)==True:
			return True
			
		if (lsEmail.find ("@"))==-1:
			print ("       Falta el arroba @ ")
			liEntrar=1
			
		if (lsEmail.find ("com"))==-1  or (lsEmail.find ("COM"))==-1:
			if (lsEmail.find ("."))==-1  or (lsEmail.find ("."))==-1:
				print ("       Falta el dominio .com ")
				liEntrar=1
		
		if ("." in lsEmail) and (("com" in lsEmail) or ("COM" in lsEmail)) and ("@" in lsEmail):
			liEntrar=0  #podria colocarse break para romper el while
	return lsEmail

# los \n son salto de linea para que al imprimir en pantalla no se haga corrido en una linea
# los \ son para poder continuar los comentarios en el codigo fuente en la lina siguiente
lsBienvenida= "\n\n\n                          BIENVENIDO... \n\n \
          Este es un mini sistema donde podra registrar,\n\
     datos de diferentes personsas incluyendo, la cedula,\n\
     nombre y apellido, telefono y correo electronivo de \n\
     contacto. Ademas de agregar y registrar, tambien en \n\
     caso de cometer algun error al hacer los registros,\n\
     puede modificar los datos que decee. Puede mostrar\n\
     todos los datos que se han registrado y si lo decea\n\
     eliminar todos los datos de una persona e inclusive\n\
     vaciar toda la lista...\
     \n\n\n\n\n         Proyecto Programacion v1.5.8\
     \n\n         By: EdwinBetanc0urt"

lsRegistro="\n\n   ************ D A T O S - R E G I S T R A D O S ************\n\
   Cedula  -  Nombre  -  Apellido  -  Telefono   -   CorreoE \n"

lsCancelar="\n      Escriba la palabra SALIR o el numero 232 para \
cancelar la operacion cuando lo decee en el momento que decee"

lsRegistrado="\n   Estos son los nuevos datos registrados\n\
   Cedula  -  Nombre  -  Apellido  -  Telefono   -   CorreoE \n"


lsAgregar="\n\
   Esta opcion, Agregar permite insertar datos personales en la\n\
   lsita y ser guardados como por ejemplo la Cedula, el Nombre,\n\
   el Apellido, Telefono sea celular o local,  el Emali o Correo\n\
    Electronio... \n"

lsBuscar="\n\
   Esta opcion, Buscar permitira buscar el datos personales que\n\
   se ha introducido sea como lo es la Cedula, el Nombre, el\n\
   Apellido, Telefono o el Correo Electronio ser comparado con\n\
   los datos que internamente estan guardados ya, y de existir \n\
   coincidencias o no, mostrara si existe y quien es, junto con\n\
   todos sus datos registrados...\n"

Eliminar="\n\
   Con este, Eliminar permite borrar todos los datos que estan\n\
   registrados de una sola persona, buscando mediante la cedula\n\
   unicamente, donde se debera confirmar el eliminar mediante\n\
   codigos de seguridad para evitar borrar los datos de alguien\n\
   por accidente...\n"

lsModificar="\n\
   Si ha introducido la mayoria de los datos de manera correcta\n\
   y solo en una parte se ha equivocado no hay necesidad de\n\
   eliminar todos los datos, sino de manera mas facil y sencilla\n\
   editar si lo quiere solo el dato que esta erroneo, o aunque no\n\
   limitado unicamente uno solo sino tambien todos aquellos datos\n\
   que decee modificar o editar...\n"

lsListar="\n\
   Permite ver todos aquellos datos personales que actualmente estan\n\
   registrados, los vera en forma de lista y de manera ascendente\n\
   del ultimo que se agrego al primero... \n"
   
lsVaciar="\n\
   MUCHO CUIDADO CON ESTA OPCION, eliminara todos y cada uno de los\n\
   datos que han sido registrados y estos no se pueden recuperar\n\
   una vez que ha finalizado la operacion, por seguiridad debe ser\n\
   verificado pr codigos de seguridad para evitar que sean borrados\n\
   por accidene TODOS LOS DATOS... \n"
			


lis=clsLista()
liOpcion=9

print lsBienvenida
fsContinuar()

while (liOpcion!=0):
	liOpcion=fiMenu()

	if liOpcion == 1:    #Agregar elementos
		fIntroducir()

	elif liOpcion == 2:    #Buscar elementos 
		if lis.fbVacia()==True:
			print "\n\n   La Lista esta vacia, no hay datos para buscar"
			fsContinuar()
		else:
			lsElemento=fsCadenaS("\n\n   Elemento a Buscar (Cedula, Nombre, Apellido, Telefono o Email):\n      ")
			lis.fBuscar(lsElemento)
		
	elif liOpcion == 3:   #Eliminar elementos
		if lis.fbVacia()==True:
			print "\n\n   La Lista esta vacia, no hay datos para eliminar"
			fsContinuar()
		else:
			lsCI=fsCadenaS("\n\n   Introduzca el numero de cedula de la persona que va a elminiar:\n      ")
			if fbCancelar(lsCI)==False:
				lis.fEliminar(lsCI)

	elif liOplsBuscarcion == 4:    #Modificar elementos
		if lis.fbVacia()==True:
			print "\n\n   La Lista esta vacia, no hay datos para modficar"
			fsContinuar()
		else:
			lsCI=fiEntero("\n\n   Por favor introduzca la CEDULA de la persona decea modificar los datos:\n      ")
			if fbCancelar(lsCI)==False:
				lis.fModificar(lsCI)
		
	elif liOpcion == 5:  #Listar los elemnetos
		lis.fListar()
		fsContinuar()

	elif liOpcion == 6:
		lis.fVaciar()
		fsContinuar

	elif liOpcion == 7:  #Mostrar instrucciones basicas
		fsInstrucciones()

	elif (liOpcion == 0) or (liOpcion==232):
		print ("\n\n   Gracias por usar este programa. ADIOS...")

	else:
		lsValido=fsCadenaS("\n\n   OPCION SELECCIONADA NO VALIDA... \n   Por favor introduzca su opcion del 0 al 7")

