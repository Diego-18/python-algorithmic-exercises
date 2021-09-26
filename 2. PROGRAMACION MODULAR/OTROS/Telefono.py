#!/usr/bin/env python
#-*- coding:cp1252 -*-

#Telefonia
#v1.4 Elaborado por Diego Chavez


#Clases:

class ClsTelefono(object):
    Marca=""
    Modelo=""

    def __Init__(Self):
        Self.Marca=""
        Self.Modelo=""

    def GetMarca(Self,pmarca):
        Self.Marca=pmarca

    def GetModelo(Self,pmodelo):
        Self.Modelo=pmodelo

    def SetMarca(Self):
        return Self.Marca

    def SetModelo(Self):
        return Self.Modelo

class ClsMovistar(ClsTelefono):
    Encendido=""
    Apagado=""

    def __Init__(Self):
        Self.Encendido=""
        Self.Apagado=""

    def GetEncendido(Self,pencendido):
        Self.Encendido=pencendido

    def GetApagado(Self,papagado):
        Self.Apagado=papagado

    def Planes(Self):
        P=raw_input(" 1.Plan Rendidor(300bs) 2.Plan Hablador(500bs) 3.Plan Navegador(700bs) " )
        O=int(raw_input("Introduzca la Opcion: "))

        if (O==1):
            print "100s, 600MB, 200 SMS"
            print "1.Activar 2.Volver "
            o=int(raw_input("Introduzca la Opcion: "))
            if (o==1):
                print "Su renta basica sera de 300bs"
            if (o==2):
                return P

        if (O==2):
            print "300s, 600MB, 215 SMS"
            print "1.Activar 2.Volver "
            o=int(raw_input("Introduzca la Opcion: "))
            if (o==1):
                print "Su renta basica sera de 500bs"
            if (o==2):
                return P
            
        if (O==3):
            print "200s, 1GB, 300 SMS"
            print "1.Activar 2.Volver "
            o=int(raw_input("Introduzca la Opcion: "))
            if (o==1):
                print "Su renta basica sera de 700bs"
            if (o==2):
                return P

    def SetEncendido(Self):
        return Self.Encendido

    def SetApagado(Self):
        return Self.Apagado

class ClsMovilnet(ClsTelefono):
    Encendido=""
    Apagado=""

    def __Init__ (Self):
        Self.Encendido=""
        Self.Apagado=""

    def GetEncendido (Self,pencendido):
        Self.Encendido=pencendido

    def GetApagado (Self,papagado):
        Self.Apagado=papagado

    def Planes (Self):
        P=raw_input( " 1.Plan Rumbero(250bs) 2.Plan Interactivo(350bs) 3.Plan Ejecutivo(500bs) ")
        O=int(raw_input("Introduzca la Opcion: "))

        if (O==1):
            print "300s, 600MB, 300 SMS"
            print "1.Activar 2.Volver "
            o=int(raw_input("Introduzca la Opcion: "))
            if (o==1):
                print "Su renta basica sera de 250bs"
            if (o==2):
                return P

        if (O==2):
            print "400s, 700MB, 300 SMS"
            print "1.Activar 2.Volver "
            o=int(raw_input("Introduzca la Opcion: "))
            if (o==1):
                print "Su renta basica sera de 350bs"
            if (o==2):
                return P

        if (O==3):
            print "550s, 1GB, 450 SMS"
            print "1.Activar 2.Volver "
            o=int(raw_input("Introduzca la Opcion: "))
            if (o==1):
                print "Su renta basica sera de 500bs"
            if (o==2):
                return P

    def SetEncendido (Self):
        return Self.Encendido

    def  SetApagado (Self):
        return Self.Apagado

class ClsDigitel(ClsTelefono):
    Encendido=""
    Apagado=""

    def __Init__ (Self):
        Self.Encendido=""
        Self.Apagado=""

    def GetEncendido (Self,pencendido):
        Self.Encendido=pencendido

    def GetApagado (Self,papagado):
        Self.Apagado=papagado

    def Planes (Self):

        P=raw_input(" 1.Plan Contigo Siempre (350bs) 2.Plan Navega Full (600bs) 3.Plan Donde quiera que vallas (690bs) ")
        O=int(raw_input("Introduzca la Opcion: "))

        if (O==1):
            print "400s(150O/Op, 100Loc., 150Digit.), 500MB, 200 SMS"
            print "1.Activar 2.Volver "
            o=int(raw_input("Introduzca la Opcion: "))
            if (o==1):
                print "Su renta basica sera de 350bs"
            if (o==2):
                return P

        if (O==2):
            print "500s(200O/Op, 100Loc, 200Digit.), 800MB, 400 SMS"
            print "1.Activar 2.Volver "
            o=int(raw_input("Introduzca la Opcion: "))
            if (o==1):
                print "Su renta basica sera de 600bs"
            if (o==2):
                return P

        if (O==3):
            print "600s(250O/Op, 100Loc., 250Digit.), 1GB, 550 SMS"
            print "1.Activar 2.Volver "
            o=int(raw_input("Introduzca la Opcion: "))
            if (o==1):
                print "Su renta basica sera de 690bs"
            if (o==2):
                return P

    def SetEncendido(Self):
        return Self.Encendido

    def SetApagado(Self):
        return Self.Apagado

#Aplicacion:

Seguir="S"
Movistar=ClsMovistar()
Movilnet=ClsMovilnet()
Digitel=ClsDigitel()
Opc=9

print ("1.Movistar, 2.Movilnet, 3.Digitel")
Opc=int(raw_input("Elija su Operador: "))

while (Seguir=="S") or (Seguir=="s"):
    if (Opc==1):
        MarcM=raw_input("Introduzca la Marca del Telefono: ")
        ModM=raw_input("Introduzca el Modelo del Telefono: ")
        InicM=raw_input("Movistar")
        ApagM=raw_input("Gracias por elegir nuestros servicios")
        Movistar.GetMarca(MarcM)
        Movistar.GetModelo(ModM)
        Movistar.GetEncendido(InicM)
        Movistar.GetApagado(ApagM)
        print Movistar.SetMarca(),Movistar.SetModelo(),Movistar.SetEncendido(), Movistar.Planes(),
        Movistar.SetApagado()
  
    if (Opc==2):
        MarcMovil=raw_input("Introduzca la Marca del Telefono: ")
        ModMovil=raw_input("Introduzca el Modelo del Telefono: ")
        InicMovil=raw_input("Movilnet, Contigo Siempre")
        ApagMovil=raw_input("Gracias por elegir nuestros servicios")
        Movilnet.GetMarca(MarcMovil)
        Movilnet.GetModelo(ModMovil)
        Movilnet.GetEncendido(InicMovil)
        Movilnet.GetApagado(ApagMovil)
        print Movilnet.SetMarca(),Movilnet.SetModelo(),Movilnet.SetEncendido(), Movilnet.Planes(), 
        Movilnet.SetApagado()

    if (Opc==3):
        MarcDig=raw_input("Introduzca la Marca del Telefono: ")
        ModDig=raw_input("Introduzca el Modelo del Telefono: ")
        InicDig=raw_input("DIGITEL")
        ApagDig=raw_input("Gracias por elegir nuestros red")
        Digitel.GetMarca(MarcDig)
        Digitel.GetModelo(ModDig)
        Digitel.GetEncendido(InicDig)
        Digitel.GetApagado(ApagDig)
        print Digitel.SetMarca(),Digitel.SetModelo(),Digitel.SetEncendido(), Digitel.Planes(),
        Digitel.SetApagado()

    Seguir=raw_input("Desea continuar? (S/N) ")
