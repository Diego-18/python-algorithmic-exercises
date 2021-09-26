mes = int(raw_input('Dame un mes: '))

if 1 <= mes <= 3:
  print 'Invierno.'
else:
  if mes == 4  or  mes == 5  or  mes == 6:
    print 'Primavera.'
  else:
    if not (mes < 7  or  9 < mes):
      print 'Verano.'
    else:
      if not (mes != 10  and  mes != 11  and  mes != 12):
        print 'Otoño.'
      else:
        print 'Ningún año tiene %d meses.' % mes
