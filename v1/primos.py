limite = int(raw_input('Dame un número: '))

for num in range(1, limite+1):
  creo_que_es_primo = True
  for divisor in range(2, num):
    if num % divisor == 0:
      creo_que_es_primo = False
      break
  if creo_que_es_primo:
    print num
