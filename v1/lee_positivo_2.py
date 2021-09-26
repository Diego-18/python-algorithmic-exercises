def lee_entero_positivo():
  numero = int(raw_input())
  while numero < 0:
    numero = int(raw_input())
  return numero

a = lee_entero_positivo()
