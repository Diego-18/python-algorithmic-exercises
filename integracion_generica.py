def cuadrado(x):
  return x**2

def cubo(x):
  return x**3

def integral_definida(f, a, b, n):
  if n == 0:
    sumatorio = 0
  else:
    deltax = (b-a) / float(n)
    sumatorio = 0
    for i in range(n):
      sumatorio += deltax * f(a + i * deltax)
  return sumatorio

a = 1
b = 2
print 'Integración entre %f y %f' % (a, b)
print 'Integral de x**2:', integral_definida(cuadrado, a, b, 100)
print 'Integral de x**3:', integral_definida(cubo, a, b, 100)
