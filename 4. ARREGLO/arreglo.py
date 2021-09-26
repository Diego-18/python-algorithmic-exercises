#!/usr/bin/env python
#-*- coding: UTF8 -*-

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

 #Arreglo es una variable que guarda un valor en una posicion predefinida.
"""
#Tupla: son arreglos pero que no se pueden modificar.
laArregloT=(15, "Jose", "Mata", 18)
print laArregloT[0],+ laArregloT[3] #[posicion que se desea mostrar]
"""


#Lista: Son los arreglos que si permite modificar los valores de las diferentes posiciones, se puede agregar, y se puede eliminar elementos.
laArregloL=[12,14,16,18]
print laArregloL[0]

laArregloL[0]=20 #Modifica el valor de alguna posición por el valor deseado
print laArregloL

laArregloL.append(22) #Agrega algún elemento a la lista
print laArregloL

del(laArregloL[2]) #Elimina alguna posición o elemento de la lista
print laArregloL

laArregloL.insert(2,30) #Inserta o modifica el valor de una posición por otro valor deseado

"""
#Diccionario: Este arreglo es igual a la lista, sólo que, en vez de manejar
#los valores por posición, los maneja por un índice, se puede eliminar
#elementos pero no se puede agregar elementos


laArregloD={'azul':"01", 'verde':"02", 'amarillo':"03"}
print laArregloD['azul']
laArregloD['azul']="30"  #Modifica el valor de alguna posición.
print laArregloD
del(laArregloD['amarillo'])
print laArregloD
"""
#UPTP S1-T1