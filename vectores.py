#---------------------------------------------------------------------
# Módulo vectores
#---------------------------------------------------------------------
# Proporciona constantes y funciones para el cálculo vectorial en 3 dimensiones.
#---------------------------------------------------------------------
# Constantes que exporta:
# \qquad\emph{v\texttt{_}i}, \emph{v\texttt{_}j}, \emph{v\texttt{_}k}: vectores unidad
#
# Funciones que exporta:
# \qquad\emph{v\texttt{_}lee\texttt{_}vector}:
# \qquad\quad sin parámetros
# \qquad\quad devuelve un vector leído de teclado que se pide al usuario 
#
# \qquad\emph{v\texttt{_}muestra\texttt{_}vector}($v$):
# \qquad\quad muestra por pantalla el vector v con la notación $(x,y,z)$
# \qquad\quad no devuelve nada
#
# \qquad\emph{v\texttt{_}longitud}($v$):
# \qquad\quad devuelve la longitud del vector $v$
#
# \qquad\emph{v\texttt{_}suma}($u$, $v$):
# \qquad\quad devuelve el vector resultante de sumar $u$ y $v$
#
# \qquad\emph{v\texttt{_}producto_escalar}($u$, $v$):
# \qquad\quad devuelve el escalar resultante del producto escalar de $u$ por $v$
#
# \qquad\emph{v\texttt{_}producto_vectorial}($u$, $v$):
# \qquad\quad devuelve el vector resultante del producto vectorial de $u$ por $v$
#
# \qquad\emph{v\texttt{_}son_perpendiculares}($u$, $v$):
# \qquad\quad devuelve cierto si $u$ y $v$ son perpendiculares, y falso en caso contrario
#---------------------------------------------------------------------

# Constantes

v_i =[1, 0, 0]
v_j =[0, 1, 0]
v_k =[0, 0, 1]


# Funciones de entrada/salida

def v_lee_vector():
  x = float(raw_input('Componente x:'))
  y = float(raw_input('Componente y:'))
  z = float(raw_input('Componente z:'))
  return [x, y, z]

def v_muestra_vector(v):
  print '(%f, %f, %f)' % (v[0], v[1], v[2])


# Funciones de cálculo

def v_longitud(v):
  return sqrt(v[0]**2 + v[1]**2 + v[2]**2)

def v_suma(u, v):
  return [ u[0] + v[0], u[1] + v[1], u[2] + v[2] ]

def v_producto_escalar(u, v):
  return u[0]*v[0] + u[1]*v[1] + u[2]*v[2]

def v_producto_vectorial(u, v):
  resultado_x = u[1]*v[2] - u[2]*v[1]
  resultado_y = u[2]*v[0] - u[0]*v[2]
  resultado_z = u[0]*v[1] - u[1]*v[0]
  return [resultado_x, resultado_y, resultado_z]


# Predicados

def v_son_perpendiculares(u, v):
  return v_producto_escalar(u, v) == 0
