def es_perfecto(n):
  for i in range(1, n):
    sumatorio = 0
    if n % i == 0:
      sumatorio += i
  return sumatorio == n
