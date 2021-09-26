from random import random

def crea_matriz(filas, columnas):
  matriz = []
  for i in range(filas):
    matriz.append([None] * columnas)
  return matriz

def dimension(matriz):
  return [len(matriz), len(matriz[0])]

def rellena_simbolos(simbolo):
  filas = len(simbolo)
  columnas = len(simbolo[0])
  numsimbolo = 0.0
  for i in range(filas):
    for j in range(columnas):
      simbolo[i][j] = chr(ord('a')+int(numsimbolo))
      numsimbolo += 0.5
  for i in range(1000):
    [f1, c1] = [int(filas * random()), int(columnas * random())]
    [f2, c2] = [int(filas * random()), int(columnas * random())]
    tmp = simbolo[f1][c1] 
    simbolo[f1][c1] = simbolo[f2][c2]
    simbolo[f2][c2] = tmp

def dibuja_simbolos(simbolo):
  filas = len(simbolo)
  columnas = len(simbolo[0])  
  for i in range(filas):
    for j in range(columnas):
      create_text(j+.5, i+.5, simbolo[i][j], 18)

# Programa principal
filas = 4
columnas = 6
window_coordinates(0,0,columnas,filas)
window_size(columnas*40, filas*40)

simbolo = crea_matriz(filas, columnas)
baldosa = crea_matriz(filas, columnas)
rellena_simbolos(simbolo)
dibuja_simbolos(simbolo)
