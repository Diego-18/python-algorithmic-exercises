def es_perfecto(n): # Averigua si el número $n$ es o no es perfecto.
  sumatorio = 0
  for i in range(1, n):
    if n % i == 0:
      sumatorio += i
  return sumatorio == n

def tabla_perfectos(m): # Muestra todos los números perfectos entre 1 y $m$.
  for i in range(1, m+1):
    if es_perfecto(i):
      print i, 'es un número perfecto'

numero = int(raw_input('Dame un número: '))
tabla_perfectos(numero)
