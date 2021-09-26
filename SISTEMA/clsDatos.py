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

import MySQLdb

class clsDatos(object):
	
	#Crear una conexión con la base de datos y el cursor
	def frConectar(self):
		lsServidor='localhost'
		lsUsuario='root'
		lsContrasena=''
		lsBaseDatos='prueba'
		self.arConexion=MySQLdb.connect(lsServidor,lsUsuario,lsContrasena,lsBaseDatos)
		self.arCursor=self.arConexion.cursor()
	
	#Ejecutar una SQL
	def frEjecutar(self,psSql):
		self.arCursor.execute(psSql)
		if psSql.upper().startswith('SELECT'):
			laDatos = self.arCursor.fetchall()
		else:
			self.arConexion.commit()
			laDatos = None
		return laDatos
	
	#Cerrar cursor y conexión
	def frDesconectar(self):
		self.arCursor.close()
		self.arConexion.close()
		
