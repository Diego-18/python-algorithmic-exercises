nombre_entrada = raw_input('Nombre del fichero de entrada: ')
nombre_salida = raw_input('Nombre del fichero de salida: ')
f_entrada = open(nombre_entrada, 'r')
f_salida = open(nombre_salida, 'w')
while 1:
  caracter = f_entrada.read(1)
  if caracter == '':
    break
  elif caracter >= 'a' and caracter <='y':
    f_salida.write(chr(ord(caracter) + 1))
  elif caracter == 'z':
    f_salida.write('a')
  else:
    f_salida.write(caracter)
f_entrada.close()
f_salida.close()
