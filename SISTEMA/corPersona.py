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

from clsPersona import clsPersona
from visPersona import visPersona

class corPersona(object):
	lobjVista=visPersona()
	lobjPersona=clsPersona()
	
	def frControladora(self):
		liOpcion=9
		while liOpcion!=0:
			liOpcion=self.lobjVista.fiMenu()
			if liOpcion==1:
				self.frCrear()
			elif liOpcion==2:
				self.frListar()
			elif liOpcion==3:
				self.frBuscar()
			elif liOpcion==4:
				self.frModificar()
			elif liOpcion==5:
				self.frEliminar()
	
	def frCrear(self):
		lsCedula,lsNombres,lsApellidos=self.lobjVista.fsCrear()
		self.lobjPersona.fsGetCedula(lsCedula)
		self.lobjPersona.fsGetNombres(lsNombres)
		self.lobjPersona.fsGetApellidos(lsApellidos)
		self.lobjPersona.frIncluir()
		self.lobjVista.fsMensaje()
	
	def frListar(self):
		laArreglo=self.lobjPersona.faListar()
		self.lobjVista.fsListar(laArreglo)
	
	def frBuscar(self):
		lsCedula=self.lobjVista.fsBuscar()
		self.lobjPersona.fsGetCedula(lsCedula)
		self.lobjPersona.frBuscar()
		self.lobjVista.fsMostrar(self.lobjPersona.fsSetCedula(),self.lobjPersona.fsSetNombres(),self.lobjPersona.fsSetApellidos())
	
	def frModificar(self):
		self.frBuscar()
		lsNombres,lsApellidos=self.lobjVista.fsModificar()
		self.lobjPersona.fsGetNombres(lsNombres)
		self.lobjPersona.fsGetApellidos(lsApellidos)
		self.lobjPersona.frModificar()
		self.lobjVista.fsMensaje()
	
	def frEliminar(self):
		self.frBuscar()
		self.lobjPersona.frEliminar()
		self.lobjVista.fsMensaje()
		
		


lobjControla=corPersona()
lobjControla.frControladora()
		
	
