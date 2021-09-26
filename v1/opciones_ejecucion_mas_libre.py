from sys import argv, exit

numero = 10
nombre = ''
i = 1
while i < len(argv):
  if argv[i] == '-n':
    i += 1
    if i < len(argv):
      numero = int(argv[i])
    else:
      print 'Error: en la opción -n no indica valor numérico.'
      exit(0) # La función \emph{exit} finaliza en el acto la ejecución del programa.
  else:
    if nombre == '':
      nombre = argv[i]
    else:
      print 'Error: hay más de un nombre de fichero.'
      exit(0) 
  i += 1

f = open(nombre, 'r')
n = 0
for linea in f:
  n += 1
  print linea.rstrip()
  if n == numero:
    break
f.close()
