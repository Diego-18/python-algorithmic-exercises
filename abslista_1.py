def abs_lista(lista):
  for i in range(len(lista)):
    lista[i] = abs(lista[i])

milista = [1, -1, 2, -3, -2, 0]
abs_lista(milista)
print milista    
