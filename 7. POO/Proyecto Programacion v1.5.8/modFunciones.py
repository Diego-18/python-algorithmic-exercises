#!usr/bin/env python
#-*-coding:UTF-8-*-

import os
from modClases import clsLista


"""
Junio del 2015
Universidad Politecnica Territorial de Portuguesa "Juan de Jesus Montilla"
Programa Nacional de Formacion en Informatica Seccion 232
Maria J. Carrasco C.  v24.019.728
Edwin A. Betancourt T. v24.587.403

clsNombre es una clase
aNombre es un atributo
fNombre es una funcion
fbNombre es una funcion booleana
fsNombre es una funcion cadena
fiNombre es una funcion entero
pNombre es un parametro
piNombre es un parametro entero
psNombre es un parametro cadena
lsNombre es una variable cadena
liNombre es una variable entero
lfNombre es una variable flotante
"""

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


lis=clsLista()
