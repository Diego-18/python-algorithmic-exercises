def muestra_nota_de_alumno(alumnos, notas, alumno_buscado):
  encontrado = False
  for i in range(len(alumnos)):
    if alumnos[i] == alumno_buscado:
      print alumno_buscado, nota[i]
      encontrado = True
      break
  if not encontrado:
    print 'El alumno %s no pertenece al grupo' % alumno_buscado
