from math import pi

radio = float(raw_input('Dame el radio de un círculo: '))

opcion = ''
while opcion != 'd':
  print 'Escoge una opción: '
  print 'a) Calcular el diámetro.'
  print 'b) Calcular el perímetro.'
  print 'c) Calcular el área.'
  print 'd) Finalizar.'
  opcion = raw_input('Teclea a, b o c y pulsa el retorno de carro: ')
  if opcion == 'a':
    diametro = 2 * radio
    print 'El diámetro es', diametro
  elif opcion == 'b':
    perimetro = 2 * pi * radio
    print 'El perímetro es', perimetro
  elif opcion == 'c':
    area = pi * radio ** 2
    print 'El área es', area
  elif opcion != 'd':
    print 'Sólo hay cuatro opciones: a, b, c o d. Tú has tecleado', opcion

print 'Gracias por usar el programa'
