a = int(raw_input('Dame el primer número: '))
b = int(raw_input('Dame el segundo número: '))
c = int(raw_input('Dame el tercer número: '))

candidato = a
if b > candidato:
  candidato = b
if c > candidato:
  candidato = c
maximo = candidato

print 'El máximo es', maximo
