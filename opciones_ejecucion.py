from sys import argv

nombre = argv[1]
numero = int(argv[2])

f = open(nombre, 'r')
n = 0
for linea in f:
  n += 1
  print linea.rstrip()
  if n == numero:
    break
f.close()
