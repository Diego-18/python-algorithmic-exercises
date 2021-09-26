from record import record

class Persona(record):
  nombre   = ''
  dni   = ''
  edad   = 0

def copia(pers):
  return Persona(nombre=pers.nombre[:], dni=pers.dni[:], edad=pers.edad)

def nada_util(persona1, persona2):
  persona1.edad = persona1.edad + 1
  persona3 = persona2
  persona4 = copia(persona2)
  persona3.edad = persona3.edad - 1
  persona4.edad = persona4.edad - 2
  return persona4

juan = Persona(nombre='Juan Paz', dni='12345679Z', edad=19)
pedro = Persona(nombre='Pedro López', dni='23456789D', edad=18)
otro = nada_util(juan, pedro)
print juan
print pedro
print otro
