#! usr/bin/env python
# -*- coding: cp1252 -*-
import random
import os

def Leer(psTexto):
    lsV=raw_input(psTexto)
    lsV=lsV.upper()
    return lsV


def validacionLetra(letra):
    
    if len(letra)==1 and letra.isalpha():
        return True
    else:
        return False
    return letra


def TamanoPalabra(palabra):
    tamano=len(palabra)
    return tamano


def Espacio(palabra,paArreglo):
    Piso=TamanoPalabra(palabra)
    for I in range(0,Piso):
        paArreglo.append("_")
    return paArreglo

def Palabra(palabra,paArreglo):
    for liX in palabra:
        paArreglo.append (liX)


def Buscar(paArreglo,letra):
    Tamano=TamanoPalabra(paArreglo)
    for li in range (0,Tamano):
        if (paArreglo[li]==letra):
            return li
    return -1

def Muerte(Vidas):
    if Vidas==7:
        print"      ...... "
        print"     /  _  _\ "
        print"    c|  ´ .´ | "
        print"     (   === ) "
        print"   __|\__.__/ __"
    if Vidas==6:
        print"      ...... "
        print"     /  _  _\ "
        print"    c|  ´ .´ | "
        print"     (   === ) "
        print"   __|\__.__/ __"
        print"  /    \__/     \ "
        print"  |__|       |__| "
        print"     |       |   "
        print"     |       |   "
        print"     |_______|  "
    if Vidas==5:
        print"      ...... "
        print"     /  _  _\ "
        print"    c|  ´ .´ | "
        print"     (   === ) "
        print"   __|\__.__/ __"
        print"  /    \__/     \ "
        print"  |__|       |__| "
        print"  |  |       |   "
        print"  |  |       |   "
        print"  |  |_______|   "
        print" ( ...)"
    if Vidas==4:
        print"      ...... "
        print"     /  _  _\ "
        print"    c|  ´ .´ | "
        print"     (   === ) "
        print"   __|\__.__/ __"
        print"  /    \__/     \ "
        print"  |__|       |__| "
        print"  |  |       |  |   "
        print"  |  |       |  | "
        print"  |  |_______|  | "
        print" ( ...)     (... ) "
    if Vidas==3:
        print"      ...... "
        print"     /  _  _\ "
        print"    c|  ´ .´ | "
        print"     (   === ) "
        print"   __|\__.__/ __"
        print"  /    \__/     \ "
        print"  |__|       |__| "
        print"  |  |       |  |   "
        print"  |  |       |  | "
        print"  |  |_______|  | "
        print" ( ...)     (... ) "
        print"   |         "
        print"   |    / "
        print"   |   |   "
        print"   |   |   "
        print"   |___|   "
        print"   | __|   "
        print"   |___|   "
    if Vidas==2:
        print"      ...... "
        print"     /  _  _\ "
        print"    c|  ´ .´ | "
        print"     (   === ) "
        print"   __|\__.__/ __"
        print"  /    \__/     \ "
        print"  |__|       |__| "
        print"  |  |       |  |   "
        print"  |  |       |  | "
        print"  |  |_______|  | "
        print" ( ...)     (... ) "
        print"   |          | "
        print"   |    /\    | "
        print"   |   |  |   | "
        print"   |   |  |   | "
        print"   |___|  |___| "
        print"   | __|  | __| "
        print"   |___|  |___| "
    
    if Vidas==1:
        print"                     ## "
        print"      ......         ## "
        print"     /  _  _\        ## "
        print"    c|  ´ .´ |       ## "
        print"     (   === )       ## "
        print"   __|\__.__/ __     ## "
        print"  /    \__/     \    ## "
        print"  |__|       |__|    ## "
        print"  |  |       |  |    ## "
        print"  |  |       |  |    ## "
        print"  |  |_______|  |    ## "
        print" ( ...)     (... )   ## "
        print"   |          |      ## "
        print"   |    /\    |      ## "
        print"   |   |  |   |      ## "
        print"   |   |  |   |      ## "
        print"   |___|  |___|      ## "
        print"   | __|  | __|      ## "
        print"   |___|  |___|      ## "
        
    if Vidas==0:
        print"  ##################### "
        print"        ##           ## "
        print"      ......         ## "
        print"     /  _  _\        ## "
        print"    c|  X .X |       ## "
        print"     (   === )       ## "
        print"   __######### __    ## "
        print"  /    \__/     \    ## "
        print"  |__| \  /  |__|    ## "
        print"  |  |  \/   |  |    ## "
        print"  |  |  /\   |  |    ## "
        print"  |  |_/__\__|  |    ## "
        print" ( ...)     (... )   ## "
        print"   |          |      ## "
        print"   |    /\    |      ## "
        print"   |   |  |   |      ## "
        print"   |   |  |   |      ## "
        print"   |___|  |___|      ## "
        print"   | __|  | __|      ## "
        print"   |___|  |___|      ## "
        print"                     ## "
        print"                     ## "


    

