#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import sys
import argparse
import os

def raros(arch):
	if "@" in arch:
		os.rename(archivo,archivo.replace("@","_"))
	if "!" in arch:
		os.rename(archivo,archivo.replace("!","_"))
	if "~" in arch:
		os.rename(archivo,archivo.replace("~","_"))

def vocales(arch):
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

def espacios(arch):
	if " " in arch:
		os.rename(archivo,archivo.replace(" ","_"))

def enn(arch):
	if "ñ" in arch:
		os.rename(archivo,archivo.replace("ñ","nn"))

usage = "%prog [opciones]"
parser = argparse.ArgumentParser(description = "Short sample app")
parser.add_argument("-r","--recursive",action="store_true",dest="recursive",help="Recorrer os directorios recursivamente")
parser.add_argument("-s","--spaces",action="store_true",dest="spaces",help="Reemplazar los espacios por barra baja")
parser.add_argument("-c","--case",action="store_true",dest="case",help="Reemplazar las mayusculas por minusculas")
parser.add_argument("-n","--enne",action="store_true",dest="enne",help="Reemplazar las eñe por otra combinacino de letras")
parser.add_argument("-t","--accent",action ="store_true",dest="accent",help="Remplazar las vocales por acento")
parser.add_argument("-w","--weird",action="store_true",dest="weird",help="Remplazar los caracteres raros")
parser.add_argument("-f","--fichero",action="store",dest="fichero",help="-f [Path] Path en el que quieres hacer las modificiacines")

args = parser.parse_args()

if args.fichero:
	path = args.fichero
	print path
else:
	path = os.getcwd()
	print path

if os.path.exists(path):
	os.chdir(path)
else:
	print "No exist"
	print path

lista = os.listdir(".")
if args.recursive:
	for x in os.walk(path):
		print x

if args.spaces:
	for archivo in lista:
		espacios(archivo)

if args.case:
	print "case metido"

if args.enne:
	for archivo in lista:
		enn(archivo)

if args.accent:
	for archivo in lista:
		vocales(archivo)

if args.weird:
	for archivo in lista:
		raros(archivo)
