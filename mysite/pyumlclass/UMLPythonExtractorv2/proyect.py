#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

"""
Analizador de proyectos
"""

import sys
import os
from xml.etree import ElementTree
from os import walk
import ExtractorClases

def conteo(Lista_py, Lista_uml):
	""""cuenta = 0
	cuenta_exi = 0
	cuenta_ham = 0
	cuenta_mayus = 0
	lista_inex = []
	for valor in Lista_uml:
		if valor in Lista_py:
			cuenta += 1
			cuenta_exi += 1
		else:
		 	lista_inex.append(valor)

	lista_aux = []
	for i in Lista_py:
		lista_aux.append(i.upper())

	if (len(lista_inex) > 0): #Comprobaci�n mayusculas
		for i in lista_inex:
			if i.upper() in lista_aux:
				cuenta += 1
				lista_inex.remove(i)
				frase = "Palabra corregida por may�sculas: " + i
				ExtractorClases.log.log(frase)
				cuenta_mayus += 1

	if (len(lista_inex) > 0): #Comprobaci�n distancia hamming
		for i in lista_inex:
			for Clase_python in Lista_py:
				if(ExtractorClases.hamdist(Clase_python, i)<2):
					cuenta += 1
					cuenta_ham += 1
					lista_inex.remove(i)
					frase = "Palabra corregida por hamming: " + i
					ExtractorClases.log.log(frase)
					break
"""

	UML_Set = ExtractorClases.ListToSet(Lista_uml)
	Python_Set = ExtractorClases.ListToSet(Lista_py)

	### EXACTAMENTE IGUAL ###
	PythonUMLClass_Set = Python_Set.intersection(UML_Set)
	cuenta_exi = len(Python_Set.intersection(UML_Set))

	### COMPARACION POR ERRORES MAYUSCULAS MINUSCULAS ###
	MinusUML_Set = set()
	MinusPython_Set = set()
	# Creamos una lista con las clases uml en minuscula que no esten ya en coincidentes
	for UML_Class in UML_Set:
		if UML_Class not in PythonUMLClass_Set:
			MinusUML_Set.add(UML_Class.lower())
	# Creamos una lista con las clases python en minuscula que no esten ya en coincidentes
	for Python_Class in Python_Set:
		if Python_Class not in PythonUMLClass_Set:
			MinusPython_Set.add(Python_Class.lower())
	# Creamos una lista con las que sean iguales
	MinusPythonUMLClass_Set = MinusPython_Set.intersection(MinusUML_Set)
	cuenta_mayus = len(MinusPythonUMLClass_Set)
	# Actualizamos a la lista general
	PythonUMLClass_Set.update(MinusPythonUMLClass_Set)

	### COMPARACION CON DISTANCIA HAMMING ###
	cuenta_ham = 0
	for Python_Class in Python_Set.difference(PythonUMLClass_Set):
		if Python_Class.lower() not in MinusPythonUMLClass_Set:
			for UML_Class in UML_Set.difference(PythonUMLClass_Set):
				if UML_Class.lower() not in MinusPythonUMLClass_Set:
					#print "Comparamos ", Python_Class, " con ", UML_Class
					#print "		distancia es: ", ExtractorClases.hamdist(UML_Class, Python_Class)
					if (ExtractorClases.hamdist(UML_Class, Python_Class)<3):
						if (abs(len(UML_Class)-len(Python_Class))<3):
							#print "\nAgregada ", Python_Class, "\n"
							PythonUMLClass_Set.add(Python_Class)
							cuenta_ham += 1
							break



	cuenta = len(PythonUMLClass_Set)
	PythonClassNotInUML = list(Python_Set.difference(PythonUMLClass_Set))
	UMLClassNotInPython = list(UML_Set.difference(PythonUMLClass_Set))
	return cuenta, cuenta_exi, cuenta_ham, cuenta_mayus, PythonClassNotInUML,UMLClassNotInPython, list(PythonUMLClass_Set)

def AddResultsToFile(name, results):
	fichero = open("results.csv", "a")
	string = "\n" + name + ";"
	string += ';'.join(str(e) for e in results)
	fichero.write(string)
	fichero.close()

def Analyze(ProjectLink):
	TodasClases_UML = []
	TodasClases_py = []

	Carpeta_proyecto = ProjectLink.split("/")[-1]

	aEjecutar = "git clone " + ProjectLink
	os.system(aEjecutar)

	# Recorrer todas las carpetas y extraer todas las clases
	for (path, carpetas, archivos) in walk(Carpeta_proyecto):
		for archivo in archivos:
			if (archivo[-3:] == ".py"):
				fullpath = os.path.join(path, archivo)
				TodasClases_py += ExtractorClases.ClasesPy(fullpath)
			if (archivo[-4:] == ".xmi"):
				fullpath = os.path.join(path, archivo)
				TodasClases_UML += ExtractorClases.ClasesUML(fullpath)

	Clases_py = ExtractorClases.Depurar(TodasClases_py)
	Clases_UML = ExtractorClases.Depurar(TodasClases_UML)
	[Umlenpy, Umlenpy_igual, Umlenpy_ham, Umlenpy_may, PythonClassNotInUML, UMLClassNotInPython, ComunClass] = conteo(Clases_py, Clases_UML)
	results = [len(Clases_UML), len(Clases_py),Umlenpy, Umlenpy_igual, Umlenpy_ham, Umlenpy_may, PythonClassNotInUML, UMLClassNotInPython, ComunClass]

	aEjecutar = "rm -rf " + Carpeta_proyecto
	os.system(aEjecutar)

	return results

if __name__ == "__main__":
	ProjectLink = sys.argv[1]
	results = Analyze(ProjectLink)

	#print "Clases uml\n------------\n", Clases_UML, "\n\n"
	#print "Clases py\n------------\n", Clases_py, "\n\n"
	#print "Total UML: ", len(Clases_UML)
	#print "Total Py: ", len(Clases_py)
	#print "_________"
	#print "Clases Py en UML: ", Umlenpy
	#print "Exactamente igual: ", Umlenpy_igual
	#print "Corregidas dist_ham: ", Umlenpy_ham, " y mayus ", Umlenpy_may
	print results

	AddResultsToFile(ProjectLink.split("/")[-1],results)

	ExtractorClases.log.fin_log()
