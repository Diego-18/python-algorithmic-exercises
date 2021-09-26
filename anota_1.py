nota = raw_input('Nota a añadir: ')
f = open('notas.txt', 'a')
f.write(nota + '\n')
f.close()  
