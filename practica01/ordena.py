#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import types
import sys
import argparse

def mi_ordena(x,y):
	indice_x = 0
	indice_y = 0
	total_x = 0
	total_y = 0
	while indice_x < len(x):
		if type(x[indice_x]) == types.IntType:
			total_x = total_x + x[indice_x]
			indice_x = indice_x + 1
		else:
			print "Error, elemento no permitido"
			raise SystemExit
	while indice_y  < len(y):
		if type(y[indice_y]) == types.IntType:
			total_y = total_y + y[indice_y]
			indice_y = indice_y + 1
		else:
			print "Error, elemento no permitido"
			raise SystemExit
	if total_x < total_y:
		return -1
	elif total_x == total_y:
		if len(x) > len(y):
			return 1
		else:
			return -1
	else: 
		return 1

def leer_valores():
	valor = linea[:-1].split(",")
	#if (valor == " "):
	#	sys.sterr.write("Error /n")
	#else:
	valor = [int(i) for i in valor]
	lista.append(valor)

usage = "%prog [opciones]"
parser = argparse.ArgumentParser(description = "Short sample app")
parser.add_argument("-i", "--input",action ="store", dest = "input",help = "-i [fichero] Leer desde un fichero")
parser.add_argument("-o", "--output",action ="store", dest = "output",help = "-o [fichero] Escrbir a un fichero")

args = parser.parse_args()


lista = []
if args.input:
	fichero = open(args.input,"r")
	for linea in fichero:
		leer_valores()
	fichero.close()
else:
	for linea in sys.stdin:
		leer_valores()
		
lista.sort(mi_ordena)
if args.output:
	fichero = open(args.output,"w")
	for x in lista:
		fichero.write(str(x)+"\n")
	fichero.close()
else:
	sys.stdout.write(bytes(lista)+"\n")


