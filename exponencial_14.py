def exponencial(a, n):
  numerador = 1
  denominador = 1
  sumatorio = 1.0
  for k in range(1, n):
    numerador = a * numerador
    denominador = k * denominador
    sumatorio += numerador / denominador
  return sumatorio
