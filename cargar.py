import pickle

# Leemos la lista cargándola del fichero \texttt{mifichero.mio}...
lista = pickle.load(open('mifichero.mio'))
# y la mostramos por pantalla.
print lista
