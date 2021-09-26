from record import record

class Estudiante(record):
  nombre     = ''
  grupo    = ''
  nota     = 0.0
  practica  = False

# Funciones

def existe_estudiante(lista, nombre):
  # Averigua si hay un estudiante en \emph{lista} con \emph{estudiante.nombre} igual a \emph{nombre}.
  for estudiante in lista:
    if nombre == estudiante.nombre:
      return True
  return False

def crea_estudiante_por_teclado():
  # Lee los datos de un estudiante por teclado y crea y devuelve un registro de tipo \emph{Estudiante}.
  nombre = raw_input('Nombre: ')
  grupo = raw_input('Grupo (A, B o C): ')
  while grupo not in ['A', 'B', 'C']:
    grupo = raw_input('Grupo (A, B o C): ')
  nota = float(raw_input('Nota de examen: '))
  while nota < 0 or nota > 10:
    nota = float(raw_input('Nota de examen: '))
  entregada = raw_input('Práctica entregada (s/n): ')
  while entregada.lower() not in ['s', 'n']:
    entregada = raw_input('Práctica entregada (s/n): ')
  practica  = entregada.lower() == 's'
  return Estudiante(nombre=nombre, grupo=grupo, nota=nota, practica=practica)

def anyade_estudiante(lista, estudiante):
  # Recibe una lista de estudiantes y un estudiante y, si no estaba ya, lo añade a la lista.
  # Devuelve \emph{True} si hay éxito y \emph{False} en caso contrario.
  if not existe_estudiante(lista, estudiante.nombre):
    lista.append(estudiante)
    return True
  else:
    return False

def modifica_estudiante(lista, estudiante):
  # Recibe una lista de estudiantes y un estudiante y, si ya estaba, sustituye sus datos
  # viejos por los nuevos.
  # Devuelve \emph{True} si hay éxito y \emph{False} en caso contrario.
  for i in range(len(lista)):
    if lista[i].nombre == estudiante.nombre:
      lista[i] = estudiante
      return True
  return False

def elimina_estudiante(lista, nombre):
  # Recibe una lista de estudiantes y el nombre de uno. Si está en la lista, lo elimina.
  # Devuelve \emph{True} si hay éxito y \emph{False} en caso contrario.
  for i in range(len(lista)):
    if lista[i].nombre == nombre:
      del lista[i]
      return True
  return False

def muestra_estudiante(estudiante):
  # Muestra todos los campos de un registro de tipo \emph{Estudiante}
  print 'Nombre:      %s' % estudiante.nombre
  print 'Grupo:       %s' % estudiante.grupo
  print 'Nota examen: %3.1f' % estudiante.nota
  if estudiante.practica:
    print 'Memoria de prácticas entregada'
  else:
    print 'Memoria de prácticas no entregada'

def busca_y_muestra_estudiante(lista, nombre):
  # Muestra la ficha del estudiante llamado \emph{nombre} en \emph{lista}.
  # No devuelve nada. Si no encuentra al estudiante, da un aviso en pantalla.
  for estudiante in lista:
    if estudiante.nombre == nombre:
      muestra_estudiante(estudiante)
      return
  print 'No existe ese estudiante'

def listado_completo(lista):
  # Muestra la ficha completa de todos los estudiantes de la lista suministrada.
  for estudiante in lista:
    muestra_estudiante(estudiante)

def listado_de_nombres(lista):
  # Muestra el nombre de todos los estudiantes de la lista suministrada.
  for estudiante in lista:
    print estudiante.nombre

def menu():
  print '-' * 79
  opcion = 0
  while opcion < 1 or opcion > 7:
    print ' 1) Dar de alta un nuevo estudiante.'
    print ' 2) Modificar los datos de un estudiante.'
    print ' 3) Dar de baja un estudiante.'
    print ' 4) Mostrar ficha de un estudiante.'
    print ' 5) Mostrar listado completo.'
    print ' 6) Mostrar listado de nombres.'
    print ' 7) Salir.'
    opcion = int(raw_input('Escoge opción: '))
  return opcion

# Programa principal

estudiantes = [] # Inicialmente la lista de estudiantes está vacía

opcion = 0
while opcion != 7:
  opcion = menu()
  if opcion == 1: # Dar de alta a un estudiante.
    estudiante = crea_estudiante_por_teclado()
    if anyade_estudiante(estudiantes, estudiante):
      print 'Estudiante %s dado de alta.' % estudiante.nombre
    else:
      print 'El estudiante %s ya había sido dado de alta.' % estudiante.nombre
  elif opcion == 2: # Modificar estudiante.
    estudiante = crea_estudiante_por_teclado()
    if modifica_estudiante(estudiantes, estudiante):
      print 'Estudiante %s modificado.' % estudiante.nombre
    else:
      print 'No existe el estudiante %s.' % estudiante.nombre
  elif opcion == 3: # Eliminar estudiante.
    nombre = raw_input('Nombre: ')
    if elimina_estudiante(estudiantes, nombre):
      print 'Estudiante %s eliminado.' % nombre
    else:
      print 'No existe el estudiante %s.' % nombre
  elif opcion == 4: # Mostrar ficha de un estudiante.
    nombre = raw_input('Nombre: ')
    busca_y_muestra_estudiante(estudiantes, nombre)
  elif opcion == 5: # Mostrar listado completo
    listado_completo(estudiantes)
  elif opcion == 6: # Mostrar listado de nombres.
    listado_de_nombres(estudiantes)

print 'Gracias por usar el programa.'
