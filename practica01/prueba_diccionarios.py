#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

def muestra_alfabetico(dicc):
	lista_keys = dicc.keys()
	lista_keys.sort()
	for k in lista_keys:
		print '\n' + k + ":"
		for x in dicc[k]:
			print x

def muestra_por_longitud(dicc):
	val_escr= 0
	aux_long = 0
	while val_escr < len(dicc):
		for x in dicc:
			if len(dicc[x]) == aux_long:
				print '\n' + x + ":"
				val_escr = val_escr + 1
				for v in dicc[x]:
					print v
		aux_long = aux_long +1
	
dicc = {"valencia":["paella"],"madrid":["cocido"],"rioja":["vino"]}
dicc["segovia"]=["cochinillo"]
#print "Diccionario"
#print dicc

dicc["madrid"].append("bocadillo de calamares")
dicc["alcoholicas"] = ["vino","sidra","cerveza"]
#print "Diccionario"
#print dicc

del dicc["alcoholicas"]
dicc["comunidad_valenciana"]=["valencia","alicante","castellon"]
#print "Diccionario"
#print dicc

print '\n' + "Diccionario ordenado alfabeticamente:"
muestra_alfabetico(dicc)
print '\n' + "Diccionario ordenado por longitud de valores:"
muestra_por_longitud(dicc)
dicc.clear()

