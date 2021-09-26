#!usr/bin/env python
#-*-coding:UTF-8-*-

import os

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
				break
				
			print ("\n\n     Se ha culminado la busqueda completamente...")
			fsContinuar()



	def fEliminar(self, pCI):  #Opcion 3
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

class clsVariables:
	def __init__(self):
		
	
