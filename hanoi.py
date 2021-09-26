def resuelve_hanoi(n, inicial, final, libre):
  if n == 1:
    print 'Mover disco superior de aguja', inicial, 'a', final
  else:
    resuelve_hanoi(n-1, inicial, libre, final)
    print 'Mover disco superior de aguja', inicial, 'a', final
    resuelve_hanoi(n-1, libre, final, inicial)

resuelve_hanoi(4,1,3,2)
