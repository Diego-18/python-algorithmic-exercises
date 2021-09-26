cadena = raw_input('Escribe una frase: ')
while cadena != '':
  cambios = 0
  anterior = ' '
  for caracter in cadena:
    if caracter == ' ' and anterior != ' ':
      cambios += 1
    anterior = caracter

  if cadena[-1] == ' ':
    cambios = cambios - 1

  palabras = cambios + 1
  print 'Palabras:', palabras

  cadena = raw_input('Escribe una frase: ')
