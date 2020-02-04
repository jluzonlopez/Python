#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import json
import sys

fichero = open("papeleria.txt","r")

for linea in fichero:
	lista = json.loads(linea)
	print "Ref.",'\t',"Precio",'\t',"Descripcion"
	print "-----------------------------------"
	for obj in lista:
		print obj['ref'],'\t',obj['precio'],'\t',obj['descripcion']
