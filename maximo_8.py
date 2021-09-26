def maximo(lista):
  candidato = lista[0]
  for elemento in lista:
    if elemento > candidato:
      candidato = elemento
  return candidato  
