#!/usr/bin/env python
#-*- coding: cp1252 -*-

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#Clases:

class ClsTelefono(object):
     Marca=""
     Modelo=""

     def __Init__(Self):
          Self.Marca=""
          Self.Modelo=""

     def GetMarca(Self,pmarca):
          Self.Marca=pmarca

     def SetMarca(Self):
          return Self.Marca

     def GetModelo(Self,pmodelo):
          Self.Modelo=pmodelo

     def SetModelo(Self):
          return Self.Modelo

class ClsMovistar(ClsTelefono):
     Encendido1=""
     Apagado1=""

     def __Init__(Self):
         Self.Encendido1=""
         Self.Apagado1=""

     def GetEncendido(Self,pencendido):
          Self.Encendido1=pencendido

     def SetEncendido(Self):
          return Self.Encendido1

     def GetApagado(Self,papagado):
          Self.Apagado1=papagado

     def SetApagado(Self):
          return Self.Apagado1

class ClsMovilnet(ClsTelefono):
     Encendido2=""
     Apagado2=""

     def __Init__ (Self):
          Self.Encendido2=""
          Self.Apagado2=""

     def GetEncendido (Self,pencendido):
          Self.Encendido2=pencendido

     def SetEncendido (Self):
          return Self.Encendido2
    
     def GetApagado (Self,papagado):
          Self.Apagado2=papagado

     def SetApagado (Self):
          return Self.Apagado2

class ClsDigitel(ClsTelefono):
     Encendido3=""
     Apagado3=""

     def __Init__ (Self):
          Self.Encendido3=""
          Self.Apagado3=""

     def GetEncendido (Self,pencendido):
          Self.Encendido3=pencendido

     def SetEncendido(Self):
          return Self.Encendido3

     def GetApagado (Self,papagado):
          Self.Apagado3=papagado

     def SetApagado(Self):
          return Self.Apagado3

#Aplicacion:
    
Seguir="s"
Operador1=ClsMovistar()
Operador2=ClsMovilnet()
Operador3=ClsDigitel()
O=0

print ("1.Movistar, 2.Movilnet, 3.Digitel")
O=int(raw_input("Elija su Operador: "))

if (O==1):
    print ("Movistar")
    MarcM=raw_input("Introduzca la Marca del Telefono: ")
    ModM=raw_input("Introduzca el Modelo del Telefono")
    InicM=raw_input("Movistar")
    ApagM=raw_input("Gracias por elegir nuestros servicios")
    Operador1.GetMarca (MarcM)
    Operador1.GetModelo (ModM)
    Operador1.GetEncendido (InicM)
    Operador1.GetApagado (ApagM)
    print Operador1.SetMarca(), Operador1.SetModelo(), Operador1.SetEncendido(), Operador1.SetApagado()

if (O==2):
    print ("Movilnet")
    MarcMovil=raw_input("Introduzca la Marca del Telefono: ")
    ModMovil=raw_input("Introduzca el Modelo del Telefono")
    InicMovil=raw_input("Movilnet, Contigo Siempre")
    ApagMovil=raw_input("Gracias por elegir nuestros servicios")
    Operador2.GetMarca (MarcMovil)
    Operador2.GetModelo (ModMovil)
    Operador2.GetEncendido (InicMovil)
    Operador2.GetApagado (ApagMovil)
    print Operador2.SetMarca(),Operador2.SetModelo(),Operador2.SetEncendido(),Operador2.SetApagado()

if (O==3):
    print ("Digitel")
    MarcDig=raw_input("Introduzca la Marca del Telefono: ")
    ModDig=raw_input("Introduzca el Modelo del Telefono")
    InicDig=raw_input("DIGITEL")
    ApagDig=raw_input("Gracias por elegir nuestros red")
    Operador3.GetMarca (MarcDig)
    Operador3.GetModelo (ModDig)
    Operador3.GetEncendido (InicDig)
    Operador3.GetApagado (ApagDig)
    print Operador3.SetMarca(),Operador3.SetModelo(),Operador3.SetEncendido(),Operador3.SetApagado()

#UPTP S2-T1