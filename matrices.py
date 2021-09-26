def matriz_nula(filas, columnas):
  M = []
  for i in range(filas):
    M.append( [0] * columnas )
  return M

def lee_matriz(filas, columnas):
  M = matriz_nula(filas, columnas)
  for i in range(filas):
    for j in range(columnas):
      M[i][j] = float(raw_input('Introduce el componente (%d,%d): ' % (i, j)))
  return M

def dimension(M):
  return [len(M), len(M[0])]

def suma(A, B):
  if dimension(A) != dimension(B):
    return None
  else:
    [m, n] = dimension(A)
    C = crea_matriz_nula(m, n)
    for i in range(m):
      for j in range(n):
        C[i][j] = A[i][j] + B[i][j]
    return C
