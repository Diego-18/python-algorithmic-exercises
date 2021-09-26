def buscar_entrada(nombre, apellido):
  f = open('agenda.txt', 'r')
  while 1:
    linea1 = f.readline()
    linea2 = f.readline()
    linea3 = f.readline()
    if linea1 == '':
      break
    if nombre == linea1[:-1] and apellido == linea2[:-1]:
      f.close()
      return linea3[:-1]
  f.close()
  return ''

def anyadir_entrada(nombre, apellido, telefono):
  f = open('agenda.txt', 'a')
  f.write(nombre + '\n')
  f.write(apellido + '\n')
  f.write(telefono + '\n')
  f.close()

def borrar_entrada(nombre, apellido):
  f = open('agenda.txt', 'r')
  fcopia = open('agenda.txt.copia', 'w')
  while 1:
    linea1 = f.readline()
    linea2 = f.readline()
    linea3 = f.readline()
    if linea1 == '':
      break
    if nombre != linea1[:-1] or apellido != linea2[:-1]:
      fcopia.write(linea1)
      fcopia.write(linea2)
      fcopia.write(linea3)
  f.close()
  fcopia.close()

  fcopia = open('agenda.txt.copia', 'r')
  f = open('agenda.txt', 'w')
  for linea in fcopia:
    f.write(linea)
  fcopia.close()
  f.close()
