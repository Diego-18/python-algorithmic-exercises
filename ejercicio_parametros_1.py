def modifica(a, b):
  for elemento in b:
    a.append(elemento)
  b = b + [4]
  a[-1] = 100
  del b[0]
  return b[:]

lista1 = [1, 2, 3]
lista2 = [1, 2, 3]

lista3 = modifica(lista1, lista2)

print lista1
print lista2
print lista3      
