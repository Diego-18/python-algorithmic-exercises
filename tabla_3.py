f = open('tabla.txt', 'w')

for i in range(1, 5001):
  f.write('%8d %8d\n' % (i, i**2))

f.close()
