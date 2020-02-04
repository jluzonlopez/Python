#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import types
a =[1,3]
b = [5]
c = [0]
d = [2,"a",2]
e = [4]
f = [0,1,1]
lista = [a,b,c,d,e,f]
print "Lista sin ordenar"
print lista

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

lista.sort(mi_ordena)
print "Lista ordenada"
print lista