listaPalabras=["HOLA","UNO","LUZ","IGLU","ALBUM","BOMBA","AJEDREZ","MANGO","OLIMPIADAS","YELMO","INFORMATICA","SIGUIENTE","NUEVO","TSUNAMI","TEMPESTAD","MANZANA","PERA","CAJA","LAPTOP","CASCADA"]
listaPalabras2=["VENEZUELA","GOBIERNO","NECESIDAD","AHORCADO","CORTINA","MAIZ","MALDAD","PUREZA","ALMA","CACHORRO","AMENAZA","NIVEL","TEATRO","TITANES"]
listaPalabras3=["CARACOL","CORAZON","HOLGAZAN","DESPECHO","IMPECABLE","MALETA","CONJUGAR","EXCEPCION","PRONOMBRES","FILAMENTO","FINIQUITAR","IMPOTENTE"]
listaPalabras4=["EDIFICIO","PARLANTE","ORQUIDEA","AMAZONAS","CAPARAZON","CACHIVACHE","VOLUPTUOSIDADA","VOCACION","HONESTIDADA","FILTRAR","TRAMPA"]
listaPalabras5=["ELECTRICIDAD","VACACIONES","KILOMETRICO","INDIGENA","IMPOSIBLE","ENCICLOPEDIA","DOCUMENTADO","ANIQUILACION","AMONTONAMIENTO","RISA"]
PalabraElegida= random.choice(listaPalabras)

Arreglo1=[]# este es el que son los espacios(aqui se agregan)
Arreglo2=[]# la palabra por letras(de aqui se borran)
Arreglo3=[]#sirve de Guia
Arreglo4=[]#para llevar el control de las letras usadas
#print PalabraElegida
#print TamanoPalabra(PalabraElegida)

Espacio(PalabraElegida,Arreglo1) #pala lograr hacer la cantidad de pisos de la palabra

#print Arreglo1

Palabra(PalabraElegida,Arreglo2)#llamado del modulo palabra para que ingrese letra a letra en el arreglo

Palabra(PalabraElegida,Arreglo3)# la guia para comparar al final en caso de victoria
#print Arreglo2



Vidas=8 #total de vidas
Victoria=0 #necesaria para igualar a la guia, si ocurre sale del while y gana
TotalV=0

while Vidas!=0 and Victoria!=1:
    print""
    print "==========================JUEGO DEL AHORCADO==========================="
    print "=                                                                     ="
    print "=","                                                                    ="
    print "=      ",Arreglo1
    print "=                                                                     ="
    print "=  Letras que llevas Usadas" , Arreglo4
    print "=  Total de Vidas" , Vidas, "                                                  ="
    Muerte(Vidas)
    print "=","                                                                 ","="
    
    Letra=Leer("=  Elige Una Letra: ")
    
    
    Arreglo4.append(Letra)
    MismaLetra=Arreglo3.count(Letra)
    if validacionLetra(Letra)==True:
        print Letra
    else:
        print "es una sola letra, no valen numeros"
    liX1=Buscar(Arreglo2,Letra)
    if(liX1==-1):
        Vidas=Vidas-1
        print "=   no esta"
        z=Leer("presiona enter")
        print "======================================================================="

        os.system("cls")
    else:
        print "=   si esta"
        print "======================================================================="
        x=Leer("presiona enter")
        os.system("cls")
        while MismaLetra!=0:
            liX1=Buscar(Arreglo2,Letra)
            if(liX1!=-1):
                del(Arreglo2[liX1])
                Arreglo2.insert(liX1,"_")

                del(Arreglo1[liX1])
                Arreglo1.insert(liX1,Letra)
                MismaLetra=MismaLetra-1

            if Arreglo3==Arreglo1:
                Victoria=Victoria+1
                print ""
                print "                          ============"
                print "                          =HAS=GANADO="
                print "                          ============"
                print ""
                print "la palabra era" , Arreglo3
                TotalV=TotalV+1
                print "llevas ganadas", TotalV

            

