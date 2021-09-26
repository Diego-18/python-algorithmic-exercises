#!usr/bin/env python
#-*-coding:UTF-8-*-

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


from modClases import clsElemento
from modClases import clsLista

from modFunciones import fbDecicion
from modFunciones import fsCadenaS
from modFunciones import fsCadena
from modFunciones import fbCancelar
from modFunciones import fiEnteroS
from modFunciones import fiEntero
from modFunciones import fsContinuar
from modFunciones import fiMenuMod
from modFunciones import fiMenuIns
from modFunciones import fsInstrucciones
from modFunciones import fiMenu
from modFunciones import fIntroducir
from modFunciones import fiContarCI
from modFunciones import fiContarTlf
from modFunciones import fsEmail
	

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
     \n\n\n\n\n         Proyecto Programacion v1.5.5\
     \n\n         By: EdwinBetanc0urt"


			


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

	elif liOpcion == 4:    #Modificar elementos
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

