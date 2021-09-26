import pickle

# Creamos una lista ...
lista = [1, 2, 3, 4] 
# y ahora la guardamos en un fichero llamado \texttt{mifichero.mio}.
pickle.dump(lista, open('mifichero.mio', 'w'))
