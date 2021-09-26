#!/usr/bin/env python
#-*- coding:UTF8 -*-

################################
# Elaborado por: DIEGO CHAVEZ  #
################################

#Algoritmo capaz de calcular el sueldo neto de un empleado calculando sus deducciones, 
#sus bonos y de igual forma la cantidad de dinero que la empresa necesita para solventar el pago de nomina

#Inicio
def fsleerS (psNombre):
	lsVar=raw_input(psNombre)
	return lsVar

def fileerI (psHijos):
        liVar=int(raw_input(psHijos))
        return liVar

def fsleerS (psEC):
        lsVar=raw_input(psEC)
        return lsVar

def ffleerF (psSueldo):
        lfVar=float(raw_input(psSueldo))
        return lfVar

def fbCalc (pfmultiplicando, pfmultiplicador):
        lfvalor=pfmultiplicando*pfmultiplicador
        return lfvalor

#Programa

lsseguir="s"
lfsso=0.02
lfpf=0.01
lffahov=0.01
lfca=0.1
libh=650
libec=850
lfacum=0
lfSueldo=0

while lsseguir=="s" or lsseguir=="S":
        lsNombre=fsleerS("Nombre del Empleado: ")
        licant_h=fileerI("Cantidad de Hijos: ")
        lsec=fsleerS("Estado Civil del empleado: ")
        lfSueldo=ffleerF("El sueldo base: ")

        #Deducciones
        lftsso=fbCalc(lfSueldo,lfsso)
        lftpf=fbCalc(lfSueldo,lfpf)
        lftfahov=fbCalc(lfSueldo,lffahov)
        lftca=fbCalc(lfSueldo,lfca)

        #Asignaciones
        lftbh=fbCalc(licant_h,libh)
        if (lsec=="Casado") or (lsec=="casado"):
                libec=850
        else:
                libec=0

        lfs_neto=lfSueldo+(lftbh+libec)-(lftsso+lftpf+lftfahov+lftca)
        print "El sueldo neto del empleado es: ",lfs_neto
        lfacum=lfacum+lfs_neto
        lfsso=0
        lfpf=0
        lffahov=0
        lfca=0
        lfbh=0
        libec=0
        lsseguir=raw_input("Desea Seguir?: (S/N) ")
print "La empresa necesita para pagar la nomina del mes: ",lfacum
#Fin

#UPTP S1-T1