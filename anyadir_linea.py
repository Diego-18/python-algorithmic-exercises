nombre_fichero = raw_input('Fichero:')
nueva_linea = raw_input('Línea:')
nombre_copia = nombre_fichero + '.copia'

# Hacemos una copia
f1 = open(nombre_fichero,'r')
f2 = open(nombre_copia, 'w')
for linea in f1:
  f2.write(linea)
f2.close()
f1.close()

# y rehacemos el original añadiendo la nueva línea.
f1 = open(nombre_copia,'r')
f2 = open(nombre_fichero, 'w')
for linea in f1:
  f2.write(linea)
f2.write(nueva_linea + '\n')
f2.close()
f1.close()
