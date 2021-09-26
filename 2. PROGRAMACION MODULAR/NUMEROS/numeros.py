#!/usr/bin/env python
#-*- coding:UTF8 -*-

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#Algoritmo capaz de mostrar los numeros pares, primos, positivos, perfectos, enteros, de los numeros del 1 al 100

#Inicio

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
print "Los numero primos del 1 al 100 son:"
for liX in range (1,101):
        if(fbprimo(liX)==True):
                print liX
        
print "Los numero pares del 1 al 100 son:"
for liY in range (1,101):
        if(fbpar(liY)==True):
                print liY
        
print "Los numero perfectos del 1 al 100 son:"
for liZ in range (1,101):
        if(fbperfecto(liZ)==True):
                print liZ
        
print "Los numero enteros del 1 al 100 son:"
for liA in range (1,101):
        if(fbentero (liA)==True):
                print liA
#Fin

#UPTP S1-T1