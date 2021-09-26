from estadisticas import media, desviacion_tipica

notas = []
nota = 0
while not (0 <= nota <= 10):
  nota = float(raw_input('Dame una nota (entre 0 y 10): '))
  if 0 <= nota <= 10:
    notas.append(nota)

print 'Media:', media(notas)
print 'Desviacion típica:', desviacion_tipica(notas)
