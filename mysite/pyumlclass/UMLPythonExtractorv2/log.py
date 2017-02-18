#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

"""
	MODULO PARA LOGS
"""

import time

class Log():
	def __init__(self):
		self.f = open("log.txt", "w")
		texto = time.strftime('%H:%M:%S') + " Comienza la ejecucion...\n"
		self.f.write(texto)

	def log(self,txt):
		texto = time.strftime('%H:%M:%S') + ":" + txt +"\n"
		self.f.write(texto)

	def fin_log(self):
		texto = time.strftime('%H:%M:%S') + " Fin del log...\n"
		self.f.write(texto)
		self.f.close()