if Vidas==0:
    print "la palabra era" , Arreglo3
    print "lograste ganar", TotalV, "veces"
    Muerte(Vidas)
    Z=Leer("............GAME OVER..............")


#nivel dos
PalabraElegida2= random.choice(listaPalabras2)

ArregloN2_1=[]
ArregloN2_2=[]
ArregloN2_3=[]
ArregloN2_4=[]


Espacio(PalabraElegida2,ArregloN2_1) 
Palabra(PalabraElegida2,ArregloN2_2)
Palabra(PalabraElegida2,ArregloN2_3)



Vidas=8 
Victoria=0
if TotalV==1:
    N2=Leer("PREPADARO PARA EL SEGUNDO NIVEL..PRESIONA ENTER")
    os.system("cls")
    while Vidas!=0 and Victoria!=1:
        print""
        print "==========================JUEGO DEL AHORCADO==========================="
        print "=                                                                     ="
        print "=","                                                                    ="
        print "=      ",ArregloN2_1
        print "=                                                                     ="
        print "=  Letras que llevas Usadas" , ArregloN2_4
        print "=  Total de Vidas" , Vidas, "                                                  ="
        Muerte(Vidas)
        print "=","                                                                   ","="
        Letra=Leer("=  Elige Una Letra: ")

        ArregloN2_4.append(Letra)
        MismaLetra=ArregloN2_3.count(Letra)
        if validacionLetra(Letra)==True:
            print Letra
        else:
            print "es una sola letra, no valen numeros"
        liX1=Buscar(ArregloN2_2,Letra)
        if(liX1==-1):
            Vidas=Vidas-1
            print "=   no esta"
            
            print "======================================================================="
            z=Leer("presiona enter")
            os.system("cls")
        else:
            print "=   si esta"
            print "======================================================================"
            x=Leer("presiona enter")
            os.system("cls")
            while MismaLetra!=0:
                liX1=Buscar(ArregloN2_2,Letra)
                if(liX1!=-1):

                    del(ArregloN2_2[liX1])
                    ArregloN2_2.insert(liX1,"_")

                    del(ArregloN2_1[liX1])
                    ArregloN2_1.insert(liX1,Letra)
                    MismaLetra=MismaLetra-1
        
        
        if ArregloN2_3==ArregloN2_1:
            Victoria=Victoria+1
            print ""
            print "                          ============"
            print "                          =HAS=GANADO="
            print "                          ============"
            print ""
            print "la palabra era" , ArregloN2_3
            TotalV=TotalV+1
            print "llevas ganadas", TotalV

            

if Vidas==0:
    print "la palabra era" , ArregloN2_3
    print "lograste ganar", TotalV, "veces"
    Muerte(Vidas)
    Z=Leer("............GAME OVER..............")

#tercer nivel
PalabraElegida3= random.choice(listaPalabras3)

ArregloN3_1=[]
ArregloN3_2=[]
ArregloN3_3=[]
ArregloN3_4=[]


Espacio(PalabraElegida3,ArregloN3_1) 
Palabra(PalabraElegida3,ArregloN3_2)
Palabra(PalabraElegida3,ArregloN3_3)



