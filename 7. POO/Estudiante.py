#!usr/bin/env python
# -*- coding: UTF8 -*-

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#crear promedio de notas de un estudiante (4notas)
#calificacion. ver si esta aprobado o reprobado

class clsPersona (object):                 # "clsPersona" "cls" significa= Clase u objeto
	__Nombre=''
	__Apellido=''
	def __init__(self):           # "__init__" es el inicializador del objeto o clase, es indispensable en todo procedimiento de una clase u objeto
		self.__Nombre=""
		self.__Apellido=""
	def GetNombre(self,Pnombre):               # "Get" significa= Obtener la información
		self.__Nombre=Pnombre
	def GetApellido(self,Papellido):
		self.__Apellido=Papellido
	def SetNombre(self):                       # "Set" significa= Enviar la información a la pantalla
		return self.__Nombre
	def SetApellido(self):
		return self.__Apellido
		
		
		
class clsEstudiante (clsPersona):
	__Promedio=""
	
	def __init__(self):
		self.__Promedio=0
		
	def GetPromedio(self,pPromedio):
		self.__Promedio=pPromedio
		
	def SetPromedio(self):
		return self.__Promedio
	
	def GetCalificaciones (pPromedio):
		if pPromedio>=56:
			print ("Aprobo")
		else:
			print ("ta raspao")


class clsNotas (clsEstudiante):
	__Nota1=0
	__Nota2=0
	__Nota3=0
	__Nota4=0
	def __init__(self):
		self.__Nota1=0
		self.__Nota2=0
		self.__Nota3=0
		self.__Nota4=0
		
	def GetNota1(self,pNota):
		self.__Nota1=pNota
	
	def GetNota2(self,pNota):
		self.__Nota2=pNota
	 
	def GetNota3(self,pNota):
		self.__Nota3=pNota
		
	def GetNota4(self,pNota):
		self.__Nota4=pNota

	def SetNota1(self):
		return self.__Nota1
		
	def SetNota2(self):
		return self.__Nota2
	
	def SetNota3(self):
		return self.__Nota3
	
	def SetNota4(self):
		return self.__Nota4



def fsCadena(psTexto):
	lsVar=raw_input(psTexto)
	return lsVar

def fiEntero(psTexto):
	liVar=int(raw_input(psTexto))
	return liVar

Seguir="s"
Estudiante=clsEstudiante()
Nota=clsNotas()

while (Seguir=="s" or Seguir=="S"):
	print ("Datos del Estudiante")
	Nombre_E=fsCadena("Nombre del estudiante: ")
	Apellido_E=fsCadena("Apellido del estudiante: ")
	Nota1=fiEntero("Nota1 del estudiante: ")
	Nota2=fiEntero("Nota2 del estudiante: ")
	Nota3=fiEntero("Nota3 del estudiante: ")
	Nota4=fiEntero("Nota4 del estudiante: ")
	Estudiante.GetNombre(Nombre_E)
	Estudiante.GetApellido(Apellido_E)
	Nota.GetNota1(Nota1)
	Nota.GetNota2(Nota2)
	Nota.GetNota3(Nota3)
	Nota.GetNota4(Nota4)
	Promedio=(Nota1+Nota2+Nota3+Nota4)/4
	Estudiante.GetPromedio(Promedio)
	Estudiante.GetCalificaciones(Promedio)

	print ("La nota del estudiante"), Estudiante.SetNombre(), Estudiante.SetApellido(), ("es de:"), Estudiante.SetPromedio()  , ("puntos")
	print Estudiante.GetCalificaciones()

	
	Seguir=fsCadena("Continuar (s/n): ")
	
#UPTP S2-T1