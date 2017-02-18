#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import os

if __name__ == "__main__":
	
	fichero_repos = open("repos.txt", "r")
	for repo in fichero_repos:
		print("Descargamos: ", repo)
		aEjecutar = "git clone " + repo
		os.system(aEjecutar)
		
		folder_name = repo.split("/")[-1]
		
		aEjecutar = "python proyect.py " + folder_name
		os.system(aEjecutar)
		
		aEjecutar = "rm -rf " + folder_name
		os.system(aEjecutar)