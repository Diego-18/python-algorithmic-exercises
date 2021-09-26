#!usr/bin/env python
#*-*coding:latin-1*-*

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#inicio

def fsLeer(psTexto):
    lsvar=raw_input(psTexto)
    return lsvar


def fsInverso(psTexto): #funcion de la palabra al reves
    lsvarl=psTexto[::-1]
    return lsvarl
lsno=" cosas"
lsnombre=fsLeer("intruzuca una frase o una oracion: ")

print lsnombre.lower()# te presenta las cosas en minuscula
print lsnombre.upper()# te presenta el texto en mayuscula
print lsnombre.title()# de todo lo que ingreses lo pone tipo titulo
print lsnombre.capitalize()# coloca la primera en mayuscula
print lsnombre[0:5]# saca los caracteres por sectores

print len(lsnombre)# cuenta cuantos caracteres ingresaron
print lsnombre*3#multiplica y muestra lo ingresado tantas  veces como coloques
print lsnombre.find("a")# te indica en que sector esta lo que colocaste entre los parentisis y sino esta aparece -1
print lsnombre.count("a")# cuenta cuantas cosas iguales a lo colocado entre parenesis esten en la frase

print fsInverso(lsnombre)#con la funcion primero y entre parentesis la variable donde se guardo la frase coloca todo al reves
print lsnombre + ' a' + lsno # se crea una cadena nueva a partir de la original, y despues de la 'a' se puede agregar otra cosa y la une, siempre y cuando sea una variable y antes sea declarada

if 'la' in lsnombre: #esto sirve para buscar algo especifico en la variable, aqui busca "la" y luego muestra si esta o no
     print "¡Está!"
else:
    "no esta "

print lsnombre.replace('hola', 'mundo')# esto remplaza una palabra por otra, si se introduce hola en la variable el la cambia por mundo, sirve para letras o frases
print lsnombre.split()# separa todo y lo coloca con comillas y comas

lsvariable="/".join(lsnombre)# esto separa todoo con lo que esta entre las comillas,
print lsvariable

print lsnombre.strip()# elimina los espacios del principio y fin
print lsnombre.rstrip()#elimina los espacios de la derecha
print lsnombre.lstrip()#elimina los espacios de la izquierda

if (lsnombre.isalpha()):
    print "es alfabetica"
    
if (lsnombre.isalnum()):
    print "es alfanumerica"

if (lsnombre.isdigit()):
    print "es numerica"
    
#UPTP S1-T1