Vidas=8 
Victoria=0
if TotalV==2:
    N3=Leer("PREPADARO PARA EL TERCER NIVEL..PRESIONA ENTER")
    os.system("cls")
    while Vidas!=0 and Victoria!=1:
        print""
        print "==========================JUEGO DEL AHORCADO==========================="
        print "=                                                                     ="
        print "=","                                                                    ="
        print "=      ",ArregloN3_1
        print "=                                                                     ="
        print "=  Letras que llevas Usadas" , ArregloN3_4
        print "=  Total de Vidas" , Vidas, "                                                  ="
        Muerte(Vidas)
        print "=","                                                                   ","="
        Letra=Leer("=  Elige Una Letra: ")

        ArregloN3_4.append(Letra)
        MismaLetra=ArregloN3_3.count(Letra)
        if validacionLetra(Letra)==True:
            print  "        ",Letra
        else:
            print "es una sola letra, no valen numeros"
        liX1=Buscar(ArregloN3_2,Letra)
        if(liX1==-1):
            Vidas=Vidas-1
            print "=   no esta"
            print "======================================================================"
            z=Leer("presiona enter")
            os.system("cls")
        else:
            print "=   si esta"
            print "======================================================================"
            x=Leer("presiona enter")
            os.system("cls")
            while MismaLetra!=0:
                liX1=Buscar(ArregloN3_2,Letra)
                if(liX1!=-1):

                    del(ArregloN3_2[liX1])
                    ArregloN3_2.insert(liX1,"_")

                    del(ArregloN3_1[liX1])
                    ArregloN3_1.insert(liX1,Letra)
                    MismaLetra=MismaLetra-1
        
        
        if ArregloN3_3==ArregloN3_1:
            Victoria=Victoria+1
            print "                          ============"
            print "                          =HAS=GANADO="
            print "                          ============"
            print "la palabra era" , ArregloN3_3
            TotalV=TotalV+1
            print "llevas ganadas", TotalV

            

if Vidas==0:
    print "la palabra era" , ArregloN3_3
    print "lograste ganar", TotalV, "veces"
    Muerte(Vidas)
    Z=Leer("............GAME OVER..............")

#cuarto nivel


PalabraElegida4= random.choice(listaPalabras4)

ArregloN4_1=[]
ArregloN4_2=[]
ArregloN4_3=[]
ArregloN4_4=[]


Espacio(PalabraElegida4,ArregloN4_1) 
Palabra(PalabraElegida4,ArregloN4_2)
Palabra(PalabraElegida4,ArregloN4_3)



Vidas=8 
Victoria=0
if TotalV==3:
    N3=Leer("PREPADARO PARA EL CUERTO NIVEL..PRESIONA ENTER")
    os.system("cls")
    while Vidas!=0 and Victoria!=1:
        print""
        print "==========================JUEGO DEL AHORCADO==========================="
        print "=                                                                     ="
        print "=","                                                                    ="
        print "=      ",ArregloN4_1
        print "=                                                                     ="
        print "=  Letras que llevas Usadas" , ArregloN4_4
        print "=  Total de Vidas" , Vidas, "                                                  ="
        Muerte(Vidas)
        print "=","                                                                   ","="
        Letra=Leer("=  Elige Una Letra: ")

        ArregloN4_4.append(Letra)
        MismaLetra=ArregloN4_3.count(Letra)
        if validacionLetra(Letra)==True:
            print  "        ",Letra
        else:
            print "es una sola letra, no valen numeros"
        liX1=Buscar(ArregloN4_2,Letra)
        if(liX1==-1):
            Vidas=Vidas-1
            print "=   no esta"
            print "======================================================================"
            z=Leer("presiona enter")
            os.system("cls")
        else:
            print "=   si esta"
            print "======================================================================"
            x=Leer("presiona enter")
            os.system("cls")
            while MismaLetra!=0:
                liX1=Buscar(ArregloN4_2,Letra)
                if(liX1!=-1):

                    del(ArregloN4_2[liX1])
                    ArregloN4_2.insert(liX1,"_")

                    del(ArregloN4_1[liX1])
                    ArregloN4_1.insert(liX1,Letra)
                    MismaLetra=MismaLetra-1
        
        
        if ArregloN4_3==ArregloN4_1:
            Victoria=Victoria+1
            print "                          ============"
            print "                          =HAS=GANADO="
            print "                          ============"
            print "la palabra era" , ArregloN4_3
            TotalV=TotalV+1
            print "llevas ganadas", TotalV

            

if Vidas==0:
    print "la palabra era" , ArregloN4_3
    print "lograste ganar", TotalV, "veces"
    Muerte(Vidas)
    Z=Leer("............GAME OVER..............")
    
#echo por luis jose Vivas rodriguez
