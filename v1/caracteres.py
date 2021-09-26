nombre = raw_input('Nombre del fichero: ')
fichero = open(nombre, 'r')

contador = 0
while 1:
  caracter = fichero.read(1)
  if caracter == '':
    break
  contador += 1 

fichero.close()
print contador
