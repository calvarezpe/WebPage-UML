#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

"""
Modulo extractor de clases de ficheros .py
"""

import os
from xml.etree import ElementTree
import log

log = log.Log()


def ClasesPy(nombre_arch):
	Clases = []
	nombre_arch = nombre_arch.replace(" ", "\ ")
	cmd_ej = "ctags " + nombre_arch;
	texto = "Ejecutamos el comando " + cmd_ej
	log.log(texto)
	os.system(cmd_ej)

	Fichero_etiquetas = open("tags", "r")

	for line in Fichero_etiquetas:
		array_line = line.split()
		if ((array_line[-1] == "c")):
			Clases.append(array_line[0])

	Fichero_etiquetas.close()

	cmd_ej = "rm tags"
	os.system(cmd_ej)
	return Clases

def ClasesUML(nombre_arch):
	Clases = []
	print "Vamos a parsear ", nombre_arch
	tree = ElementTree.parse(nombre_arch)
	for node in tree.iter():
		if (node.tag[0] == "{"):
			tipo = node.tag.split("}")[-1]
			if (tipo == "Class"):
				try:
					Clases.append(node.attrib["name"])
					texto = " EXITO, clase " + node.attrib["name"] + " agregada"
					log.log(texto)
				except KeyError:
					texto = " ERROR, name no encontrado en el archivo " + nombre_arch
					texto += ". Elemento clase de UML sin nombre."
					log.log(texto)
	return Clases

def Depurar(lista):
	lista_nueva = []
	for i in lista:
		if i not in lista_nueva:
			lista_nueva.append(i)

	return lista_nueva

def hamdist(str1, str2):
	"""Count the # of differences between equal length strings str1 and str2"""
	diffs = 0
	for ch1, ch2 in zip(str1, str2):
		if ch1 != ch2:
			diffs += 1
	return diffs

def ListToSet(List):
	a = set()
	for Element in List:
		a.add(Element)

	return a
