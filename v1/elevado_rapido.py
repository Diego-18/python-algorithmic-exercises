a = 2
valor = 1
print 'elevado(%d, %d) = %d' % (a, 0, valor)
for n in range(1, 8):
  valor = a * valor
  print 'elevado(%d, %d) = %d' % (a, n, valor)
