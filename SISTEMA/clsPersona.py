#!/usr/bin/env python
# -*- coding: utf-8 *-*

"""
corPersona.py
Copyright 2014 José B. Silva H. y Pausides D. Calderon

Este programa es software libre; usted puede redistribuirlo y / o modificarlo
Bajo los términos de la Licencia Pública General de GNU según lo publicado por
La Fundación para el Software Libre; ya sea la versión 2 de la Licencia, o
(A su elección) cualquier versión posterior.
Este programa se distribuye con la esperanza de que sea útil,
Pero SIN NINGUNA GARANTÍA; ni siquiera la garantía implícita de
COMERCIALIZACIÓN o IDONEIDAD PARA UN PROPÓSITO PARTICULAR. consulte la
GNU General Public License para más detalles.
"""

from clsDatos import clsDatos

class clsPersona(clsDatos):
	__asCedula=""
	__asNombres=""
	__asApellidos=""
	
	def fsGetCedula(self,psCedula):
		self.__asCedula=psCedula
			
	def fsGetNombres(self,psNombres):
		self.__asNombres=psNombres
		
	def fsGetApellidos(self,psApellidos):
		self.__asApellidos=psApellidos
	
	def fsSetCedula(self):
		return self.__asCedula
	
	def fsSetNombres(self):
		return self.__asNombres
		
	def fsSetApellidos(self):
		return self.__asApellidos
	
	def faListar(self):
		lsSql="SELECT * FROM persona"
		self.frConectar()
		laDatos=self.frEjecutar(lsSql)
		self.frDesconectar()
		return laDatos
	
	def frBuscar(self):
		lsSql="SELECT * FROM persona WHERE cedula='"+self.__asCedula+"'"
		self.frConectar()
		laDatos=self.frEjecutar(lsSql)
		self.frDesconectar()
		for laRegistro in laDatos:
			self.__asCedula=laRegistro[0]
			self.__asNombres=laRegistro[1]
			self.__asApellidos=laRegistro[2]
	
	def frIncluir(self):
		lsSql="INSERT INTO persona (cedula,nombres,apellidos) values ('"+self.__asCedula+"','"+self.__asNombres+"','"+self.__asApellidos+"')"
		self.frConectar()
		laDatos=self.frEjecutar(lsSql)
		self.frDesconectar()

	def frModificar(self):
		lsSql="UPDATE persona SET nombres='"+self.__asNombres+"',apellidos='"+self.__asApellidos+"' WHERE cedula='"+self.__asCedula+"'"
		self.frConectar()
		laDatos=self.frEjecutar(lsSql)
		self.frDesconectar()
	
	def frEliminar(self):
		lsSql="DELETE FROM persona WHERE cedula='"+self.__asCedula+"'"
		self.frConectar()
		laDatos=self.frEjecutar(lsSql)
		self.frDesconectar()	
