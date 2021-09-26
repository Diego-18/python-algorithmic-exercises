f = open('tabla.txt', 'w')

for i in range(1, 5001):
  f.write(str(i) + ' ' + str(i**2) + '\n')

f.close()
