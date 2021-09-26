#! usr/bin/env python
# -*- coding: UTF8 -*-

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#Funciones
def fsLeerS (psTexto):		#Funcion para Texto
	lsVar=raw_input(psTexto)
	return lsVar
	
def fsInverso (psTexto):  #voltea la cadena
	lsVar=psTexto[::-1]
	return lsVar

def fbPalindrome (psTexto):
	psTexto=psTexto.lower() #convierte el valor a minuscula para que no de error si hay mayuscula
	lsInverso=fsInverso(psTexto)
	if (psTexto==lsInverso):
		return True
	else:
		return False


lsNombre=" algo en comun"
lsCadena=fsLeerS("Introduzca la cadena: ")

print lsCadena.lower() #Minuscula
print lsCadena.upper() #MAYUSCULA
print lsCadena.title() # Titulo
print lsCadena.capitalize() #Inicial en mayuscula
print lsCadena [0:2] #imprime un rango del pimer caracter al 2do, estos valores cambian
print len(lsCadena) #cuenta la cantidad de caracteres incluyendo los espacios
print lsCadena*3 #muestra lo introducido 3 veces en la misma linea
print lsCadena.strip() #elimina espacios al inicio y final de la cadena
print lsCadena.rstrip()#elimina espacios al lado derecho de la cadena
print lsCadena.lstrip()#elimina espacios al lado izquierdo de la cadena

print lsCadena.count ("a") #cuenta las A en toda la cadena
print lsCadena.replace("A","O") #reemplaza la antes de la coma por la despues de la coma
print lsCadena.find("a")# te indica en que sector esta lo que colocaste entre los parentisis y sino esta aparece -1


"""se crea una cadena nueva a partir de la original, agrega la 'a'
y despues de esta agregar otra cosa y la une, siempre y cuando
sea una variable y antes sea declarada, en este caso lsNombre que
vale " algo en comun" """
print lsCadena + ' a' + lsNombre 


print fsInverso(lsCadena)


""".find Cuenta la ubicacion donde se encuentra la A y el
-1 por si no existe no de error"""
if (lsCadena.find ("a"))==-1: 
	print "No existe a en la cadena"
else:
	lsCadena.find ("a")


if (fbPalindrome(lsCadena))==True:
        print "Es palindrome"
else:
        print "No es palindrome"

#Determina si lo introducido es alfabetico, alfanumerico o numerico
if (lsCadena.isalpha()):
	print "alfabetico"

if (lsCadena.isalnum()):
	print "alfanumerico"
	
if (lsCadena.isdigit()):
	print "numerico"


#convierte la cadena en una lista donde hay espacios 
lsLista=lsCadena.split(" ") 
print lsLista


#muestra la lista separada por " / "
lsCadena2=" / ".join(lsLista)
print lsCadena2


#esto sirve para buscar algo especifico en la variable,
#aqui busca "la" y luego muestra si esta o no
if 'la' in lsCadena:
     print "¡Está!"
else:
    "no esta "

#UPTP S1-T1