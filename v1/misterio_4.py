from math import ceil # \emph{ceil} redondea al alza.

grados = float(raw_input('Dame un ángulo (en grados): '))

cuadrante = int(ceil(grados) % 360) / 90
if cuadrante == 0:
  print 'primer cuadrante'
if cuadrante == 1:
  print 'segundo cuadrante'
if cuadrante == 2:
  print 'tercer cuadrante'
if cuadrante == 3:
  print 'cuarto cuadrante'
