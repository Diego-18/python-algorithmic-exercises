a = float(raw_input('Valor de a: '))
b = float(raw_input('Valor de b: '))

try:
  x = -b/a
  print 'Solución: ', x
except:
  if b != 0:
    print 'La ecuación no tiene solución.'   
  else:
    print 'La ecuación tiene infinitas soluciones.' 
