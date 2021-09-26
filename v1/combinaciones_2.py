def factorial(n): 
  productorio = 1.0 
  for i in range(1, n+1): 
    productorio *= i 
  return productorio

def combinaciones(n, m):
  return factorial(n) / (factorial(n-m) * factorial(m))
