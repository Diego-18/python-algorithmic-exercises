from math import sqrt

G = 6.67e-11
M_Tierra = 5.97e24
R_Tierra = 6.37e6
M_Luna = 7.35e22
R_Luna = 1.74e6

def fuerza_grav(M, m, r):
  return G * M * m / r**2

def distancia(M, m, F):
  return sqrt( G * M * m / F )

def velocidad_escape(M, R):
  return sqrt( 2 * G * M / R )

ve_Tierra = velocidad_escape(M_Tierra, R_Tierra)
ve_Luna = velocidad_escape(M_Luna, R_Luna)
