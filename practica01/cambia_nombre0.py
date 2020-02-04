#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import sys
import os

def renom(arch):
	if "á" in arch:
		os.rename(archivo,archivo.replace("á","a"))
	if "é" in arch:
		os.rename(archivo,archivo.replace("é","e"))
	if "í" in arch:
		os.rename(archivo,archivo.replace("í","i"))
	if "ó" in arch:
		os.rename(archivo,archivo.replace("ó","o"))
	if "ú" in arch:
		os.rename(archivo,archivo.replace("ú","u"))
	if " " in arch:
		os.rename(archivo,archivo.replace(" ","_"))
	if "ñ" in arch:
		os.rename(archivo,archivo.replace("ñ","nn"))
	if "@" in arch:
		os.rename(archivo,archivo.replace("@","_"))
	if "!" in arch:
		os.rename(archivo,archivo.replace("!","_"))
	if "~" in arch:
		os.rename(archivo,archivo.replace("~","_"))

if len(sys.argv[:]) == 1:
	path = os.getcwd()
	print path
else:
	path = sys.argv[:].pop()
	print path

if os.path.exists(path):
	os.chdir(path)
	lista = os.listdir(".")
	for archivo in lista:
		renom(archivo)
else:
	print "No exist"
	print path



