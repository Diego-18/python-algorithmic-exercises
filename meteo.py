from record import record

class Meteo(record):
  estacion   =''
  temp     = [0, 0, 0, 0]
  lluvia   = [0, 0, 0, 0]

def mostrar_meteo(meteo):
  print 'Estación meteorólogica', meteo.estacion
  print 'Hora   Temperatura Litros/m2'
  print ' 0:00  %11.2f %9.2f' % (meteo.temp[0], meteo.lluvia[0])
  print ' 6:00  %11.2f %9.2f' % (meteo.temp[1], meteo.lluvia[1])
  print '12:00  %11.2f %9.2f' % (meteo.temp[2], meteo.lluvia[2])
  print '18:00  %11.2f %9.2f' % (meteo.temp[3], meteo.lluvia[3])
