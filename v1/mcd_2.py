def min(a, b):
  if a < b:
    return a
  else:
    return b

def max(a, b):
  if a > b:
    return a
  else:
    return b

def mcd(m, n):
  menor = min(m, n)
  mayor = max(m, n)
  resto = mayor % menor
  if resto == 0:
    return menor
  else:
    return mcd(menor, resto)
