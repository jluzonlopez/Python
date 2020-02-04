#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import json
import sys

INFLACION = 3
fichero = open("papeleria.txt","r")

def inflacion(prec):
	return prec+(INFLACION*(prec/100))

for linea in fichero:
	lista = json.loads(linea)
	print "Ref.",'\t',"Precio",'\t',"Descripcion"
	print "-----------------------------------"
	for obj in lista:
		print obj['ref'],'\t',inflacion(obj['precio']),'\t',obj['descripcion']
