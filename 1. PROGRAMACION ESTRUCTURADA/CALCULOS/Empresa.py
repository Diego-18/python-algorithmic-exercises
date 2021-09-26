#!/usr/bin/env python
#-*-coding:UTF8-*-

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#Algoritmo capaz de calcular el sueldo neto de un empleado con deducciones y bonificacion y de igual forma calcular 
#el monto que debe tener la empresa para el pago de nomina

lsseguir="s"
liacum=0
licont=0
licont2=0
licont3=0

while lsseguir=="S" or lsseguir=="s":
    lsnombre=raw_input("Introduzca el nombre del empleado: ")
    lfsueldob=float(raw_input("Introduzca el sueldo base: "))
    lsedocivil=raw_input("Introduzca el estado civil: ")
    lihijos=int(raw_input("Introduzca la cantidad de hijos: "))
    lianos=int(raw_input("Introduzca la cantidad de anos: "))
    lfsso=lfsueldob*0.02
    lfpf=lfsueldob*0.01
    lfca=lfsueldob*0.10
    lffahov=lfsueldob*0.10
    if (lihijos>0):
        libonoh=lihijos*700
        licont=licont+1
    else:
        libonoh=lihijos*0
    if (lsedocivil=="C") or (lsedocivil=="c"):
        libonoec=lfsueldob+300
        licont2=licont2+1
    else:
        libonoec=lfsueldob*0
    if (lianos>=10):
        libonoa=lfsueldob+500
        licont3=licont3+1
    elif(lianos<10):
        libonoa=lfsueldob+200
    lfsueldon=lfsueldob+(libonoh+libonoec+libonoa)-(lfsso+lfpf+lfca+lffahov)
    liacum=liacum+lfsueldon
    print "El sueldo neto del empleado es: ",lfsueldon
    lsseguir=raw_input("Desea seguir? (S/N): ")
print "La cantidad de empleados con hijos es: ",licont
print "La cantidad de empleados casados es: ",licont2
print "La cantidad de empleados con mas de 10 anos de labor es: ",licont3
print "La empresa necesita para pagar a los empleados: ",liacum

#UPTP S1-T1
