################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#FUNCIONES#

def fbprom (psnota,pinnota):    		#Funcion de Promedio
    lfacum=0
    if psnota>=0:
        lfacum=lfacum+psnota
        return True
    return False
    if (psnota==True):
        lfprom=lfacum/pinnota
    return lfprom
    
def fbprimo (pinumero):					#Funcion de N° Primos
        licont=0
        for liN in range (1,pinumero+1):
                if (pinumero%liN==0):
                        licont=licont+1
        if (licont==2):
                return True
        return False
 
def fbPrimo(pfN):						#Funcion de N° Primos (2)
	if (pfN<2):
		return False
	for i in range (2,pfN):
		if (pfN%i==0):
			return False
	return True

def fbpar (pinumero):					#Funcion de N° Par
        if (pinumero%2==0):
                return True
        return False

def fbpositivo (pinumero):				#Funcion de N° Positivo
        if (pinumero>0):
                return True
        return False
        
def fbperfecto (pinumero):				#Funcion de N° Perfecto
        liacum=0
        for liN in range (1,pinumero):
                if (pinumero%2==0):
                        liacum=liacum+liN
                if (liacum==pinumero):
                        return True
        return False

def fbentero (pinumero):				#Funcion de N° Entero
        if (pinumero%1==0):
                return True
        return False

def fsLeerS(psTexto):					#Funcion de Cadena
	lsVar=raw_input(psTexto)
	return lsVar

def ffLeerF(psTexto):					#Funcion de Flotante
	lfVar=float(raw_input(psTexto))
	return lfVar

def fiLeerI(psTexto):					#Funcion de Entero
	liVar=int(raw_input(psTexto))
	return liVar

def fsInverso(psTexto): 				#Funcion para inverso
    lsVar=psTexto[::-1]
    return lsVar

def fbPalindrome(psTexto): 				#Funcion para Palindrome
    psTexto=psTexto.lower()
    lsInverso=fsInverso(psTexto)
    if (psTexto==lsInverso):
        return True
    else:
        return False

def fiPartir (paArreglo, piInicio, piFin):  #Funcion de Partir (Se utiliza mas que todo con el Quicksort)
	liMarca=paArreglo[piFin]
	liComienzo=piInicio-1
	liFinal=piFin
	liListo=0
	while not liListo:
		while not liListo:
			liComienzo=liComienzo+1
			if (liComienzo==liFinal):
				liListo=1
				break
			if (paArreglo[liComienzo]>liMarca):                #De menor a mayor (>)....de mayor a menor (<)
				paArreglo[liFinal]=paArreglo[liComienzo]
				break
		while not liListo:
			liFinal=liFinal-1
			if (liFinal==liComienzo):
				liListo=1
				break
			if (paArreglo[liFinal]<liMarca):                  #De menor a mayor(<)... de mayor a menor (>)
				paArreglo[liComienzo]=paArreglo[liFinal]
				break
	paArreglo[liFinal]=liMarca
	return liFinal
	
def faQuickSort(paArreglo,piInicio,piFin): #Funcion QuickSort
	if (piInicio<piFin):
		liMitad=fiPartir(paArreglo,piInicio,piFin)
		faQuickSort(paArreglo,piInicio,liMitad-1)
		faQuickSort(paArreglo,liMitad+1,piFin)
	else:
		return

def faBurbuja (paArreglo):      		#Funcion Burbuja
	liTamano=len(paArreglo)
	for liX in range (0,liTamano):
		for liJ in range (liX, liTamano-1):
			if (paArreglo[liX]<paArreglo[liJ+1]):
				liAux=paArreglo[liX]
				paArreglo[liX]=paArreglo[liJ+1]
				paArreglo[liJ+1]=liAux
	return paArreglo

def fiBuscar(paArreglo,piNum):  		#Funcion Buscar (Numeros)
	liTamano=len(paArreglo)
	for liI in range(0,liTamano):
		if (paArreglo[liI]==piNum):
			return liI
	return -1

def faImprimir(paArreglo):				#Funcion Imprimir (Numeros)
	print paArreglo

def faImprimir2(paArreglo):				#Funcion Imprimir por Seccion (Numeros)
	for liX in paArreglo:
		print liX

def faEliminar(paArreglo,piNum):		#Funcion de Eliminar 
	liX=fiBuscar(paArreglo,piNum)
	if liX!=-1:
		del(paArreglo[liX])
	return paArreglo

def faCargar(paArreglo):				#Funcion de Cargar
	liNum=fiLeerI("Introduzca el Numero: ")
	paArreglo.append(liNum)
	return paArreglo

def fiMenu():							#Funcion de Menu
	print "1.-Opcion 1"
	print "2.-Opcion 2"
	print "3-Opcion 3"
	print "4.-Opcion 4"
	print "5.-Opcion 5"
	print "6.-Opcion 6"
	print "0.-Salir"
	liOpcion=fiLeerI("Introduzca su opcion: ")
	return liOpcion

def fsContinuar():						#Funcion de Continuar
        return fsLeerS("Pulse Enter")

def foNuevoA(poArchivo):			  	#Funcion de Nuevo Archivo
	os.system("clear")
	lsContenido=fsLeerS("Contenido: ")
	poArchivo=open("132.txt","w")
	poArchivo.write(lsContenido)
	poArchivo.close()
	return poArchivo

def foLeerA(poArchivo):				  	#Funcion de Leer Archivo
	os.system("clear")
	poArchivo=open("132.txt", "r")
	lsContenido=poArchivo.read()
	print lsContenido
	poArchivo.close()
	fsContinuar()
	return poArchivo

def foEditarA(poArchivo):				#Funcion de Editar Archivo
	os.system("clear")
	poArchivo=open("132.txt","r+")
	lsContenido=poArchivo.read()
	print lsContenido
	lsContenido=fsLeerS ("Agregar contenido: ")
	poArchivo.write(lsContenido)
	poArchivo.close()
	return poArchivo

def faSacar(paArreglo):				  	#Funcion de Sacar en Pilas
	os.system("clear")
	print paArreglo.pop()
	fsLeerS("Pulse Enter para continuar")
	return paArreglo

def faSacar(paArreglo):				  	#Funcion de Sacar en Colas
	os.system("clear")
	print paArreglo.popleft()
	fsLeerS("Pulse Enter para continuar")
	return paArreglo

def faSacar(paArreglo):				  	#Funcion de Sacar con excepciones (si se utiliza para pilas se coloca unicamente "pop" sin el "left")
    os.system("cls")
    try:
        print paArreglo.popleft()
    except IndexError:
        print "La cola esta vacia"
    fsContinuar()

def faImprimir(paArreglo):			  	#Funcion de Imprimir en cadena los 5 primeros de la Cola
	for liX in range(0,5):
		print paArreglo[liX]
	fsContinuar()

