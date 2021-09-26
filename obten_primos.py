n = raw_input('Introduce el valor máximo: ')

primos = []
for i in range(1, n+1):
  # Determinamos si $i$ es primo.
  creo_que_es_primo = True
  for divisor in range(2, n):
    if num % divisor == 0:
      creo_que_es_primo = False
      break
  # Y si es primo, lo añadimos a la lista.
  if creo_que_es_primo:
    primos.append(i)

print primos
