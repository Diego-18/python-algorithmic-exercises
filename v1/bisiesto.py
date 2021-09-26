anyo = int(raw_input('Dame un año: '))

if anyo % 4 == 0  and  (anyo % 100 != 0  or  anyo % 400 == 0):
  print 'El año %d es bisiesto.' % anyo
else:
  print 'El año %d no es bisiesto.' % anyo
