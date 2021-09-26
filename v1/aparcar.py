dia = int(raw_input('Dime qué día es hoy: '))

if 0 < dia <= 15:
  print 'Puedes aparcar en el lado izquierdo de la calle'
else:
  if 15 < dia < 32:
    print 'Puedes aparcar en el lado derecho de la calle'
  else:
    print 'Ningún mes tiene %d días.' % dia
