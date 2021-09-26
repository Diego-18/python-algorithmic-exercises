#usr/bin/env python
#-*- coding: utf8-*-
import os

################################
# Elaborado por: DIEGO CHAVEZ  #
################################
	
class clsPersona(object):
	__nombre= ""
	__apellido=""
	__Cedula=""
	def __init__(self):
		self.__Nombre=""
		self.__Apellido=""
		self.__Cedula=""
	def GetNombre (self,PNombre):
		self.__Nombre=PNombre
		
	def setNombre(self):
		return self.__Nombre
		
	def GetApellido(self,PApellido):
		self.__Apellido=PApellido
	
	def setApellido(self):
		return self.__Apellido	
		
		
	def GetCedula(self,PCedula):
		self.__Cedula=PCedula
		
	def setCedula(self):
		return self.__Cedula
	
	def Saludo():
		print "Adios"
		
		
class clsProfesor(clsPersona):
	__Categoria=""
	__HorasA=""
	__Sueldo=""
	
	def __init__(self):
		self.__Categoria=""
		self.__HorasA=""
		self.__Sueldo=""
				
		
	def GetCategoria(self,PCategoria):
		self.__Categoria=PCategoria
		
	def setCategoria(self):
		return self.__Categoria
	
	def GetHorasA(self, PHorasA):
		self.__HorasA=PHorasA
		
	def setHorasA(self):
		return self.__HorasA
		
	def GetSueldo(self,pSueldo):
		self.__Sueldo=PSueldo
		
	def setSueldo(self):
		return self.__Sueldo
	
	def GetHoras(self,pSueldo):
		self.__Sueldo=PSueldo
		
	def setSueldo(self):
		return self.__Sueldo
		
					
class clsEstudiante(clsPersona):
	__NotaFinal=""
	__CantidadMateria=""
	
	def __init__(self):
		self.__NotaFinal=""
		self.__CantidadM=""
		
	def GetNotaFinal(self,PNotaFinal):
		self.__NotaFinal=PNotaFinal
		
	def setNotaFinal(self):
		return self.__NotaFinal

	def GetCantidadM(self,PCantidadM):
		self.__CantidadM=PCantidadM
		
	def setCantidadM(self):
		return self.__CantidadM
	

def fsCadena (psTexto):
	lsVar= raw_input(psTexto)
	return lsVar
	
def fiEntero (psTexto):
	liVar= int (raw_input(psTexto))
	return liVar

def fsContinuar():
	return fsCadena ("pulse una tecla para continuar ")

def Menu():
	os.system ("clear")
	print "1. Estudiante"
	print "2. Profesor"
	print "0. Salir"
	liOpcion=fiEntero("introduzca su opcion ")
	return liOpcion
	
liOpcion=9 
lsSeguir= "s"
Estudiante=clsEstudiante()
Profesor=clsProfesor()
while (liOpcion!=0):
	liOpcion=Menu()
	
	if liOpcion== 1:
		print ("Datos del estudiante ")
		NombreE= fsCadena("intruduzca el Nombre ")
		ApellidoE= fsCadena("introduzca el Apellido ")
		CedulaE= fiEntero("introduzca la Cedula ")
		NotaFinalE= fiEntero("introduzca su nota final ")
		CantM=fiEntero("Introduzca la cantidad de materias ")
		
		
		Estudiante.GetNombre(NombreE)
		Estudiante.GetApellido(ApellidoE)
		Estudiante.GetCedula(CedulaE)
		Estudiante.GetNotaFinal(NotaFinalE)
		
		Paga=CantM*50
		Estudiante.GetCantidadM(Paga)
		print ("el estudiante") , Estudiante.setNombre()
		print Estudiante.setApellido()
		print Estudiante.setCedula()
		print Estudiante.setNotaFinal() 
		print Estudiante.setCantidadM()
		fsContinuar()
	
	if liOpcion==2:
		print ("Datos del Profesor ")
		NombreP= fsCadena("intruduzca el Nombre ")
		ApellidoP= fsCadena("introduzca el Apellido ")
		CedulaP= fiEntero("introduzca la Cedula ")
		CategoriaP= fsCadena("introduzca categoria ")
		CantH= fiEntero("introduzca la cantidad de horas ")
		HorasA=CantH*100
		Profesor.GetNombre(NombreP)
		Profesor.GetApellido(ApellidoP)
		Profesor.GetCedula(CedulaP)
		Profesor.GetCategoria(CategoriaP)
		Profesor.GetHorasA(HorasA)
		print ("el profesor") , Profesor.setNombre(), Profesor.setApellido(), Profesor.setCedula(), Profesor.setCategoria(), Profesor.setHorasA()
		fsContinuar()
		
	if liOpcion==0:
		print ("adios")
	
#UPTP S2-T1