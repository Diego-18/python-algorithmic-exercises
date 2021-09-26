from math import sin, cos, pi

def curva_von_koch(xa, ya, xb, yb, n):
  if n == 0:
    create_line(xa, ya, xb, yb)
  else:
    xc = xa + (xb - xa) / 3.0
    yc = ya + (yb - ya) / 3.0
    xd = xb + (xa - xb) / 3.0
    yd = yb + (ya - yb) / 3.0
    xe = (xc+xd)*cos(pi/3)-(yd-yc)*sin(pi/3)
    ye = (yc+yd)*cos(pi/3)+(xd-xc)*sin(pi/3)
    curva_von_koch(xa, ya, xc, yc, n-1)
    curva_von_koch(xc, yc, xe, ye, n-1)
    curva_von_koch(xe, ye, xd, yd, n-1)
    curva_von_koch(xd, yd, xb, yb, n-1)  

def copo_von_koch(t, n):
  v1x = 0
  v1y = 0
  v2x = t*cos(2*pi/3)
  v2y = t*sin(2*pi/3)
  v3x = t*cos(pi/3)
  v3y = t*sin(pi/3)
  curva_von_koch(v1x, v1y, v2x, v2y, n)
  curva_von_koch(v2x, v2y, v3x, v3y, n)
  curva_von_koch(v3x, v3y, v1x, v1y, n)

window_coordinates(-200,0,200,400)
copo_von_koch (325, 3)
