from record import record

class Persona(record):
  nombre   = ''
  dni   = ''
  edad   = 0

juan   = Persona(nombre='Juan Paz',   dni='12345678Z',   edad=19)
ana   = Persona(nombre='Ana Mir',   dni='23456789Z',   edad=18)
