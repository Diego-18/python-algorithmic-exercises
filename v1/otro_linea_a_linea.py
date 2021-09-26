f = open('unfichero.txt', 'r')
for linea in f:
  print linea.rstrip()
f.close()
