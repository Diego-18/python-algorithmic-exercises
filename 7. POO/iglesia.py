#!usr/bin/env python
#-*- coding: utf:8-*-

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#inicio
import os
class clsPersona(object):
    __Nombre=''
    __Apellido=''
    __Edad=''
	
    def __init__(self):
        self.__Nombre=''
        self.__Apellido=''
        self.__Edad=''
		
    def GetNombre(self,pnombre):
        self.__Nombre=pnombre
		
    def GetApellido(self,pApellido):
        self.__Apellido =pApellido
		
    def GetEdad(self,pEdad):
        self.__Edad=pEdad
		
    def SetNombre(self):
        return self.__Nombre
		
    def SetApellido(self):
        return self.__Apellido
	
    def SetEdad(self):
        return self.__Edad

class clsPadre(clsPersona): #en parentesis tenias persona y la clase se llama clsPersona
    __AnosE=''
    __HoraP=''
	
    def __init__(self):
        self.__AnosE=''
        self.__HoraM=''
		
    def GetAnosE(self,pAnosE):
        self.__AnosE=pAnosE

    def SetAnosE(self):
        return self.__AnosE
			
    def GetHorasP(self,pHorasP):
        self.__HorasP=pHorasP

    def SetHorasP(self):
        return self.__HorasP
		
		
class clsMonaguillo(clsPersona): #en parentesis tenias persona y la clase se llama clsPersona
    __HorasA=''
	
    def GetHorasA(self,pHorasA):
        self.__HorasA=pHorasA
		
    def SetHorasA(self):
        return self.__HorasA

def fsCadena(psTexto):
    lsVar=raw_input(psTexto)
    return lsVar
	
def fiEntero (psTexto):
    liVar= int (raw_input(psTexto))
    return liVar
	
def fsContinuar():
    return fsCadena("pulse enter para continuar")
	
def Menu():
    os.system ("clear")
    print "1. Padre"
    print "2. Monaguillo"
    print "0. Salir"
    liOpcion=fiEntero ("itroduzca su opcion")
    return liOpcion
	
liOpcion=9
lsSeguir= "s"
Padre=clsPadre()  #faltaban parentesis
Monaguillo=clsMonaguillo()  #y aqui

while (liOpcion!=0):
    liOpcion=Menu()
	
    if (liOpcion==1):
        print("introduzca los datos del padre ")
        NombreP=fsCadena("Intrpduzca el nombre ")
        ApellidoP=fsCadena("introduzca el apellido ")
        EdadP=fiEntero("introduzca su Edad ")
        AnosE=fiEntero ("introduzca los años de servicio ")
        HorasP=fiEntero("introduzca las horas que trabaja")
        if AnosE>=20:
            print ("Jubilado")
        else:
            print ("Aun le quedan años de servicio")
        HorasT=HorasM*100

        Padre.GetNombreP(NombreP)
        Padre.GetApellidoP(ApellidoP)
        Padre.GetEdadP(EdadP)
        Padre.GetAnosE(AnosE)
        Padre.GetHorasP(HorasP)

        print ("el padre") , Padre.SetNombreP(), Padre.SetApellidoP(), Padre.SetEdadP(), Padre.SetAnosE(), Padre.SetHorasP()
	
	
    if liOpcion==2:
        print ("introduzca los datos del monaguillo")
        NombreM=fsCadena("Intrpduzca el nombre ")
        ApellidoM=fsCadena("introduzca el apellido ")
        EdadM=fiEntero("introduzca su Edad ")
        HorasA=fiEntero("Horas de servicio ")

        Monaguillo.GetNombreM(NombreM)
        Monaguillo.GetApellidoM(ApellidoM)
        Monaguillo.GetEdadM(EdadM)
        Monaguillo.GetHorasA(HorasA)

        print ("el monaguillo") , Monaguillo.SetNombreM(), Monaguillo.SetApellido(), Monaguillo.SetEdadP(), Monaguillo.SetHorasA()

    if liOpcion==0:
        print ("Adios")
        
#UPTP S2-T1