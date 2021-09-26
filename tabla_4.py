f = open('tabla.txt', 'w')

for i in range(1, 5001):
  f.write(i)
  f.write(i**2)

f.close()
