#!/usr/bin/env python
#-*- coding:UTF8 -*-

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#Algoritmo capaz de verificar si un numero es par, primo, positivo, perfecto, entero

#Inicio

def fileerI (psnumero):
        liVarI=int(raw_input(psnumero))
        return liVarI

def fbprimo (pinumero):
        licont=0
        for liN in range (1,pinumero+1):
                if (pinumero%liN==0):
                        licont=licont+1
        if (licont==2):
                return True
        return False

def fbpar (pinumero):
        if (pinumero%2==0):
                return True
        return False

def fbpositivo (pinumero):
        if (pinumero>0):
                return True
        return False

def fbperfecto (pinumero):
        liacum=0
        for liN in range (1,pinumero):
                if (pinumero%2==0):
                        liacum=liacum+liN
                if (liacum==pinumero):
                        return True
        return False

def fbentero (pinumero):
        if (pinumero%1==0):
                return True
        return False

#Programa
lsseguir="s"

while lsseguir=="S" or lsseguir=="s":
        linumero=fileerI("Introduzca el numero: ")
        if (fbprimo(linumero)==True):
                print "El numero es primo"
        elif (fbprimo(linumero)==False):
                print "El numero no es primo"

        if (fbpar(linumero)==True):
                print "El numero es par"
        elif (fbpar(linumero)==False):
                print "El numero no es par"

        if (fbpositivo(linumero)==True):
                print "El numero es positivo"
        elif (fbpositivo(linumero)==False):
                print "El numero es negativo"

        if (fbperfecto(linumero)==True):
                print "El numero es perfecto"
        elif (fbperfecto(linumero)==False):
                print "El numero no es perfecto"
                
        if (fbentero(linumero)==True):
                print "El numero es entero"
        elif (fbentero(linumero)==False):
                print "El numero no es entero"
        lsseguir=raw_input("Desea Seguir?: (S/N) ")
#Fin
        
#UPTP S1-T1