#usr/bin/env python
#-*- coding: utf8-*-

import os

class clsPersona(object):
	__asNombre= ""
	__asApellido=""
	__aiCedula=""
	def __init__(self):
		self.__asNombre=""
		self.__asApellido=""
		self.__aiCedula=""

	def GetNombre (self,psNombre):
		self.__asNombre=psNombre
	def setNombre(self):
		return self.__asNombre
		
	def GetApellido(self,psApellido):
		self.__asApellido=psApellido
	def setApellido(self):
		return self.__asApellido	
		
	def GetCedula(self,piCedula):
		self.__aiCedula=piCedula
	def setCedula(self):
		return self.__aiCedula

class clsArtista(clsPersona):
	__asGenero=""
	__asDiscografia=""
	__afPaga=""
	__afSueldo=""
	def __init__(self):
		self.__asGenero=""
		self.__asDiscografia=""
		self.__afPaga=0
		self.__afSueldo=0

	def GetPaga(self, pfPaga):
		self.__afPaga=pfPaga
	def setPaga(self):
		return self.__afPaga
	
	def GetSueldo(self, pfSueldo):
		self.__afSueldo=pfSueldo
	def setSueldo(self):
		return self.__afSueldo
		
	def GetGenero(self, psGenero):
		self.__asGenero=psGenero
	def setGenero(self):
		return self.__lsGenero

	def GetDiscografia(self, psDiscografia):
		self.__asDiscografia=psDiscografia
	def setDiscografia (self):
		return self.__asDiscografia

class clsProductor(clsPersona):
	__afGanancia=""
	__afHonorario=""
	
	def __init__(self):
		self.__afGanancia=0
		self.__afHonorario=0
		
	def GetGanancia(self,pfGanancia):
		self.__afGanancia=pfGanancia
	def setGanancia(self):
		return self.__afGanancia

	def GetHonorario(self,pfHonorario):
		self.__afHonorario=pfHonorario
	def setHonorario(self):
		return self.__afHonorario

def fsCadena (psTexto):
	lsVar= raw_input(psTexto)
	return lsVar

def fiEntero (psTexto):
	liVar= int (raw_input(psTexto))
	return liVar

def ffFlotante(psTexto):
	lfVar= float (raw_input(psTexto))
	return lfVar

def fsContinuar():
	return fsCadena ("pulse una tecla para continuar ")

def fiMenu():
	os.system ("clear")
	print "1. Productor"
	print "2. Artista"
	print "0. Salir"
	liOpcion=fiEntero("introduzca su opcion ")
	return liOpcion

liOpcion=9 
lcProductor=clsProductor()
lcArtista=clsArtista()
while (liOpcion!=0):
	liOpcion=Menu()
	
	if liOpcion== 1: #productor
		print ("Datos del Artista ")
		NombreA= fsCadena("intruduzca el Nombre ")
		ApellidoA= fsCadena("introduzca el Apellido ")
		CedulaA= fiEntero("introduzca la Cedula ")

		lcProductor.GetNombre(NombreE)
		lcProductor.GetApellido(ApellidoE)
		lcProductor.GetCedula(CedulaE)
		lcProductor.GetNotaFinal(NotaFinalE)
		
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
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
