 from record import record

class Fecha(record):
  dia     = 1
  mes     = 1
  anyo    = 1

def fecha_breve(fecha):
  return '%d/%d/%d' % (fecha.dia, fecha.mes, fecha.anyo)

def fecha_en_anyo_bisiesto(fecha):
  if fecha.anyo % 4 != 0:
    return False
  if fecha.anyo % 400 == 0:
    return True
  return fecha.anyo % 100 != 0

def lee_fecha():
  dia = int(raw_input('Día: '))
  while dia <1 or dia > 31:
    dia = int(raw_input('Día: '))

  mes = int(raw_input('Mes: '))
  while mes <1 or mes > 12:
    mes = int(raw_input('Mes: '))

  anyo = int(raw_input('Año: '))

  return Fecha(dia=dia, mes=mes, anyo=anyo)

def fecha_es_menor(fecha1, fecha2):
  if fecha1.anyo < fecha2.anyo:
    return True
  elif fecha1.anyo > fecha2.anyo:
    return False
  if fecha1.mes < fecha2.mes:
    return True
  elif fecha1.mes > fecha2.mes:
    return False
  return fecha1.dia < fecha2.dia
