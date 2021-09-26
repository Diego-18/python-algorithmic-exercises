f = open('unfichero.txt', 'r')
while 1:
  linea = f.readline()
  if linea == '':
    break
  print linea.rstrip()
f.close()
