a = float(raw_input('Inicio del intervalo: '))
b = float(raw_input('Final del intervalo: '))
n = int(raw_input('Número de rectángulos: '))

if n == 0:
  sumatorio = 0
else:
  deltax = (b-a) / float(n)
  sumatorio = 0
  for i in range(n):
    sumatorio += deltax * (a + i * deltax) ** 2

print 'La integral de x**2 entre %f y %f es (aprox) %f' % (a, b, sumatorio)
