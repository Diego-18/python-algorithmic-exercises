
m = int(raw_input('Dime el número de filas: '))
n = int(raw_input('Dime el número de columnas: '))

# Creamos dos matrices nulas...
A = []
for i in range(m):
  A.append( [0] * n )

B = []
for i in range(m):
  B.append( [0] * n )

# ... y leemos sus contenidos de teclado.
print 'Lectura de la matriz A'
for i in range(m):
  for j in range(n):
    A[i][j] = float(raw_input('Dame el componente (%d,%d): ' % (i, j)))

print 'Lectura de la matriz B'
for i in range(m):
  for j in range(n):
    B[i][j] = float(raw_input('Dame el componente (%d,%d): ' % (i, j)))

# Construímos otra matriz nula para albergar el resultado.
C = []
for i in range(m):
  C.append( [0] * n )

# Empieza el cálculo de la suma.
for i in range(m):
  for j in range(n):
    C[i][j] = A[i][j] + B[i][j]

# Y mostramos el resultado por pantalla
print "Suma:"
for i in range(m):
  for j in range(n):
    print C[i][j],
  print
