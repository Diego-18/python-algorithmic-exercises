n = int(raw_input('Dame un número: ')) 
m = int(raw_input('Dame otro número: '))

if n * m == 100:
  print 'El producto %d * %d es igual a 100' % (n, m)
if n * m != 100:
  print 'El producto %d * %d es distinto de 100' % (n, m)
