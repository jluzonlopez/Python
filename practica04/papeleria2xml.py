#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import xml.etree.cElementTree as ET
import json
import sys
import types

nombre_fichero = sys.stdin.readline()

fichero = open(nombre_fichero[:-1],"r")
for linea in fichero:
	linea = json.loads(linea)
	root = ET.Element(u"Objetos")
	root.text= u'Lista de objetos'
	for obj in linea:
		elemento = ET.SubElement(root,u"Elemento")
		claves = obj.keys()
		atributos = {}
		for clave in claves:
			if type(obj[clave]) == types.FloatType or type(obj[clave]) == types.IntType:
				obj[clave] = str(obj[clave])
			atributos[clave] = obj[clave]
		elemento.attrib = atributos

print ET.tostring(root, encoding="utf-8", method="xml")
fichero.close()
