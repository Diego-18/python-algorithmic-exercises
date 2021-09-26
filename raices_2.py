numero = float(raw_input('Dame un número: '))

for n in range(2, 101):
  print 'la raíz %d-ésima de %f es %f' % (numero, n, numero**(1.0/n)) 
