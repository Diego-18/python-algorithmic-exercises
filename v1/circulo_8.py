from math import pi

radio = float(raw_input('Dame el radio de un c?rculo: '))

opcion = ''
while opcion != 'd':
  print 'Escoge una opci?n: '
  print 'a) Calcular el di?metro.'
  print 'b) Calcular el per?metro.'
  print 'c) Calcular el ?rea.'
  print 'd) Finalizar.'
  opcion = raw_input('Teclea a, b o c y pulsa el retorno de carro: ')
  if opcion == 'a':
    diametro = 2 * radio
    print 'El di?metro es', diametro
  elif opcion == 'b':
    perimetro = 2 * pi * radio
    print 'El per?metro es', perimetro
  elif opcion == 'c':
    area = pi * radio ** 2
    print 'El ?rea es', area
  elif opcion != 'd':
    print 'S?lo hay cuatro opciones: a, b, c o d. T? has tecleado', opcion

print 'Gracias por usar el programa'
