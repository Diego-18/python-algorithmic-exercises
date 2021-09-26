car = raw_input('Dame un carácter: ')

if 'a' <= car.lower() <= 'z'  or  car == '_':
  print 'Este carácter es válido en un identificador en Python.'
else:
  if not (car < '0'  or  '9' < car):
    print 'Un dígito es válido en un identificador en Python,',
    print 'siempre que no sea el primer carácter.'
  else:
    print 'Carácter no válido para formar un identificador en Python.'
